from dysql_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="1",
      instruction="I am Markus Klein, an auto dealer. Please update the price of the Volkswagen Dasher (car ID: 173) in your records to $38,000.00. Additionally, remove the erroneous production record for this vehicle specifically tied to model year 1974 (ID: 173, model_year: 1974), as it should only be listed under model year 1975.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 38000.0 WHERE ID = 173;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM production WHERE ID = 173 AND model_year = 1974;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6",
      instruction="My name is Marissa Clark and my email is marissa.clark4012@example.com. I want to update the sale price of my Ford Pinto (car ID 113) to $45,000. Additionally, update the production record for this car (ID 113) with model year 1974, changing the country from USA (code 1) to Japan (code 2).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 45000.0 WHERE ID = 113;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE production SET country = 2 WHERE ID = 113 AND model_year = 1974;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="11",
      instruction="Please update the database records for my vehicle (Car ID: 250). Set the horsepower to 120 in the specifications and update the sale price to $33,000.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE data SET horsepower = 120 WHERE ID = 250;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 33000.0 WHERE ID = 250;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="14",
      instruction="I need to update the price for car ID 336 (triumph tr7 coupe) to 32000.0 and add a new production record with model year 80 and country ID 5. Please confirm both the price adjustment and production entry have been applied specifically to vehicle ID 336.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 32000.0 WHERE ID = 336;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO production (ID, model_year, country) VALUES (336, 80, 5);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="15",
      instruction="I am Lisa Torres. As the owner of car ID 221 (datsun f-10 hatchback, model year 77), add a production record with country 'Japan' for this vehicle and update its price to $32,500.0 due to a premium sound system installation. Confirm both actions for ID 221.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO production (ID, model_year, country) VALUES (221, 77, 'Japan');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 32500.0 WHERE ID = 221;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="18",
      instruction="This is Emily West from inventory management. Authenticate my ID emily_west. Update the Ford Maverick (car ID 156) price to $28,500 in the price table. Separately, delete the production year 1973 entry for car ID 156 from the production records, as it was never stocked.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 28500.0 WHERE ID = 156;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM production WHERE ID = 156 AND model_year = 1973;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="19",
      instruction="As the dealership manager, I need to run a summer promotion by reducing the price of the 'pontiac astro' (car ID 171) from $30,000 to $27,500. First, update the price in the system. Then, retrieve the full specifications including mileage per gallon, number of cylinders, displacement, horse power, weight, acceleration, model year, car name, and the updated price for verification before finalizing the marketing materials.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 27500.0 WHERE ID = 171;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT d.mpg, d.cylinders, d.displacement, d.horsepower, d.weight, d.acceleration, d.model AS model_year, d.car_name, p.price FROM data d JOIN price p ON d.ID = p.ID WHERE d.ID = 171;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="sabrina_wright",
      instruction="Hi, I'm Sabrina Wright. Please update the price of car ID 25 (amc gremlin) to $15,000.00. Also add a production record for this vehicle with model year 1972 and country ID 1 (USA).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 15000.00 WHERE ID = 25"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO production (ID, model_year, country) VALUES (25, 1972, 1)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="alex_ramirez_tx",
      instruction="You are Alex Ramirez from Houston, TX. You need to update two records for your 1978 Chevrolet Monte Carlo Landau (ID 231): 1) Correct the listed price from $40,000 to $38,500 in sales records. 2) Confirm the production details show USA origin (country ID 1) for model year 1978.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 38500 WHERE ID = 231"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE production SET country = 1 WHERE ID = 231 AND model_year = 1978"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="30",
      instruction="I am Mark Reynolds and I recently restored my 1975 Ford Pinto (car ID 175). Please update the price to $42,500 for car ID 175 in the database, and add a new production record for the same car indicating the restoration occurred in the USA (country code 1) during 2024.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 42500.0 WHERE ID = 175;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO production (ID, model_year, country) VALUES (175, 2024, 1);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="31",
      instruction="Please update the price for the car named 'ford gran torino (sw)', with model year 1974 and country USA, to $32,500 in the price table. Ensure the correct car ID is identified through verification of the car name, model year, and country before proceeding with the price update.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT data.ID FROM data JOIN production ON data.ID = production.ID JOIN country ON production.country = country.origin WHERE data.car_name = 'ford gran torino (sw)' AND production.model_year = 1974 AND country.country = 'USA';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 32500.0 WHERE ID = 75;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="classic-car-owner-1973-ford-ltd",
      instruction="Update the price of my 1973 Ford LTD (ID: 160) to $42,500 in the price table and ensure its production country code is set to 1 (USA) in the production table. Use car ID 160, new price 42500.0, and country code 1 for these updates.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 42500.0 WHERE ID = 160;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE production SET country = 1 WHERE ID = 160;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="37",
      instruction="As Lucas Everett (user ID: lucas.everett), sales manager, I need to: (1) Retrieve full specifications for the car 'fiat 131' with ID 183 from the data table (mileage per gallon, cylinders, displacement, horse power, weight, acceleration, model), then (2) Update the price to $38,500 specifically for vehicle ID 183 in the price table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT mpg, cylinders, displacement, horsepower, weight, acceleration, model FROM data WHERE ID = 183 AND car_name = 'fiat 131';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 38500 WHERE ID = 183;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="39",
      instruction="My name is Jason Lee, zip code 20135. I need to update the listing price of my Fiat 124 Sport Coupe (vehicle ID 115) from $20,000 to $18,500. Additionally, please create a production record for this specific car (ID 115) with model year 73 and manufacturing country Italy.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 18500.0 WHERE ID = 115;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO production (ID, model_year, country) VALUES (115, 73, 'Italy');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="40",
      instruction="Hello, I am Lucie Lemieux updating my car records. For my VW Rabbit with ID 310, please (1) update horsepower from 76 to 78, (2) change price to 49999.99, and (3) update production year from 1976 to 1977.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE data SET horsepower = 78 WHERE ID = 310;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 49999.99 WHERE ID = 310;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE production SET model_year = 1977 WHERE ID = 310 AND model_year = 1976;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="154",
      instruction="You are Jordan Baker, a car collector. Update your Chevrolet Nova (ID: 154) with these changes: set its price to $36,000.00, modify horsepower to 110, and register a new production record for model year 1978 with country code 1 (USA).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 36000.00 WHERE ID = 154;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE data SET horsepower = 110 WHERE ID = 154;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO production (ID, model_year, country) VALUES (154, 1978, 1);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="collector_usa1974",
      instruction="I need to update two fields for my 1974 Chevrolet Vega (ID: 133). Please set its horsepower to 85 in the data table and adjust its price to $32,500 in the price table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE data SET horsepower = 85 WHERE ID = 133;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 32500.0 WHERE ID = 133;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="47",
      instruction="I need to update the mileage per gallon (mpg) of my Pontiac Sunbird Coupe with car ID 235 from 24.5 to 28.5 in the data table. After confirming this update, please also set its price to 24500.00 in the price table for the same car ID.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE data SET mpg = 28.5 WHERE ID = 235"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 24500.00 WHERE ID = 235"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="48",
      instruction="I am the inventory manager. Please update the car record with ID 20 and car name 'volkswagen 1131 deluxe sedan'. Change its horsepower in the data table to 60, and update its price in the price table to 28500.50.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE data SET horsepower = 60 WHERE ID = 20 AND car_name = 'volkswagen 1131 deluxe sedan';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 28500.50 WHERE ID = 20;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="car_owner_9272",
      instruction="I own the Chrysler Newport Royal (Car ID: 71). After an engine upgrade, I need to update its price to $35,000.50. Please modify the price record specifically for vehicle ID 71 in the system.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 35000.50 WHERE ID = 71;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="53",
      instruction="I need to update my car records. For the vehicle with ID 119 currently listed as a 1974 model priced at $30,000, please change the production year to 1975 and update the price to $31,500.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE production SET model_year = 1975 WHERE ID = 119 AND model_year = 1974;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 31500.0 WHERE ID = 119 AND price = 30000.0;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Steven Barnes",
      instruction="You are Steven Barnes. To comply with dealership eco requirements for your purchased vehicle 'oldsmobile delta 88 royale' (ID 70), create a new production record confirming this car was manufactured in model year 73 with origin country 'USA'. Use production ID=70, model_year=73, and country='USA' for this entry.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM data WHERE car_name = 'oldsmobile delta 88 royale' AND ID = 70"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO production (ID, model_year, country) VALUES (70, 73, 'USA')"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="marsha_taylor",
      instruction="As Marsha Taylor, update the Chrysler LeBaron Medallion (car ID:389) price to $36,000. Additionally, create a new production record for this vehicle with model year 82 manufactured in the USA. Ensure both changes are executed.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 36000 WHERE ID = 389;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO production (ID, model_year, country) VALUES (389, 82, 'USA');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="57",
      instruction="Hi there! I noticed an error in my car's production details. My 1980 Mazda 626 (ID 320) currently shows country code 3 (Japan) but should be listed as country code 1 (United States). Could you verify and update this record?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM production WHERE ID = 320 AND model_year = 1980 AND country = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE production SET country = 1 WHERE ID = 320 AND model_year = 1980;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="21",
      instruction="You are Alex Fischer, an organized car collector (user ID 21). Update your 1979 Peugeot 504 (car ID 21): 1) Delete its European (country code 2) production record for model year 1979. 2) Add a new European (country code 2) production record for model year 1981. 3) Set its price to 42000 USD. Perform these database updates sequentially.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM production WHERE ID=21 AND model_year=1979 AND country=2"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO production (ID, model_year, country) VALUES (21, 1981, 2)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price=42000.0 WHERE ID=21"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="60",
      instruction="I want to update the price of the car named 'amc concord' to 32000.0, but only if it was produced in country ID 1 (USA). Please execute an update that checks the car's country linkage and modifies the price accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 32000.0 WHERE ID IN (SELECT data.ID FROM data INNER JOIN production ON data.ID = production.ID WHERE data.car_name = 'amc concord' AND production.country = 1)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Sam Miller",
      instruction="You are Sam Miller. Update the sale price of your car (ID: 105) to $22,000. Check if there are any production records for car ID 105, delete them, and confirm deletion by providing the previous production details like model year and country.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE price SET price = 22000.0 WHERE ID = 105;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT model_year, country FROM production WHERE ID = 105;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM production WHERE ID = 105;"
               }
            ),
       ],
       outputs=[]
   ),
]
