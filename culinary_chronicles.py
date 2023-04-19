from flask import Flask, flash, redirect, url_for, render_template, session
from flask import request

from flask_sqlalchemy import SQLAlchemy

DB_HOST = "localhost"
DB_NAME = "culinary_chronicles"
DB_USERNAME = "root"
DB_Password = "Kyren_13!"

database_file = f"mysql+pymysql://{DB_USERNAME}:{DB_Password}@{DB_HOST}:3306/{DB_NAME}"

app = Flask(__name__)
app.secret_key = "mysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Breakfast(db.Model):
    __tablename__ = 'breakfasts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    ingredients = db.Column(db.String(800), nullable=False)
    directions = db.Column(db.String(1000), nullable=False)

    def __init__(self, id, title, servings, ingredients, directions):
        self.id = id
        self.title = title
        self.servings = servings
        self.ingredients = ingredients
        self.directions = directions


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/category")
def category():
    return render_template("category/categories.html")


@app.route("/upload")
def upload():
    return render_template("upload/listRecipe.html", breakfasts=Breakfast.query.all())


@app.route("/contact")
def contact():
    return render_template("contact/contactUs.html")


@app.route('/addrecipe', methods=['GET', 'POST'])
def add_breakfast():
    if request.method == 'POST':
        if not request.form['id'] or not request.form['title'] or not request.form['servings'] \
                or not request.form['ingredients'] or not request.form['directions']:
            flash('Please enter all the fields', 'error')
        else:
            breakfast = Breakfast(request.form['id'], request.form['title'], request.form['servings'],
                                  request.form['ingredients'], request.form['directions'])

            db.session.add(breakfast)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('upload'))
    return render_template('upload/addRecipe.html')


@app.route('/updaterecipe/<int:id>/', methods=['GET', 'POST'])
def update_breakfast(id):
    if request.method == 'POST':
        if not request.form['id'] or not request.form['title'] or not request.form['servings'] \
                or not request.form['ingredients'] or not request.form['directions']:
            flash('Please enter all the fields', 'error')
        else:
            breakfast = Breakfast.query.filter_by(id=id).first()
            breakfast.id = request.form['id']
            breakfast.title = request.form['title']
            breakfast.servings = request.form['servings']
            breakfast.ingredients = request.form['ingredients']
            breakfast.directions = request.form['directions']
            db.session.commit()

            flash('Record was successfully updated')
            return redirect(url_for('upload'))
    data = Breakfast.query.filter_by(id=id).first()
    return render_template("upload/updateRecipe.html", data=data)


@app.route('/deleterecipe/<int:id>/', methods=['GET', 'POST'])
def delete_breakfast(id):
    if request.method == 'POST':
        breakfast = Breakfast.query.filter_by(id=id).first()
        db.session.delete(breakfast)
        db.session.commit()

        flash('Record was successfully deleted')
        return redirect(url_for('upload'))
    data = Breakfast.query.filter_by(id=id).first()
    return render_template("upload/deleteRecipe.html", data=data)


if __name__ == '__main__':
    app.run(port=3003, host="localhost", debug=True)
