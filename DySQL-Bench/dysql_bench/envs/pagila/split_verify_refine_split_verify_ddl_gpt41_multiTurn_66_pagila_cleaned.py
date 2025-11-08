from tau_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="0",
      instruction="I am Emily Diaz (CustomerID 99). For my rental of film 'CONNECTION MICROCOSMOS' (film_id 178, inventory_id 817, rental_id 11593), I need to update the return date to '2006-02-17 15:30:00' as I returned it late. Also, log a late payment with payment_id 3001, amount $2.99, processed by staff_id 1 on payment_date '2006-02-17 15:35:00' for this rental.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2006-02-17 15:30:00' WHERE rental_id = 11593 AND customer_id = 99;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO payment (payment_id, customer_id, staff_id, rental_id, amount, payment_date) VALUES (3001, 99, 1, 11593, 2.99, '2006-02-17 15:35:00');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="246",
      instruction="I am Marian Mendoza, customer ID 246, and I need to fix a double-charge error for my rental of 'MOD SECRETARY' (film_id 587, rental_id 14360). Please verify my account first. Then, delete the duplicate payment record with payment_id 6675 associated with rental_id 14360. After deletion, show me a summary of all my current payment records including payment_id, amount, payment_date, and rental_id for customer ID 246.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 246 AND first_name = 'Marian' AND last_name = 'Mendoza';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 6675 AND customer_id = 246 AND rental_id = 14360;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT payment_id, amount, payment_date, rental_id FROM payment WHERE customer_id = 246;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2",
      instruction="My name is NATALIE MEYER (email: NATALIE.MEYER@sakilacustomer.org). For my latest rental (film title: SWEDEN SHINING, rental_id: 12970, inventory_id: 3999), I just returned the movie today, so please update the return_date to 2024-06-17 15:00:00. Also, I was supposed to be charged 4.99 for this rental but was charged 5.98 (payment_id: 5879). Please update the payment amount for payment_id 5879 to 4.99 instead of 5.98.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2024-06-17 15:00:00' WHERE rental_id = 12970 AND inventory_id = 3999 AND customer_id IN (SELECT customer_id FROM customer WHERE first_name = 'NATALIE' AND last_name = 'MEYER' AND email = 'NATALIE.MEYER@sakilacustomer.org');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 4.99 WHERE payment_id = 5879 AND customer_id IN (SELECT customer_id FROM customer WHERE first_name = 'NATALIE' AND last_name = 'MEYER' AND email = 'NATALIE.MEYER@sakilacustomer.org');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5",
      instruction="Hello, I'm Daniel Cabral (customer_id 310) and I need to clean up my rental and payment history. Please perform these updates: 1) Update the payment record with payment_id 8417 to set staff_id to 2 for customer_id 310. 2) Update the payment record with payment_id 8422 to set staff_id to 2 for customer_id 310. 3) Delete the rental record with rental_id 1333 for customer_id 310, as it was entered in error. Confirm once all changes are complete.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 2 WHERE payment_id = 8417 AND customer_id = 310;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 2 WHERE payment_id = 8422 AND customer_id = 310;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 1333 AND customer_id = 310;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6",
      instruction="Hello, I'm Gene Sanborn. My customer ID is 498 and email is GENE.SANBORN@sakilacustomer.org. I'm disputing a $2.99 charge (payment ID: 13417) for my rental. I returned the item early—please reverse this payment.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 498 AND email = 'GENE.SANBORN@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 0 WHERE payment_id = 13417 AND customer_id = 498;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="8",
      instruction="First, please authenticate me. My name is Todd Tan and my customer id is 386. After authentication, I request: Create a new category named 'Favorite Actor: Ed Chase' with category_id 21. Then, re-categorize all films I previously rented that feature actor 'ED CHASE' (actor_id=3) to category_id 21. Use my rental records to identify these films. Required parameters: customer_id=386, category_id=21, actor_id=3.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 386 AND first_name = 'Todd' AND last_name = 'Tan';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO category (category_id, name, last_update) VALUES (21, 'Favorite Actor: Ed Chase', CURRENT_TIMESTAMP);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film_category SET category_id = 21, last_update = CURRENT_TIMESTAMP WHERE film_id IN (SELECT DISTINCT inventory.film_id FROM rental JOIN inventory ON rental.inventory_id = inventory.inventory_id JOIN film_actor ON inventory.film_id = film_actor.film_id WHERE rental.customer_id = 386 AND film_actor.actor_id = 3);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9",
      instruction="I am Dorothy Taylor (DOROTHY.TAYLOR@sakilacustomer.org). For my rental of 'ALI FOREVER' (Rental ID: 15370), I was mistakenly charged twice with two payments of $5.99. Please refund the extra $5.99 by recording a negative payment for the same rental. Use staff ID 1 for the refund, and set the payment date to the current timestamp.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'DOROTHY.TAYLOR@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT payment_id, amount, payment_date, staff_id FROM payment WHERE customer_id = 10 AND rental_id = 15370 AND amount = 5.99;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO payment (payment_id, customer_id, staff_id, rental_id, amount, payment_date, last_update) VALUES (NEXT VALUE FOR payment_seq, 10, 1, 15370, -5.99, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="10",
      instruction="Hello, I'm Emma Boyd (EMMA.BOYD@sakilacustomer.org, customer_id=134). On my last rental, I accidentally rented GOODFELLAS SALUTE (rental_id=10864, payment_id=3627) from Store 2 instead of Store 1. Please delete payment_id 3627 and rental_id 10864. Then, create a new rental using inventory_id 1102 from Store 1 with rental_id 20000, customer_id 134, staff_id 1, and rental_date '2024-06-01 10:00:00'. Also, add a payment of 6.99 USD for this rental with payment_id 9999, staff_id 1, and payment_date '2024-06-01 10:00:00'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 134 AND email = 'EMMA.BOYD@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 3627;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 10864;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO rental (rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update) VALUES (20000, '2024-06-01 10:00:00', 1102, 134, NULL, 1, CURRENT_TIMESTAMP);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO payment (payment_id, customer_id, staff_id, rental_id, amount, payment_date, last_update) VALUES (9999, 134, 1, 20000, 6.99, '2024-06-01 10:00:00', CURRENT_TIMESTAMP);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="11",
      instruction="I am Willard Lumpkin with customer ID 578. On 2005-08-01, I rented the film IMAGE PRINCESS (film_id 453, rental_id 10779) and was charged $7.99 (payment_id 15501) instead of the correct $2.99 rate. Please authenticate my identity and adjust the payment to $2.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 578 AND first_name = 'Willard' AND last_name = 'Lumpkin';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 15501 AND customer_id = 578 AND rental_id = 10779;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12",
      instruction="I am Charles Kowalski, email CHARLES.KOWALSKI@sakilacustomer.org. I need to correct a payment error for my rental (rental_id 7225). Please delete my existing payment with payment_id 8304 (customer_id 306) and create a new payment with payment_id 99999, customer_id 306, staff_id 1, rental_id 7225, amount $6.99, and payment_date '2005-07-27 09:47:12.000'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE email = 'CHARLES.KOWALSKI@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 8304 AND customer_id = 306;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO payment (payment_id, customer_id, staff_id, rental_id, amount, payment_date) VALUES (99999, 306, 1, 7225, 6.99, '2005-07-27 09:47:12.000');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="15",
      instruction="I am Bobby Boudreau (Customer ID 381). I request permanent deletion of my rental record for 'CONTACT ANONYMOUS' (rental_id: 7645) and its associated payment (payment_id: 10323). Please delete the payment record first, followed by the rental record. I confirm authorization for both deletions.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 10323 AND customer_id = 381;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 7645 AND customer_id = 381;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="424",
      instruction="Hello, I'm Kyle Spurlock (customer_id 424). I noticed my rental for 'DANCES NONE' (rental_id 15094, inventory_id 922, payment_id 11479) lacks a return date. To clean my records, please: 1) Set the return_date to '2024-06-16 12:00:00' for this rental, 2) Remove the payment record for payment_id 11479, and 3) Update my email to kyle.spurlock2024@outlook.com.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2024-06-16 12:00:00' WHERE rental_id = 15094 AND inventory_id = 922 AND customer_id = 424;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 11479 AND customer_id = 424 AND rental_id = 15094;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET email = 'kyle.spurlock2024@outlook.com' WHERE customer_id = 424;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="481",
      instruction="I am Herman Devore (Customer ID: 481). For my rental of 'WATCH TRACY' (Rental ID: 3293), the payment record (Payment ID: 12983) shows an incorrect amount of $0.99. The correct charge should be $4.99. Please update this payment to reflect the accurate amount.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 4.99 WHERE payment_id = 12983 AND customer_id = 481 AND rental_id = 3293;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="18",
      instruction="I am Marshall Thorn (MARSHALL.THORN@sakilacustomer.org, CustomerID 583). On July 8, 2005, my rental for 'WITCHES PANIC' (rental_id 4464) at store 2 was processed incorrectly—the return was recorded for 'QUEEN LUKE' instead. Please update rental record 4464 to set inventory_id to 4484 (the correct inventory for 'WITCHES PANIC' at store 2). Also update payment record 15622 to link it to rental_id 4464. Additionally, change my email address to marshall.t.thorn2024@example.com.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET inventory_id = 4484 WHERE rental_id = 4464 AND customer_id = 583;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET rental_id = 4464 WHERE payment_id = 15622 AND customer_id = 583;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET email = 'marshall.t.thorn2024@example.com' WHERE customer_id = 583;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="19",
      instruction="I am Marion Ocampo with customer ID 588. I request full refunds for two disputed payments: payment for rental ID 15109 (amount $1.99) and rental ID 13064 (amount $4.99). Please void these rentals by setting their return dates to NULL.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE rental_id = 15109 AND customer_id = 588 AND amount = 1.99"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE rental_id = 13064 AND customer_id = 588 AND amount = 4.99"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = NULL WHERE rental_id = 15109 AND customer_id = 588"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = NULL WHERE rental_id = 13064 AND customer_id = 588"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22",
      instruction="I am Brandon Huey (customer ID 366). I request a refund for my rental of 'CELEBRITY HORN' (payment ID 9909) because I received the wrong DVD. Please delete the payment record for payment ID 9909 from the payment table and remove my rental record for rental ID 13563 from the rental table for privacy reasons. Also, update my email address to brandon.huey.new@email.com in the customer table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id=9909 AND customer_id=366 AND rental_id=13563;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id=13563 AND customer_id=366;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET email='brandon.huey.new@email.com' WHERE customer_id=366;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="23",
      instruction="Hello, I'm Byron Box (customer ID 573). I need to cancel a mistaken rental: rental ID 10296 with payment ID 15357. Please delete both the payment record and rental from my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 15357 AND customer_id = 573 AND rental_id = 10296;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 10296 AND customer_id = 573;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="452",
      instruction="You are Tom Milner (CustomerID: 452). After watching 'Gentlemen Stage' (film_id: 353) rented under rental_id 11715, you realized its category should be 'Drama' (category_id: 7) instead of 'Foreign'. First, verify that rental_id 11715 belongs to you. Then, update the film_category to category_id 7.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT rental_id FROM rental WHERE rental_id = 11715 AND customer_id = 452;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film_category SET category_id = 7 WHERE film_id = 353;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="26",
      instruction="I am Melanie Armstrong (email: MELANIE.ARMSTRONG@sakilacustomer.org). Please update my rental with ID 14503 to use inventory ID 3041. Also, adjust the payment for payment ID 5126 to $2.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE email = 'MELANIE.ARMSTRONG@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET inventory_id = 3041 WHERE rental_id = 14503 AND customer_id = 188;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 5126 AND customer_id = 188;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="27",
      instruction="Hello, I'm Henry Billingsley (Customer ID: 344). I rented the film 'GLEAMING JAWBREAKER' with Rental ID 4028, but I noticed the staff ID is listed as 2. I'm sure it was staff ID 1 who helped me. Could you update the staff ID to 1 for this rental?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET staff_id = 1 WHERE rental_id = 4028 AND customer_id = 344;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="29",
      instruction="I am Louis Leone (email: LOUIS.LEONE@sakilacustomer.org). I noticed that my rental of the film 'ZHIVAGO CORE' (film_id: 998, inventory_id: 4568) under rental_id 11739 was never marked as returned, even though I brought it back. Could you please update the return_date for rental_id 11739 to '2006-02-17 16:00:00'? Since it was late, I would like to add a penalty payment of $2.50, assigned to staff_id 2, on payment date '2006-02-17 16:10:00', and link it to the same rental (rental_id 11739) and my customer account (customer_id 373).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE email = 'LOUIS.LEONE@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2006-02-17 16:00:00' WHERE rental_id = 11739 AND customer_id = 373;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO payment (customer_id, staff_id, rental_id, amount, payment_date) VALUES (373, 2, 11739, 2.50, '2006-02-17 16:10:00');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="30",
      instruction="I am Beth Franklin with email BETH.FRANKLIN@sakilacustomer.org. I request to permanently delete my open rental (ID: 13952) and its associated payment (ID: 5417). Please remove the payment record, the rental entry, and the linked inventory item (ID: 224).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE first_name = 'BETH' AND last_name = 'FRANKLIN' AND email = 'BETH.FRANKLIN@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 5417 AND customer_id = 199;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 13952 AND customer_id = 199 AND inventory_id = 224;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM inventory WHERE inventory_id = 224;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="33",
      instruction="My name is Alfredo McAdams (customer ID 567). Please delete the payment record with payment_id 15208 and the rental record with rental_id 15594 from my account, as they were recorded in error.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 15208 AND customer_id = 567;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 15594 AND customer_id = 567;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="34",
      instruction="Hi, I'm Dale Ratcliff (customer ID: 407, email: DALE.RATCLIFF@sakilacustomer.org). I recently rented 'TROOPERS METAL' (film ID: 913) and need to update its rating to PG-13. Please authenticate me first, then change the rating.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 407 AND email = 'DALE.RATCLIFF@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film SET rating = 'PG-13' WHERE film_id = 913;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="37",
      instruction="I am Willard Lumpkin (email WILLARD.LUMPKIN@sakilacustomer.org, customer_id 578). Please void payment ID 15501 for rental ID 10779 by setting its amount to $0. Additionally, record a $7.99 refund as a negative payment to my account for the same rental, processed by staff ID 1 on 2005-08-01 21:11:54.000.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 0 WHERE payment_id = 15501 AND customer_id = 578 AND rental_id = 10779;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO payment (payment_id, customer_id, staff_id, rental_id, amount, payment_date) VALUES (NEXTVAL('payment_payment_id_seq'), 578, 1, 10779, -7.99, '2005-08-01 21:11:54.000');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="38",
      instruction="I am JEANETTE GREENE (email: JEANETTE.GREENE@sakilacustomer.org, customer_id: 191). Please update my rental record (rental_id: 14361) to set the return_date to '2006-02-18 18:00:00'. Also, correct the associated payment (payment_id: 5195) to set the amount to 2.99 instead of the current value.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE email = 'JEANETTE.GREENE@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2006-02-18 18:00:00' WHERE rental_id = 14361 AND customer_id = 191;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 5195 AND customer_id = 191;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="40",
      instruction="You are RICARDO MEADOR (customer_id: 489, email: RICARDO.MEADOR@sakilacustomer.org). You recently rented 'STEPMOM DREAM' (film_id 845) from store 2 with rental_id 13462 on 2005-08-20 00:49:19.000 and were charged $4.99 (payment_id 13203). You believe you should have received a $3.00 promotional discount for store 2 rentals after 2005-08-15, so the charge should have been $1.99. Please update the payment for payment_id 13203 to amount $1.99 accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 1.99 WHERE payment_id = 13203 AND customer_id = 489 AND rental_id = 13462;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="41",
      instruction="Hello, I'm Wilma Richards, customer ID 212 with email WILMA.RICHARDS@sakilacustomer.org. I need to cancel an erroneous rental of 'ROOTS REMEMBER' (rental ID 15872) from 2005-08-23 and request a refund for the associated $4.99 payment (payment ID 5771). Please permanently remove both the payment and rental records from the system.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 212 AND email = 'WILMA.RICHARDS@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 5771 AND customer_id = 212;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 15872 AND customer_id = 212;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="42",
      instruction="As EDDIE TOMLIN (customer ID 434), I need to correct an error in my payment record. Please verify my identity using my customer ID and name, then update the staff_id to 1 for payment ID 11716.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 434 AND first_name = 'EDDIE' AND last_name = 'TOMLIN';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 1 WHERE payment_id = 11716 AND customer_id = 434;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="43",
      instruction="I am TAMMY SANDERS, customer ID 75. I need to delete rental records for privacy: rental ID 180 (movie: SHAKESPEARE) and rental ID 2161 (movie: POSEIDON FOREVER). Please remove these rentals and their associated payment records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE first_name = 'TAMMY' AND last_name = 'SANDERS' AND customer_id = 75;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE rental_id = 180 AND customer_id = 75;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 180 AND customer_id = 75;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE rental_id = 2161 AND customer_id = 75;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 2161 AND customer_id = 75;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="45",
      instruction="Authentication: I am Herman Devore (customer_id=481). Requesting record corrections: 1) For my rental ID 11885 (payment ID 13000), update the staff_id to 2. 2) For my rental ID 1109 (payment ID 12979), update the staff_id to 1. 3) For the film 'FUGITIVE MAGUIRE' (film ID 342), remove category ID 16 (Travel) and add category ID 7 (Drama).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE first_name = 'HERMAN' AND last_name = 'DEVORE' AND customer_id = 481;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 2 WHERE payment_id = 13000 AND rental_id = 11885 AND customer_id = 481;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 1 WHERE payment_id = 12979 AND rental_id = 1109 AND customer_id = 481;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM film_category WHERE film_id = 342 AND category_id = 16;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO film_category (film_id, category_id, last_update) VALUES (342, 7, CURRENT_TIMESTAMP);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="389",
      instruction="My name is Alan Kahn (customer ID 389), and I believe I was overcharged on payment ID 10537 (for rental ID 6104, inventory ID 3531, film 'SEABISCUIT PUNK'). There was supposed to be a 20% promotion for Sports category movies, which means my payment should have been $2.39 instead of $2.99. Please update my payment record so that amount is $2.39, and refund the $0.60 overcharge to my account (use the same rental_id 6104, staff_id 2). Also, my phone number has changed, please update my contact number for my address (address_id 1) to '555-8812'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id=389 AND first_name='Alan' AND last_name='Kahn' AND address_id=1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.39 WHERE payment_id = 10537 AND customer_id = 389;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO payment (customer_id, staff_id, rental_id, amount, payment_date) VALUES (389, 2, 6104, -0.60, CURRENT_TIMESTAMP);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE address SET phone = '555-8812' WHERE address_id = 1;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="50",
      instruction="Hello, I'm Juanita Mason, and my email is JUANITA.MASON@sakilacustomer.org. I recently returned my rental (ID: 13390) on 2006-02-18 at 10:32:00, but I see the return date is missing in the system. Could you please update it to 2006-02-18 10:32:00.000?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'JUANITA.MASON@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2006-02-18 10:32:00.000' WHERE rental_id = 13390 AND customer_id = 135;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="52",
      instruction="I am Catherine Campbell (Customer ID: 46). I need to dispute the payment for rental ID 15438 ('HUNTING MUSKETEERS') due to damage. Please issue a refund of $2.99 using Staff ID 1 and the current date/time.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO payment (customer_id, staff_id, rental_id, amount, payment_date) VALUES (46, 1, 15438, -2.99, CURRENT_TIMESTAMP);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="53",
      instruction="Hello, I am Erica Matthews with customer ID 169 (email: ERICA.MATTHEWS@sakilacustomer.org). I need two updates: First, reactivate my account by setting my status to active. Second, delete my rental record for rental ID 5066 (associated with the film 'GORGEOUS BINGO') and all its linked payments.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 169 AND email = 'ERICA.MATTHEWS@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET active = '1' WHERE customer_id = 169;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE rental_id = 5066 AND customer_id = 169;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 5066 AND customer_id = 169;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="54",
      instruction="Hello, I'm Cecil Vines (customer ID 512, email CECIL.VINES@sakilacustomer.org). Please cancel my open rental with ID 12786 immediately and issue a full refund of 0.99. Process this by marking the rental as returned now and adding a refund payment for -0.99 handled by staff member 1.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = CURRENT_TIMESTAMP WHERE rental_id = 12786 AND customer_id = 512 AND return_date IS NULL;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO payment (customer_id, staff_id, rental_id, amount, payment_date) VALUES (512, 1, 12786, -0.99, CURRENT_TIMESTAMP);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="55",
      instruction="Hello, I am Lorraine Stephens with email LORRAINE.STEPHENS@sakilacustomer.org. I need to report a payment discrepancy: For payment_id 4471 and rental_id 3784, I was charged $5.99, but the correct rental rate is $0.99. Please update the payment amount to $0.99 and note this correction in the rental record today.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'LORRAINE.STEPHENS@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 0.99, last_update = CURRENT_TIMESTAMP WHERE payment_id = 4471 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'LORRAINE.STEPHENS@sakilacustomer.org') AND rental_id = 3784;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET last_update = CURRENT_TIMESTAMP WHERE rental_id = 3784 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'LORRAINE.STEPHENS@sakilacustomer.org');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="56",
      instruction="I am Margaret Moore (email: MARGARET.MOORE@sakilacustomer.org). Please remove my rental record with rental_id 15813 that hasn't been returned yet, along with its associated payment (payment_id 253).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'MARGARET.MOORE@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 253 AND customer_id = 9 AND rental_id IN (SELECT rental_id FROM rental WHERE rental_id = 15813 AND customer_id = 9 AND return_date IS NULL);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 15813 AND customer_id = 9 AND return_date IS NULL;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="57",
      instruction="Hello, I'm Ron DeLuca with customer ID 519 and email RON.DELUCA@sakilacustomer.org. I need to authenticate and request deletion of my erroneous rental record for rental_id 12648 and its associated payment record for payment_id 13983. Please remove both records as I did not intend to complete this rental.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 519 AND email = 'RON.DELUCA@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 13983 AND customer_id = 519;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 12648 AND customer_id = 519;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="58",
      instruction="You are Michael Silverman (email: michael.silverman@sakilacustomer.org). You noticed that the payment recorded for your rental of the film 'KISSING DOLLS' (rental_id = 12126) is incorrect and should be 5.99 USD instead of 7.99 USD. Please update the payment amount for this rental to 5.99 USD, and provide a list of all your rental payments after this correction for your personal records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 5.99 WHERE rental_id = 12126 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'michael.silverman@sakilacustomer.org');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT payment_id, rental_id, amount, payment_date FROM payment WHERE customer_id = (SELECT customer_id FROM customer WHERE email = 'michael.silverman@sakilacustomer.org') ORDER BY payment_date ASC;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="60",
      instruction="I'm HERMAN DEVORE (CustomerID 481, email HERMAN.DEVORE@sakilacustomer.org). To confirm my identity for account modification, please authenticate me. I noticed a rental for 'SMILE EARRING' (rental_id 10018) and its payment (payment_id 12996) was logged to my account by mistake. Please remove both records after verification.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id, first_name, last_name, email FROM customer WHERE customer_id = 481 AND first_name = 'HERMAN' AND last_name = 'DEVORE' AND email = 'HERMAN.DEVORE@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT r.rental_id, f.title FROM rental r JOIN inventory i ON r.inventory_id = i.inventory_id JOIN film f ON i.film_id = f.film_id WHERE r.rental_id = 10018 AND r.customer_id = 481 AND f.title = 'SMILE EARRING';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT payment_id, rental_id, customer_id FROM payment WHERE payment_id = 12996 AND customer_id = 481 AND rental_id = 10018;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 12996 AND customer_id = 481;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 10018 AND customer_id = 481;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="61",
      instruction="Authenticate me with email TONI.HOLT@sakilacustomer.org. Verify that rental ID 7564 belongs to me and is for film ID 634. Then, add 'Comedy' (category ID 5) to film ID 634 only if not already present.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'TONI.HOLT@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT rental.rental_id FROM rental JOIN inventory ON rental.inventory_id = inventory.inventory_id WHERE rental.rental_id = 7564 AND rental.customer_id = (SELECT customer_id FROM customer WHERE email = 'TONI.HOLT@sakilacustomer.org') AND inventory.film_id = 634;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO film_category (film_id, category_id, last_update) SELECT 634, 5, CURRENT_TIMESTAMP WHERE NOT EXISTS (SELECT 1 FROM film_category WHERE film_id = 634 AND category_id = 5);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="62",
      instruction="Hello, I am Samuel Marlow (email: SAMUEL.MARLOW@sakilacustomer.org). I rented the film 'UNTOUCHABLES SUNRISE' under rental ID 12452 and was charged 6.99 for payment ID 9681. The correct rate is 2.99. Please update my payment to reflect this.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'SAMUEL.MARLOW@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 9681 AND rental_id = 12452 AND customer_id = 358;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="64",
      instruction="My name is VANESSA SIMS and my current email address is VANESSA.SIMS@sakilacustomer.org. I need to permanently delete all rental and payment records linked to rental ID 12099 (associated with 'GREEDY ROOTS') and rental ID 16040 (associated with 'SCORPION APOLLO') from my account. Also, update my email address to simsvanessa2024@protonmail.com. Please confirm these changes are applied exclusively to my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE rental_id = 12099 AND customer_id = (SELECT customer_id FROM customer WHERE first_name = 'VANESSA' AND last_name = 'SIMS' AND email = 'VANESSA.SIMS@sakilacustomer.org');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 12099 AND customer_id = (SELECT customer_id FROM customer WHERE first_name = 'VANESSA' AND last_name = 'SIMS' AND email = 'VANESSA.SIMS@sakilacustomer.org');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE rental_id = 16040 AND customer_id = (SELECT customer_id FROM customer WHERE first_name = 'VANESSA' AND last_name = 'SIMS' AND email = 'VANESSA.SIMS@sakilacustomer.org');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 16040 AND customer_id = (SELECT customer_id FROM customer WHERE first_name = 'VANESSA' AND last_name = 'SIMS' AND email = 'VANESSA.SIMS@sakilacustomer.org');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET email = 'simsvanessa2024@protonmail.com' WHERE customer_id = (SELECT customer_id FROM customer WHERE first_name = 'VANESSA' AND last_name = 'SIMS' AND email = 'VANESSA.SIMS@sakilacustomer.org');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="65",
      instruction="Hello, I'm Marsha Douglas (MARSHA.DOUGLAS@sakilacustomer.org). I recently rented the film 'UNBREAKABLE KARATE' and was charged $2.99 on 2005-08-19 01:55:55. My payment record ID is 6946, and the rental record ID is 12841. I returned the film on time, so this charge is an error. Please issue a full refund by deleting this payment record. Also, update my email address to marsha.douglas88@example.com for all future communications.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE email = 'MARSHA.DOUGLAS@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 6946 AND customer_id = 257 AND amount = 2.99 AND payment_date = '2005-08-19 01:55:55.000' AND rental_id = 12841;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET email = 'marsha.douglas88@example.com' WHERE customer_id = 257;"
               }
            ),
       ],
       outputs=[]
   ),
]
