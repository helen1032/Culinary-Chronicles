DROP DATABASE IF EXISTS culinary_chronicles;
CREATE DATABASE culinary_chronicles;
USE culinary_chronicles;

DROP TABLE IF EXISTS breakfasts;
CREATE TABLE breakfasts (
id				INT NOT NULL AUTO_INCREMENT,
category		VARCHAR(50) NOT NULL,
title			VARCHAR(800) NOT NULL,
servings		INT NOT NULL,
ingredients		VARCHAR(800) NOT NULL,
directions		VARCHAR(1000) NOT NULL,
PRIMARY KEY (id)
);

INSERT INTO breakfasts (category, title, servings, ingredients, directions) VALUES ('Breakfast', 'Italian Cloud Eggs', 4, '4 large eggs, separated
																														1/4 teaspoon Italian seasoning
																														1/8 teaspoon salt
																														1/8 teaspoon pepper
																														1/4 cup shredded Parmesan cheese
																														1 tablespoon minced fresh basil
																														1 tablespoon finely chopped oil-packed sun-dried tomatoes', '1. Preheat oven to 450°. Separate eggs; place whites in a large bowl and yolks in 4 separate small bowls.
																																														Beat egg whites, Italian seasoning, salt and pepper until stiff peaks form.
																																													2. In a 9-in. cast-iron skillet generously coated with cooking spray, drop egg white mixture into 4 mounds.
																																														With the back of a spoon, create a small well in the center of each mound.
																																														Sprinkle with cheese. Bake until light brown, about 5 minutes.
																																														Gently slip an egg yolk into each of the mounds. Bake until yolks are set, 3-5 minutes longer.
																																														Sprinkle with basil and tomatoes. Serve immediately.'),
																				  ('Breakfast', 'Fruity Waffle Paraits', 4, '4 frozen low-fat multigrain waffles
																															1/2 cup almond butter or creamy peanut butter
																															2 cups strawberry yogurt
																															2 large bananas, sliced
																															2 cups sliced fresh strawberries
																															Toasted chopped almonds, optional
																															Maple syrup, optional', '1. Toast waffles according to package directions. Spread each waffle with 2 tablespoons almond butter.
																																						Cut waffles into bite-sized pieces.
																																					2. Layer half the yogurt, bananas, strawberries and waffle pieces into 4 parfait glasses.
																																						Repeat layers. If desired, top with toasted almonds and maple syrup. Serve immediately.'),
																				  ('Breakfast', 'Banana Oatmeal Pancakes', 8, '2 cups complete whole wheat pancake mix
																																1 large firm banana, finely chopped
																																1/2 cup old-fashioned oats
																																1/4 cup chopped walnuts', '1. Prepare pancake batter according to package directions. Stir in the banana, oats and walnuts.
																																								Pour batter by 1/4 cupfuls onto a hot griddle coated with cooking spray; turn when bubbles form on top.
                                                                                                                                                                Cook until the second side is golden brown.');

SELECT * FROM breakfasts;