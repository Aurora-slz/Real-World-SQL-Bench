from tau_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="7295",
      instruction="My name is Murray Burnns and my email is Burnns@company.example.com. I recently moved, so I need to update my address to 122 Newtown Ave, Pittsfield (city_id: 51700, postal_code: 63288, state: 'MA', state_province_id: 52649), and change my default city and postal code. Also, I want to update the price for my frequently bought item 'Linseed Oil' (prod_id: 30) to $11.99 for both its prod_list_price and prod_min_price, since I've seen a price change elsewhere. Please update these details for me.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address = '122 Newtown Ave', cust_city = 'Pittsfield', cust_city_id = 51700, cust_postal_code = '63288', cust_state_province = 'MA', cust_state_province_id = 52649 WHERE cust_email = 'Burnns@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = 11.99, prod_min_price = 11.99 WHERE prod_id = 30;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2493",
      instruction="I am Delia Overton (email Overton@company.example.com, cust_id 2493). I purchased several 'Pitching Machine and Batting Cage Combo' (prod_id=14) last year. I want to request a refund for the earliest of these purchases in 2020. Please delete only the first sales record for prod_id=14 that year (which is: time_id='2020-03-10', channel_id=3, promo_id=999, quantity_sold=1, amount_sold=1290.74), and set my customer record to have 'cust_valid' status 'P' until my refund is processed.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Overton@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=2493 AND prod_id=14 AND time_id='2020-03-10' AND channel_id=3 AND promo_id=999 AND quantity_sold=1 AND amount_sold=1290.74;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_valid = 'P' WHERE cust_id = 2493;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6126",
      instruction="My name is Galen Kaden and my email is Kaden@company.example.com. I noticed that for my previous sale of the Genuine Series MIX Wood Bat (product ID 127) on 2019-10-09 via the Internet channel (channel ID 4), the unit price in the costs table is incorrect. It should be 39.99 instead of the current value. Please update the unit price to 39.99 for prod_id=127, time_id='2019-10-09', promo_id=999, and channel_id=4 in the costs table. Also, update the corresponding amount_sold in the sales table for this product, date, promo, channel, and my customer ID (6126) to 39.99. All parameters are: prod_id=127, time_id='2019-10-09', promo_id=999, channel_id=4, cust_id=6126, new_unit_price=39.99, new_amount_sold=39.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Kaden@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 39.99 WHERE prod_id = 127 AND time_id = '2019-10-09' AND promo_id = 999 AND channel_id = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 39.99 WHERE prod_id = 127 AND cust_id = 6126 AND time_id = '2019-10-09' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="133",
      instruction="You are Liane Player (liane.player@company2.example.com) and you discovered your July 8, 2022 Direct Sales purchase of Linseed Oil (prod_id=30, channel_id=3, promo_id=999) was invoiced incorrectly. Please update the product description for prod_id=30 to 'Cricket Bat - Premium Linseed Oil' and adjust the amount_sold in your sales record for prod_id=30, cust_id=133, time_id='2022-07-08', channel_id=3, promo_id=999 from 10.2 to 11.5.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'liane.player@company2.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_desc = 'Cricket Bat - Premium Linseed Oil' WHERE prod_id = 30;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 11.5 WHERE prod_id = 30 AND cust_id = 133 AND time_id = '2022-07-08' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5712",
      instruction="My name is Tania Reid (email: Reid@company.example.com). I have noticed that my purchase of 'Team shirt' (product id 40) made on 2020-12-13 via channel 2 (Partners), promotion 999, is showing the wrong sales amount and price—45.71 instead of the intended 44.99. Please correct this so that amount_sold in sales and unit_price in costs for that transaction are both set to 44.99. The specific parameters are: prod_id=40, cust_id=5712, time_id='2020-12-13', channel_id=2, promo_id=999. Update both sales.amount_sold and costs.unit_price accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Reid@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 44.99 WHERE prod_id = 40 AND cust_id = 5712 AND time_id = '2020-12-13' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 44.99 WHERE prod_id = 40 AND time_id = '2020-12-13' AND promo_id = 999 AND channel_id = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6207",
      instruction="My name is Henrietta Roisston (cust_id: 6207). I noticed my last trade for product Indoor Cricket Ball (prod_id: 48) on 2021-02-21 via Direct Sales (channel_id: 3) with no promotion (promo_id: 999) is incorrect. I actually bought 2 units, not 1. Please update this sales record to quantity_sold: 2 and amount_sold: 25.64. Also, ensure the associated costs record for this product, date, channel, and promo has unit_cost: 10.92 and unit_price: 12.82.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 25.64 WHERE prod_id = 48 AND cust_id = 6207 AND time_id = '2021-02-21' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 10.92, unit_price = 12.82 WHERE prod_id = 48 AND time_id = '2021-02-21' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7347",
      instruction="You are Xanthe Murphy (cust_id 7347). After reviewing your records, you realized that you need to correct a previous order made on 2022-04-20 for the 'English Willow Cricket Bat' (prod_id 28), which you purchased via Direct Sales (channel_id 3) under no promotion (promo_id 999). You intended to buy 2 units instead of 1. Please update the 'sales' table so that for prod_id=28, cust_id=7347, time_id='2022-04-20', channel_id=3, promo_id=999, the quantity_sold is 2 and amount_sold is 419.92. The 'costs' table does not require any change as unit_cost and unit_price are per unit and not quantity-dependent.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 419.92 WHERE prod_id = 28 AND cust_id = 7347 AND time_id = '2022-04-20' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="400",
      instruction="I, Clematis Garner (cust_id=400), want to update the record for all 'Team shirt' products I have previously purchased: prod_ids 40 (West Indies Team), 41 (South African Team), 42 (New Zealand Cricket Team), 43 (Australian Cricket Team), 44 (Indian Cricket Team), and 45 (English Cricket Team). Please increase the prod_list_price for each of these products by 10% in the products table. After the update, retrieve the prod_id, prod_name, and the updated prod_list_price for each of these items so I can confirm the changes.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = prod_list_price * 1.10 WHERE prod_id IN (40, 41, 42, 43, 44, 45);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT prod_id, prod_name, prod_list_price FROM products WHERE prod_id IN (40, 41, 42, 43, 44, 45);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1015",
      instruction="I am Pam Lanston (cust_id=1015, email=Lanston@company.example.com). Please first retrieve a detailed history of all my purchases of products with prod_name like 'Team shirt' (including all teams). Show purchase dates, channel, promo info, quantity_sold, amount_sold, unit_cost, and unit_price for each. After I review, update the quantity_sold to 2 (from 1) for my purchase of prod_id=40 ('Team shirt' - West Indies Team), made on 2020-02-21 via channel_id=3 (Direct Sales) and promo_id=999. Confirm the update by displaying the revised entry for this transaction.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT s.prod_id, p.prod_name, p.prod_desc, s.time_id, t.day_name, s.channel_id, c.channel_desc, s.promo_id, pr.promo_name, s.quantity_sold, s.amount_sold, cs.unit_cost, cs.unit_price FROM sales s JOIN products p ON s.prod_id=p.prod_id JOIN times t ON s.time_id=t.time_id JOIN channels c ON s.channel_id=c.channel_id JOIN promotions pr ON s.promo_id=pr.promo_id JOIN costs cs ON s.prod_id=cs.prod_id AND s.time_id=cs.time_id AND s.channel_id=cs.channel_id AND s.promo_id=cs.promo_id WHERE s.cust_id=1015 AND p.prod_name LIKE '%Team shirt%';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=2 WHERE prod_id=40 AND cust_id=1015 AND time_id='2020-02-21' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold FROM sales WHERE prod_id=40 AND cust_id=1015 AND time_id='2020-02-21' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2061",
      instruction="You are Rebba Robbins (Robbins@company.example.com) from Galway City. You want to update your street address to '415 Galway Harbor Drive', postal code to '34428', and phone number to '635-294-5555'. Also, on your past purchase dated '2021-09-19' through channel_id 3, you realize you received a 'Team shirt' for the South African Team (prod_id 41), but the sale was recorded as prod_id 43 ('Australian Cricket Team'). Update this record to the correct prod_id 41 (keeping all other sale details unchanged) and ensure the costs table is also updated for the same transaction (change prod_id 43 to 41, date '2021-09-19', promo_id 999, channel_id 3).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Robbins@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address = '415 Galway Harbor Drive', cust_postal_code = '34428', cust_main_phone_number = '635-294-5555' WHERE cust_id = 2061;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET prod_id = 41 WHERE cust_id = 2061 AND time_id = '2021-09-19' AND channel_id = 3 AND prod_id = 43;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET prod_id = 41 WHERE prod_id = 43 AND time_id = '2021-09-19' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2271",
      instruction="Your name is Vida Bane, email Bane@company.example.com, and customer ID is 2271. After reviewing your recent purchases, you have decided to return the 'Pitching Machine and Batting Cage Combo' (prod_id=14) purchased on 2020-04-20 through Direct Sales (channel_id=3, promo_id=999) for 1304.25 EUR (quantity_sold=1). You request to remove this purchase and its associated cost record (unit_cost=947.58, unit_price=1304.25) from your account. Additionally, you want to increase your customer credit limit from 3000.0 to 4000.0. All IDs and parameters are provided.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id=14 AND cust_id=2271 AND time_id='2020-04-20' AND channel_id=3 AND promo_id=999 AND quantity_sold=1 AND amount_sold=1304.25;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=14 AND time_id='2020-04-20' AND promo_id=999 AND channel_id=3 AND unit_cost=947.58 AND unit_price=1304.25;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit=4000.0 WHERE cust_id=2271;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="10975",
      instruction="I'm Roberta Pardue (cust_id=10975). I noticed an error in my historical record: my Pro Maple Bat (prod_id=129) bought on 2021-12-11 should have unit_cost=180.00 and unit_price=190.00 instead of the currently recorded values (unit_cost=184.45, unit_price=194.86). Please update both the costs and sales records for this transaction. Set amount_sold to 190.00 as well. The other identifiers are: channel_id=3, promo_id=999, time_id='2021-12-11'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=180.00, unit_price=190.00 WHERE prod_id=129 AND time_id='2021-12-11' AND promo_id=999 AND channel_id=3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=190.00 WHERE prod_id=129 AND cust_id=10975 AND time_id='2021-12-11' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="8885",
      instruction="I'm Hiram Coe (email: Coe@company.example.com). I've recently gotten married and need to update my profile. Please change my marital status to 'married' and also lower my credit limit from $1500.00 to $1200.00 as I want to monitor my spending more closely. My customer ID is 8885.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_marital_status = 'married', cust_credit_limit = 1200.00 WHERE cust_id = 8885;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="10990",
      instruction="You are Homer Valentino and you need to 1) update your profile to set your email to homer.valentino@newmail.com and your income level to 'F: 110,000 - 129,999', and 2) completely delete the sale and related cost record for your purchase of 'Pro Maple Youth Bat' (prod_id 130) made on 2020-12-04 via Direct Sales channel (channel_id 3, promo_id 999), ensuring both the sale and cost are removed from your account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_email = 'homer.valentino@newmail.com', cust_income_level = 'F: 110,000 - 129,999' WHERE cust_id = 10990;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 130 AND cust_id = 10990 AND time_id = '2020-12-04' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 130 AND time_id = '2020-12-04' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4461",
      instruction="I am Idette York (York@company.example.com), and I need to correct a sale from 2020-08-28: for the product 'Team shirt' (prod_id 40) sold through channel_id 3 (Direct Sales), only 1 shirt was recorded, but the correct quantity is 3. Update the sales table so that quantity_sold becomes 3 and amount_sold is 155.88 for that transaction (cust_id 4461, prod_id 40, time_id '2020-08-28', channel_id 3). Make sure the costs entry remains as it is.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 3, amount_sold = 155.88 WHERE prod_id = 40 AND cust_id = 4461 AND time_id = '2020-08-28' AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7303",
      instruction="You are Nora Niu (Niu@company.example.com), a data-driven small business owner who likes to keep precise sales records. Please update your Direct Sales transaction for the product 'Team shirt' (prod_id=41, channel_id=3, time_id='2021-10-31', promo_id=999) to have quantity_sold=2. Also, set the quantity_sold for your 'Genuine Series MIX Wood Bat' (prod_id=127, channel_id=3, time_id='2021-11-01', promo_id=999) to zero to reflect a returned item.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email='Niu@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=2 WHERE cust_id=7303 AND prod_id=41 AND time_id='2021-10-31' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=0 WHERE cust_id=7303 AND prod_id=127 AND time_id='2021-11-01' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3345",
      instruction="You are Calbert Gibb from Perry, IL (cust_id 3345, address: 37 West Kent Street). You recently bought an English Willow Cricket Bat (prod_id 28) for $210.07 on 2021-06-17 via Direct Sales (channel_id 3). You now want to: (1) update your main phone number to 309-222-3141, and (2) request an increase of your credit limit to $2000.00 due to your recent high-value purchases. Update both values in the customers table for your cust_id, ensuring your changes are recorded.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_main_phone_number = '309-222-3141' WHERE cust_id = 3345;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 2000.00 WHERE cust_id = 3345;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="10660",
      instruction="You are Hill Everley (customer ID: 10660) from 47 South Routt Road, Dolores, CO, 58488. On October 4th, 2020, you purchased a 'Pro Maple Youth Bat' (product ID: 130) through the Direct Sales channel (channel ID: 3) with promotion ID: 999. You noticed that the unit cost for this product was incorrectly recorded as 84.95 in the system. Please update the unit cost for this transaction to 79.95, keeping all other information the same.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 79.95 WHERE prod_id = 130 AND time_id = '2020-10-04' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100396",
      instruction="You are Jayden Prabu (customer id 100396) from Weissport, PA. You want to simulate a test transaction by adding a new sales record for product prod_id=410, with sale date 2024-06-22, channel_id=2, promo_id=13, quantity_sold=3, amount_sold=99.99. In addition, you want to insert a corresponding cost record for that same product and date with promo_id=13, channel_id=2, unit_cost=27.50, unit_price=33.33.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (410, 100396, '2024-06-22', 2, 13, 3, 99.99);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (410, '2024-06-22', 13, 2, 27.50, 33.33);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1485",
      instruction="My name is Barnaby Malone (customer ID: 1485). Please update all my records for the product 'Indoor Cricket Ball' (prod_id=48) for the year 2019 so that the amount sold in the 'sales' table is changed to 15.50 and the unit price in the 'costs' table is also set to 15.50. Make these updates for all sales that occurred in 2019 (time_id from 2019-01-01 to 2019-12-31).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 15.50 WHERE cust_id = 1485 AND prod_id = 48 AND time_id >= '2019-01-01' AND time_id <= '2019-12-31';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 15.50 WHERE prod_id = 48 AND time_id >= '2019-01-01' AND time_id <= '2019-12-31';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="13333",
      instruction="I'm Holmes Glassman. I want to correct the pricing for my last two purchases of 'English Willow Cricket Bat' (prod_id 28), made on 2021-06-08 and 2021-05-08. The price I actually paid should have been 205.00 for each bat due to a supplier discount. Please update both the sales (amount_sold = 205.00) and costs (unit_price = 205.00) for these purchases. All relevant parameters: cust_id 13333, prod_id 28, time_id 2021-06-08 and 2021-05-08, new amount_sold 205.00, new unit_price 205.00.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id = 13333"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 205.00 WHERE prod_id = 28 AND cust_id = 13333 AND time_id = '2021-06-08'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 205.00 WHERE prod_id = 28 AND time_id = '2021-06-08'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 205.00 WHERE prod_id = 28 AND cust_id = 13333 AND time_id = '2021-05-08'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 205.00 WHERE prod_id = 28 AND time_id = '2021-05-08'"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3702",
      instruction="I am Marshall Kotch (cust_id=3702). Please update my email to 'marshall.kotch2024@example.com' and my main phone number to '555-212-9999'. Also, for my purchase of the 'Pro Maple Youth Bat' (prod_id=130) on 2019-07-18 through Direct Sales (channel_id=3, promo_id=999), it should show that I bought 2 units and the total amount_sold was 250.04. Correct the sales record accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_email = 'marshall.kotch2024@example.com', cust_main_phone_number = '555-212-9999' WHERE cust_id = 3702;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 250.04 WHERE prod_id = 130 AND cust_id = 3702 AND time_id = '2019-07-18' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="283",
      instruction="You are Jacqueline Bradley (cust_id: 283, email: j.bradley@company2.example.com). On 2021-12-09, you accidentally bought 1 unit of the 'Pro Maple Bat' (prod_id: 129) through Direct Sales (channel_id: 3), under promo_id 999. You intended to purchase the 'Pro Maple Youth Bat' (prod_id: 130) instead, under the same channel and promotion. Please: 1) Delete your sales record for prod_id 129 on 2021-12-09. 2) Delete the associated cost record for prod_id 129 on 2021-12-09, promo_id 999, channel_id 3. 3) Insert a new sales record for prod_id 130, cust_id 283, date 2021-12-09, channel_id 3, promo_id 999, quantity_sold 1, amount_sold 89.92. 4) Insert the corresponding cost record for prod_id 130 on 2021-12-09, promo_id 999, channel_id 3, with unit_cost 87.55, unit_price 89.92.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 129 AND cust_id = 283 AND time_id = '2021-12-09' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 129 AND time_id = '2021-12-09' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (130, 283, '2021-12-09', 3, 999, 1, 89.92);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (130, '2021-12-09', 999, 3, 87.55, 89.92);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="8499",
      instruction="Hi, I'm Wileen Crabtree (cust_id 8499, email Crabtree@company.example.com). Please increase my credit limit to 8000.0, and also update the price of product 'Team shirt' with prod_id 40 to 54.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 8000.0 WHERE cust_id = 8499;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = 54.99 WHERE prod_id = 40;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1181",
      instruction="My name is Gary Ridgeway (cust_id 1181). I noticed a mistake in one of my recent sales records. For the 'Cricket Bat Bag' (prod_id 19) purchased on 2022-07-19, the sales record currently shows quantity_sold as 1 and amount_sold as 58.17, but it should be quantity_sold 2 and amount_sold 120.00. Also, the corresponding costs record has unit_cost 46.66 and unit_price 58.17, but it should be updated to unit_cost 48.00 and unit_price 60.00 for that transaction. The channel used was Direct Sales (channel_id 3) and the promotion was NO PROMOTION # (promo_id 999). Please update the database so the sales table and the costs table reflect these corrected numbers for this transaction only.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id = 1181;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 120.00 WHERE cust_id = 1181 AND prod_id = 19 AND time_id = '2022-07-19' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 48.00, unit_price = 60.00 WHERE prod_id = 19 AND time_id = '2022-07-19' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12024",
      instruction="You are Lyle Robbins (cust_id=12024), living at 17 East Colorado Court, FL. On 2021-02-15, you bought the 'Pro Maple Youth Bat' (prod_id=130) through the Partners channel (channel_id=2, promo_id=999). Your purchase was recorded as quantity_sold=1, amount_sold=99.78, but you actually bought 2 bats and want the sales record updated to quantity_sold=2 and amount_sold=199.56. Please update the corresponding sales row with these correct values.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=2, amount_sold=199.56 WHERE prod_id=130 AND cust_id=12024 AND time_id='2021-02-15' AND channel_id=2 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100591",
      instruction="You are Joshua Clark (cust_id 100591), residing at 117 North Harvey Avenue, Navy Yard City, WA, postal code 36632. You noticed that on 2019-11-30, the sales record for your purchase of '2 Competition Grade NFHS Baseballs' (prod_id 46) through Tele Sales (channel_id 9) with promo_id 33 shows the amount as $22.99, but you were actually charged $18.99. Please update the sales record for this transaction to the correct amount_sold, and also record the cost of this transaction as unit_cost $15.00 and unit_price $18.99 in the costs table for the same product, time, channel, and promo. Additionally, you want to update your supplementary demographics to reflect your new occupation as 'Sales Manager'. Finally, submit a request to increase your credit limit in the customers table to $10,000.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 18.99 WHERE prod_id = 46 AND cust_id = 100591 AND time_id = '2019-11-30' AND channel_id = 9 AND promo_id = 33;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (46, '2019-11-30', 33, 9, 15.00, 18.99);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET occupation = 'Sales Manager' WHERE cust_id = 100591;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 10000.0 WHERE cust_id = 100591;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7902",
      instruction="You are Gale Wright and you noticed an error in your trading records. On 2019-11-04, you bought the product Pro Maple Youth Bat (prod_id=130) through Partners (channel_id=2) with no promotion (promo_id=999), but the sales amount was wrongly recorded as 125.02. Please correct the sales 'amount_sold' to 130.00 and also update the costs 'unit_cost' to 85.00 for that same product, date, channel, and promotion. My customer id is 7902.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 130.00 WHERE cust_id = 7902 AND prod_id = 130 AND time_id = '2019-11-04' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 85.00 WHERE prod_id = 130 AND time_id = '2019-11-04' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1758",
      instruction="Hello, this is Harriett Lassiter (Lassiter@company.example.com). I've recently moved to a new residence and also would like to increase my credit limit due to higher recent purchases. Please update my street address to 200 Maple Avenue, Apartment 304, postal code 38401, and raise my credit limit to 4500.00. Thank you!",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Lassiter@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address = '200 Maple Avenue, Apartment 304', cust_postal_code = '38401' WHERE cust_id = 1758;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 4500.00 WHERE cust_id = 1758;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="209",
      instruction="I am Regina Abrams (regina.abrams@company2.example.com, cust_id 209). On 2021-11-18, I purchased a 'Pro Maple Youth Bat' (prod_id 130) through Direct Sales (channel_id 3), but the sales and costs records have the promotion set as 'NO PROMOTION #' (promo_id 999) by mistake. Please update both my sales and costs record for prod_id 130, time_id '2021-11-18', and channel_id 3 so that the promo_id is changed to 350 ('internet promotion #29-350').",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id = 350 WHERE cust_id = 209 AND prod_id = 130 AND time_id = '2021-11-18' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET promo_id = 350 WHERE prod_id = 130 AND time_id = '2021-11-18' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7330",
      instruction="My name is Patience Leopard, my email is Leopard@company.example.com. For privacy reasons, please remove all my sales history related to the product 'Genuine Series MIX Wood Bat' (prod_id: 127). My customer id is 7330. Additionally, make sure to also remove from the costs table all records with prod_id = 127 and time_id, channel_id, promo_id matching the deleted sales. Please confirm all deletions.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 7330 AND prod_id = 127"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 127 AND (time_id, channel_id, promo_id) IN (SELECT time_id, channel_id, promo_id FROM sales WHERE cust_id = 7330 AND prod_id = 127)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2232",
      instruction="You are Tyrone Bradley (cust_id 2232). You would like to cancel your recent order of the product '6 Gallon Empty Ball Bucket' (prod_id 47) made on '2021-10-26' through Direct Sales (channel_id 3) with no promotion (promo_id 999, quantity_sold 1), and instead, on the same date and channel, purchase '2 Competition Grade NFHS Baseballs' (prod_id 46) with quantity 1, at amount_sold 24.13 (unit_cost 21.12, unit_price 24.13). Please make all relevant changes in both the sales and costs records accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=2232 AND prod_id=47 AND time_id='2021-10-26' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=47 AND time_id='2021-10-26' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (46, 2232, '2021-10-26', 3, 999, 1, 24.13);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (46, '2021-10-26', 999, 3, 21.12, 24.13);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="16984",
      instruction="You are Lucette Titus (cust_id 16984, email Titus@company.example.com). You want to update the unit_cost of the 'Team shirt' (prod_id 40) for the trade on 2020-10-17 (channel_id 3, promo_id 999) to 39.99 due to a revised supplier invoice. Afterwards, confirm the updated cost for this item, date, and channel.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Titus@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 39.99 WHERE prod_id = 40 AND time_id = '2020-10-17' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM costs WHERE prod_id = 40 AND time_id = '2020-10-17' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="13642",
      instruction="My name is Robert Farmer (email: Farmer@company.example.com). I recently purchased a Pro Maple Youth Bat (prod_id=130) on 2021-08-06 via Direct Sales (channel_id=3). I realized the recorded unit cost and price were incorrect. Please update the unit_cost to 80.00 and the unit_price to 90.00 in the costs record for product_id 130, time_id '2021-08-06', channel_id 3, promo_id 999.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 80.00, unit_price = 90.00 WHERE prod_id = 130 AND time_id = '2021-08-06' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2369",
      instruction="Your name is Bailey Hatcher, email Hatcher@company.example.com, and you want to correct the recorded sale for your Slugger Youth Series Maple Bat sold on 2021-10-24 via Direct Sales (channel_id 3). Please update the sales record so that amount_sold is 34.99 instead of 30.07, and adjust the corresponding costs record so unit_price is also 34.99. The prod_id is 128, cust_id is 2369, channel_id is 3, promo_id is 999, and time_id is 2021-10-24.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 34.99 WHERE prod_id = 128 AND cust_id = 2369 AND time_id = '2021-10-24' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 34.99 WHERE prod_id = 128 AND time_id = '2021-10-24' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="28022",
      instruction="I am Urban Ogletree (cust_id 28022). I accidentally purchased the 'Genuine Series MIX Wood Bat' (prod_id 127) twice. Please delete my earlier purchase made on 2019-06-24 via Direct Sales (channel_id 3, promo_id 999). Also, update my supplementary demographics so my 'baseball' affinity is set to 1. If you need to remove any corresponding cost record, do so for prod_id 127, time_id '2019-06-24', promo_id 999, channel_id 3.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=28022 AND prod_id=127 AND time_id='2019-06-24' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=127 AND time_id='2019-06-24' AND promo_id=999 AND channel_id=3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET baseball=1 WHERE cust_id=28022;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2805",
      instruction="My name is Mara Sandoval (cust_id 2805). I see two transactions for 'English Willow Cricket Bat' (prod_id: 28) on 2022-08-30: one via Partners (channel_id: 2), and one via Direct Sales (channel_id: 3). Please remove my Partners purchase for prod_id: 28, cust_id: 2805, time_id: '2022-08-30', channel_id: 2. Then show me the total quantity and total amount sold for 'English Willow Cricket Bat' (prod_id: 28) across all channels.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 28 AND cust_id = 2805 AND time_id = '2022-08-30' AND channel_id = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT SUM(quantity_sold) AS total_quantity, SUM(amount_sold) AS total_amount FROM sales WHERE prod_id = 28;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4401",
      instruction="Hello, this is Hal Smyth. Please change my customer credit limit to 8000.00 and update my postal code to 99999. Also, set the product list price for 'Team shirt' (prod_id 42) to 49.99. My cust_id is 4401 and the product to update is prod_id 42.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 8000.00, cust_postal_code = '99999' WHERE cust_id = 4401;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = 49.99 WHERE prod_id = 42;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100128",
      instruction="I am Jayden Cackett living at 57 East Faulkner Drive, Lavallette, NJ 76071. Please update my occupation in your records to 'Senior VP'. After that, I would like my credit limit to be increased from 9000.0 to 12000.0. All changes are for my account only (cust_id 100128).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET occupation = 'Senior VP' WHERE cust_id = 100128;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 12000.0 WHERE cust_id = 100128;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="17011",
      instruction="You are Madeline Conard (customer ID 17011), and your current email is Conard@company.example.com. You want to update your email address in the system to madeline.conard.new@email.com. After that, you also noticed that your credit limit should be 2000.00 instead of the current 1500.00. Please update both your email and your credit limit to the new values.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_email = 'madeline.conard.new@email.com' WHERE cust_id = 17011 AND cust_email = 'Conard@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 2000.00 WHERE cust_id = 17011;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2636",
      instruction="I am Leta Salvadore (cust_id 2636). I need to update my credit limit to 9000 in my customer profile. Also, there is a mistake in my sale record: on 2021-07-04, I sold 1 unit of 'Pro Maple Youth Bat' (prod_id 130), but it was linked to promo_id 999 instead of the correct promo_id 100. Please update this sale record to promo_id 100. I need confirmation when both are done.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 9000 WHERE cust_id = 2636;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id = 100 WHERE cust_id = 2636 AND prod_id = 130 AND time_id = '2021-07-04';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6752",
      instruction="You are Xerxes Coe (cust_id 6752). You want to update the unit cost of every past purchase you made of the 'Pro Maple Youth Bat' (prod_id 130) to 75.00 due to a new supplier agreement, and also update its current product list price to 91.99 in the catalog. Make sure all relevant cost records (matching prod_id=130 and any time_id/channel_id/promo_id where you made a purchase) are updated. Apply these changes for all records pertaining to your purchases only.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=75.00 WHERE prod_id=130 AND (time_id, channel_id, promo_id) IN (SELECT s.time_id, s.channel_id, s.promo_id FROM sales s WHERE s.cust_id=6752 AND s.prod_id=130);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price=91.99 WHERE prod_id=130;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100656",
      instruction="I am Cole Nicholo (Nicholo@company.example.com), and I recently purchased 1 unit of the '2 Competition Grade NFHS Baseballs' (prod_id=46) via Tele Sales (channel_id=9) on 2019-12-31, under promotion promo_id=33. I have just received a new promo code that is expiring soon (promo_id=40) and would like to apply this promotion to the same purchase instead, keeping all other details the same. Please update the sales record for me: set promo_id=40 where prod_id=46, cust_id=100656, time_id='2019-12-31', channel_id=9, and promo_id=33.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id=40 WHERE prod_id=46 AND cust_id=100656 AND time_id='2019-12-31' AND channel_id=9 AND promo_id=33;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100656",
      instruction="I am Cole Nicholo (Nicholo@company.example.com), and I recently purchased 1 unit of the '2 Competition Grade NFHS Baseballs' (prod_id=46) via Tele Sales (channel_id=9) on 2019-12-31, under promotion promo_id=33. I have just received a new promo code that is expiring soon (promo_id=40) and would like to apply this promotion to the same purchase instead, keeping all other details the same. Please update the sales record for me: set promo_id=40 where prod_id=46, cust_id=100656, time_id='2019-12-31', channel_id=9, and promo_id=33.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id=40 WHERE prod_id=46 AND cust_id=100656 AND time_id='2019-12-31' AND channel_id=9 AND promo_id=33;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="86",
      instruction="You are Atalie Capps (atalie.capps@company2.example.com). You recently noticed your records have an outdated address and phone number. Please update your address to '321 New Horizons Drive', main phone number to '(312) 555-2198'. Also, there was a recording error for your sale of Pro Maple Youth Bat (prod_id 130) on 2020-05-31 via Internet (channel_id 4), no promotion (promo_id 999): the quantity_sold should be 2 instead of 1. Please correct this in the sales records (for cust_id 86).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'atalie.capps@company2.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address = '321 New Horizons Drive', cust_main_phone_number = '(312) 555-2198' WHERE cust_id = 86;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2 WHERE prod_id = 130 AND cust_id = 86 AND time_id = '2020-05-31' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="13642",
      instruction="My name is Robert Farmer (cust_id: 13642), and I noticed I accidentally purchased the 'Cricket Bat Bag' (prod_id: 19) twice on 2021-10-14, once through Partners (channel_id: 2) and once via Direct Sales (channel_id: 3). Please remove the sales and cost records for the Direct Sales channel (channel_id: 3, promo_id: 999, time_id: '2021-10-14') for this product. Also, update my income bracket to 'G: 130,000 - 149,999'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 19 AND cust_id = 13642 AND time_id = '2021-10-14' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 19 AND time_id = '2021-10-14' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_income_level = 'G: 130,000 - 149,999' WHERE cust_id = 13642;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="14457",
      instruction="You are Pete Woodman (cust_id=14457). While reviewing your trade records, you notice that for your purchase of the 'Genuine Series MIX Wood Bat' (prod_id=127) on 2019-11-24, the amount_sold and unit_price were recorded as $51.39, but it should be $55.00. Please update the sales record where cust_id=14457, prod_id=127, time_id='2019-11-24', channel_id=3, promo_id=999, to set amount_sold=55.00. Also, update the corresponding costs record (prod_id=127, time_id='2019-11-24', channel_id=3, promo_id=999) to set unit_price=55.00 as well, so the cost accounting matches the updated sale price.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=55.00 WHERE cust_id=14457 AND prod_id=127 AND time_id='2019-11-24' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price=55.00 WHERE prod_id=127 AND time_id='2019-11-24' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9167",
      instruction="My name is Rayburn Luna, residing at 47 North Dooly Road, Mackville, KY 45704 and my customer ID is 9167. I noticed a pricing mistake on my recent sale of 'Indoor Cricket Ball' (prod_id: 48) that occurred on 2022-07-04 via Internet channel (channel_id: 4, promo_id: 999). Please update the sales record so that the amount_sold is corrected from 12.01 to 10.99 for this specific transaction, and also adjust the unit_price for the corresponding costs entry to 10.99. Confirm when these changes are done.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 10.99 WHERE cust_id = 9167 AND prod_id = 48 AND time_id = '2022-07-04' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 10.99 WHERE prod_id = 48 AND time_id = '2022-07-04' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3079",
      instruction="You are Tiffany Hatcher (cust_id=3079, email=Hatcher@company.example.com, born 1980, address: 37 West Chippewa Street, Los Angeles, CA). For privacy reasons, you want to permanently remove your entire customer profile and all associated sales records from the system. Please ensure that your sales history (cust_id=3079 in sales table) is deleted before your customer profile (cust_id=3079 in customers table) is erased.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 3079;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM customers WHERE cust_id = 3079;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9349",
      instruction="I am Ulysses Ballard (cust_id 9349). Please update my supplementary demographics to set my occupation as 'Retired Coach' and my education as 'Master of Sports Science'. Also, I want my customer credit limit increased from 9000.0 to 12000.0.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET occupation = 'Retired Coach', education = 'Master of Sports Science' WHERE cust_id = 9349;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 12000.0 WHERE cust_id = 9349;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2328",
      instruction="I am Zenas Justice (cust_id 2328). On 2019-10-17, I purchased a Plastic Cricket Bat (prod_id 23) through Direct Sales (channel_id 3, promo_id 999), but the quantity was wrongly entered as 1. Please update the record so that quantity_sold is 2 and amount_sold is 48.16 (double the single-unit price). Ensure my user is authenticated first.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id = 2328 AND cust_first_name = 'Zenas' AND cust_last_name = 'Justice';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 48.16 WHERE cust_id = 2328 AND prod_id = 23 AND time_id = '2019-10-17' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4597",
      instruction="I am Mason Murray (cust_id 4597). Due to a recall of 'Linseed Oil', I need to update my sales and cost records for my purchase of prod_id 30, bought on 2022-10-02 via channel_id 3 and promo_id 999. Please set quantity_sold and amount_sold to 0 in sales, and set unit_cost and unit_price to 0 in costs for this specific record. This is only for that specific transaction.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 0, amount_sold = 0 WHERE prod_id = 30 AND cust_id = 4597 AND time_id = '2022-10-02' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 0, unit_price = 0 WHERE prod_id = 30 AND time_id = '2022-10-02' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5077",
      instruction="I'm Blake Carmudi (email: Carmudi@company.example.com), and I noticed that for my sale on October 31, 2021, the product name for product ID 41 was incorrectly recorded as 'Team shirt' instead of 'Proteas Shirt'. Please update the name in the products table where prod_id = 41 from 'Team shirt' to 'Proteas Shirt' immediately. I expect confirmation when it is done.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_name = 'Proteas Shirt' WHERE prod_id = 41 AND prod_name = 'Team shirt';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4928",
      instruction="I am Vania Yates (cust_id: 4928). I recently bought 'Indoor Cricket Ball' (prod_id: 48) twice through channel_id 4 and promo_id 999: once on '2022-07-01' for 12.01 (unit_cost currently set to 10.3), and again on '2022-08-04' for 11.94 (unit_cost was 9.83). My supplier says the correct unit_cost for both should be 9.83. Please update the 'costs' table for prod_id 48, time_id '2022-07-01', channel_id 4, promo_id 999 so that unit_cost is 9.83 (instead of 10.3), and then provide me confirmation by showing the updated record for that date.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 9.83 WHERE prod_id = 48 AND time_id = '2022-07-01' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM costs WHERE prod_id = 48 AND time_id = '2022-07-01' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="26630",
      instruction="I am Hardy Gentle. For my purchase made on 2019-10-07 through Direct Sales (channel_id=3) using the NO PROMOTION # promotion (promo_id=999), the product recorded is Indoor Cricket Ball (prod_id=48), but it should have been 2 Competition Grade NFHS Baseballs (prod_id=46). Please update the product in both the sales and costs records from prod_id=48 to prod_id=46 for that transaction.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET prod_id=46 WHERE cust_id=26630 AND prod_id=48 AND time_id='2019-10-07' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET prod_id=46 WHERE prod_id=48 AND time_id='2019-10-07' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7557",
      instruction="I am Dixie Dally (Dally@company.example.com) and during an inventory audit I noticed a mistake: on '2019-06-13' for the sale of 'Fiber Tape' (prod_id: 31), the quantity_sold should be 0 and amount_sold 0.0. Please update the 'sales' record where cust_id=7557, prod_id=31, time_id='2019-06-13', channel_id=3, promo_id=999 to quantity_sold=0 and amount_sold=0.0. Also, update the corresponding 'costs' entry for prod_id=31, time_id='2019-06-13', channel_id=3, promo_id=999 so that unit_cost=0.0 and unit_price=0.0.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=0, amount_sold=0.0 WHERE cust_id=7557 AND prod_id=31 AND time_id='2019-06-13' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=0.0, unit_price=0.0 WHERE prod_id=31 AND time_id='2019-06-13' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1819",
      instruction="I'm Joshie Petroff (cust_id 1819, email Petroff@company.example.com). I noticed that my purchase of the 'Team shirt' (prod_id 41) on 2022-04-15 (channel_id 3, promo_id 999) was incorrectly logged. The sale should show quantity_sold=2 and amount_sold=96.04, not 1 and 48.02. Also, for this transaction, each unit had unit_cost=37.91 and unit_price=48.02, so please update the costs entry so the unit_cost and unit_price are 37.91 and 48.02, but also make sure the sales entry reflects quantity_sold=2 and amount_sold=96.04. Make these corrections for my records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 96.04 WHERE prod_id = 41 AND cust_id = 1819 AND time_id = '2022-04-15' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 37.91, unit_price = 48.02 WHERE prod_id = 41 AND time_id = '2022-04-15' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6873",
      instruction="You are Brand Zanth (cust_id 6873). On 2020-10-24, you purchased a 'Team shirt' for the South African Team (prod_id 41) via Direct Sales (channel_id 3). You've just received a promo code for promo_id 2001 and want to retroactively apply this promotion to that transaction for both the sales and costs records. Please update the records to set the promo_id to 2001 for your transaction: cust_id=6873, prod_id=41, time_id='2020-10-24', channel_id=3, promo_id=999 (current, to be replaced).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id = 2001 WHERE cust_id = 6873 AND prod_id = 41 AND time_id = '2020-10-24' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET promo_id = 2001 WHERE prod_id = 41 AND time_id = '2020-10-24' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100210",
      instruction="My name is Jayden Clark, my email is Clark@company.example.com. For my next business order, I want to see a list of all product IDs and product names of items I have purchased before, but only include those where, at my most recent purchase of that product (to me), the per-unit gross margin (amount_sold divided by quantity_sold minus the unit_cost at that time) was over $20. Please compute this only for my own latest purchase of each product. I want to use the most recent sale record (for cust_id=100210) for each product I bought, and use the corresponding costs at that same prod_id, time_id, and channel_id to obtain unit_cost. All required parameters are explicitly: cust_id=100210, sales.prod_id, sales.time_id, sales.channel_id, sales.amount_sold, sales.quantity_sold, costs.unit_cost. Please return prod_id and prod_name for the filtered list.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT p.prod_id, p.prod_name FROM products p JOIN ( SELECT s.prod_id, s.time_id, s.channel_id, s.amount_sold, s.quantity_sold, c.unit_cost FROM sales s JOIN ( SELECT prod_id, MAX(time_id) as max_time_id FROM sales WHERE cust_id=100210 GROUP BY prod_id ) latest ON s.prod_id = latest.prod_id AND s.time_id = latest.max_time_id JOIN costs c ON s.prod_id = c.prod_id AND s.time_id = c.time_id AND s.channel_id = c.channel_id WHERE s.cust_id=100210 ) mr ON p.prod_id = mr.prod_id WHERE ((mr.amount_sold / CAST(mr.quantity_sold AS REAL)) - mr.unit_cost) > 20;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12050",
      instruction="My name is Virginia Lee (email: Lee@company.example.com). I want to update the unit price of the product 'Genuine Series MIX Wood Bat' (prod_id=127) for the sale that happened on 2021-08-11 via the Partners channel (channel_id=2) under promotion 999, to $41.00 (unit_price). Please update the costs table entry for prod_id=127, time_id='2021-08-11', channel_id=2, promo_id=999 with the new unit_price 41.00.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 41.00 WHERE prod_id = 127 AND time_id = '2021-08-11' AND promo_id = 999 AND channel_id = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100134",
      instruction="I am Cole Desai (customer ID: 100134). For personal reasons, I want to erase my full trading history from your system immediately. This includes all sales and any associated cost records. Please delete every sales record where cust_id = 100134 and then remove all cost entries related to my trades (that is, matching on prod_id, time_id, promo_id, and channel_id values present in my sales).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 100134;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE (prod_id, time_id, promo_id, channel_id) IN (SELECT prod_id, time_id, promo_id, channel_id FROM sales WHERE cust_id = 100134);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7601",
      instruction="I am Victoria Paintor (cust_id 7601) and recently bought an English Willow Cricket Bat (prod_id 28) on 2022-05-17 through the Internet channel (channel_id 4). There is now a special discount promotion available (promo_id 101) that should apply to this type of purchase. Please update my sale and cost record for this transaction to use promo_id 101 instead of the previous promo_id, and then show me the updated sale price and cost details for my reference.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id = 101 WHERE cust_id = 7601 AND prod_id = 28 AND time_id = '2022-05-17' AND channel_id = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET promo_id = 101 WHERE prod_id = 28 AND time_id = '2022-05-17' AND channel_id = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT s.amount_sold, s.quantity_sold, c.unit_cost, c.unit_price, s.promo_id FROM sales s JOIN costs c ON s.prod_id = c.prod_id AND s.time_id = c.time_id AND s.channel_id = c.channel_id WHERE s.cust_id = 7601 AND s.prod_id = 28 AND s.time_id = '2022-05-17' AND s.channel_id = 4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6824",
      instruction="My name is Baxter Colter. Please correct a transaction for my purchase of 'Pro Maple Bat' (prod_id=129) on 2022-02-11. The sales amount_sold should be 151.21 USD instead of 161.21. Update both the sales record (prod_id=129, cust_id=6824, time_id='2022-02-11', channel_id=4, promo_id=999) and the costs record (prod_id=129, time_id='2022-02-11', channel_id=4, promo_id=999) so unit_price matches the correct sales amount. Then, tell me the corrected profit for this transaction (amount_sold - unit_cost).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 151.21 WHERE prod_id = 129 AND cust_id = 6824 AND time_id = '2022-02-11' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 151.21 WHERE prod_id = 129 AND time_id = '2022-02-11' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT 151.21 - unit_cost AS profit FROM costs WHERE prod_id = 129 AND time_id = '2022-02-11' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100002",
      instruction="You are Kaitlyn Conway (user id 100002). You want to place a test sales order for 3 units of product id 2001 ('EcoSmart Blender') on 2024-06-01 via channel id 1 (online), using promotion id 501. The sales amount should use the unit price of 120.00 per product. You also want a cost record created for this transaction with unit cost 90.00 and unit price 120.00, all for date 2024-06-01 and channel id 1 with promo id 501.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (2001, 100002, '2024-06-01', 1, 501, 3, 360.00);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (2001, '2024-06-01', 501, 1, 90.00, 120.00);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="238",
      instruction="You are Mara Weatherford (email: Weatherford@company.example.com, address: 37 Bureau Street, Montpellier, zip code: 79421). You would like to update the product description for all products in the 'Bats' subcategory (prod_subcategory_id=2036) to 'Premium performance baseball bat - verified'. Apply this update to all relevant products.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Weatherford@company.example.com' AND cust_street_address = '37 Bureau Street' AND cust_postal_code = '79421';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_desc = 'Premium performance baseball bat - verified' WHERE prod_subcategory_id = 2036;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100715",
      instruction="Hi, this is Uma Prabu. Before we begin, please confirm that my account number is 100715. I want to activate my Affinity card. Then, I wish to purchase 20 units of the product with prod_id 308 (Premium Cricket Bat), using promotion promo_id 32 through channel_id 4 (Online), and I'd like the sale recorded under the date 2024-06-19. Please process the purchase and update my affinity card status first.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET affinity_card = 1 WHERE cust_id = 100715;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (308, 100715, '2024-06-19', 4, 32, 20, (SELECT prod_list_price FROM products WHERE prod_id = 308) * 20);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="11552",
      instruction="I am Holly Grier (customer ID 11552). Please update my credit limit to $10,000. Also, I want to discontinue the 'Fiber Tape' cricket bat (product ID 31) from my purchases and inventory by setting its status to inactive ('I').",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 10000.00 WHERE cust_id = 11552;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_valid = 'I' WHERE prod_id = 31;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="19022",
      instruction="My name is Rufus Glassman. I recently purchased a 'Team shirt' (South African Team) with product id 41, on the date 2021-01-15, through the Direct Sales channel (channel_id 3) and with promo_id 999. I realized I bought the wrong team's shirt and want to cancel ONLY this specific sale. Please confirm before deleting: Product ID 41, Date 2021-01-15, Channel ID 3, Promo ID 999, for customer id 19022 (me). Proceed with cancellation after confirmation.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 41 AND cust_id = 19022 AND time_id = '2021-01-15' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2484",
      instruction="My name is Deann Dutton and my email is Dutton@company.example.com. For my previous purchase of product id 127 (Genuine Series MIX Wood Bat) on 2019-01-09 via Internet (channel id 4) with promo id 999, please update the unit_cost to 35.55 in the costs table, then show me the updated cost record for that product/date/channel/promo combination.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Dutton@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 35.55 WHERE prod_id = 127 AND time_id = '2019-01-09' AND promo_id = 999 AND channel_id = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM costs WHERE prod_id = 127 AND time_id = '2019-01-09' AND promo_id = 999 AND channel_id = 4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4865",
      instruction="Hi, this is Titus Lindsey. I previously bought the Slugger Youth Series Maple Bat (prod_id 128) using the Internet channel (channel_id 4) on 2019-02-22 and 2019-05-24. I want to update the amount_sold for these purchases in the sales table to 24.99 each, as I saw a new offer. Please also update the related records in the costs table for these two transactions: keep the existing unit_cost but change unit_price to 24.99. My customer ID is 4865.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 24.99 WHERE prod_id = 128 AND cust_id = 4865 AND channel_id = 4 AND time_id IN ('2019-02-22', '2019-05-24');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 24.99 WHERE prod_id = 128 AND channel_id = 4 AND time_id IN ('2019-02-22', '2019-05-24');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1623",
      instruction="My name is Disa Legard (cust_id 1623). Please mark all my purchases of products in the Cricket category after 2020-10-01 as reimbursed for business expenses, by adding a 'Reimbursed: Cricket purchases after 2020-10-01' note in my supplementary demographics comments. Additionally, increase my credit limit from $10,000 to $12,000 to accommodate future reimbursable purchases.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET comments = COALESCE(comments, '') || ' Reimbursed: Cricket purchases after 2020-10-01' WHERE cust_id = 1623;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 12000.0 WHERE cust_id = 1623;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1537",
      instruction="I am Boyd Manning (cust_id 1537) and would like to update my purchase on 2021-04-13 of the 'Indoor Cricket Ball' (prod_id 48), bought via Direct Sales (channel_id 3) and no promotion (promo_id 999). I want to retroactively apply a 10% discount so that amount_sold and unit price should be 11.38 instead of 12.64. Please update the sales record (prod_id 48, cust_id 1537, time_id '2021-04-13', channel_id 3, promo_id 999) to amount_sold=11.38, and the costs record (prod_id 48, time_id '2021-04-13', channel_id 3, promo_id 999) to unit_price=11.38, keeping unit_cost unchanged.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=11.38 WHERE prod_id=48 AND cust_id=1537 AND time_id='2021-04-13' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price=11.38 WHERE prod_id=48 AND time_id='2021-04-13' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="42420",
      instruction="I am Bonnibelle Goode (cust_id=42420), and I'd like to add a sale record for selling 2 units of the SuperBlend Coffee Machine (prod_id=30052) through the Online channel (channel_id=1) on 2024-06-18. The sale used the Father's Day Sale promotion (promo_id=2101), with each unit sold at €159.99, making the total €319.98. The cost per unit to me was €100.00 and the reporting unit price is €159.99. Please add these records accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (30052, 42420, '2024-06-18', 1, 2101, 2, 319.98);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (30052, '2024-06-18', 2101, 1, 100.00, 159.99);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6578",
      instruction="My name is Rufus Killman, and my customer ID is 6578. I’m quite detail-oriented. I recently found an error in the recorded sale of the English Willow Cricket Bat (product ID 28) that I purchased on 2021-10-23. It was recorded through channel ID 2 and promotion ID 999. The system currently shows quantity_sold as 1 and amount_sold as 210.6. It should be quantity_sold 2 and amount_sold 421.2. Also, the costs record for this sale (same prod_id 28, time_id 2021-10-23, channel_id 2, promo_id 999) should have unit_cost 192.0 and unit_price 210.6. Please update both the sales and costs records with these details.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 421.2 WHERE prod_id = 28 AND cust_id = 6578 AND time_id = '2021-10-23' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 192.0, unit_price = 210.6 WHERE prod_id = 28 AND time_id = '2021-10-23' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7329",
      instruction="Hello, I am Pansy Lance (cust_id: 7329). I'd like to update the unit cost to 18.50 and the unit price to 23.50 for my Plastic Cricket Bat (prod_id: 23), bought on 2022-12-08 via channel_id 2 and promo_id 999. Additionally, please record a new sale for a Team shirt (prod_id: 45) for me: date is 2023-01-15, channel_id 3, promo_id 999, quantity_sold 2, amount_sold 95.38.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 18.50, unit_price = 23.50 WHERE prod_id = 23 AND time_id = '2022-12-08' AND promo_id = 999 AND channel_id = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (45, 7329, '2023-01-15', 3, 999, 2, 95.38);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1072",
      instruction="I am Oakes Naber. Please help me return the 'Team shirt' (prod_id: 42) that I bought on 2022-09-12 via Direct Sales (channel_id: 3). Delete the sales record for this transaction (prod_id: 42, cust_id: 1072, time_id: '2022-09-12', channel_id: 3, promo_id: 999). Then, insert a new record in costs for the refund with prod_id: 42, time_id: '2022-09-12', promo_id: 999, channel_id: 3, unit_cost: -37.35, unit_price: -48.77.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 42 AND cust_id = 1072 AND time_id = '2022-09-12' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (42, '2022-09-12', 999, 3, -37.35, -48.77);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1185",
      instruction="My name is Reuben Zanth, and my postal code is 55176. I need to update my previously sold product '6 Gallon Empty Ball Bucket' (prod_id 47). The supplier price has changed, so please set the new product list price and minimum price to $33.50. Also, update the unit_cost to $27.90 and unit_price to $33.50 in the costs table for product 47, for the sale on 2022-02-17 (promo_id 999, channel_id 3).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_first_name = 'Reuben' AND cust_last_name = 'Zanth' AND cust_postal_code = '55176';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = 33.50, prod_min_price = 33.50 WHERE prod_id = 47;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 27.90, unit_price = 33.50 WHERE prod_id = 47 AND time_id = '2022-02-17' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12979",
      instruction="I am Yolanda Reed (email: Reed@company.example.com). Please verify my identity. I want to return the most recent 'Cricket Bat Bag' (prod_id 19) that I purchased via the Partners channel (channel_id 2). After processing the return (deleting this sale and the associated cost record), please update my street address to '1015 New Era Avenue', postal code '62999', city to 'Ryder'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Reed@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT time_id FROM sales WHERE cust_id = 12979 AND prod_id = 19 AND channel_id = 2 ORDER BY time_id DESC LIMIT 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 12979 AND prod_id = 19 AND channel_id = 2 AND time_id = '2020-10-14';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 19 AND channel_id = 2 AND time_id = '2020-10-14';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address = '1015 New Era Avenue', cust_postal_code = '62999', cust_city = 'Ryder' WHERE cust_id = 12979;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7392",
      instruction="You are Reagan Ellis from 47 East Lemhi Road, Montara, CA 55787 (cust_id=7392). You are methodical and meticulous about records. You wish to return your recently purchased 'Indoor Cricket Ball' (prod_id=48), which you bought on 2020-09-17 (channel_id=3, promo_id=999). Additionally, you want to exchange your 'Genuine Series MIX Wood Bat' (prod_id=127), bought on 2020-10-18 (channel_id=3, promo_id=999), for a 'Genuine Series Maple Bat' (prod_id=128) of the same quantity, recording this on the same date and sales channel with a promo_id of 999. For the new bat, use quantity_sold=1, amount_sold=47.26, unit_cost=35.92, and unit_price=47.26. Please update all affected tables accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=7392 AND prod_id=48 AND time_id='2020-09-17' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=48 AND time_id='2020-09-17' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=7392 AND prod_id=127 AND time_id='2020-10-18' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=127 AND time_id='2020-10-18' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (128, 7392, '2020-10-18', 3, 999, 1, 47.26);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (128, '2020-10-18', 999, 3, 35.92, 47.26);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1733",
      instruction="I am Gwynne Grandy from 37 Spink Street, Cloverdale, CA 67272 (cust_id 1733). Please update the following: for the 'Team shirt' with prod_id 40, change the prod_desc to 'West Indies Limited Edition Shirt' and the prod_list_price to 54.99; for the 'Team shirt' with prod_id 42, change the prod_desc to 'New Zealand Cricket World Cup Shirt' and the prod_list_price to 59.99. Apply these updates immediately.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_desc = 'West Indies Limited Edition Shirt', prod_list_price = 54.99 WHERE prod_id = 40;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_desc = 'New Zealand Cricket World Cup Shirt', prod_list_price = 59.99 WHERE prod_id = 42;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100110",
      instruction="I am Dakota Prabu (cust_id=100110). Please delete ALL of my sales transactions for product with prod_id=2005 on the date '2023-11-15'. Additionally, remove the related costs records for the same product (prod_id=2005), date ('2023-11-15'), and promo_id=302.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id = 100110 AND cust_first_name = 'Dakota' AND cust_last_name = 'Prabu';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 100110 AND prod_id = 2005 AND time_id = '2023-11-15';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 2005 AND time_id = '2023-11-15' AND promo_id = 302;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2920",
      instruction="You are Rachel East (cust_id=2920, email=East@company.example.com). On 2019-08-28, you purchased a Team shirt (prod_id=40) through Direct Sales (channel_id=3) with the 'internet promotion #29-350' (promo_id=350). You were incorrectly charged 49.49 EUR, but the discounted list price should have been 44.99 EUR. Please update the corresponding sales record so that amount_sold is 44.99. Also, update the costs table for the same product, date, channel, and promotion so that the unit_price is 44.99 as well.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=44.99 WHERE cust_id=2920 AND prod_id=40 AND time_id='2019-08-28' AND channel_id=3 AND promo_id=350;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price=44.99 WHERE prod_id=40 AND time_id='2019-08-28' AND channel_id=3 AND promo_id=350;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3233",
      instruction="You are Adel Peebles (cust_id: 3233, email: Peebles@company.example.com). For your most recent sale (prod_id: 43, 'Team shirt', purchased on 2022-01-30 via channel_id 3, currently promo_id 999), update the sale and its associated cost record to use the new promotion with promo_id 101 instead of 999. After making these changes, tell me the promo_name for promo_id 101 as confirmation.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Peebles@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id = 101 WHERE cust_id = 3233 AND prod_id = 43 AND time_id = '2022-01-30' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET promo_id = 101 WHERE prod_id = 43 AND time_id = '2022-01-30' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT promo_name FROM promotions WHERE promo_id = 101;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1957",
      instruction="I am Mortimer Valentino (cust_id 1957), from Los Angeles (city_id 51806), email Valentino@company.example.com. I want to return the 6 Gallon Empty Ball Bucket (prod_id 47) I purchased on 2022-12-17 via Internet (channel_id 4, promo_id 999, quantity 1, amount_sold 27.91). Instead, I want to immediately purchase another Pro Maple Youth Bat (prod_id 130) that I bought previously, for the same price as before (114.98), via Direct Sales (channel_id 3), no promotion (promo_id 999), on 2023-05-20, quantity 1.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=1957 AND prod_id=47 AND time_id='2022-12-17' AND channel_id=4 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (130, 1957, '2023-05-20', 3, 999, 1, 114.98);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2885",
      instruction="You are Pansy Edison (email: Edison@company.example.com), detail-focused and careful about your expenses. You recently found an overcharge for your English Willow Cricket Bat purchase on 2020-03-26. You want to: (1) confirm your identity using your email; (2) update the costs table so the unit_price for your purchase of prod_id=28, time_id='2020-03-26', channel_id=3, promo_id=999 matches the prod_list_price 199.99; (3) verify that the unit_price was updated to 199.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Edison@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 199.99 WHERE prod_id = 28 AND time_id = '2020-03-26' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT unit_price FROM costs WHERE prod_id = 28 AND time_id = '2020-03-26' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7809",
      instruction="I am Caspar Dahl (cust_id 7809). I would like to return my purchase of one 'Pro Maple Youth Bat' (prod_id 130) that I bought on 2021-04-22 through the Direct Sales channel (channel_id 3). Please remove this sale and its related cost record for me.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id = 7809"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 7809 AND prod_id = 130 AND time_id = '2021-04-22' AND channel_id = 3"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 130 AND time_id = '2021-04-22' AND channel_id = 3"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1121",
      instruction="You are Pepita Kish (Kish@company.example.com), and you realized a mistake in your recent order record for 'Plastic Cricket Bat' (prod_id: 23) purchased on 2022-12-07 via the Internet channel (channel_id: 4) under no promotion (promo_id: 999). You actually bought 2 units instead of 1. Please update the sales table for this record with quantity_sold=2 and amount_sold=41.0 (both bats together), and adjust the costs table for this entry so that unit_cost=18.7 and unit_price=20.5. Make sure all identifiers and details match: prod_id=23, time_id='2022-12-07', channel_id=4, promo_id=999, cust_id=1121.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email='Kish@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=2, amount_sold=41.0 WHERE prod_id=23 AND cust_id=1121 AND time_id='2022-12-07' AND channel_id=4 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=18.7, unit_price=20.5 WHERE prod_id=23 AND time_id='2022-12-07' AND promo_id=999 AND channel_id=4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3332",
      instruction="You are Bryant Jackson. Your email is Jackson@company.example.com. Please update your street address to '101 New Street' and increase your credit limit to 4000.0. Also, you purchased a 'Team shirt' (prod_id 42) on 2022-11-19 via channel_id 2 and promo_id 999; please process a return for this item by deleting the sale (quantity_sold=1) and its corresponding costs record.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Jackson@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address = '101 New Street' WHERE cust_id = 3332;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 4000.0 WHERE cust_id = 3332;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 42 AND cust_id = 3332 AND time_id = '2022-11-19' AND channel_id = 2 AND promo_id = 999 AND quantity_sold = 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 42 AND time_id = '2022-11-19' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100304",
      instruction="I am Madison Wilbur (cust_id 100304) from Forest Heights. Please delete all my information from your records, including my entire customer profile and any supplementary demographic information. I want all of my data fully erased from your database due to privacy reasons.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM supplementary_demographics WHERE cust_id = 100304;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM customers WHERE cust_id = 100304;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7659",
      instruction="Hi, this is Zel Berry. I have just relocated to 325 Ocean Avenue, Apt 24B, Jacksonville FL 32250 and need my customer profile updated with this new address and postal code. Also, considering I have spent over $1000 this quarter, please increase my credit limit to $12000. My previous address on file was 47 East Ross Road, Palmdale FL 75603.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address='325 Ocean Avenue, Apt 24B', cust_postal_code='32250', cust_city='Jacksonville', cust_state_province='FL' WHERE cust_id=7659;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit=12000.0 WHERE cust_id=7659;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4691",
      instruction="You are Portia Colter (cust_id 4691). You purchased a 'Cricket Bat Bag' (prod_id 19) on 2022-08-25 through the Internet channel (channel_id 4) with no promotion (promo_id 999). You noticed your invoice shows the correct amount should be 60.00 instead of the original 56.65. Please update the corresponding sales record to amount_sold = 60.00, and ensure the costs record's unit_price is updated to 60.00 as well. My details: Portia Colter, Blagnac 77637, cust_id 4691.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=60.00 WHERE cust_id=4691 AND prod_id=19 AND time_id='2022-08-25' AND channel_id=4 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price=60.00 WHERE prod_id=19 AND time_id='2022-08-25' AND channel_id=4 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100102",
      instruction="My name is Connor Zwolinsky (cust_id 100102). I want to add a new purchase record for myself: I bought product prod_id 234 on June 12, 2024 (time_id '2024-06-12'), through channel_id 3, using promo_id 22, quantity 4, amount $512.00. After logging the sale, please also record the associated cost for this product and transaction: prod_id 234, time_id '2024-06-12', promo_id 22, channel_id 3, unit_cost 100.00, unit_price 128.00.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (234, 100102, '2024-06-12', 3, 22, 4, 512.00);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (234, '2024-06-12', 22, 3, 100.00, 128.00);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="17637",
      instruction="You are Emmet Gilmour (cust_id=17637). Please correct the sales and costs records for July 17, 2020 (time_id='2020-07-17') for the 'Team shirt' (prod_id=43, channel_id=3, promo_id=999): set quantity_sold=1, amount_sold=45.71 in sales, and set unit_cost=38.53, unit_price=45.71 in costs. After this, add a new sale and costs entry for 'Cricket Bat Bag' (prod_id=19) on the same day (time_id='2020-07-17'), channel_id=3, promo_id=999, quantity_sold=1, amount_sold=64.07 for sales and unit_cost=53.06, unit_price=64.07 for costs.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=1, amount_sold=45.71 WHERE cust_id=17637 AND prod_id=43 AND time_id='2020-07-17' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=38.53, unit_price=45.71 WHERE prod_id=43 AND time_id='2020-07-17' AND promo_id=999 AND channel_id=3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (19, 17637, '2020-07-17', 3, 999, 1, 64.07);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (19, '2020-07-17', 999, 3, 53.06, 64.07);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6315",
      instruction="My name is Luana Crisp (customer ID: 6315), and my current registered address is 47 Iowa Road, Stockdale, PA 91887. I need to update my main phone number in your records to '555-777-3311'. Also, for product 'Slugger Youth Series Maple Bat' with product ID 128, please change the listed price from $27.99 to $29.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_main_phone_number = '555-777-3311' WHERE cust_id = 6315;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = 29.99 WHERE prod_id = 128;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100834",
      instruction="You are Aidan Cackett and want to purchase 2 units of product with prod_id 110 through the Online channel (channel_id 2) on 2024-06-11. Please retrieve the cost (unit_cost, unit_price) for prod_id 110 on 2024-06-11 with promo_id 5 and channel_id 2 before confirming. If the unit price is acceptable, proceed to add a sales record with cust_id 100834, prod_id 110, time_id '2024-06-11', channel_id 2, promo_id 5, quantity_sold 2, amount_sold = 2 x unit_price.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT unit_cost, unit_price FROM costs WHERE prod_id = 110 AND time_id = '2024-06-11' AND promo_id = 5 AND channel_id = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (110, 100834, '2024-06-11', 2, 5, 2, (SELECT unit_price FROM costs WHERE prod_id = 110 AND time_id = '2024-06-11' AND promo_id = 5 AND channel_id = 2) * 2);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="213",
      instruction="I am Poppy Jacobs (cust_id=213). Please update my street address to '8259 New Arrival Avenue', postal code to '60111', city to 'Subang Jaya', city_id to 51790, and state_province to 'Selangor', state_province_id to 52738. Also, please correct my year of birth to 1995.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address = '8259 New Arrival Avenue', cust_postal_code = '60111', cust_city = 'Subang Jaya', cust_city_id = 51790, cust_state_province = 'Selangor', cust_state_province_id = 52738 WHERE cust_id = 213;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_year_of_birth = 1995 WHERE cust_id = 213;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12083",
      instruction="I am Xavier Polk (Polk@company.example.com), and I want to cancel the duplicate purchase of Linseed Oil (prod_id=30) that was made via the Partners channel (channel_id=2) on 2020-12-02. Please completely remove this transaction, including its sales and costs records. All relevant parameters: cust_id=12083, prod_id=30, channel_id=2, promo_id=999, time_id='2020-12-02'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id=30 AND cust_id=12083 AND time_id='2020-12-02' AND channel_id=2 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=30 AND time_id='2020-12-02' AND channel_id=2 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100373",
      instruction="My name is Dakota Cackett (cust_id=100373), residing at 57 Pierce Drive, Canaseraga, NY 51815. As of today ('2024-06-13'), I want to be completely removed from all your marketing and product lists: (1) Mark my customer profile as invalid by updating 'cust_valid' to 'N' and 'cust_eff_to' to '2024-06-13'; (2) Remove all my records from your 'sales' table; (3) Delete all my supplementary demographic records as well.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_valid='N', cust_eff_to='2024-06-13' WHERE cust_id=100373;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=100373;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM supplementary_demographics WHERE cust_id=100373;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="30604",
      instruction="I am Teri Husky (customer ID 30604) and I want to correct the cost details for my past purchase of Linseed Oil (prod_id 30) from October 23, 2019. Please set the unit cost to 9.50 and the unit price to 12.00 for this record, where the channel was 'Direct Sales' (channel_id 3) and the promotion was 'NO PROMOTION #' (promo_id 999).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=9.50, unit_price=12.00 WHERE prod_id=30 AND time_id='2019-10-23' AND promo_id=999 AND channel_id=3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100404",
      instruction="My name is Adriana Shea. My email is Shea@company.example.com. I want to return the 'Slugger Youth Series Maple Bat' (prod_id: 128) I bought on 2019-10-31 by tele sales (channel_id: 9) with promotion #20-33 (promo_id: 33). Instead, I want to buy 'Linseed Oil' (prod_id: 30) with 1 unit on the same date (2019-10-31), through the same channel (channel_id: 9) and promotion (promo_id: 33), for 9.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Shea@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 100404 AND prod_id = 128 AND time_id = '2019-10-31' AND channel_id = 9 AND promo_id = 33;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (30, 100404, '2019-10-31', 9, 33, 1, 9.99);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="14247",
      instruction="You are Ronald Adams, with the email Adams@company.example.com, and you recently noticed a pricing discrepancy in your records. On 2022-04-20, you purchased the 'Pitching Machine and Batting Cage Combo' (prod_id: 14) via the Direct Sales channel (channel_id: 3) and NO PROMOTION (promo_id: 999). The unit cost should have been 900.00 and the unit price should have been 1200.00 for that date, instead of the recorded values. Please update the 'costs' table for prod_id 14, time_id '2022-04-20', promo_id 999, and channel_id 3 with the new unit_cost 900.00 and unit_price 1200.00. Make sure to authenticate this request belongs to user Ronald Adams (cust_id: 14247).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Adams@company.example.com' AND cust_first_name = 'Ronald' AND cust_last_name = 'Adams';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 900.00, unit_price = 1200.00 WHERE prod_id = 14 AND time_id = '2022-04-20' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5859",
      instruction="You are Wynnee Zimmer, and your email is Zimmer@company.example.com. You purchased a 'Cricket Bat Bag' before (prod_id 19). Please update the list price of 'Cricket Bat Bag' (prod_id 19) in the products table to 59.99 due to a recent price correction.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Zimmer@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = 59.99 WHERE prod_id = 19;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1655",
      instruction="My name is Eve Jewell and my email is Jewell@company.example.com. I recently bought the 'Pro Maple Bat' (product ID 129) online (channel ID 4) on 2020-03-11 with promo ID 999. There is a manufacturer defect and I want a full refund for this purchase (remove the sales record for prod_id 129, cust_id 1655, time_id '2020-03-11', channel_id 4, promo_id 999), and I also need the cost record for this product and date updated to a unit cost of 0 to note the write-off (prod_id 129, time_id '2020-03-11', promo_id 999, channel_id 4). Afterward, can you provide me a summary of the remaining products I have purchased?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Jewell@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 129 AND cust_id = 1655 AND time_id = '2020-03-11' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 0 WHERE prod_id = 129 AND time_id = '2020-03-11' AND promo_id = 999 AND channel_id = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT s.prod_id, p.prod_name, s.time_id, s.quantity_sold, s.amount_sold FROM sales s JOIN products p ON s.prod_id = p.prod_id WHERE s.cust_id = 1655;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6098",
      instruction="My name is Evan Glidden. For my transaction of 'Pro Maple Youth Bat' (prod_id=130) purchased via Internet (channel_id=4) on 2022-08-18 (time_id='2022-08-18'), I actually bought 2 units, not 1. Please update the sales record to set quantity_sold to 2, amount_sold to 197.00, and promo_id to 999 (NO PROMOTION #). Also, update the related costs record for this product, date, channel, and promo to set unit_price to 98.5. My cust_id is 6098, promo_id is 999.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 197.00, promo_id = 999 WHERE cust_id = 6098 AND prod_id = 130 AND time_id = '2022-08-18' AND channel_id = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 98.5 WHERE prod_id = 130 AND time_id = '2022-08-18' AND promo_id = 999 AND channel_id = 4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7667",
      instruction="You are Zylina Cattlett, and your email is Cattlett@company.example.com. You wish to return your 'Pro Maple Youth Bat' (prod_id=130) purchased on 2022-07-21 via channel_id=4 (Internet), promo_id=999, and instead receive a 'Cricket Bat Bag' (prod_id=19) as an exchange. Record 1 unit sold at amount_sold=55.99 (using the product list price) for this same date, channel, and promotion, and update the related cost entry with unit_cost=45.42 and unit_price=55.99 for the exchanged product.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id=130 AND cust_id=7667 AND time_id='2022-07-21' AND channel_id=4 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=130 AND time_id='2022-07-21' AND channel_id=4 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (19, 7667, '2022-07-21', 4, 999, 1, 55.99);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (19, '2022-07-21', 999, 4, 45.42, 55.99);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7991",
      instruction="I am Bailey Hatcher from El Sobrante, CA 59500 (customer id 7991). Please update my record for the product 'Pro Maple Youth Bat' (prod_id 130) that I traded on 2020-06-06 via Direct Sales (channel_id 3) with no promotion (promo_id 999). Change the unit_price to 120.00 and unit_cost to 90.00 for this transaction in the costs table, and also update the products table so that its prod_list_price becomes 120.00 and prod_min_price becomes 90.00.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 120.00, unit_cost = 90.00 WHERE prod_id = 130 AND time_id = '2020-06-06' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = 120.00, prod_min_price = 90.00 WHERE prod_id = 130;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9924",
      instruction="My name is Marshall Rubens. I want to return the 'Pro Maple Youth Bat' (product id 130) that I bought on 2020-06-27 via channel 2 (Partners) under promo 999. Instead, I'd like to purchase 2 'Slugger Youth Series Maple Bat' (product id 128) today (2024-06-05) via Direct Sales (channel_id=3) with no promotion (promo_id=999). Please remove the old sale and its associated cost, and add new sales and costs records for my replacement purchase with the following details: customer id 9924, quantity 2, amount_sold 2 x 27.99, and unit_cost and unit_price as per current product listing. Confirm all changes.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=9924 AND prod_id=130 AND time_id='2020-06-27' AND channel_id=2 AND promo_id=999"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=130 AND time_id='2020-06-27' AND channel_id=2 AND promo_id=999"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (128, 9924, '2024-06-05', 3, 999, 2, 55.98)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (128, '2024-06-05', 999, 3, 27.99, 27.99)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1686",
      instruction="I am Garrett Nappier (Nappier@company.example.com). I noticed there was a cost miscalculation for my purchases of 'Linseed Oil' (prod_id=30). Please update all my cost records for this product where the unit_cost was either 8.85 or 9.31 to now be 10.5 instead. My customer id is 1686. Please ensure you update only the records where the prod_id=30 and previous unit_cost was 8.85 or 9.31.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=10.5 WHERE (unit_cost=8.85 OR unit_cost=9.31) AND prod_id=30 AND (time_id, promo_id, channel_id) IN (SELECT s.time_id, s.promo_id, s.channel_id FROM sales s WHERE s.prod_id=30 AND s.cust_id=1686);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5329",
      instruction="You are a retired coach and have carefully tracked recent purchases made for the youth cricket event. For accounting and recognition, you want to retroactively apply a new promotion to three specific sales made in 2022 via the 'Direct Sales' channel for Team shirts (product_ids: 40, 41, 44), purchased on '2022-03-26', '2022-02-15', and '2022-01-26'. Please add a new promotion with promo_id=555, promo_name='Coach Thank You 2022', promo_subcategory='Cricket Event', promo_subcategory_id=888, promo_category='Special', promo_category_id=7, promo_cost=10.00, promo_begin_date='2022-01-01', promo_end_date='2022-12-31', promo_total='Coach promo total', promo_total_id=22, and update all relevant sales (for cust_id=5329, prod_id in (40,41,44), time_id in ['2022-03-26','2022-02-15','2022-01-26'], channel_id=3) and costs records to reference this new promo_id (555) instead of their previous value.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO promotions (promo_id, promo_name, promo_subcategory, promo_subcategory_id, promo_category, promo_category_id, promo_cost, promo_begin_date, promo_end_date, promo_total, promo_total_id) VALUES (555, 'Coach Thank You 2022', 'Cricket Event', 888, 'Special', 7, 10.00, '2022-01-01', '2022-12-31', 'Coach promo total', 22);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id=555 WHERE cust_id=5329 AND prod_id IN (40, 41, 44) AND time_id IN ('2022-03-26', '2022-02-15', '2022-01-26') AND channel_id=3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET promo_id=555 WHERE prod_id IN (40, 41, 44) AND time_id IN ('2022-03-26', '2022-02-15', '2022-01-26') AND channel_id=3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5427",
      instruction="I am Lucas Gilboy and I recently realized that my purchase of the 'Pro Maple Bat' (prod_id=129) on 2021-10-31 via Direct Sales (channel_id=3) under NO PROMOTION (promo_id=999) had an accounting error. Please update the unit_cost for this cost record to 185.50. My email is Gilboy@company.example.com.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Gilboy@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 185.50 WHERE prod_id = 129 AND time_id = '2021-10-31' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3204",
      instruction="I am Yvette Fairfax (cust_id=3204). I purchased a Team shirt (prod_id=40) on 2020-09-22 (time_id='2020-09-22'), through Direct Sales (channel_id=3) with no promotion (promo_id=999). I noticed I was charged 52.69 (amount_sold), but the product list price is 44.99. Please update my sales record to set amount_sold=44.99 for that transaction. Also, I am eligible for a 10% promotional discount on this order; update the promo_cost in promotions where promo_id=999 to 4.50 to reflect this discount.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=44.99 WHERE cust_id=3204 AND prod_id=40 AND time_id='2020-09-22' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE promotions SET promo_cost=4.50 WHERE promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="33741",
      instruction="I am Harland Maccarthy (cust_id 33741) and I would like to update my email address to eco.harland73@example.com. In addition, please add a note to my account that says 'Prefers eco-friendly products' in the comments section of my supplementary demographics. If a supplementary demographics entry does not exist for me yet, create one with this comment.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_email = 'eco.harland73@example.com' WHERE cust_id = 33741;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT 1 FROM supplementary_demographics WHERE cust_id = 33741;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET comments = 'Prefers eco-friendly products' WHERE cust_id = 33741;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO supplementary_demographics (cust_id, comments) SELECT 33741, 'Prefers eco-friendly products' WHERE NOT EXISTS (SELECT 1 FROM supplementary_demographics WHERE cust_id = 33741);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100537",
      instruction="I am Grace Herold (cust_id 100537), and today (2024-06-21) I purchased 4 units of product 3021 using channel 3 and promo 201. Please record this sale. Also, register a new cost record for product 3021 on the same date, channel 3, promo 201, with a unit cost of $14.00 and a unit price of $20.00. After adding, give me a summary of the product description for product 3021.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (3021, 100537, '2024-06-21', 3, 201, 4, 80.00);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (3021, '2024-06-21', 201, 3, 14.00, 20.00);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT prod_name, prod_desc FROM products WHERE prod_id = 3021;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5040",
      instruction="I am Barnaby Malone from Hiseville. I recently reviewed my direct sale for the Plastic Cricket Bat (prod_id=23) on 2021-12-17 through Direct Sales (channel_id=3) with promotion 999 (promo_id=999). I noticed the unit cost recorded was 21.01, but I have confirmation that the correct unit cost should be 19.99. Please update the cost record for this transaction to reflect the correct unit cost of 19.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_first_name='Barnaby' AND cust_last_name='Malone' AND cust_city='Hiseville';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=19.99 WHERE prod_id=23 AND time_id='2021-12-17' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2238",
      instruction="My name is Ulrick Hammill from Warstein, and on April 5th, 2022, I purchased one '6 Gallon Empty Ball Bucket' (product id 47) online (channel id 4) with no promotion (promo id 999). Please update the unit price for this specific sale in the costs table to 32.99 EUR and confirm that the update has been made immediately.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 32.99 WHERE prod_id = 47 AND time_id = '2022-04-05' AND promo_id = 999 AND channel_id = 4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="10",
      instruction="I'm Gertrude Atkins (cust_id=10) from Blountstown, FL. I'd like to update the product details for my 'Pro Maple Youth Bat' (prod_id=130): please change its prod_name to 'Pro Maple Power Bat', its prod_desc to 'Pro Maple Power Bat, enhanced grip', its prod_list_price to 94.99, and prod_min_price to 94.99. After that, update all my sales (cust_id=10) for this prod_id=130, setting the amount_sold to 129.99 wherever it was previously 125.02 or 127.75, and in the costs table for this prod_id=130, update unit_price to 129.99 wherever it matches the previous values for my records. Ensure all updates happen for the following time_ids associated with my transactions: '2019-05-27', '2019-10-18', '2019-12-18'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_name = 'Pro Maple Power Bat', prod_desc = 'Pro Maple Power Bat, enhanced grip', prod_list_price = 94.99, prod_min_price = 94.99 WHERE prod_id = 130;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 129.99 WHERE prod_id = 130 AND cust_id = 10 AND (time_id = '2019-05-27' OR time_id = '2019-10-18' OR time_id = '2019-12-18') AND (amount_sold = 125.02 OR amount_sold = 127.75);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 129.99 WHERE prod_id = 130 AND (time_id = '2019-05-27' OR time_id = '2019-10-18' OR time_id = '2019-12-18') AND (unit_price = 125.02 OR unit_price = 127.75);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5420",
      instruction="Hi, I am Lotus Alden from Perry, IL, 43866, and my email is Alden@company.example.com. Please help me update the record for my prior purchase of the '6 Gallon Empty Ball Bucket' (prod_id: 47), which was sold to me on 2021-10-30 through the Internet channel (channel_id: 4) under promotion 999. I want to set the unit cost to 32.00 and the unit price to 34.00 for this product in my records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 32.00, unit_price = 34.00 WHERE prod_id = 47 AND time_id = '2021-10-30' AND promo_id = 999 AND channel_id = 4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9729",
      instruction="My name is Gwen Rutherford, my email is Rutherford@company.example.com and I live at 47 North Snyder Road. I recently noticed an error in my records for my purchase of the 'Pro Maple Youth Bat' (product ID 130) on 2021-08-27. The transaction was entered as being through the 'Partners' channel (channel ID 2), but it should have been 'Direct Sales' (channel ID 3). Please update both the sales and costs tables for cust_id 9729, prod_id 130, time_id '2021-08-27', promo_id 999 to set channel_id to 3 instead of 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Rutherford@company.example.com' AND cust_street_address = '47 North Snyder Road';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET channel_id = 3 WHERE cust_id = 9729 AND prod_id = 130 AND time_id = '2021-08-27' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET channel_id = 3 WHERE prod_id = 130 AND time_id = '2021-08-27' AND promo_id = 999 AND channel_id = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3770",
      instruction="You are Page Atkins (Atkins@company.example.com). You want to update the 'Pro Maple Youth Bat' product (prod_id=130) so that for all future records where the product becomes effective after 2022-01-01, both the prod_list_price and prod_min_price should be set to 94.99. Please make this change for me.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id = 3770 AND cust_email = 'Atkins@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = 94.99, prod_min_price = 94.99 WHERE prod_id = 130 AND prod_eff_from > '2022-01-01';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="18386",
      instruction="My name is Belle Lowers and my email is Lowers@company.example.com. For my previous purchase of the 'Plastic Cricket Bat' (product_id 23) on 2020-07-19, I noticed the product description currently says 'Plastic - Beach Cricket Bat', which is incorrect. Please update the description in the products table for prod_id 23 to 'Plastic - Regular Cricket Bat'. After this, tell me my total amount_sold and total cost (where total cost = sum of quantity_sold * unit_cost) for all my purchases of product_id 23 across all sales records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Lowers@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_desc = 'Plastic - Regular Cricket Bat' WHERE prod_id = 23;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT SUM(sales.quantity_sold * costs.unit_cost) AS total_cost, SUM(sales.amount_sold) AS total_amount_sold FROM sales JOIN costs ON sales.prod_id = costs.prod_id AND sales.time_id = costs.time_id AND sales.channel_id = costs.channel_id AND sales.promo_id = costs.promo_id WHERE sales.cust_id = 18386 AND sales.prod_id = 23;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="34678",
      instruction="I am Hugo Alex (cust_id 34678, email Alex@company.example.com). For my tax documentation, I need to correct two sales transactions and their corresponding costs entries. For the 'Slugger Youth Series Maple Bat' (prod_id=128) sold on 2022-03-15 via Direct Sales (channel_id=3) with promo_id=999, please update the sales record to amount_sold=32.21 and the cost record to unit_cost=26.00 and unit_price=32.21. Similarly, for the same product sold on 2022-12-16 via Direct Sales (channel_id=3) with promo_id=999, update the sales record to amount_sold=30.79 and the cost record to unit_cost=25.00 and unit_price=30.79.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Alex@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 32.21 WHERE prod_id = 128 AND cust_id = 34678 AND time_id = '2022-03-15' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 26.00, unit_price = 32.21 WHERE prod_id = 128 AND time_id = '2022-03-15' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 30.79 WHERE prod_id = 128 AND cust_id = 34678 AND time_id = '2022-12-16' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 25.00, unit_price = 30.79 WHERE prod_id = 128 AND time_id = '2022-12-16' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5349",
      instruction="I am Idette Stokley and my registered email is Stokley@company.example.com. I noticed my city name in your records is wrong. Please update my city from 'Alma' to 'Almah' and change my street address from '37 South King Street' to '137 South King Street' in my customer profile (cust_id=5349).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_first_name = 'Idette' AND cust_last_name = 'Stokley' AND cust_email = 'Stokley@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_city = 'Almah' WHERE cust_id = 5349;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address = '137 South King Street' WHERE cust_id = 5349;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="10575",
      instruction="I am Garth Sandburg (cust_id: 10575). I found that for product '6 Gallon Empty Ball Bucket' (prod_id: 47) via the Internet channel (channel_id: 4), the cost record for '2022-11-26' (time_id: '2022-11-26', promo_id: 999) lists unit_cost as 25.10 and unit_price as 28.05, but on '2022-10-15' it should be (unit_cost: 23.46, unit_price: 29.07) for the same channel and promo. Please update the unit_cost and unit_price for the record (prod_id: 47, time_id: '2022-11-26', channel_id: 4, promo_id: 999) to unit_cost 23.46 and unit_price 29.07. Also, please increase my credit limit to 10000.0.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 23.46, unit_price = 29.07 WHERE prod_id = 47 AND time_id = '2022-11-26' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 10000.0 WHERE cust_id = 10575;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6038",
      instruction="I am Chester Charles (cust_id 6038). I want to increase the listed price (prod_list_price) by 10% for every product that I personally bought through Direct Sales (channel_id 3) between 2020-01-01 and 2020-12-31. Please perform this update for each relevant prod_id.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT DISTINCT prod_id FROM sales WHERE cust_id=6038 AND channel_id=3 AND time_id BETWEEN '2020-01-01' AND '2020-12-31';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = prod_list_price * 1.1 WHERE prod_id IN (30, 48, 31, 43, 42, 127);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2506",
      instruction="I am Diamond Pearson, email Pearson@company.example.com. I want to remove my two most recent sales records for '2 Competition Grade NFHS Baseballs' (product ID 46) from my history, with purchase dates '2022-02-25' and '2022-02-17'. Please also remove the corresponding cost records. After doing this, tell me what my new total spent amount is on all Baseballs-category (prod_category_id=203) products. My user ID is 2506.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=2506 AND prod_id=46 AND time_id='2022-02-25';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=2506 AND prod_id=46 AND time_id='2022-02-17';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=46 AND time_id='2022-02-25';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=46 AND time_id='2022-02-17';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT SUM(s.amount_sold) AS total_baseballs_spent FROM sales s JOIN products p ON s.prod_id = p.prod_id WHERE s.cust_id=2506 AND p.prod_category_id=203;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="13905",
      instruction="My name is Annie Lanston, and my customer ID is 13905. I frequently purchase the 'Team shirt' product (product ID: 40). I want to enable price tracking for this product, so that my account will flag if its unit price ever drops below 40.00 EUR in future offers or sales. Please update my supplementary demographics to indicate I wish to track the 'Team shirt' price, including the price threshold (40.00 EUR) in the comments.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET comments = 'Track Team shirt (prod_id 40) price below 40.00 EUR' WHERE cust_id = 13905;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2509",
      instruction="My name is Dinah Ireland (email: Ireland@company.example.com). Please correct a sale record: For product_id=28 (English Willow Cricket Bat), on date 2022-11-30, channel_id=2 (Partners), promo_id=999, update the sales entry so quantity_sold=2 and amount_sold=419.00. Also, update the costs entry for this same sale so unit_cost=160.00 and unit_price=209.50. My customer_id is 2509.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Ireland@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 419.00 WHERE prod_id = 28 AND cust_id = 2509 AND time_id = '2022-11-30' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 160.00, unit_price = 209.50 WHERE prod_id = 28 AND time_id = '2022-11-30' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2484",
      instruction="I am Deann Dutton (cust_id:2484). Please 1) update my income level in my customer profile to 'F: 110,000 - 129,999', 2) remove my oldest sale (Genuine Series MIX Wood Bat, prod_id 127, time_id '2019-01-09', channel_id 4), 3) add a new sale for Cricket Bat Bag (prod_id 19) on 2023-05-10 through the Internet (channel_id 4), promo_id 999, quantity 2, amount_sold per unit as 55.99, 4) change the description of Linseed Oil (prod_id 30) to 'Premium Linseed Oil for Bats'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_income_level = 'F: 110,000 - 129,999' WHERE cust_id = 2484;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 127 AND cust_id = 2484 AND time_id = '2019-01-09' AND channel_id = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (19, 2484, '2023-05-10', 4, 999, 2, 111.98);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_desc = 'Premium Linseed Oil for Bats' WHERE prod_id = 30;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22478",
      instruction="Hi, I'm Rae Edwards (cust_id=22478), currently living at 77 East Modoc Avenue, Yokohama, 37400, Japan. I want to update my income level in your records to 'G: 170,000 - 189,999'. Also, please set my cricket affinity card status (in supplementary_demographics) to active, with affinity_card=1. Lastly, for my sale of product_id=44 ('Team shirt', Indian Cricket Team) made on '2020-09-12' via channel_id=4 and promo_id=999, please correct the unit_cost in the costs table to 36.00. Confirm all these changes, thanks.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_income_level='G: 170,000 - 189,999' WHERE cust_id=22478;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET affinity_card=1 WHERE cust_id=22478;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=36.00 WHERE prod_id=44 AND time_id='2020-09-12' AND promo_id=999 AND channel_id=4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7809",
      instruction="You are Caspar Dahl (cust_id: 7809) from Hiseville, KY. You noticed that the unit cost for your purchase of 'Indoor Cricket Ball' (prod_id 48) on 2021-04-22 through Direct Sales (channel_id 3), with promotion id 999, is higher than expected. Please update the cost record for prod_id 48, time_id '2021-04-22', channel_id 3, promo_id 999 to set the unit_cost to 9.99 instead of the old value. After updating, retrieve and show me the current unit_cost and unit_price for that specific product, time, channel, and promotion.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 9.99 WHERE prod_id = 48 AND time_id = '2021-04-22' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT unit_cost, unit_price FROM costs WHERE prod_id = 48 AND time_id = '2021-04-22' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="19526",
      instruction="You are Harvey Lickey (customer id: 19526). Recently, you bought an 'English Willow Cricket Bat' (product id: 28) on 2020-07-13, and after negotiation, the seller agreed to reduce the price from 225.28 to 210.00 for that transaction. Please update both the 'sales' and 'costs' records for this product and date so the amount_sold and unit_price reflect the new price (210.00) for the matching prod_id (28), time_id (2020-07-13), and cust_id (19526). Additionally, update your supplementary demographics info so 'affinity_card' is set to 1, 'household_size' to '2', and 'yrs_residence' to 6.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 210.00 WHERE cust_id = 19526 AND prod_id = 28 AND time_id = '2020-07-13';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 210.00 WHERE prod_id = 28 AND time_id = '2020-07-13';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET affinity_card = 1, household_size = '2', yrs_residence = 6 WHERE cust_id = 19526;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3915",
      instruction="Hi, my name is Rutherford Overton (email: Overton@company.example.com, cust_id: 3915). I recently updated my marital status from 'married' to 'single' and would like my customer profile to reflect this. Additionally, I made a purchase for 'Pro Maple Bat' (prod_id: 129) on '2021-11-22' through Direct Sales (channel_id: 3, promo_id: 999) and would like to update the purchased quantity from 1 to 2, since I need one more. Please update the marital status and also modify the sales record as described.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_marital_status = 'single' WHERE cust_id = 3915 AND cust_marital_status = 'married';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2 WHERE cust_id = 3915 AND prod_id = 129 AND time_id = '2021-11-22' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="134",
      instruction="My name is Heidi Kidwell, email heidi.kidwell@company2.example.com, and I noticed that I accidentally recorded a sale for a Team shirt (prod_id 43) on 2019-01-30 through Direct Sales (channel_id 3) with promo_id 999. Please delete both the sales and costs records for this product, on that date, for my customer ID (134), with the given channel and promotion.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'heidi.kidwell@company2.example.com' AND cust_first_name = 'Heidi' AND cust_last_name = 'Kidwell'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 134 AND prod_id = 43 AND time_id = '2019-01-30' AND channel_id = 3 AND promo_id = 999"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 43 AND time_id = '2019-01-30' AND channel_id = 3 AND promo_id = 999"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9053",
      instruction="My name is Michael Vail and my email is Vail@company.example.com. I want to request a refund for a defective 'Team shirt' (South African Team, prod_id 41) that I bought on 2020-07-17 through Direct Sales (channel_id 3), promo_id 999. Please remove this purchase record from my history and also adjust the costs accordingly. Here are all the relevant details: cust_id 9053, prod_id 41, time_id '2020-07-17', channel_id 3, promo_id 999.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Vail@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 41 AND cust_id = 9053 AND time_id = '2020-07-17' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 41 AND time_id = '2020-07-17' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2252",
      instruction="You are Vale King (King@company.example.com, cust_id 2252). For your sale of the Pro Maple Youth Bat (prod_id 130) made on 2020-05-15 via Direct Sales (channel_id 3, promo_id 999), please update the sales record to set quantity_sold to 2 and amount_sold to 228.66. Also, update the related costs record for this product/time/channel/promo to set unit_cost to 90.00 and unit_price to 115.00.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id=2252 AND cust_email='King@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=2, amount_sold=228.66 WHERE prod_id=130 AND cust_id=2252 AND time_id='2020-05-15' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=90.00, unit_price=115.00 WHERE prod_id=130 AND time_id='2020-05-15' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2159",
      instruction="My name is Horatio Ivy and my email is Ivy@company.example.com. Please authenticate me. I need to return two items: my 'Team shirt' (prod_id: 45, purchased on 2021-06-26 via channel_id 3 and promo_id 999) and my most recent 'Slugger Youth Series Maple Bat' purchase (prod_id: 128, purchased on 2021-06-24 via channel_id 3 and promo_id 999). Remove both trades and their associated cost records from your system for my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Ivy@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 45 AND time_id = '2021-06-26' AND cust_id = 2159 AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 45 AND time_id = '2021-06-26' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 128 AND time_id = '2021-06-24' AND cust_id = 2159 AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 128 AND time_id = '2021-06-24' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6490",
      instruction="My name is Randal Zoldos and my customer ID is 6490. I want to update the product information for the English Willow Cricket Bat that I previously purchased (prod_id = 28). Please set the prod_list_price to 225.50 and the prod_min_price to 210.00.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id = 6490;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = 225.50, prod_min_price = 210.00 WHERE prod_id = 28;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4108",
      instruction="My name is Zillah Driscoll and my email is Driscoll@company.example.com. On 2020-09-14, I purchased a 'Cricket Bat Bag' (product ID 19) through Direct Sales (channel ID 3) with promo ID 999, but I meant to buy two 'Team shirts' (product ID 40) instead on the same date and channel. Please (1) delete my sale and cost records for the Cricket Bat Bag on 2020-09-14, channel 3, promo 999, and (2) insert sales and cost records for two 'Team shirts' on 2020-09-14, channel 3, promo 999, quantity 2, using unit_cost 42.63 and unit_price 52.69 per shirt.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Driscoll@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 19 AND cust_id = 4108 AND time_id = '2020-09-14' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 19 AND time_id = '2020-09-14' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (40, 4108, '2020-09-14', 3, 999, 2, 105.38);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (40, '2020-09-14', 999, 3, 42.63, 52.69);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7086",
      instruction="You are Heath Chan (cust_id 7086). You realized that your purchase of 'Linseed Oil' (prod_id 30) made on 2019-09-03 via channel Partners (channel_id 2), for 1 unit with promo_id 999, was for an old formula and you want to cancel just this trade. Please remove this trade and issue a refund of the full amount (10.79) to your credit balance. Then, record a new trade of 'Linseed Oil' (prod_id 30), for 1 unit, with the latest product details (unit_price 9.99, unit_cost 9.99 from products table) on the same date (2019-09-03), same channel (channel_id 2), with no promotion (promo_id 999). Apply both sales and costs records for this corrected trade.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 7086 AND prod_id = 30 AND time_id = '2019-09-03' AND channel_id = 2 AND promo_id = 999 AND quantity_sold = 1 AND amount_sold = 10.79"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 30 AND time_id = '2019-09-03' AND channel_id = 2 AND promo_id = 999"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = cust_credit_limit + 10.79 WHERE cust_id = 7086"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (30, 7086, '2019-09-03', 2, 999, 1, 9.99)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (30, '2019-09-03', 999, 2, 9.99, 9.99)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7335",
      instruction="I am Dione Cummins (customer ID: 7335, email: Cummins@company.example.com) from Arbuckle, CA 67843. I bought a 'Team shirt' (product ID: 40) via Direct Sales (channel ID: 3) with no promotion (promotion ID: 999) on 2020-09-29, but the quantity should have been 2, not 1. Please update the sales record for that transaction (product ID: 40, customer ID: 7335, time ID: 2020-09-29, channel ID: 3, promo ID: 999) to quantity_sold = 2 and amount_sold = 105.38 (which is 52.69 * 2). Also, please add to my supplementary demographics (cust_id: 7335): education='Bachelor', occupation='Manager', household_size='3', yrs_residence=5, affinity_card=1, cricket=1, baseball=0, tennis=0, soccer=0, golf=0, unknown=0, misc=0, comments='Active cricket fan and regular buyer'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 105.38 WHERE prod_id = 40 AND cust_id = 7335 AND time_id = '2020-09-29' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO supplementary_demographics (cust_id, education, occupation, household_size, yrs_residence, affinity_card, cricket, baseball, tennis, soccer, golf, unknown, misc, comments) VALUES (7335, 'Bachelor', 'Manager', '3', 5, 1, 1, 0, 0, 0, 0, 0, 0, 'Active cricket fan and regular buyer');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="8858",
      instruction="My name is Calbert Rider from Saint-Brieuc. Please update my profile with my new phone number: 331-999-8888 and correct my year of birth to 1943 (it was set to 1944 by mistake). Additionally, I would like to change the quantity purchased for my 'English Willow Cricket Bat' (product id 28) order from 2021-02-10 in the Direct Sales channel (channel_id 3, promo_id 999) from 1 to 2 units, as I intended to order two bats. My customer ID is 8858.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_main_phone_number = '331-999-8888' WHERE cust_id = 8858;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_year_of_birth = 1943 WHERE cust_id = 8858;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2 WHERE prod_id = 28 AND cust_id = 8858 AND time_id = '2021-02-10' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="11904",
      instruction="My name is Royden Barrett (customer ID 11904, email: Barrett@company.example.com). Please update all of my costs records for the Indoor Cricket Ball (prod_id 48) to set unit_cost = 9.99 and unit_price = 11.99. The affected records are for time_id '2022-09-17', channel_id 2, promo_id 999; time_id '2022-01-17', channel_id 3, promo_id 999; and time_id '2022-09-17', channel_id 3, promo_id 999. Update each matching record in the costs table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_first_name = 'Royden' AND cust_last_name = 'Barrett' AND cust_email = 'Barrett@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 9.99, unit_price = 11.99 WHERE prod_id = 48 AND time_id = '2022-09-17' AND promo_id = 999 AND channel_id = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 9.99, unit_price = 11.99 WHERE prod_id = 48 AND time_id = '2022-01-17' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 9.99, unit_price = 11.99 WHERE prod_id = 48 AND time_id = '2022-09-17' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1868",
      instruction="My name is Louis Smeed (cust_id: 1868, email: Smeed@company.example.com). I want to return the 'Linseed Oil' (prod_id: 30) that I bought on 2020-11-12. Please delete my trade records for this purchase from both the sales and costs tables (where channel_id is 3 and promo_id is 999), and update the status of this product to 'RETURNED' in the products table. All relevant parameters: prod_id=30, cust_id=1868, time_id='2020-11-12', channel_id=3, promo_id=999.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id=1868 AND cust_email='Smeed@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id=30 AND cust_id=1868 AND time_id='2020-11-12' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=30 AND time_id='2020-11-12' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_status='RETURNED' WHERE prod_id=30;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1598",
      instruction="I am Debbie Grier, customer ID 1598. Please update my sales record for my purchase of the 'Indoor Cricket Ball' (product ID 48), bought on 2021-10-12 via the Partners channel (channel_id 2) and no promotion (promo_id 999). Change the quantity sold to 2 units and set the amount sold to $25.52. Also, update the related costs record for that day so that unit_cost is $22.36 (double $11.18) and unit_price is $25.52 (double $12.76). Ensure this change only applies to my customer ID and these exact parameters.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 25.52 WHERE prod_id = 48 AND cust_id = 1598 AND time_id = '2021-10-12' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 22.36, unit_price = 25.52 WHERE prod_id = 48 AND time_id = '2021-10-12' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4924",
      instruction="You are Van Leary (cust_id: 4924) and your email is Leary@company.example.com. You recently found that you were charged 222.17 GBP for your English Willow Cricket Bat (prod_id: 28) purchased on 2020-08-19 and 2020-10-19 through channel_id 3 (Direct Sales), whereas the same product on 2020-10-19 through channel_id 2 (Partners) was only 203.18 GBP. Please adjust the sales records on 2020-08-19 and 2020-10-19 through channel_id 3 so that the amount_sold matches the lower price of 203.18 GBP. Also, update the corresponding costs table records (unit_price) for these purchases to 203.18.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Leary@company.example.com'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 203.18 WHERE prod_id = 28 AND cust_id = 4924 AND time_id = '2020-08-19' AND channel_id = 3 AND amount_sold = 222.17"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 203.18 WHERE prod_id = 28 AND cust_id = 4924 AND time_id = '2020-10-19' AND channel_id = 3 AND amount_sold = 222.17"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 203.18 WHERE prod_id = 28 AND time_id = '2020-08-19' AND channel_id = 3"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 203.18 WHERE prod_id = 28 AND time_id = '2020-10-19' AND channel_id = 3"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="8785",
      instruction="I am Fred Hamilton (Hamilton@company.example.com). I want to correct two things in my trade records: (1) For my purchase of the 'West Indies Team shirt' (product id 40) made on 2020-06-22 via Direct Sales (channel id 3), the sale should be updated to show I used the TV promotion #13-351 (promo id 351), not no promotion; please change the promo_id on this sales record to 351. (2) For my purchase of the '6 Gallon Empty Ball Bucket' (product id 47) made on 2022-12-17 via Internet (channel id 4), the recorded amount_sold should be the product's list price, 28.99; please update this record to amount_sold=28.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Hamilton@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id = 351 WHERE prod_id = 40 AND cust_id = 8785 AND time_id = '2020-06-22' AND channel_id = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 28.99 WHERE prod_id = 47 AND cust_id = 8785 AND time_id = '2022-12-17' AND channel_id = 4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3445",
      instruction="My name is Francis Hamrick (customer id 3445), and I need to correct a trade record. On 2022-12-20, I purchased the 'Team shirt' for the Australian Cricket Team (product id 43) through Direct Sales (channel id 3) using the TV promotion #13-351 (promo_id 351), but the recorded quantity sold is 1. It should actually be 2 units, with the amount sold being 97.60. The cost per unit should be updated to 38.18 and the unit price to 48.80, according to my records. Please update both the sales and the costs tables for this entry.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id = 3445;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 97.60 WHERE prod_id = 43 AND cust_id = 3445 AND time_id = '2022-12-20' AND channel_id = 3 AND promo_id = 351;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 38.18, unit_price = 48.80 WHERE prod_id = 43 AND time_id = '2022-12-20' AND channel_id = 3 AND promo_id = 351;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3789",
      instruction="I am Persis Jewell (cust_id 3789), residing at 37 West Traverse Street, Weissport, PA 46744. On July 10, 2022, I purchased one Linseed Oil (prod_id 30) via the Internet channel (channel_id 4) and no promotion (promo_id 999). I noticed that the recorded amount sold was $10.10 but it should have been $12.50. Please update the 'sales' record for cust_id 3789, prod_id 30, time_id '2022-07-10', channel_id 4, promo_id 999 to amount_sold 12.50. Also, update the 'costs' table for prod_id 30, time_id '2022-07-10', promo_id 999, channel_id 4 to set unit_price to 12.50 to reflect the correction.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 12.50 WHERE cust_id = 3789 AND prod_id = 30 AND time_id = '2022-07-10' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 12.50 WHERE prod_id = 30 AND time_id = '2022-07-10' AND promo_id = 999 AND channel_id = 4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1571",
      instruction="My name is Camilla Rohrback, I live at 37 Pasco Street, Hiseville, KY, 69776, and my email is Rohrback@company.example.com. I would like to remove all sales and cost records for every purchase I made of the product 'English Willow Cricket Bat' (product id 28). Please ensure that all corresponding entries are deleted from both the sales and costs tables, specifically for my customer id 1571 and product id 28, including all time_id, channel_id, and promo_id as relevant for these sales.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_first_name = 'Camilla' AND cust_last_name = 'Rohrback' AND cust_street_address = '37 Pasco Street' AND cust_postal_code = '69776' AND cust_city = 'Hiseville' AND cust_email = 'Rohrback@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 1571 AND prod_id = 28;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 28 AND (time_id, promo_id, channel_id) IN (SELECT time_id, promo_id, channel_id FROM sales WHERE cust_id = 1571 AND prod_id = 28);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7534",
      instruction="My name is Tobin Colter. Please help me with the following: I recently purchased one 'Slugger Youth Series Maple Bat' (product ID 128) on 2022-10-11 via channel 3, promo 999, and I want to return this purchase (remove it from my record). Instead, I want to buy two '6 Gallon Empty Ball Bucket' (product ID 47), sold via channel 3, with promo 999, on today's date (2024-06-15), and please use the listed product price of 28.99 for both amount_sold and cost. Please update my records accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_first_name = 'Tobin' AND cust_last_name = 'Colter' AND cust_id = 7534;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 7534 AND prod_id = 128 AND time_id = '2022-10-11' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (47, 7534, '2024-06-15', 3, 999, 2, 57.98);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (47, '2024-06-15', 999, 3, 28.99, 28.99);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6397",
      instruction="I am Morel Sullivan (email: Sullivan@company.example.com). On 2019-03-27, I purchased a Pro Maple Youth Bat (prod_id 130) through the Internet channel (channel_id 4) with no promotion (promo_id 999). I realized I meant to buy a Pro Maple Bat (prod_id 129) instead. Please update the corresponding sales and costs records so the purchase is for prod_id 129 on 2019-03-27 through channel 4, promo 999. The customer id is 6397 and all other values (quantity, amount, unit_cost, unit_price) should remain the same as in the original transaction.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_id = 6397 AND cust_email = 'Sullivan@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET prod_id = 129 WHERE prod_id = 130 AND cust_id = 6397 AND time_id = '2019-03-27' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET prod_id = 129 WHERE prod_id = 130 AND time_id = '2019-03-27' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="30381",
      instruction="You are Maynard Lengel from Magdeburg (cust_id=30381), who values record accuracy and gifts. You recently purchased 1 'Pro Maple Youth Bat' (prod_id=130) on 2021-07-04 via the Partners channel (channel_id=2), promo_id=999, for 95.66 EUR. You've decided to buy one more for a friend, so you want to update your sales record for this transaction: set quantity_sold to 2 and amount_sold to 191.32 EUR. Ensure the correct record is modified, and that only sales (not costs) are changed. Confirm the operation is done for: prod_id=130, cust_id=30381, time_id='2021-07-04', channel_id=2, promo_id=999.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 191.32 WHERE prod_id = 130 AND cust_id = 30381 AND time_id = '2021-07-04' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100021",
      instruction="My name is Cole Cackett and my customer ID is 100021. Please update my supplementary demographics record: set 'baseball' to 0, set 'soccer' to 1, set 'occupation' to 'Senior Exec.', and update 'comments' to 'Please update my primary sport preference to soccer as my family joined a local soccer league. Also, note my recent job promotion.'",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET baseball = 0 WHERE cust_id = 100021;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET soccer = 1 WHERE cust_id = 100021;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET occupation = 'Senior Exec.' WHERE cust_id = 100021;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET comments = 'Please update my primary sport preference to soccer as my family joined a local soccer league. Also, note my recent job promotion.' WHERE cust_id = 100021;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2417",
      instruction="I am Bo Lyon (cust_id 2417). I want to update the purchase of the 'Pro Maple Bat' (prod_id 129) that I made on 2019-10-11 (time_id '2019-10-11'), channel_id 2, promo_id 999. Please change the sale amount and the recorded unit price to 150.00 in both the sales and costs records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 150.00 WHERE prod_id = 129 AND time_id = '2019-10-11' AND promo_id = 999 AND channel_id = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 150.00 WHERE prod_id = 129 AND cust_id = 2417 AND time_id = '2019-10-11' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1169",
      instruction="You are Raymond Early, customer id 1169. You want to return one 'Indoor Cricket Ball' (product id 48) purchased on 2020-05-15, which means removing the sales and associated cost record for product id 48, customer id 1169, time_id '2020-05-15', channel_id 3, promo_id 999. After doing this, show your updated total amount spent on products in the 'Cricket' category (category_id 205).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 48 AND cust_id = 1169 AND time_id = '2020-05-15' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 48 AND time_id = '2020-05-15' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT SUM(amount_sold) FROM sales INNER JOIN products ON sales.prod_id = products.prod_id WHERE sales.cust_id = 1169 AND products.prod_category_id = 205;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3026",
      instruction="I am Rutherford Callihan (cust_id 3026) from Molino, FL. I recently received a salary bump, so I want to update my credit limit to $4,500.00. Right after that, show me my most recent sales transactions for products in the 'Cricket Bat' subcategory (prod_subcategory = 'Cricket Bat'), including product names and sale dates. Please process the credit limit update first, then provide the latest Cricket Bat purchases.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 4500.00 WHERE cust_id = 3026;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT s.time_id, p.prod_name, s.quantity_sold, s.amount_sold FROM sales s INNER JOIN products p ON s.prod_id = p.prod_id INNER JOIN times t ON s.time_id = t.time_id WHERE s.cust_id = 3026 AND p.prod_subcategory = 'Cricket Bat' ORDER BY s.time_id DESC;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4806",
      instruction="You are Sabina Napper. On 2020-11-09, you purchased the product 'Pro Maple Youth Bat' (prod_id: 130) via Direct Sales (channel_id: 3) without any promotion (promo_id: 999). You have noticed the unit cost recorded for this purchase is incorrect and should be updated to 82.00. Please update the 'costs' table so that for product 130, date '2020-11-09', promo_id 999, and channel_id 3, the unit_cost is set to 82.00.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 82.00 WHERE prod_id = 130 AND time_id = '2020-11-09' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4962",
      instruction="I am Worth Blankenship (cust_id=4962). Please update my credit limit to 2200.00 and change my marital status to 'married' in my account. Also, I need my previous sale for the 'Indoor Cricket Ball' (prod_id=48) from 2021-01-24 via Direct Sales (channel_id=3), which currently has no promotion (promo_id=999), to be associated with the new promotion promo_id=12 instead. Update any related costs record for this product, date, and channel so that it uses promo_id=12 as well.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 2200.00 WHERE cust_id = 4962;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_marital_status = 'married' WHERE cust_id = 4962;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id = 12 WHERE cust_id = 4962 AND prod_id = 48 AND time_id = '2021-01-24' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET promo_id = 12 WHERE prod_id = 48 AND time_id = '2021-01-24' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22750",
      instruction="Hi, I'm Xavier Polk (customer ID 22750). I recently checked my account and noticed an error in my purchase records. On 2020-12-30, for the 'Indoor Cricket Ball' (prod_id 48), the sales record under Direct Sales (channel_id 3) and promotion NO PROMOTION (promo_id 999) shows I bought 1 unit, but I actually purchased 2 units. Please update the sales record to reflect quantity_sold=2 and amount_sold=27.32 accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 27.32 WHERE cust_id = 22750 AND prod_id = 48 AND time_id = '2020-12-30' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4240",
      instruction="I am Candice Lotto (cust_id=4240, candice email: Lotto@company.example.com). On my purchase dated 2020-10-28, I bought a Team shirt (prod_id=43) through Direct Sales (channel_id=3) and was charged $51.96, but there was supposed to be a $7 discount so the correct amount should be $44.96. Please: (1) update the sales record for cust_id=4240, prod_id=43, time_id='2020-10-28', channel_id=3, promo_id=999 to amount_sold=44.96; (2) update the costs table for prod_id=43, time_id='2020-10-28', promo_id=999, channel_id=3 to unit_price=44.96; and (3) show me the updated sales and costs records for that product/date/channel.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=44.96 WHERE cust_id=4240 AND prod_id=43 AND time_id='2020-10-28' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price=44.96 WHERE prod_id=43 AND time_id='2020-10-28' AND promo_id=999 AND channel_id=3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM sales WHERE cust_id=4240 AND prod_id=43 AND time_id='2020-10-28' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM costs WHERE prod_id=43 AND time_id='2020-10-28' AND promo_id=999 AND channel_id=3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5356",
      instruction="You are Ines Hanson (email Hanson@company.example.com, customer ID 5356). You recently moved and want to update your contact info: change your street address to '123 Newfield Close', your city to 'Oxford' (city_id 51699), your postal code to 'OX1 1YZ', your state to 'England - Oxfordshire' (state_province_id 52592), and your main phone number to '555-333-1212'. Please update all these fields in your customer record.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Hanson@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address = '123 Newfield Close', cust_city = 'Oxford', cust_city_id = 51699, cust_state_province = 'England - Oxfordshire', cust_state_province_id = 52592, cust_postal_code = 'OX1 1YZ', cust_main_phone_number = '555-333-1212' WHERE cust_id = 5356;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="183",
      instruction="Hi, I'm Michelle Early (email: michelle.early@company2.example.com). I noticed on my order for the 'Pro Maple Youth Bat' (prod_id: 130) from 2020-04-05, the unit_cost was recorded as 70.55, but the correct cost should have been 65.00. Please update the unit_cost to 65.00 for that exact product (prod_id: 130) on 2020-04-05, with promo_id: 999 and channel_id: 4. Also, I want to lower my credit limit from 9000.0 to 7000.0 for safety. My customer ID is 183.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 65.00 WHERE prod_id = 130 AND time_id = '2020-04-05' AND promo_id = 999 AND channel_id = 4 AND unit_cost = 70.55;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 7000.0 WHERE cust_id = 183 AND cust_credit_limit = 9000.0;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1524",
      instruction="You are Blenda Vale (email: Vale@company.example.com) from Moerdijk. Authenticate with your email. Then, show details (product name, price paid, purchase date, sales channel) for all Baseball bats you've bought since 2021-01-01. For your most recent Baseball bat purchase, update its sales channel from Internet (channel_id=4) to Direct Sales (channel_id=3) in the sales table. Also, for this record, decrease its unit_cost in the costs table by 10% (set unit_cost = unit_cost * 0.9).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Vale@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT s.prod_id, p.prod_name, s.amount_sold, s.time_id, c.channel_desc FROM sales s JOIN products p ON s.prod_id = p.prod_id JOIN channels c ON s.channel_id = c.channel_id WHERE s.cust_id = 1524 AND p.prod_category = 'Baseball' AND (p.prod_subcategory LIKE '%Bat%' OR p.prod_subcategory LIKE '%Bats%') AND s.time_id >= '2021-01-01';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT s.prod_id, s.time_id, s.promo_id, s.channel_id FROM sales s JOIN products p ON s.prod_id = p.prod_id WHERE s.cust_id = 1524 AND p.prod_category = 'Baseball' AND (p.prod_subcategory LIKE '%Bat%' OR p.prod_subcategory LIKE '%Bats%') AND s.time_id >= '2021-01-01' ORDER BY s.time_id DESC LIMIT 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET channel_id = 3 WHERE cust_id = 1524 AND prod_id = 130 AND time_id = '2022-03-27' AND channel_id = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = unit_cost * 0.9 WHERE prod_id = 130 AND time_id = '2022-03-27' AND promo_id = 999 AND channel_id = 4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1419",
      instruction="You are Xerxes Abbassi (cust_id 1419). You want to update your supplementary demographics: set education to 'Graduate Degree', occupation to 'Coach', household_size to '2', yrs_residence to 5, affinity_card to 1, cricket to 1, baseball to 1, tennis to 0, soccer to 0, golf to 0, unknown to 0, misc to 0, and comments to 'Updated info for coaching and hobbies'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT 1 FROM supplementary_demographics WHERE cust_id = 1419"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET education = 'Graduate Degree', occupation = 'Coach', household_size = '2', yrs_residence = 5, affinity_card = 1, cricket = 1, baseball = 1, tennis = 0, soccer = 0, golf = 0, unknown = 0, misc = 0, comments = 'Updated info for coaching and hobbies' WHERE cust_id = 1419"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3618",
      instruction="My name is Liane Malone, and I want to correct a past transaction. Please update my sales record where prod_id=101, time_id='2023-08-15', channel_id=2, promo_id=5 to use prod_id=205 instead, as the wrong product was registered. Also, update the related costs record for the same transaction so that prod_id=205 is used instead of prod_id=101. My customer ID is 3618.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id=3618 AND cust_first_name='Liane' AND cust_last_name='Malone';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET prod_id=205 WHERE cust_id=3618 AND prod_id=101 AND time_id='2023-08-15' AND channel_id=2 AND promo_id=5;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET prod_id=205 WHERE prod_id=101 AND time_id='2023-08-15' AND promo_id=5 AND channel_id=2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9608",
      instruction="My name is Deloris Eaton (cust_id 9608). While checking my recent purchases, I realized that I have accidentally ordered the 'Slugger Youth Series Maple Bat' (prod_id 128) twice: once on 2021-07-15 and once again on 2021-08-15. I only need one, so please remove the most recent purchase, which is on 2021-08-15, from my records. The product details are prod_id 128, ordered via channel_id 2, promotion id 999. I want the purchase and all its costs data fully removed from my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 128 AND cust_id = 9608 AND time_id = '2021-08-15' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 128 AND time_id = '2021-08-15' AND promo_id = 999 AND channel_id = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5525",
      instruction="You are Roy Stockman (cust_id 5525, email Stockman@company.example.com). On 2019-09-08 you purchased 1 English Willow Cricket Bat (prod_id 28) through Direct Sales (channel_id 3) with no promotion (promo_id 999). You realized you actually wanted to purchase 2 instead of 1 and wish to update the sales record for that purchase on 2019-09-08 to quantity_sold = 2 and amount_sold = 432.76 (2 * 216.38). You also need the corresponding costs entry updated: set unit_cost = 180.00 and unit_price = 216.38 for this (prod_id=28, time_id='2019-09-08', promo_id=999, channel_id=3). Please make sure both tables are updated accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 432.76 WHERE prod_id = 28 AND cust_id = 5525 AND time_id = '2019-09-08' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 180.00, unit_price = 216.38 WHERE prod_id = 28 AND time_id = '2019-09-08' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12526",
      instruction="You are Lolita Kaden (cust_id=12526). Please correct the sales record for your purchase of the 'Genuine Series MIX Wood Bat' (prod_id=127): change the sale and cost date from '2020-12-22' to '2020-12-20'. This record uses channel_id=3 and promo_id=999. All other information remains the same.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET time_id = '2020-12-20' WHERE cust_id = 12526 AND prod_id = 127 AND time_id = '2020-12-22' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET time_id = '2020-12-20' WHERE prod_id = 127 AND time_id = '2020-12-22' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="17081",
      instruction="You are Nora Marker, email Marker@company.example.com. You noticed an error in your cost records. For the product 'Pro Maple Youth Bat' (prod_id=130), for the trade on 2020-02-27 (time_id='2020-02-27'), channel 'Direct Sales' (channel_id=3), under 'NO PROMOTION #' (promo_id=999), please update the unit_cost to 79.99 and unit_price to 120.00.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 79.99, unit_price = 120.00 WHERE prod_id = 130 AND time_id = '2020-02-27' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="473",
      instruction="You are Gala Lockhard (email gala.lockhard@company2.example.com). You recently discovered that the sale record for 'Slugger Youth Series Maple Bat' (prod_id 128) sold to you on 2022-07-27 via Direct Sales (channel_id 3), using promotion id 999, was incorrectly recorded: the actual amount sold should be 25.73, not 30.73. Please update the sales record in the database for prod_id 128, cust_id 473, time_id '2022-07-27', channel_id 3, promo_id 999, and set amount_sold to 25.73. Also, update the related costs table record for the same prod_id, time_id '2022-07-27', promo_id 999, channel_id 3, and set unit_price to 25.73.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_first_name = 'Gala' AND cust_last_name = 'Lockhard' AND cust_email = 'gala.lockhard@company2.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 25.73 WHERE prod_id = 128 AND cust_id = 473 AND time_id = '2022-07-27' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 25.73 WHERE prod_id = 128 AND time_id = '2022-07-27' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5590",
      instruction="My name is Rae Taylor and I previously bought the 'Cricket Bat Bag' (prod_id=19). I would like to update its product listing so that both the prod_list_price and prod_min_price are increased by 5 units. Please update the products table for prod_id=19 to reflect these new prices.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = prod_list_price + 5, prod_min_price = prod_min_price + 5 WHERE prod_id = 19;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9164",
      instruction="You are Raphaela Williamson (Williamson@company.example.com). On 2019-09-07, you purchased a 'Team shirt' (product_id 45, English Cricket Team) via the Internet (channel_id 4) with promo_id 999 and were charged $47.45 instead of $44.99. Please: (1) Update the sales record for prod_id=45, cust_id=9164, time_id='2019-09-07', channel_id=4, promo_id=999 to set amount_sold to 44.99; (2) Update the corresponding costs record (prod_id=45, time_id='2019-09-07', channel_id=4, promo_id=999) to set unit_price to 44.99, keeping unit_cost unchanged.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Williamson@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 44.99 WHERE prod_id = 45 AND cust_id = 9164 AND time_id = '2019-09-07' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 44.99 WHERE prod_id = 45 AND time_id = '2019-09-07' AND channel_id = 4 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2019",
      instruction="Hi, this is Phyllis Clatterbuck from Solingen, postal code 38432. I found an error in my previous purchase record for the English Willow Cricket Bat (prod_id 28), bought on 2022-07-19 via Direct Sales (channel_id 3) with promo_id 999. Please update the costs entry for that purchase to unit_cost 160.50 and unit_price 210.00. Also, correct the sales record for that same purchase to amount_sold 210.00 and quantity_sold 1.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_first_name = 'Phyllis' AND cust_last_name = 'Clatterbuck' AND cust_postal_code = '38432';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 160.50, unit_price = 210.00 WHERE prod_id = 28 AND time_id = '2022-07-19' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 210.00, quantity_sold = 1 WHERE prod_id = 28 AND cust_id = 2019 AND time_id = '2022-07-19' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3320",
      instruction="I am Brant Kitts (email Kitts@company.example.com). On 2022-12-31, I incorrectly recorded a sale for 1 unit of '6 Gallon Empty Ball Bucket' (prod_id=47), sold via Direct Sales (channel_id=3) under promotion promo_id=351, with amount_sold=28.77. The associated cost recorded was unit_cost=23.23 and unit_price=28.77. Please delete both this sales record (cust_id=3320, prod_id=47, time_id='2022-12-31', channel_id=3, promo_id=351, quantity_sold=1, amount_sold=28.77) and the related costs record (prod_id=47, time_id='2022-12-31', promo_id=351, channel_id=3, unit_cost=23.23, unit_price=28.77) from the database.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id=3320 AND prod_id=47 AND time_id='2022-12-31' AND channel_id=3 AND promo_id=351 AND quantity_sold=1 AND amount_sold=28.77;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id=47 AND time_id='2022-12-31' AND promo_id=351 AND channel_id=3 AND unit_cost=23.23 AND unit_price=28.77;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100127",
      instruction="I am Nicholas Desai (cust_id=100127). Please record that I bought 3 units of product prod_id=2005 on 2024-06-12, via channel_id=1, under promo_id=17. The total amount sold was 90.0. Each unit cost to the company is 20.0, and for accounting, the unit price is 30.0. Please ensure both the sales and costs entries are logged for me.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (2005, 100127, '2024-06-12', 1, 17, 3, 90.0);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (2005, '2024-06-12', 17, 1, 20.0, 30.0);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1666",
      instruction="You are Fran Keeting. Please verify and then update your sales record for the 'English Willow Cricket Bat' (prod_id=28) purchased through Direct Sales (channel_id=3) on 2022-03-23. The original sale amount_sold was entered as 212.3, but you need this corrected to 199.99 (matching your product's list price). Also, ensure the matching unit_price in costs is changed from 212.3 to 199.99 for prod_id=28, time_id='2022-03-23', promo_id=999, channel_id=3. Your customer id is 1666, and your email is Keeting@company.example.com.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id=1666 AND cust_email='Keeting@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT s.prod_id, s.cust_id, s.time_id, s.channel_id, s.promo_id, s.amount_sold, c.unit_cost, c.unit_price FROM sales s LEFT JOIN costs c ON s.prod_id = c.prod_id AND s.time_id = c.time_id AND s.channel_id = c.channel_id AND s.promo_id = c.promo_id WHERE s.prod_id=28 AND s.cust_id=1666 AND s.time_id='2022-03-23' AND s.channel_id=3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=199.99 WHERE prod_id=28 AND cust_id=1666 AND time_id='2022-03-23' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price=199.99 WHERE prod_id=28 AND time_id='2022-03-23' AND promo_id=999 AND channel_id=3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3268",
      instruction="You are Basil Wolf (cust_id: 3268) and want to: (1) get the profit margins for each cricket bat (prod_category = 'Cricket') you purchased, using product, sales, and cost info, and (2) update the unit_cost for your purchase of 'English Willow Cricket Bat' (prod_id: 28) on 2019-01-23 (channel_id: 3, promo_id: 999) to 182.00, as you noticed the cost was previously recorded incorrectly. All specified IDs are given for accuracy.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT p.prod_id, p.prod_name, s.quantity_sold, s.amount_sold, c.unit_cost, (s.amount_sold - c.unit_cost*s.quantity_sold) AS profit_margin FROM sales s JOIN products p ON s.prod_id = p.prod_id JOIN costs c ON s.prod_id = c.prod_id AND s.time_id = c.time_id AND s.promo_id = c.promo_id AND s.channel_id = c.channel_id WHERE s.cust_id = 3268 AND p.prod_category = 'Cricket';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 182.00 WHERE prod_id = 28 AND time_id = '2019-01-23' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6033",
      instruction="You are Chadwick Nutter (cust_id: 6033). On 2022-02-17, you bought one 'Team shirt' (prod_id: 42) for the New Zealand Cricket Team through channel_id 3 and promo_id 999. You want to return this shirt and instead purchase one more 'Team shirt' for the West Indies Team (prod_id: 40), also through channel_id 3 and promo_id 999, at the price of $45.85. Please process the return by deleting the original sale, and record the new sale and related cost for prod_id 40 on today's date (2024-06-01), with quantity_sold 1, amount_sold 45.85, unit_cost 43.0, unit_price 45.85.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 6033 AND prod_id = 42 AND time_id = '2022-02-17' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (40, 6033, '2024-06-01', 3, 999, 1, 45.85);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (40, '2024-06-01', 999, 3, 43.0, 45.85);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7801",
      instruction="My name is Carl Bartok, and my email is Bartok@company.example.com. For auditing reasons, I want to update the sale price of all my past purchases of the 'Cricket Bat Bag' (prod_id 19) to 60.00 USD. Please update the amount_sold in the sales table to 60.00 for all my purchases (cust_id 7801) of prod_id 19, and also update the unit_price in the costs table to 60.00 wherever the product id is 19. Ensure this is applied to all channels and dates associated with my transactions.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Bartok@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 60.00 WHERE cust_id = 7801 AND prod_id = 19;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 60.00 WHERE prod_id = 19;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1733",
      instruction="I am Gwynne Grandy (cust_id=1733). I recently found a mistake in my sale records: on 2020-10-13, I purchased 2 English Willow Cricket Bats (prod_id=28) via channel_id=2 and promo_id=999, but it is recorded as only 1 unit. Please update my sale record on that date for this product to quantity_sold=2 and amount_sold=406.36. Also, the cost record for that product on that same date and channel (prod_id=28, time_id='2020-10-13', promo_id=999, channel_id=2) needs the unit_cost corrected to 180.00. Once these are fixed, show me the updated sales record for that date and product to confirm.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=2, amount_sold=406.36 WHERE prod_id=28 AND cust_id=1733 AND time_id='2020-10-13' AND channel_id=2 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=180.00 WHERE prod_id=28 AND time_id='2020-10-13' AND promo_id=999 AND channel_id=2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM sales WHERE prod_id=28 AND cust_id=1733 AND time_id='2020-10-13' AND channel_id=2 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="806",
      instruction="My name is Gordon Petrella and my email is gordon.petrella@company2.example.com. I recently checked my purchase history and found that for the product 'Indoor Cricket Ball' (prod_id=48), purchased on 2022-02-21 through the Partners channel (channel_id=2, promo_id=999), the quantity_sold should be 3 (not 1). The correct amount_sold is 31.08 and the total cost should be updated accordingly. Please update my sales record (quantity_sold=3, amount_sold=31.08) and also update the corresponding costs record (unit_cost=30.63, unit_price=31.08).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=3, amount_sold=31.08 WHERE prod_id=48 AND cust_id=806 AND time_id='2022-02-21' AND channel_id=2 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost=30.63, unit_price=31.08 WHERE prod_id=48 AND time_id='2022-02-21' AND promo_id=999 AND channel_id=2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9970",
      instruction="You are Nora Marker (Marker@company.example.com). You want to 1) return your purchase of the 'Team shirt' (prod_id: 41) made on 2021-10-07 via Direct Sales (channel_id: 3, promo_id: 999) by deleting its sales and costs records; and 2) buy 1 'Indoor Cricket Ball' (prod_id: 48) on 2021-11-10 through Direct Sales (channel_id: 3) with NO PROMOTION (promo_id: 999), using unit_cost 11.99 and unit_price 13.47. Reflect all changes in sales and costs tables.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Marker@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE cust_id = 9970 AND prod_id = 41 AND time_id = '2021-10-07' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 41 AND time_id = '2021-10-07' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (48, 9970, '2021-11-10', 3, 999, 1, 13.47);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (48, '2021-11-10', 999, 3, 11.99, 13.47);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3441",
      instruction="My name is Ford Clatterbuck and my email is Clatterbuck@company.example.com. On 2022-03-17, I purchased a 'Plastic Cricket Bat' (prod_id 23) through Direct Sales (channel_id 3) with promotion 999, but I meant to purchase a 'Pro Maple Bat' (prod_id 129) instead. Please correct my purchase for that date by updating the sales record for cust_id 3441, time_id '2022-03-17', changing the prod_id from 23 to 129 and update the corresponding entry in the costs table (prod_id 23 to 129 for the same time_id, channel_id and promo_id) so both reflect the 'Pro Maple Bat' purchase.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Clatterbuck@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET prod_id = 129 WHERE cust_id = 3441 AND prod_id = 23 AND time_id = '2022-03-17' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET prod_id = 129 WHERE prod_id = 23 AND time_id = '2022-03-17' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1679",
      instruction="Hi, I am Gail Yarborough (cust_id 1679, living at 37 Sainte Genevieve Street, Torrevieja, Alicante, ES). Please update my supplementary demographic record: set tennis=1 and occupation='Business Analyst'. Also, add this note to my supplementary demographics comments field: '2021-01-25 English Willow Bat: Gift purchase'—this corresponds to my purchase of product prod_id 28 on 2021-01-25 via channel_id 3 and promo_id 999. Keep all other supplementary demographic values unchanged.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET tennis = 1, occupation = 'Business Analyst' WHERE cust_id = 1679;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE supplementary_demographics SET comments = COALESCE(comments, '') || ' 2021-01-25 English Willow Bat: Gift purchase' WHERE cust_id = 1679;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2322",
      instruction="You are Zaneta Orson, born in 1993, from 37 East Island Street, Belfast City, Northern Ireland, postcode 46413. You want to cancel all purchases of the 'Team shirt' (prod_id 40) made on 2019-08-20. Additionally, you want to correct the price for your purchase of 'Pro Maple Youth Bat' (prod_id 130) on 2019-01-24 to 89.99. Please process these changes for cust_id 2322.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id=40 AND cust_id=2322 AND time_id='2019-08-20';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=89.99 WHERE prod_id=130 AND cust_id=2322 AND time_id='2019-01-24';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2133",
      instruction="You are Ruford Klesser (Klesser@company.example.com), and you are attentive to product information. You noticed that the description for the product 'Pro Maple Bat' (prod_id=129), which you previously bought, is no longer accurate. Please update its description to 'Premium Pro Maple Bat - Enhanced Grain Quality'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_email = 'Klesser@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_desc = 'Premium Pro Maple Bat - Enhanced Grain Quality' WHERE prod_id = 129;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100438",
      instruction="You are Jaden Prabu (email: Prabu@company.example.com), and during a recent review of your sales and inventory, you noticed that the cost data was missing for your purchase of the 'Speed Trainer Bats and Training Program' (prod_id=21) made on 2019-10-31 through Tele Sales (channel_id=9) under promotion post promotion #20-33 (promo_id=33). To ensure complete records, you want to add this cost information now. The unit cost was 700.00 and the unit price 899.99. Please insert this record into the costs table using all provided identifiers and prices.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_first_name = 'Jaden' AND cust_last_name = 'Prabu' AND cust_email = 'Prabu@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (21, '2019-10-31', 33, 9, 700.00, 899.99);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1419",
      instruction="I am Xerxes Abbassi from Sanibel, FL 59061 (cust_id 1419). I bought two 'Team shirt' (prod_id 45, English Cricket Team) by mistake, one on 2021-07-07 through Direct Sales (channel_id 3), without any promotion (promo_id 999). Please process a return by deleting the sales and costs entries for that transaction: prod_id 45, cust_id 1419, time_id '2021-07-07', channel_id 3, promo_id 999.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 45 AND cust_id = 1419 AND time_id = '2021-07-07' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 45 AND time_id = '2021-07-07' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="766",
      instruction="You are Harry Farley from 11426 Matters Circle, Duncan, SC 74673 (cust_id=766). Using your email harry.farley@company2.example.com, you noticed you were charged $208.99 instead of $199.99 for your most recent 'English Willow Cricket Bat' purchase (prod_id=28) made on 2022-12-13 through the Partners channel (channel_id=2, promo_id=999). Please correct the sale so amount_sold is $199.99, and record a refund of $9.00 issued back to your original payment method. Ensure you identify me correctly, and modify ONLY this transaction.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id=766 AND cust_email='harry.farley@company2.example.com' AND cust_street_address='11426 Matters Circle' AND cust_postal_code='74673' AND cust_city='Duncan' AND cust_state_province='SC';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=199.99 WHERE cust_id=766 AND prod_id=28 AND time_id='2022-12-13' AND channel_id=2 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "-- Simulated action: Log refund (cust_id=766, prod_id=28, amount=9.00, method='Original Payment Method', time_id='2022-12-13')"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3637",
      instruction="I am Lolita Katz (cust_id: 3637). For my record keeping, I want to standardize the unit cost of all 'Team shirt' (English Cricket Team) purchases (prod_id 45) in the year 2021. Please update the unit_cost to 41.00 for every record in the costs table where prod_id is 45 and the time_id is between '2021-01-01' and '2021-12-31'. Leave other years unchanged and do not touch other products.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 41.00 WHERE prod_id = 45 AND time_id >= '2021-01-01' AND time_id <= '2021-12-31';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1153",
      instruction="Hi, I'm Ramon Harben (email: Harben@company.example.com). I'd like to request two updates to my past purchases. First, for my purchase of 'Indoor Cricket Ball' (prod_id 48) on 2020-06-22 through the Internet (channel_id 4), I found a quality defect and request a 20% refund, so please update the sales record's amount_sold to 9.136 (which is 80% of 11.42). Second, for my 'Team shirt' (prod_id 45) purchased on 2022-06-22 through Direct Sales (channel_id 3), the quantity should be 2, not 1—please correct the quantity_sold to 2 and the amount_sold to 93.2 (unit price 46.6 x 2) for that sale. My customer ID is 1153.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 9.136 WHERE cust_id = 1153 AND prod_id = 48 AND time_id = '2020-06-22' AND channel_id = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 93.2 WHERE cust_id = 1153 AND prod_id = 45 AND time_id = '2022-06-22' AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1537",
      instruction="You are Boyd Manning (customer ID 1537). On 2021-03-22, you purchased a 'Team shirt' (product ID 40) directly (channel ID 3, promo ID 999). You later realized you received two shirts but were only billed for one. Please update the sale record so the quantity_sold is 2 and the amount_sold is 97.56. Also, update the corresponding costs entry for this transaction: change the unit_cost to 41.2 and the unit_price to 48.78 for two units. Additionally, you want to increase your credit limit to 20000 and update your address to '123 Cricket Avenue', postal code '87221'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2, amount_sold = 97.56 WHERE cust_id = 1537 AND prod_id = 40 AND time_id = '2021-03-22' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 41.2, unit_price = 48.78 WHERE prod_id = 40 AND time_id = '2021-03-22' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_credit_limit = 20000 WHERE cust_id = 1537;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_street_address = '123 Cricket Avenue', cust_postal_code = '87221' WHERE cust_id = 1537;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3937",
      instruction="You are Tara Walsh (cust_id=3937). Please retroactively update ALL your sales records of the product 'Plastic Cricket Bat' (prod_id=23) purchased via the 'Internet' channel (channel_id=4) to have the promotion 'Summer Promo' (promo_id=101). Also, update the costs records accordingly, so promo_id=101 is set for matching prod_id=23 and channel_id=4.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id=101 WHERE cust_id=3937 AND prod_id=23 AND channel_id=4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET promo_id=101 WHERE prod_id=23 AND channel_id=4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100462",
      instruction="My name is Noah Roy and my email is Roy@company.example.com. I am reviewing my past purchase and would like to update the price for the 'Team shirt' (prod_id: 40). Please change its prod_list_price and prod_min_price to 39.99. Also, add a new entry in costs for prod_id: 40, time_id: '2019-10-31', promo_id: 33, channel_id: 9, with unit_cost: 20.00 and unit_price: 39.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Roy@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE products SET prod_list_price = 39.99, prod_min_price = 39.99 WHERE prod_id = 40;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) VALUES (40, '2019-10-31', 33, 9, 20.00, 39.99);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1695",
      instruction="You are Gerald Neila, cust_id 1695. Please update your transaction history for product 'Indoor Cricket Ball' (prod_id 48) on 2022-12-17: remove both sales records for prod_id 48 on that date ((a) channel_id 3, promo_id 351, amount_sold 12.0; (b) channel_id 4, promo_id 999, amount_sold 11.76), then insert a single sales record for that date: prod_id 48, cust_id 1695, time_id 2022-12-17, channel_id 3, promo_id 351, quantity_sold 1, amount_sold 12.0. No changes to other products or dates.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id=48 AND cust_id=1695 AND time_id='2022-12-17' AND channel_id=3 AND promo_id=351 AND amount_sold=12.0;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id=48 AND cust_id=1695 AND time_id='2022-12-17' AND channel_id=4 AND promo_id=999 AND amount_sold=11.76;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) VALUES (48, 1695, '2022-12-17', 3, 351, 1, 12.0);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1944",
      instruction="I am Milburn Klemm (email: Klemm@company.example.com), and I noticed a mistake in my trading records. For the transaction involving product_id=127 (Genuine Series MIX Wood Bat) on 2020-06-22 via channel_id=3, the amount_sold was recorded as 47.00, but the correct value should be 48.50. Please update the sales record to reflect the correct amount_sold. Here are the details: prod_id=127, cust_id=1944, time_id='2020-06-22', channel_id=3, promo_id=999, new amount_sold=48.50.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold=48.50 WHERE prod_id=127 AND cust_id=1944 AND time_id='2020-06-22' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="11779",
      instruction="You are Fran Greeley (customer id 11779, email Greeley@company.example.com). On August 19, 2021, you purchased an 'Australian Cricket Team' Team shirt (product id 43) through Direct Sales (channel id 3, promo id 999). You noticed the recorded sales price is $48.78, but it should be $44.99. Please update the sales record so the amount_sold is $44.99, and also update the corresponding costs record to set unit_price to $44.99 for this transaction.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 44.99 WHERE prod_id = 43 AND cust_id = 11779 AND time_id = '2021-08-19' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 44.99 WHERE prod_id = 43 AND time_id = '2021-08-19' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5602",
      instruction="My name is Randal Rellis (cust_id 5602, email Rellis@company.example.com). I want to update my main phone number on file from 594-114-4159 to 617-222-3344. Additionally, for my purchase of 'Indoor Cricket Ball' (prod_id 48) made on 2020-10-17 through channel_id 2 (Partners) with promo_id 999, I noticed the price in both sales and costs tables is $12.18, but it should be $11.99 to match the product's minimum price. Please update the 'amount_sold' and 'unit_price' for this specific purchase to $11.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_main_phone_number = '617-222-3344' WHERE cust_id = 5602 AND cust_main_phone_number = '594-114-4159';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 11.99 WHERE cust_id = 5602 AND prod_id = 48 AND time_id = '2020-10-17' AND channel_id = 2 AND promo_id = 999 AND amount_sold = 12.18;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 11.99 WHERE prod_id = 48 AND time_id = '2020-10-17' AND promo_id = 999 AND channel_id = 2 AND unit_price = 12.18;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="10849",
      instruction="My name is Murdock Barnhouse and my email is Barnhouse@company.example.com. I want to update the sale amount for my purchase of 'Linseed Oil' (prod_id: 30) made on 2022-07-10 through Direct Sales (channel_id: 3, promo_id: 999). Please change the sales.amount_sold to 11.25, and also update the corresponding costs.unit_price for that product, channel, promo, and date to 11.25.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Barnhouse@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET amount_sold = 11.25 WHERE prod_id = 30 AND cust_id = 10849 AND time_id = '2022-07-10' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price = 11.25 WHERE prod_id = 30 AND time_id = '2022-07-10' AND promo_id = 999 AND channel_id = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1925",
      instruction="My name is Heloise Fepoi, email Fepoi@company.example.com. Please update my sales record for the Team shirt (prod_id=40) purchased on 2022-02-20 via Direct Sales (channel_id=3) under TV promotion #13-351 (promo_id=351). Change the quantity_sold from 1 to 2. My customer ID is 1925.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold = 2 WHERE prod_id = 40 AND cust_id = 1925 AND time_id = '2022-02-20' AND channel_id = 3 AND promo_id = 351;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4380",
      instruction="My name is Godfrey Knox and my email is Knox@company.example.com. I am detail-oriented and value correct records. Please update my sales records for the product 'Genuine Series MIX Wood Bat' (prod_id=127) on 2021-09-29 and 2021-10-29 (both via Direct Sales, channel_id=3) so that the quantity_sold is 1 and amount_sold is 39.18 for both. Also, update the associated cost records for product 127 on these same dates and channel so that the unit_price is also 39.18, keeping promo_id as 999. These updates must be done only for my transactions (cust_id=4380, prod_id=127, channel_id=3, dates 2021-09-29 and 2021-10-29).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET quantity_sold=1, amount_sold=39.18 WHERE cust_id=4380 AND prod_id=127 AND channel_id=3 AND (time_id='2021-09-29' OR time_id='2021-10-29');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price=39.18 WHERE prod_id=127 AND channel_id=3 AND promo_id=999 AND (time_id='2021-09-29' OR time_id='2021-10-29');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="608",
      instruction="My name is Thomas Sparks (cust_id 608, email thomas.sparks@company2.example.com). I recently received a raise and my income level should be updated to 'H: 200,000 - 224,999'. Additionally, for product_id 42 ('Team shirt' - New Zealand Cricket Team), please update its unit cost to 45.00 and unit price to 54.99 for all entries where the promo_id is 999, channel_id is 3, and time_id is '2021-01-24'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET cust_income_level = 'H: 200,000 - 224,999' WHERE cust_id = 608;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 45.00, unit_price = 54.99 WHERE prod_id = 42 AND promo_id = 999 AND channel_id = 3 AND time_id = '2021-01-24';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1286",
      instruction="You are Thaxter Hurd (cust_email: Hurd@company.example.com, cust_id: 1286). Please confirm that you have a sales record for the 'Pro Maple Youth Bat' (prod_id: 130) purchased on 2021-01-18 via channel_id 3 and promo_id 999, and show me its current unit_price from the costs table. If confirmed, update the unit_price for that costs record (prod_id: 130, time_id: '2021-01-18', channel_id: 3, promo_id: 999) to 99.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM sales WHERE cust_id=1286 AND prod_id=130 AND time_id='2021-01-18' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT unit_price FROM costs WHERE prod_id=130 AND time_id='2021-01-18' AND channel_id=3 AND promo_id=999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_price=99.99 WHERE prod_id=130 AND time_id='2021-01-18' AND channel_id=3 AND promo_id=999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3945",
      instruction="I am Tesia Lessman (cust_id 3945). For my purchase of the 'English Willow Cricket Bat' (prod_id 28) on 2022-12-20 (time_id), through channel_id 2 and using promo_id 999, I realized the cost information was entered wrong. Please update the costs table for this transaction to unit_cost 157.99 and unit_price 209.49.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE cust_id = 3945;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET unit_cost = 157.99, unit_price = 209.49 WHERE prod_id = 28 AND time_id = '2022-12-20' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1471",
      instruction="You are Aubrey Figgens (cust_id 1471, email: Figgens@company.example.com). For all purchases of products with prod_id 128 (Slugger Youth Series Maple Bat) and 130 (Pro Maple Youth Bat) made via channel_id 4 (Internet) between 2022-05-01 and 2022-05-31, where the promotion used was promo_id 999, you want to update the promotion to promo_id 2022. Please also ensure this promotion update is reflected in both sales and costs tables.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_email = 'Figgens@company.example.com'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id = 2022 WHERE cust_id = 1471 AND prod_id IN (128, 130) AND channel_id = 4 AND time_id BETWEEN '2022-05-01' AND '2022-05-31' AND promo_id = 999"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET promo_id = 2022 WHERE prod_id IN (128, 130) AND channel_id = 4 AND time_id BETWEEN '2022-05-01' AND '2022-05-31' AND promo_id = 999"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5660",
      instruction="I am Rona Fairman from 37 South Ross Street, Wakefield, 50385 (email: Fairman@company.example.com). I want to return every 'English Willow Cricket Bat' (prod_id: 28) purchased through Direct Sales (channel_id: 3), but keep the ones purchased through Partners (channel_id: 2). For every such returned bat, please exchange it for a 'Pro Maple Youth Bat' (prod_id: 130), keeping the same purchase date and promo_id. Update both sales and costs accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 28 AND cust_id = 5660 AND channel_id = 3"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 28 AND channel_id = 3 AND EXISTS (SELECT 1 FROM sales WHERE sales.prod_id = 28 AND sales.cust_id = 5660 AND sales.channel_id = 3 AND sales.time_id = costs.time_id AND sales.promo_id = costs.promo_id)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO sales (prod_id, cust_id, time_id, channel_id, promo_id, quantity_sold, amount_sold) SELECT 130, 5660, time_id, 3, promo_id, quantity_sold, (SELECT prod_list_price FROM products WHERE prod_id = 130) FROM sales WHERE prod_id = 28 AND cust_id = 5660 AND channel_id = 3"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO costs (prod_id, time_id, promo_id, channel_id, unit_cost, unit_price) SELECT 130, time_id, promo_id, 3, (SELECT prod_min_price FROM products WHERE prod_id = 130), (SELECT prod_list_price FROM products WHERE prod_id = 130) FROM sales WHERE prod_id = 28 AND cust_id = 5660 AND channel_id = 3"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2483",
      instruction="I am Chester Charles (email Charles@company.example.com). I ordered two 'Indoor Cricket Ball' items (prod_id: 48) but only need to keep the one purchased on 2022-09-09 via Direct Sales (channel_id: 3, promo_id: 999). Please cancel (i.e., remove) my purchase of the 'Indoor Cricket Ball' (prod_id: 48) from 2022-10-10 via channel_id: 2 and promo_id: 999. Additionally, for my purchase of 'Linseed Oil' (prod_id: 30) on 2022-08-23 through channel_id: 3, please update the associated promotion from promo_id: 999 to promo_id: 350 ('internet promotion #29-350').",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT cust_id FROM customers WHERE cust_first_name = 'Chester' AND cust_last_name = 'Charles' AND cust_email = 'Charles@company.example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM sales WHERE prod_id = 48 AND cust_id = 2483 AND time_id = '2022-10-10' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM costs WHERE prod_id = 48 AND time_id = '2022-10-10' AND channel_id = 2 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE sales SET promo_id = 350 WHERE prod_id = 30 AND cust_id = 2483 AND time_id = '2022-08-23' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE costs SET promo_id = 350 WHERE prod_id = 30 AND time_id = '2022-08-23' AND channel_id = 3 AND promo_id = 999;"
               }
            ),
       ],
       outputs=[]
   ),
]
