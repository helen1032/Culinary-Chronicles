from flask import Flask, abort, request, flash, redirect, send_from_directory, url_for, render_template, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:88c*02Hc@localhost/recipe_database'
app.secret_key = "mysecret"
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}
db = SQLAlchemy(app)

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    serving_amount = db.Column(db.Integer, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    directions = db.Column(db.Text, nullable=False)
    category = db.Column(db.Enum('breakfast', 'lunch', 'dinner', 'dessert'), nullable=False)
    photo_filename = db.Column(db.String(300), nullable=False)


    def __intit__(self, title, serving_amount, ingredients, directions, category, photo_filename):
        self.title = title
        self.serving_amount = serving_amount
        self.ingredients = ingredients
        self.directions = directions
        self.category = category
        self.photo_filename = photo_filename
#########################################################################################



# Homepage Index.html
@app.route("/")
def index():
    return render_template("index.html")

# Recipe Lists
@app.route("/products")
def recipe_list():
    recipes = Recipe.query.all()
    return render_template('products/recipe_list.html', recipes=recipes)

# Add a Recipe
@app.route("/upload")
def upload():
    return render_template("upload/upload.html", recipes=Recipe.query.all())

# Contact us page
@app.route("/contact")
def contact_us():
    return render_template('contact/contact_us.html')

# Method to add a recipe
@app.route('/addrecipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        if not request.form['title'] \
                or not request.form['serving_amount'] \
                or not request.form['ingredients'] \
                or not request.form['directions'] \
                or not request.form['category']:
            flash('Please enter all the fields', 'error')
        else:
            title = request.form['title']
            serving_amount = request.form['serving_amount']
            ingredients = request.form['ingredients']
            directions = request.form['directions']
            category = request.form['category']
            photo_filename = request.files['photo_filename']

            path = os.path.join(app.config['UPLOAD_FOLDER'], photo_filename.filename)
            photo_filename.save(path)

            recipe = Recipe(title=title,
                            serving_amount=serving_amount,
                            ingredients=ingredients,
                            directions=directions,
                            category=category,
                            photo_filename=photo_filename)

            db.session.add(recipe)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('upload'))

    categories = ['breakfast', 'lunch', 'dinner', 'dessert']
    return render_template('upload/add_recipe.html', categories=categories)

# Method to update any recipe
@app.route('/update_recipe/<int:id>/', methods=['GET', 'POST'])
def update_recipe(id):
    if request.method == 'POST':
        recipe = Recipe.query.filter_by(id=id).first()
        recipe.title = request.form['title']
        recipe.serving_amount = request.form['serving_amount']
        recipe.ingredients = request.form['ingredients']
        recipe.directions = request.form['directions']
        recipe.category = request.form['category']

        db.session.commit()

        flash('Record was successfully updated!', 'success')
        return redirect(url_for('upload', id=id))
    data = Recipe.query.filter_by(id=id).first()
    return render_template('upload/update_recipe.html', data=data)

# Method to delete a recipe
@app.route('/delete_recipe/<int:id>/', methods=['GET', 'POST'])
def delete_recipe(id):
        recipe = Recipe.query.get(id)
        db.session.delete(recipe)
        db.session.commit()

        flash('Record was successfully deleted!','success')
        return redirect(url_for('upload'))

# Method to generate all details of the recipe
@app.route('/products/<int:id>')
def recipe_details(id):
    recipe = Recipe.query.get(id)
    return render_template('products/recipe_details.html', recipe=recipe)

@app.template_filter('basename')
def basename_filter(path):
    return os.path.basename(path)

@app.route('/uploads/<filename>')
def displayImage(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


#########################################################################################
if __name__ == '__main__':
    app.run(port=3003, host="localhost", debug=True)