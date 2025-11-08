from tau_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="Maggie Palmer",
      instruction="This is Maggie Palmer. For my Honey Sesame Dressing (recipe ID 427), please update the plain lowfat yogurt (ingredient ID 2196, quantity ID 922) quantities to exactly 1 cup by setting both minimum and maximum to 1.0. Also update the protein per serving in the nutrition info for this recipe to 1.1 grams.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET max_qty = 1.0, min_qty = 1.0 WHERE quantity_id = 922 AND recipe_id = 427 AND ingredient_id = 2196;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET protein = 1.1 WHERE recipe_id = 427;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1",
      instruction="Hello, I'm Olivia Martinez (email: olivia.martinez912@example.com). For my Baked Fish recipe (ID: 1188), please adjust the quantity of Worcestershire Sauce (ingredient ID: 3787) to 2.0 tablespoons for both the minimum and maximum required. Additionally, update the recipe's sodium content in the nutrition information from 172.14 mg to 200 mg.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET max_qty = 2.0, min_qty = 2.0 WHERE recipe_id = 1188 AND ingredient_id = 3787;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium = 200 WHERE recipe_id = 1188;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2",
      instruction="Your name is Andrew Lopez. For the 'Oriental Pork' recipe (recipe_id: 597), you want to reduce the soy sauce (ingredient_id: 3283) quantity from 3 tablespoons to 1.5 tablespoons, and remove the toasted sesame seeds entry (quantity_id: 2451) entirely from the recipe due to dietary goals. Please update the ingredient quantities accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET max_qty = 1.5, min_qty = 1.5 WHERE recipe_id = 597 AND ingredient_id = 3283;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE quantity_id = 2451;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="casey",
      instruction="I am Casey. For recipe 672 (Summer Vegetable Paella), please do the following: 1) Update the sodium content in its nutrition details from 15.23 to 25.00 mg because I used salted oil. 2) Update the preparation directions for recipe 672 to: 'Heat olive or vegetable oil in a large nonstick skillet over medium-high heat. Stir-fry broccoli and zucchini for 5 minutes. Add tomato and nectarines; cover and cook 2 to 3 minutes.' Confirm both changes for recipe ID 672.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium = 25.00 WHERE recipe_id = 672;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Recipe SET directions = 'Heat olive or vegetable oil in a large nonstick skillet over medium-high heat. Stir-fry broccoli and zucchini for 5 minutes. Add tomato and nectarines; cover and cook 2 to 3 minutes.' WHERE recipe_id = 672;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4",
      instruction="I am modifying the 'Saffron Risotto Primavera' recipe (recipe_id=666) for a low-sodium version. Please replace the 'fat-free chicken broth' (ingredient_id=1215) in the Quantity table entry (quantity_id=3378, recipe_id=666) with a new ingredient called 'homemade vegetable broth' (category='soups', name='homemade vegetable broth', plural=NULL). After that, update the sodium content in the Nutrition table for recipe_id=666 to 50.0 mg per serving to reflect this change.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Ingredient (category, name, plural) VALUES ('soups', 'homemade vegetable broth', NULL);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET ingredient_id = (SELECT ingredient_id FROM Ingredient WHERE name = 'homemade vegetable broth') WHERE quantity_id = 3378 AND recipe_id = 666;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium = 50.0 WHERE recipe_id = 666;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5",
      instruction="I need to permanently delete recipe_id 1555 and all associated data from my cookbook database. First confirm deletion of all nutrition records where recipe_id = 1555, then remove all ingredient quantity entries where recipe_id = 1555, and finally delete the main recipe record where recipe_id = 1555.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Nutrition WHERE recipe_id = 1555"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE recipe_id = 1555"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Recipe WHERE recipe_id = 1555"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="health_conscious_user_01",
      instruction="I'm updating the 'Grape Nuts Cereal' recipe (recipe_id 935) to make it healthier. First, set the sodium content to 250.0 mg and increase dietary fiber to 3.0 g in its nutrition profile. Then, add whole wheat flakes (ingredient_id 120) as a required ingredient with exactly 50 grams (no preparation needed).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium = 250.0, fiber = 3.0 WHERE recipe_id = 935;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, min_qty, max_qty, unit, preparation, optional) VALUES (935, 120, 50, 50, 'g', 'none', 'no');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7",
      instruction="I'm making the Turkey Pot Roast (recipe_id 1022) for 4 servings and need to reduce sodium. Please: 1) Remove turkey broth (ingredient_id 3531) by setting its quantity to 0 cups, updating max_qty and min_qty to 0.0 with unit 'cup', and 2) Adjust water (ingredient_id 3649) to exactly 1.0 cup (from 0.25 cup) with 'fat-skimmed' preparation, setting both max_qty and min_qty to 1.0 with unit 'cup'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET max_qty = 0.0, min_qty = 0.0, unit = 'cup' WHERE recipe_id = 1022 AND ingredient_id = 3531;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET max_qty = 1.0, min_qty = 1.0, unit = 'cup', preparation = 'fat-skimmed' WHERE recipe_id = 1022 AND ingredient_id = 3649;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Amanda Lee",
      instruction="You are Amanda Lee. Update recipe 1531 by setting its title to 'Spring Vegetable Medley' and servings to 4. Add a nutrition entry for recipe 1531 containing 12.5g protein, 33g carbohydrates, and 250 calories (leave other nutrition fields empty). Then add an ingredient requirement for recipe 1531: use ingredient_id 8 with 2-3 cups (chopped preparation, mandatory).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Recipe SET title = 'Spring Vegetable Medley', servings = 4 WHERE recipe_id = 1531;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Nutrition (recipe_id, protein, carbo, calories) VALUES (1531, 12.5, 33, 250);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, min_qty, max_qty, unit, preparation, optional) VALUES (1531, 8, 2, 3, 'cup', 'chopped', 'no');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1001",
      instruction="As user 1001, I need to update my recipe 'Brussels Sprouts with Peppers and Potatoes' (recipe_id=419). First, reduce the sodium in its nutrition facts to 90 mg. Second, modify the existing ingredient with ID 2224 to be named 'olive oil' permanently, as I exclusively use this substitute for margarine/vegetable oil.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium = 90 WHERE recipe_id = 419;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Ingredient SET name = 'olive oil' WHERE ingredient_id = 2224;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12",
      instruction="You are Anita Patel. Update the recipe (ID: 1547) by changing its title to 'Fresh Summer Salad' and adjusting servings to 4. Then add nutritional information for this recipe: 6g protein, 24g carbs, 0g alcohol, 2.5g total fat, 0.4g saturated fat, 0mg cholesterol, 50mg sodium, 2mg iron, 15mg vitamin C, 350μg vitamin A, 4g fiber, 65% carbs calories, 10% fat calories, 25% protein calories, totaling 130 calories.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Recipe SET title = 'Fresh Summer Salad', servings = 4 WHERE recipe_id = 1547;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Nutrition (recipe_id, protein, carbo, alcohol, total_fat, sat_fat, cholestrl, sodium, iron, vitamin_c, vitamin_a, fiber, pcnt_cal_carb, pcnt_cal_fat, pcnt_cal_prot, calories) VALUES (1547, 6, 24, 0, 2.5, 0.4, 0, 50, 2, 15, 350, 4, 65, 10, 25, 130);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="13",
      instruction="As the cookbook editor reviewing recipe_id 773 ('-Papayas-'), first add the ingredient 'Papaya' (category: 'Fruit', plural: 'Papayas') to the Ingredient table. Next, link it to recipe_id 773 in the Quantity table with min_qty = 2, max_qty = 3, unit = 'pound', preparation = 'peeled and seeded', and optional = 'no'. Finally, display all ingredients for recipe_id 773 showing name, min_qty, max_qty, unit, preparation, and optional status.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Ingredient (category, name, plural) VALUES ('Fruit', 'Papaya', 'Papayas');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, min_qty, max_qty, unit, preparation, optional) SELECT 773, ingredient_id, 2, 3, 'pound', 'peeled and seeded', 'no' FROM Ingredient WHERE name = 'Papaya';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT Ingredient.name, Quantity.min_qty, Quantity.max_qty, Quantity.unit, Quantity.preparation, Quantity.optional FROM Quantity INNER JOIN Ingredient ON Quantity.ingredient_id = Ingredient.ingredient_id WHERE Quantity.recipe_id = 773;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="14",
      instruction="I am Olivia Wang (olivia.wang271@example.com). For the 'Fish Chowder' recipe (recipe_id: 1144), replace ingredient '2% lowfat milk' (ingredient_id: 12) with '1% lowfat milk' (ingredient_id: 13) in the quantity entry (quantity_id: 5154), and update the fiber content in its nutrition information to 6.5 grams.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET ingredient_id = 13 WHERE quantity_id = 5154 AND recipe_id = 1144 AND ingredient_id = 12"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET fiber = 6.5 WHERE recipe_id = 1144"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="15",
      instruction="You are editing recipe #421 ('Idaho Potato Cream Sauce'). Replace quantity_id 872 (currently ingredient #629/chicken bouillon) with ingredient #4000 (vegetable bouillon) while keeping 1.0 tablespoon(s). Update recipe #421's directions to: 'In small saucepan, combine potato and water. Bring to a boil, then cover and simmer until potato is tender, about 10 minutes. Using an electric hand mixer, blend potatoes until smooth. Stir in 1/2 cup milk along with vegetable bouillon and the remaining seasoning, blending until smooth and adding additional milk to reach a cream sauce consistency.' Remove quantity_id 870 (ingredient #370/butter flavoring granules) from recipe #421. Update recipe #421's nutrition entry to set protein content to 3.5 grams.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET ingredient_id = 4000 WHERE quantity_id = 872 AND recipe_id = 421;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Recipe SET directions = 'In small saucepan, combine potato and water. Bring to a boil, then cover and simmer until potato is tender, about 10 minutes. Using an electric hand mixer, blend potatoes until smooth. Stir in 1/2 cup milk along with vegetable bouillon and the remaining seasoning, blending until smooth and adding additional milk to reach a cream sauce consistency.' WHERE recipe_id = 421;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE quantity_id = 870 AND recipe_id = 421 AND ingredient_id = 370;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET protein = 3.5 WHERE recipe_id = 421;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="21",
      instruction="Hello, I'm user123. My Cranberries recipe (recipe_id: 759) lacks a quantity entry for ingredient_id 100. Please add minimum 2 cups, maximum 3 cups, preparation 'chopped fine', marked as not optional.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT recipe_id FROM Recipe WHERE recipe_id = 759;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, min_qty, max_qty, unit, preparation, optional) VALUES (759, 100, 2, 3, 'cup', 'chopped fine', 'no');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22",
      instruction="My username is dana_chef2001. For recipe_id 852, make these updates: 1. Change servings from 4 to 62. Update sodium in nutrition info from 191.36 mg to 100.0 mg per serving3. For quantity_id 4816 (water ingredient_id 3649), update both max_qty and min_qty from 6.0 cups to 5.0 cups",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET max_qty = 5.0, min_qty = 5.0 WHERE quantity_id = 4816 AND recipe_id = 852 AND ingredient_id = 3649;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Recipe SET servings = 6 WHERE recipe_id = 852;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium = 100.0 WHERE recipe_id = 852;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="23",
      instruction="As user 12345, I noticed the nutrition values for recipe_id 931 (All-Bran Cereal) need updating. Please set protein=2.0, carbo=10.5, alcohol=0.0, total_fat=0.25, sat_fat=0.05, cholestrl=0.0, sodium=140.0, iron=2.1, vitamin_c=7.0, vitamin_a=600.0, fiber=1.1, pcnt_cal_carb=78.0, pcnt_cal_fat=6.0, pcnt_cal_prot=16.0, calories=48.0. Also, add an ingredient with ingredient_id 205 to this recipe (recipe_id=931) in the quantity table, using min_qty=40, max_qty=40, unit='g', preparation='crushed', optional='no'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET protein=2.0, carbo=10.5, alcohol=0.0, total_fat=0.25, sat_fat=0.05, cholestrl=0.0, sodium=140.0, iron=2.1, vitamin_c=7.0, vitamin_a=600.0, fiber=1.1, pcnt_cal_carb=78.0, pcnt_cal_fat=6.0, pcnt_cal_prot=16.0, calories=48.0 WHERE recipe_id=931;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, min_qty, max_qty, unit, preparation, optional) VALUES (931, 205, 40, 40, 'g', 'crushed', 'no');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="25",
      instruction="Hi, this is cookbook_user_001. Please update my recipe #1465 with these details: title 'Simple Vegetable Soup', 4 servings, yield unit 'bowls', 15 minutes prep time, 30 minutes cook time, intro 'A hearty, healthy soup for all seasons.', directions 'Chop vegetables. Simmer in water with spices for 30 minutes. Serve hot.' Also add nutrition info: 12g protein, 24g carbo, 0g alcohol, 5g total fat, 1g saturated fat, 10mg cholesterol, 320mg sodium, 3mg iron, 18mg vitamin C, 820IU vitamin A, 4g fiber, 45% calories from carbs, 15% from fat, 40% from protein, total 210 calories.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Recipe SET title='Simple Vegetable Soup', servings=4, yield_unit='bowls', prep_min=15, cook_min=30, intro='A hearty, healthy soup for all seasons.', directions='Chop vegetables. Simmer in water with spices for 30 minutes. Serve hot.' WHERE recipe_id=1465;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Nutrition (recipe_id, protein, carbo, alcohol, total_fat, sat_fat, cholestrl, sodium, iron, vitamin_c, vitamin_a, fiber, pcnt_cal_carb, pcnt_cal_fat, pcnt_cal_prot, calories) VALUES (1465, 12, 24, 0, 5, 1, 10, 320, 3, 18, 820, 4, 45, 15, 40, 210);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="90210",
      instruction="As user 90210, update the ingredient in recipe_id=1571 with ingredient_id=7. Set its name to 'Almond Flour' and category to 'Nuts & Seeds'. For the same recipe-ingredient pair, configure quantity details to min_qty=120, max_qty=150, and unit='grams'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Recipe WHERE recipe_id=1571;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Ingredient SET name='Almond Flour', category='Nuts & Seeds' WHERE ingredient_id=7;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty=120, max_qty=150, unit='grams' WHERE recipe_id=1571 AND ingredient_id=7;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Jordan Taylor",
      instruction="This is Jordan Taylor. I need to adjust my 'Baked Fish' recipe (recipe_id 1188) to serve 4 people. Please double the ingredient quantities by updating both min_qty and max_qty for each of these specific quantity entries: quantity_id 5575 (recipe 1188), 5576 (recipe 1188), 5578 (recipe 1188), 5579 (recipe 1188), 5580 (recipe 1188), and 5581 (recipe 1188). Only update entries that match both the quantity_id and recipe_id in each case.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = min_qty * 2, max_qty = max_qty * 2 WHERE quantity_id = 5575 AND recipe_id = 1188;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = min_qty * 2, max_qty = max_qty * 2 WHERE quantity_id = 5576 AND recipe_id = 1188;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = min_qty * 2, max_qty = max_qty * 2 WHERE quantity_id = 5578 AND recipe_id = 1188;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = min_qty * 2, max_qty = max_qty * 2 WHERE quantity_id = 5579 AND recipe_id = 1188;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = min_qty * 2, max_qty = max_qty * 2 WHERE quantity_id = 5580 AND recipe_id = 1188;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = min_qty * 2, max_qty = max_qty * 2 WHERE quantity_id = 5581 AND recipe_id = 1188;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="30",
      instruction="My name is Maria Lombardi and my email is maria.lombardi8531@example.com. I am organizing my recipe records. I want to add a new ingredient named 'Whole Milk' in the 'Dairy' category, plural form 'Whole Milks'. Then, for the recipe with id 945 ('Parmesan Cheese'), add a quantity record that uses this ingredient: max_qty 2.0, min_qty 2.0, unit 'liter', preparation 'heated', optional 'no'. Please process these updates.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Ingredient (category, name, plural) VALUES ('Dairy', 'Whole Milk', 'Whole Milks');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit, preparation, optional) VALUES (945, (SELECT ingredient_id FROM Ingredient WHERE name = 'Whole Milk' AND category = 'Dairy'), 2.0, 2.0, 'liter', 'heated', 'no');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Celia Tan",
      instruction="Update the 'Stir-Fry Turkey Italiano' (recipe_id=1041) recipe's calories in the Nutrition table to 210. Then update the Quantity table entry for ingredient_id=3528 (turkey breast cutlet) in the same recipe to use 0.75 pounds by setting minimum quantity=0.75, maximum quantity=0.75, and unit='pounds'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET calories=210 WHERE recipe_id=1041;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty=0.75, max_qty=0.75, unit='pounds' WHERE recipe_id=1041 AND ingredient_id=3528;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="32",
      instruction="As the recipe editor (user_id=edit_recipe_user_101), I need to update recipe_id 534: 1) In Quantity table, set tomato juice (ingredient_id=3484) to exactly 0.75 cups by updating both min_qty and max_qty from 0.5. 2) In Nutrition table, configure sodium=900mg and calories=850kcal for this recipe.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET max_qty=0.75, min_qty=0.75 WHERE recipe_id=534 AND ingredient_id=3484;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium=900, calories=850 WHERE recipe_id=534;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="34",
      instruction="This is Jennifer Tran (user_id 1001) requesting changes to recipe ID 260 'Fudgy Date Pudding Cake'. Replace all quantity entries using ingredient ID 12 ('2% lowfat milk') with ingredient ID 13 ('whole milk'), preserving existing unit and amount values. Additionally, update the nutrition profile by adding exactly 3 grams to total_fat and 20 calories to the existing values for this recipe.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET ingredient_id = 13 WHERE recipe_id = 260 AND ingredient_id = 12;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET total_fat = total_fat + 3, calories = calories + 20 WHERE recipe_id = 260;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="35",
      instruction="To permanently delete the recipe with recipe_id 1460 and all associated data from the database, please execute the following deletions in sequence: first remove all Nutrition records linked to recipe_id 1460, then delete all Quantity records associated with recipe_id 1460, and finally delete the Recipe entry with recipe_id 1460. Confirm that no residual data for this recipe remains.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Nutrition WHERE recipe_id = 1460;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE recipe_id = 1460;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Recipe WHERE recipe_id = 1460;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="36",
      instruction="Hi, I'm Teresa Moore (user_id: teresa_moore). I need to update my 'Dessert Fruit Pizza' (recipe_id: 224) for dietary requirements. Please: 1) Delete the walnut ingredient (ingredient_id: 3640) from quantity entry 78 in this recipe. 2) In quantity entry 75, replace ingredient 2537 (part-skim mozzarella) with 4001 (nonfat mozzarella) using the same quantity. 3) Set the saturated fat value to 3.00 in the nutrition data for recipe 224.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE quantity_id = 78 AND recipe_id = 224 AND ingredient_id = 3640"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET ingredient_id = 4001 WHERE quantity_id = 75 AND recipe_id = 224 AND ingredient_id = 2537"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sat_fat = 3.00 WHERE recipe_id = 224"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="37",
      instruction="Hi, I'm Emma Jackson in Denver. I need to make two updates for my Teriyaki Sauce (recipe_id: 896). First, update the sodium value in its nutrition information to 650 mg. Second, add a new ingredient: 'Honey' (category: 'Sweetener', plural: 'Honeys') with quantity details - maximum 2.0 tablespoons, minimum 1.5 tablespoons, preparation as 'liquid', and mark it as non-optional.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium = 650 WHERE recipe_id = 896"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Ingredient (category, name, plural) VALUES ('Sweetener', 'Honey', 'Honeys')"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit, preparation, optional) VALUES (896, (SELECT ingredient_id FROM Ingredient WHERE name = 'Honey'), 2.0, 1.5, 'tablespoons', 'liquid', 'No')"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="41",
      instruction="Authenticate me as Jane Williams. For my recipe 'Snappy Bean Dip' (recipe_id: 694), update the quantity of salt (ingredient_id: 3021) from 0.75 teaspoon(s) to exactly 1.5 teaspoon(s) in both min_qty and max_qty fields. Additionally, adjust the sodium content in the nutrition facts to 372.8 mg for this recipe.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = 1.5, max_qty = 1.5 WHERE recipe_id = 694 AND ingredient_id = 3021;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium = 372.8 WHERE recipe_id = 694;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="42",
      instruction="My name is Fatima Patel from Austin. I'm updating my family hominy grits recipe for healthier eating (recipe_id 816). Please make these exact changes: 1) In the Nutrition table, reduce sodium from 291.09 mg to 180 mg. 2) In the Quantity table for quantity_id 4762 (linked to ingredient_id 1779), increase maximum quantity from 1.0 to 1.5 cups by updating both max_qty and unit fields.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium = 180 WHERE recipe_id = 816;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET max_qty = 1.5, unit = 'cups' WHERE quantity_id = 4762 AND ingredient_id = 1779;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="43",
      instruction="I need to remove all ingredient quantities linked to recipe_id 1581 from the Quantity table and delete the nutrition information for recipe_id 1581 from the Nutrition table. Please confirm both deletions are executed specifically for recipe_id 1581.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE recipe_id = 1581;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Nutrition WHERE recipe_id = 1581;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="44",
      instruction="Hello, I'm Eleanor Fox. Please completely delete Recipe ID 1526 from my collection by removing the recipe itself along with all its ingredient quantities and nutrition information. Verify all deletions strictly use recipe_id=1526 to maintain consistency in my recipe database.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE recipe_id = 1526"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Nutrition WHERE recipe_id = 1526"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Recipe WHERE recipe_id = 1526"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="sophia_nguyen",
      instruction="You're Sophia Nguyen updating the 'Oriental Curry Veggies' recipe (recipe_id: 452). Substitute 'plain lowfat yogurt' (ingredient_id: 2196) in the curry dip with 'unsweetened soy yogurt'. First, add a new ingredient: name 'unsweetened soy yogurt', category 'dairy alternatives', plural form not specified. Then update quantity_id 1119 to use this new ingredient at 0.25 cup(s), keeping the same unit and quantity.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Ingredient (category, name, plural) VALUES ('dairy alternatives', 'unsweetened soy yogurt', NULL);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT ingredient_id FROM Ingredient WHERE name = 'unsweetened soy yogurt' AND category = 'dairy alternatives';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET ingredient_id = (SELECT ingredient_id FROM Ingredient WHERE name = 'unsweetened soy yogurt' AND category = 'dairy alternatives'), max_qty = 0.25, min_qty = 0.25, unit = 'cup(s)' WHERE quantity_id = 1119 AND recipe_id = 452;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="46",
      instruction="You are Julia Garcia, a health-conscious home baker editing your recipe records. For your 'Old-Fashioned Fresh Pear Pie' (recipe_id = 242), reduce the sugar quantity (ingredient_id = 3334, quantity_id = 230) from 0.5 cup(s) to 0.25 cup(s) by updating its min_qty and max_qty in the Quantity table. Also, adjust the butter/margarine quantity (ingredient_id = 374, quantity_id = 235) from 1 tablespoon(s) to 0.5 tablespoon(s) by updating its min_qty and max_qty. Ensure only these two entries are modified.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = 0.25, max_qty = 0.25 WHERE quantity_id = 230 AND recipe_id = 242 AND ingredient_id = 3334;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = 0.5, max_qty = 0.5 WHERE quantity_id = 235 AND recipe_id = 242 AND ingredient_id = 374;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="47",
      instruction="My name is Hannah Olson. I own recipe ID 830 ('Soda Crackers'). Add 3 grams of chia seeds (ingredient_id:12) as a required (non-optional) ingredient with preparation 'whole', unit 'g', both min and max quantities set to 3. Update its nutrition profile by increasing protein content from 0.74g to 1.34g to reflect this addition.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT recipe_id FROM Recipe WHERE recipe_id = 830 AND source = 'hannah.olson';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit, preparation, optional) VALUES (830, 12, 3, 3, 'g', 'whole', 'no');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET protein = 1.34 WHERE recipe_id = 830;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Olivia Walker",
      instruction="As Olivia Walker, perform these updates for recipe #1456:1. Update recipe details:- Title: 'Super Greens Salad'- Subtitle: 'High Protein Veggie Bowl'- Servings: 4- Yield unit: 'bowl'- Prep time: 15 mins- Cook time: 0 mins- Stand time: 0 mins- Source: 'Olivia Walker's Kitchen'- Intro: 'A hearty salad rich in plant proteins.'- Directions: 'Combine all greens, toss with dressing, serve immediately.'2. Add nutrition information:- Protein: 20g- Carbohydrates: 12g- Total fat: 8g- Saturated fat: 1g- Cholesterol: 0mg- Sodium: 180mg- Iron: 2mg- Vitamin C: 20mg- Vitamin A: 900IU- Fiber: 6g- Calorie distribution: 30% carbs (30), 30% fat (30), 40% protein (40)- Total calories: 2503. Add ingredients:- 150-200 grams of Kale (ID 101), chopped (required)- 90-100 grams of Quinoa (ID 102), cooked (required)",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Recipe SET title = 'Super Greens Salad', subtitle = 'High Protein Veggie Bowl', servings = 4, yield_unit = 'bowl', prep_min = 15, cook_min = 0, stnd_min = 0, source = 'Olivia Walker''s Kitchen', intro = 'A hearty salad rich in plant proteins.', directions = 'Combine all greens, toss with dressing, serve immediately.' WHERE recipe_id = 1456;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Nutrition (recipe_id, protein, carbo, alcohol, total_fat, sat_fat, cholestrl, sodium, iron, vitamin_c, vitamin_a, fiber, pcnt_cal_carb, pcnt_cal_fat, pcnt_cal_prot, calories) VALUES (1456, 20, 12, 0, 8, 1, 0, 180, 2, 20, 900, 6, 30, 30, 40, 250);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit, preparation, optional) VALUES (1456, 101, 200, 150, 'gram', 'Chopped', 'No');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit, preparation, optional) VALUES (1456, 102, 100, 90, 'gram', 'Cooked', 'No');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="49",
      instruction="Hi, this is Sam Evans (user_id: sam.evans.1985). I need to update my recipe 'Tropical Date Sauce for Fish' (recipe_id 1132) due to a pineapple allergy. Please modify the quantity entry 5035 to use California date (ingredient_id 399) instead of pineapple, and set both minimum and maximum quantities to 1.0 cup(s).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET ingredient_id = 399, min_qty = 1.0, max_qty = 1.0, unit = 'cup(s)' WHERE quantity_id = 5035;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="50",
      instruction="My name is Alex Greenwell. I want to add 1 tablespoon of chopped walnuts to my recipe '-Dates-' (recipe_id=782) for better nutrition. Create a new ingredient entry with name='chopped walnuts', plural='chopped walnuts', category='nuts'. Then link it to the recipe with min_qty=1, max_qty=1, unit='tablespoon', preparation='chopped', optional='no'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Recipe WHERE title = '-Dates-' AND recipe_id = 782"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Ingredient (category, name, plural) VALUES ('nuts', 'chopped walnuts', 'chopped walnuts')"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, min_qty, max_qty, unit, preparation, optional) VALUES (782, (SELECT ingredient_id FROM Ingredient WHERE name = 'chopped walnuts'), 1, 1, 'tablespoon', 'chopped', 'no')"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="52",
      instruction="My name is Peter Simmons. I need to update recipe_id 445 (Provencale Tomato and Potato Soup). Please replace the existing ingredient chicken broth (ingredient_id 638) in quantity_id 1069 with sodium-free vegetable broth (ingredient_id 5010). Maintain the unit as 'cup(s)', set both max_qty and min_qty to 3.0, and leave preparation as None.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET ingredient_id = 5010, unit = 'cup(s)', max_qty = 3.0, min_qty = 3.0, preparation = NULL WHERE quantity_id = 1069 AND recipe_id = 445 AND ingredient_id = 638"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="alex.chen4382@example.com",
      instruction="You are Alex Chen (alex.chen4382@example.com) from San Diego, CA. First verify that Recipe #1530 belongs to you by checking if its source matches your email. Once confirmed, update servings to 4. Then add: 'Cilantro' (ingredient_id=5) with 10g max/min, preparation 'chopped', not optional; and 'Lime juice' (ingredient_id=6) with 20ml max/min, preparation 'freshly squeezed', not optional.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Recipe WHERE recipe_id = 1530 AND source = 'alex.chen4382@example.com'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Recipe SET servings = 4 WHERE recipe_id = 1530"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit, preparation, optional) VALUES (1530, 5, 10, 10, 'g', 'chopped', 'no')"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit, preparation, optional) VALUES (1530, 6, 20, 20, 'ml', 'freshly squeezed', 'no')"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="54",
      instruction="I'm managing your recipe with ID 1576. Please make these updates: (1) Set the number of servings to 4, and (2) Add 'Egg' (ingredient ID 101) as a required ingredient with exactly 2 pieces (beaten), using both min_qty=2 and max_qty=2, marked as non-optional.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Recipe SET servings = 4 WHERE recipe_id = 1576;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit, preparation, optional) VALUES (1576, 101, 2, 2, 'piece', 'beaten', 'no');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="user_request_001",
      instruction="I need to adjust the nutrition facts for my 'Basil Tomato Salad' (recipe ID: 632). Could you update the calories to 200.0 and the protein value to 4.0?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET calories = 200.0, protein = 4.0 WHERE recipe_id = 632;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="56",
      instruction="You are Linda Reed. You recently made the 'Sweet Cherry Ice' recipe (recipe_id 221) and found it too sweet. Please update both the minimum and maximum quantity of sugar (ingredient_id 3334) in the 'Quantity' table for this recipe to 0.2 cup(s) instead of 0.33 cup(s). Also, update the associated calories in the 'Nutrition' table for recipe_id 221 to 80 per serving, down from 89.74.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty=0.2, max_qty=0.2 WHERE recipe_id=221 AND ingredient_id=3334;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET calories=80 WHERE recipe_id=221;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="57",
      instruction="Authenticate as user_007. For recipe_id 1436 ('T.B.P.B. Smoothie'), update quantity_id 6319 to use almond butter (ingredient_id 3000) instead of peanut butter (ingredient_id 2560), maintaining 2 tablespoon(s). Update nutrition data: protein 13.5, carbo 40.8, alcohol 0.0, total_fat 17.2, sat_fat 2.9, cholestrl 0.0, sodium 52.0, iron 1.1, vitamin_c 0.0, vitamin_a 0.0, fiber 2.7, pcnt_cal_carb 45.9, pcnt_cal_fat 38.0, pcnt_cal_prot 16.1, calories 395.0.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET ingredient_id = 3000 WHERE quantity_id = 6319 AND recipe_id = 1436 AND ingredient_id = 2560;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET protein = 13.5, carbo = 40.8, alcohol = 0.0, total_fat = 17.2, sat_fat = 2.9, cholestrl = 0.0, sodium = 52.0, iron = 1.1, vitamin_c = 0.0, vitamin_a = 0.0, fiber = 2.7, pcnt_cal_carb = 45.9, pcnt_cal_fat = 38.0, pcnt_cal_prot = 16.1, calories = 395.0 WHERE recipe_id = 1436;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="party_planner_123",
      instruction="For Butterflied Lamb Leg (recipe_id 522) which I own: 1) Scale all ingredient quantities in the Quantity table by 1.5x to adjust from 14 to 21 servings. 2) Remove the existing butter entry (ingredient_id 363). 3) Add 1.5 tablespoons of olive oil (ingredient_id 720) as a replacement. Confirm each step separately.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET max_qty = max_qty * 1.5, min_qty = min_qty * 1.5 WHERE recipe_id = 522;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE recipe_id = 522 AND ingredient_id = 363;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit) VALUES (522, 720, 1.5, 1.5, 'tablespoon(s)');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="casey.dunn123",
      instruction="You are Casey Dunn. Update the peanut butter quantity (ingredient_id: 2560) in recipe 'Pasta with Peanut Sauce' (recipe_id: 660) from 2 tablespoons to 1 tablespoon for quantity entry 3029 by setting both minimum and maximum quantity to 1.0. Also modify the recipe's introduction to: 'Warning: Contains peanuts. A tasty noodle dish popular in restaurants, easy to make at home.'",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET max_qty = 1.0, min_qty = 1.0 WHERE quantity_id = 3029 AND ingredient_id = 2560 AND recipe_id = 660;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Recipe SET intro = 'Warning: Contains peanuts. A tasty noodle dish popular in restaurants, easy to make at home.' WHERE recipe_id = 660;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="64",
      instruction="You are Alex Carter with email diet.user@example.com. Update the Quantity entry (quantity_id: 2273) for recipe 580 ('Sweet'N'Sour Pot Roast') to set both minimum and maximum quantities for ingredient 1992 ('lean boned beef chuck roast') to 1.5 pounds instead of 2.0 pounds for portion control.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = 1.5, max_qty = 1.5 WHERE quantity_id = 2273 AND recipe_id = 580 AND ingredient_id = 1992;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="66",
      instruction="Hi, I'm Erica Thomas, a culinary instructor updating the course demo for Recipe ID 1579. First, remove the ingredient with ingredient_id=24 from the recipe. Next, add ingredient_id=42 to this recipe with min_qty=0.5, max_qty=1.0, unit='tsp', preparation='finely ground', and optional='no'. Finally, remove ingredient_id=33 from the recipe. Confirm when all updates to Recipe ID 1579 are complete.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE recipe_id = 1579 AND ingredient_id = 24;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, min_qty, max_qty, unit, preparation, optional) VALUES (1579, 42, 0.5, 1.0, 'tsp', 'finely ground', 'no');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE recipe_id = 1579 AND ingredient_id = 33;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="69",
      instruction="Please update recipe 1031 ('Chicken in Tomato Marsala Sauce') by replacing ingredient 527 ('canned tomato sauce') with ingredient 2000 ('fresh tomato puree'). For the new ingredient: set max_qty=8.0, min_qty=8.0, unit='ounce(s)', preparation='pureed', and optional='FALSE'. Remove all quantity entries for ingredient 527 in this recipe. Update nutrition values for recipe 1031 to carbo=13.0, calories=270, and vitamin_c=19.5.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE recipe_id = 1031 AND ingredient_id = 527"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit, preparation, optional) VALUES (1031, 2000, 8.0, 8.0, 'ounce(s)', 'pureed', 'FALSE')"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET carbo = 13.0, calories = 270, vitamin_c = 19.5 WHERE recipe_id = 1031"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="user_5478",
      instruction="I am user_5478 and want to modify my 'Meatless Chili' (recipe_id 657) to reduce sodium. Update the canned tomatoes (ingredient_id 528) to exactly 6.0 cups with unit 'cups' and preparation 'unsalted'. Then set the recipe's sodium content to 280 mg in the Nutrition table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET min_qty = 6.0, max_qty = 6.0, unit = 'cups', preparation = 'unsalted' WHERE recipe_id = 657 AND ingredient_id = 528"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Nutrition SET sodium = 280 WHERE recipe_id = 657"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="olivia.carter.personal.recipe",
      instruction="I’m Olivia M. Carter. For my personal copy of the 'Apricot Applesauce Cake' (recipe_id: 293), please substitute the 'almonds' (ingredient_id: 35) in the 0.5 cup(s) chopped quantity (quantity_id: 5909) with 'walnuts' (ingredient_id: 1750), maintaining the exact measurement of 0.5 cup(s) chopped. Update this substitution in my recipe records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Quantity SET ingredient_id = 1750 WHERE quantity_id = 5909 AND recipe_id = 293;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="dietUser339",
      instruction="I am user dietUser339. For recipe ID 839, execute the following steps: 1) Remove any existing ingredient named 'table salt' from the recipe. 2) Create a new ingredient in the Ingredient table with category 'leavening', name 'homemade salt-free baking powder', plural 'homemade salt-free baking powders'. 3) Add this new ingredient to recipe 839 with quantity values: 1.0 teaspoon (unit), min_qty=1.0, max_qty=1.0, preparation='sifted', optional='no'. Confirm completion by displaying the updated ingredient list for recipe 839 (names, units, quantities).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT ingredient_id FROM Ingredient WHERE name = 'table salt';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Quantity WHERE recipe_id = 839 AND ingredient_id = (SELECT ingredient_id FROM Ingredient WHERE name = 'table salt');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Ingredient (category, name, plural) VALUES ('leavening', 'homemade salt-free baking powder', 'homemade salt-free baking powders');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT ingredient_id FROM Ingredient WHERE name = 'homemade salt-free baking powder';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Quantity (recipe_id, ingredient_id, max_qty, min_qty, unit, preparation, optional) VALUES (839, (SELECT ingredient_id FROM Ingredient WHERE name = 'homemade salt-free baking powder'), 1.0, 1.0, 'teaspoon', 'sifted', 'no');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT Ingredient.name, Quantity.min_qty, Quantity.max_qty, Quantity.unit, Quantity.preparation, Quantity.optional FROM Quantity JOIN Ingredient ON Quantity.ingredient_id = Ingredient.ingredient_id WHERE Quantity.recipe_id = 839;"
               }
            ),
       ],
       outputs=[]
   ),
]
