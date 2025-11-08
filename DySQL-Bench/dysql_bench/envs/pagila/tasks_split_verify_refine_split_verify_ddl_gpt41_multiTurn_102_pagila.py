from tau_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="0",
      instruction="I am Suzanne Nichols (customer id 153). I recently rented 'CANDLES GRAPES' (rental_id 14944, inventory_id 535, film_id 117) and paid $4.99 (payment_id 4177). I want to dispute this charge, receive a refund, and void this rental so it no longer counts as a valid return. Please remove my payment (payment_id 4177 for customer 153) and update the rental record (rental_id 14944 for customer 153) to set the return_date to null.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id=4177 AND customer_id=153"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date=NULL WHERE rental_id=14944 AND customer_id=153"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="302",
      instruction="I am MICHAEL SILVERMAN, with customer_id 302. First, verify my identity by confirming that customer_id 302 corresponds to first name MICHAEL and last name SILVERMAN. Then, update rental_id 13916 and rental_id 14120 to set staff_id to 2, ensuring both rentals belong to me (customer_id 302). Additionally, update payment_id 8210 to staff_id 2, confirming it is associated with my account (customer_id 302). Use the provided IDs and validate ownership for all changes.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 302 AND first_name = 'MICHAEL' AND last_name = 'SILVERMAN';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET staff_id = 2 WHERE rental_id = 13916 AND customer_id = 302;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET staff_id = 2 WHERE rental_id = 14120 AND customer_id = 302;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 2 WHERE payment_id = 8210 AND customer_id = 302;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4",
      instruction="Authenticate me as HARRY ARCE with customer_id=368 and email=HARRY.ARCE@sakilacustomer.org. Deactivate my account. Issue a refund for my payment with payment_id=9971. Also, change the category_id for film_id=901 from 2 to 5.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET active='0' WHERE customer_id=368 AND email='HARRY.ARCE@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount=0.00 WHERE payment_id=9971 AND customer_id=368;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film_category SET category_id=5 WHERE film_id=901 AND category_id=2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5",
      instruction="Hello, I am Harold Martino (customer ID 342). As someone who values accuracy and sustainability, I have three requests. First, please update the category of the film 'KISS GLORY' (film ID 500) from 'Foreign' (category ID 9) to 'Drama' (category ID 7). Second, I was double-charged for my rental ID 10242, and I need the duplicate payment with ID 9253 under my account (customer ID 342) removed. Lastly, deactivate my account (customer ID 342) due to my commitment to reducing digital environmental impact.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film_category SET category_id = 7 WHERE film_id = 500;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 9253 AND rental_id = 10242 AND customer_id = 342;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET active = '0' WHERE customer_id = 342;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6",
      instruction="I am Eva Ramos (CustomerID: 140, email: EVA.RAMOS@sakilacustomer.org). Please authenticate my account first. After verification, delete the erroneous payment for rental ID 12086 of the film 'SUNDANCE INVASION'. The payment has ID 3794 and was processed on 2005-08-17 22:20:01.000.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 140 AND email = 'EVA.RAMOS@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 3794 AND customer_id = 140 AND rental_id = 12086 AND payment_date = '2005-08-17 22:20:01.000';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="572",
      instruction="Hello, I'm Sidney Burleson with the email SIDNEY.BURLESON@sakilacustomer.org. On August 1, 2005, I rented the film 'COMA HEAD' (film_id: 167) from store 1 under rental_id 10204 and payment_id 15327. The store confirmed the correct rental price is $2.99, but I was charged $4.99. Please adjust the payment for payment_id 15327 to reflect the $2.99 amount. Additionally, I noticed a typo in the film's database description. Could you update the description for film_id 167 to: 'A Dramatic Story of a Boy and a Frisbee who must Escape a Pastry Chef in California.'?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'SIDNEY.BURLESON@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 15327 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'SIDNEY.BURLESON@sakilacustomer.org');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film SET description = 'A Dramatic Story of a Boy and a Frisbee who must Escape a Pastry Chef in California.' WHERE film_id = 167;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9",
      instruction="I am Cynthia Young (email: CYNTHIA.YOUNG@sakilacustomer.org). For my most recent rental of 'SUSPECTS QUILLS' (rental_id=12938), I noticed the return date is missing, but I returned the film on '2006-02-15 10:00:00.000'. Please update the return_date for rental_id=12938 to '2006-02-15 10:00:00.000'. Also, the staff for the related payment (payment_id=781) was misattributed; it should be staff_id=1. Please correct the staff_id on payment_id=781 to 1.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'CYNTHIA.YOUNG@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2006-02-15 10:00:00.000' WHERE rental_id = 12938 AND customer_id = 28;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 1 WHERE payment_id = 781 AND customer_id = 28;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="11",
      instruction="As Andre Rapp (email: ANDRE.RAPP@sakilacustomer.org), I am requesting a refund for the rental 'SCORPION APOLLO' (rental ID: 15274) due to dissatisfaction. Please delete the payment record (payment ID: 13887) and update the rental record to show the film was not returned by setting its return date to NULL.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'ANDRE.RAPP@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 13887 AND customer_id = 515 AND rental_id = 15274;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = NULL WHERE rental_id = 15274 AND customer_id = 515;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12",
      instruction="Hello, my name is Jo Fowler with Customer ID 250. I accidentally rented 'ANNIE IDENTITY' (payment ID: 6746, rental ID: 5540, inventory ID: 132, film ID: 26). Could you please cancel this rental and issue a refund by removing payment ID 6746 and rental ID 5540? Also, set my account status to inactive (active=0) since I won't be renting for a while.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 6746 AND customer_id = 250;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 5540 AND customer_id = 250 AND inventory_id = 132;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET active = '0' WHERE customer_id = 250;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="14",
      instruction="I am EARL SHANKS, customer ID 396 with email EARL.SHANKS@sakilacustomer.org. I identified an error in payment_id 10718 for rental_id 5059 (film: SUMMER SCARFACE) – the recorded amount is $1.99, but it should be $2.99 due to a missed promotion. Please update payment_id 10718 to $2.99 for my account. After updating, confirm the change by showing the updated record for payment_id 10718.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 396 AND email = 'EARL.SHANKS@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 10718 AND customer_id = 396;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM payment WHERE payment_id = 10718 AND customer_id = 396;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="15",
      instruction="My name is RENE MCALISTER and my email is RENE.MCALISTER@sakilacustomer.org. I request deletion of my rental record with rental_id 4075 (inventory_id 1989) and a refund for the associated payment (payment_id 15880), as this was an accidental transaction for the film 'HORN WORKING'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE first_name = 'RENE' AND last_name = 'MCALISTER' AND email = 'RENE.MCALISTER@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 15880 AND customer_id = 593;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 4075 AND customer_id = 593 AND inventory_id = 1989;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="17",
      instruction="I am JULIA FLORES (CustomerID: 89, email: JULIA.FLORES@sakilacustomer.org). After speaking with your team, I request that for my three most recent rentals at store_id=1, the responsible staff be updated to staff_id=2 instead of staff_id=1. Please modify both rental and payment records accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET staff_id = 2 WHERE rental_id IN (SELECT rental_id FROM (SELECT rental_id FROM rental r JOIN inventory i ON r.inventory_id = i.inventory_id WHERE r.customer_id = 89 AND i.store_id = 1 ORDER BY r.rental_date DESC LIMIT 3) AS t)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 2 WHERE rental_id IN (SELECT rental_id FROM (SELECT rental_id FROM rental r JOIN inventory i ON r.inventory_id = i.inventory_id WHERE r.customer_id = 89 AND i.store_id = 1 ORDER BY r.rental_date DESC LIMIT 3) AS t)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="18",
      instruction="Hello, I am FRED WHEAT (email: FRED.WHEAT@sakilacustomer.org). I recently rented 'SWEETHEARTS SUSPECTS' (rental_id: 13898, inventory_id: 4007, film_id: 873), but forgot to mark it as returned. Please update the return_date for this rental (rental_id: 13898) to '2024-06-25'. Also, I paid $0.99 for this rental (payment_id: 9999), but I believe the correct amount should be $0.79. Please update the payment record for payment_id: 9999 to reflect the new amount of 0.79.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2024-06-25' WHERE rental_id = 13898 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'FRED.WHEAT@sakilacustomer.org');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 0.79 WHERE payment_id = 9999 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'FRED.WHEAT@sakilacustomer.org');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22",
      instruction="Hello, I'm Mathew Bolin with customer ID 539. I have three requests: First, for my rental of 'WORDS HUNTER' (rental_id=10922), update the staff_id from 2 to 1 for payment ID 14524. Second, for my rental of 'WRATH MILE' (rental_id=9250), delete payment record ID 14521 due to a discount voucher. Third, change the category of film 'ENTRAPMENT SATISFACTION' (film_id=287) from Action (category_id=1) to Comedy (category_id=5).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 1 WHERE payment_id = 14524 AND customer_id = 539;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 14521 AND customer_id = 539;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film_category SET category_id = 5 WHERE film_id = 287 AND category_id = 1;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="23",
      instruction="You are JOAN COOPER with email joan.cooper@sakilacustomer.org. On July 29, 2005, you rented the film 'TOURIST PELICAN' (film_id: 898) with rental_id 8360 and inventory_id 4135, for which you were charged $4.99 via payment_id 1698. You believe the correct charge should have been $2.99 due to a promotion. To verify your identity and process the adjustment, update the payment amount for payment_id 1698 from $4.99 to $2.99 in the payment table, ensuring this payment is linked to your email.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 1698 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'joan.cooper@sakilacustomer.org');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="24",
      instruction="As Charlotte Hunter (CustomerID: 130, email: CHARLOTTE.HUNTER@sakilacustomer.org), I rented 'MASSACRE USUAL' (rental_id: 2982, film_id: 563) and paid $6.99 (payment_id: 3511). The category was listed as 'Games' (category_id: 10), but I believe it should be 'Horror' (category_id: 11). Please update the category and adjust my payment to $4.99, the standard rate for Horror films.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE email = 'CHARLOTTE.HUNTER@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film_category SET category_id = 11 WHERE film_id = 563 AND category_id = 10;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 4.99 WHERE payment_id = 3511 AND rental_id = 2982 AND customer_id = 130;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="27",
      instruction="Hi, I'm Roberto Vu, customer ID 484. I need help with two incorrect charges. First, for rental ID 12993 (payment ID 13080) on 'TWISTED PIRATES', I was charged $7.99 instead of the promotional $5.99 handled by staff member 1. Second, for rental ID 12024 (payment ID 13078) on 'LION UNCUT', please remove the payment since I never completed that rental.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 484;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 5.99, staff_id = 1 WHERE payment_id = 13080 AND customer_id = 484 AND rental_id = 12993;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 13078 AND customer_id = 484 AND rental_id = 12024;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="29",
      instruction="You are FREDERICK ISBELL, email FREDERICK.ISBELL@sakilacustomer.org. You realized that for your rental (rental_id 8143) and your payment (payment_id 11592) for the film 'SHREK LICENSE', the charged amount should have been 4.99 instead of 2.99, and the staff responsible should have been staff_id 2 instead of staff_id 1. Please update your payment to amount 4.99 and staff_id 2, and update your rental to staff_id 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 4.99, staff_id = 2 WHERE payment_id = 11592 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'FREDERICK.ISBELL@sakilacustomer.org');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET staff_id = 2 WHERE rental_id = 8143 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'FREDERICK.ISBELL@sakilacustomer.org');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="30",
      instruction="Hello, I'm Willie Markham with email WILLIE.MARKHAM@sakilacustomer.org. Due to illness, I delayed returning the film 'CENTER DINOSAUR' (inventory ID 604, rental ID 15655). I'd like to return it now and request a waiver for the late fee linked to payment ID 9708. Please mark the rental as returned immediately and set the fee amount to zero.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE email = 'WILLIE.MARKHAM@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = CURRENT_TIMESTAMP WHERE rental_id = 15655 AND customer_id = 359 AND inventory_id = 604;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 0 WHERE payment_id = 9708 AND customer_id = 359;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="34",
      instruction="Hello, I'm Marshall Thorn with customer ID 583. Could you update the staff assignment for my rental ID 11002? Please change the staff ID from its current value to 1 to ensure the correct employee from my store handles it.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET staff_id = 1 WHERE rental_id = 11002 AND customer_id = 583;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="35",
      instruction="I am Justin Ngo with email JUSTIN.NGO@sakilacustomer.org. I recently rented a film (rental ID 14212) titled 'WORST BANGER' (film ID 991) and noticed errors: the category is incorrect, and actor SPENCER DEPP (actor ID 100) is wrongly listed. Please update the film's category to Drama (category ID 7) and replace actor ID 100 with MERYL GIBSON (actor ID 154) for this film.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT rental_id FROM rental JOIN customer ON rental.customer_id = customer.customer_id WHERE rental.rental_id = 14212 AND customer.email = 'JUSTIN.NGO@sakilacustomer.org'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film_category SET category_id = 7 WHERE film_id = 991"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM film_actor WHERE film_id = 991 AND actor_id = 100"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO film_actor (actor_id, film_id, last_update) VALUES (154, 991, CURRENT_TIMESTAMP)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="36",
      instruction="Hello, I am GERALDINE PERKINS (Customer ID: 161). Regarding my rental #11838, I was incorrectly charged $2.99 for payment ID 4395; it should be $1.99. Also, my return date was extended to 2005-08-23 17:00:00. Please update the payment amount to $1.99 and adjust the return date accordingly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 161;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 1.99 WHERE payment_id = 4395 AND customer_id = 161;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2005-08-23 17:00:00' WHERE rental_id = 11838 AND customer_id = 161;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="37",
      instruction="I am MIKE WAY with customer_id 403 and email MIKE.WAY@sakilacustomer.org. First, verify my identity. Then, update my payment record: change the amount to 4.99 for payment_id 10895 and rental_id 10109. Additionally, update the rating to 'PG-13' for the film with film_id 625.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 403 AND email = 'MIKE.WAY@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 4.99 WHERE payment_id = 10895 AND customer_id = 403 AND rental_id = 10109;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film SET rating = 'PG-13' WHERE film_id = 625;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="38",
      instruction="I am RANDALL NEUMANN (email: RANDALL.NEUMANN@sakilacustomer.org), CustomerID 437. I would like to dispute the payment I made for my rental with rental_id 666. The original payment was $5.99 (payment_id 11775), but I am requesting a partial refund so the new payment should be $3.99 (a $2.00 reduction). Also, please update the staff assigned to my rental (rental_id 666) to staff_id 2 for accuracy.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'RANDALL.NEUMANN@sakilacustomer.org' AND customer_id = 437;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 3.99 WHERE payment_id = 11775 AND customer_id = 437;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET staff_id = 2 WHERE rental_id = 666 AND customer_id = 437;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="48",
      instruction="I am Sue Peters, customer ID 197. On August 22, 2005, I rented 'Nash Chocolat' (rental_id 14951) and was incorrectly charged $4.99 via payment_id 5352 instead of the $2.99 rate. To resolve this, please delete payment record 5352 linked to rental_id 14951 under my account. I'll handle payment directly with the store.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 5352 AND rental_id = 14951 AND customer_id = 197 AND EXISTS (SELECT 1 FROM customer WHERE customer_id = 197 AND first_name = 'Sue' AND last_name = 'Peters');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="49",
      instruction="I am CONSTANCE REID (customer_id=232, email=CONSTANCE.REID@sakilacustomer.org). I rented inventory_id=3496 (film: 'SAVANNAH TOWN') under rental record #14527 and want to swap it for inventory_id=2911 (film: 'OPPOSITE NECKLACE', store_id=2). Update rental #14527 to use inventory_id=2911 and adjust payment #6267 to $4.99, keeping original dates and staff unchanged.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET inventory_id=2911 WHERE rental_id=14527 AND customer_id=232;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount=4.99 WHERE payment_id=6267 AND customer_id=232;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="51",
      instruction="I am Rene McAlister (email: RENE.MCALISTER@sakilacustomer.org). I was overcharged for payment 15877. The charged amount was 4.99, but it should have been 2.99. Please update payment 15877 to reflect the correct amount of 2.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'RENE.MCALISTER@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 15877 AND customer_id = 593;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="52",
      instruction="Hello, I am Barbara Jones with email BARBARA.JONES@sakilacustomer.org. I rented the film 'STAGE WORLD' (rental ID: 13807, inventory ID: 3822, payment ID: 104, film ID: 837) and noticed I was charged $6.99 instead of the correct rental rate of $2.99. Please update my payment amount for payment ID 104 to $2.99 and ensure the film's rental rate is set to $2.99 for film ID 837.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE first_name = 'BARBARA' AND last_name = 'JONES' AND email = 'BARBARA.JONES@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 104 AND customer_id = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film SET rental_rate = 2.99 WHERE film_id = 837;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="53",
      instruction="I'm Marc Outlaw and my customer ID is 499. Please verify my identity first. Then, delete my rental with rental_id 1526 because I returned it late and was charged incorrectly. Also, update my payment with payment_id 13458 to set the amount to 6.99 instead of 4.99, as I actually owe that amount.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT first_name, last_name FROM customer WHERE customer_id = 499;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 1526 AND customer_id = 499;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 6.99 WHERE payment_id = 13458 AND customer_id = 499;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="64",
      instruction="Hi, I'm Judith Cox (Customer ID 64). My rental for 'Doors President' (Rental ID 13333) hasn't been marked as returned. Could you update it to show I returned it on February 18, 2006, at 10:30 AM?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2006-02-18 10:30:00.000' WHERE rental_id = 13333 AND customer_id = 64;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="58",
      instruction="My name is Susan Wilson (email: SUSAN.WILSON@sakilacustomer.org). First, authenticate me as the customer. Then, update my most recent rental (rental_id: 15805) to use inventory_id 2773 for 'MUSCLE BRIGHT' (film_id: 609) and adjust the payment amount for payment_id: 230 to 2.99 to match the rental rate of 'MUSCLE BRIGHT'. Ensure both updates apply only to my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET inventory_id = 2773 WHERE rental_id = 15805 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'SUSAN.WILSON@sakilacustomer.org' AND first_name = 'Susan' AND last_name = 'Wilson');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 230 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'SUSAN.WILSON@sakilacustomer.org' AND first_name = 'Susan' AND last_name = 'Wilson');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="59",
      instruction="Hello, I am Jordan Archuleta with email JORDAN.ARCHULETA@sakilacustomer.org. I mistakenly rented a film (rental ID 9265) and want to permanently remove this rental and its associated payment (payment ID 15006) from my records. Please delete both entries for my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE email = 'JORDAN.ARCHULETA@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 15006 AND customer_id = 560;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 9265 AND customer_id = 560;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="63",
      instruction="Hello, I'm Justin Ngo (CustomerID: 354, email: JUSTIN.NGO@sakilacustomer.org). I accidentally rented 'TROJAN TOMORROW' twice and need to cancel the latest unreturned rental (rental_id: 12759). Please mark it as returned immediately. Separately, I loved 'SWARM GOLD' (rental_id: 8609) and want to leave a comment on that rental record. Could you add a 'customer_comment' field (TEXT type) to the rental table, then record my comment 'Amazing film! Great cast.' for rental_id 8609?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = CURRENT_TIMESTAMP WHERE rental_id = 12759 AND customer_id = 354;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "ALTER TABLE rental ADD COLUMN customer_comment TEXT;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET customer_comment = 'Amazing film! Great cast.' WHERE rental_id = 8609 AND customer_id = 354;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="64",
      instruction="You are BRITTANY RILEY (CustomerID 187). You noticed that the payment record for payment_id 5087, associated with your rental_id 6057 (film: EXPENDABLE STALLION), is incorrect. Please update the amount from $3.99 to 2.99 for accurate personal accounting, ensuring the correction applies specifically to your customer_id 187.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 5087 AND rental_id = 6057 AND customer_id = 187;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="65",
      instruction="Hi, I am Christina Ramirez with customer ID 70. I've moved outside your service area and need to deactivate my account. Please update my email to christina.ramirez.new@email.com and mark the account as inactive. Confirm the new email is saved.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET email = 'christina.ramirez.new@email.com' WHERE customer_id = 70 AND first_name = 'Christina' AND last_name = 'Ramirez';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET active = '0' WHERE customer_id = 70 AND first_name = 'Christina' AND last_name = 'Ramirez';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT email, active FROM customer WHERE customer_id = 70;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="68",
      instruction="Hello, my name is Scott Shelley (customer ID 330, email SCOTT.SHELLEY@sakilacustomer.org). I recently noticed a payment of $2.99 made on 2006-02-14 15:16:03 for rental ID 11709 (film 'GRAIL FRANKENSTEIN'). I want to dispute this transaction and request a full refund. Please delete the payment record with payment_id 8931 for this rental, and mark the rental (rental_id 11709) as 'not returned' by setting the return_date to NULL.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 330 AND email = 'SCOTT.SHELLEY@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 8931 AND customer_id = 330 AND rental_id = 11709 AND amount = 2.99 AND payment_date = '2006-02-14 15:16:03';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = NULL WHERE rental_id = 11709 AND customer_id = 330;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="372",
      instruction="Hello, I'm Steve Mackenzie (CustomerID: 372). I need to modify my existing rental (rental_id: 11134) for 'Minds Truman' to rent 'Suit Walls' instead. Please update the rental to use inventory_id 3949. Also, ensure the payment (payment_id: 10075) stays associated with rental_id 11134.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET inventory_id = 3949 WHERE rental_id = 11134 AND customer_id = 372;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET rental_id = 11134 WHERE payment_id = 10075 AND customer_id = 372;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="74",
      instruction="Hi, I'm Lorraine Stephens (customer ID: 165). Please update my email address to lorraine.stephens@gmail.com. Also, I had a late return penalty for my rental (rental ID: 9685, payment ID: 4481) of 'PINOCCHIO SIMON'. Could you waive the $2.00 late fee? The total should just be the base rental rate of $2.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET email = 'lorraine.stephens@gmail.com' WHERE customer_id = 165;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 4481 AND customer_id = 165 AND rental_id = 9685;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="76",
      instruction="My name is ALLAN CORNISH, customer ID 548, and my email is ALLAN.CORNISH@sakilacustomer.org. For my overdue rental of film_id 864 (rental_id 13584), please update the return_date to '2024-06-25 15:00:00'. Additionally, for the payment associated with this rental (payment_id 14727), update the staff_id to 2, as it was incorrectly entered. Please make both corrections now.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 548 AND email = 'ALLAN.CORNISH@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2024-06-25 15:00:00' WHERE rental_id = 13584 AND customer_id = 548;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 2 WHERE payment_id = 14727 AND customer_id = 548;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="78",
      instruction="Hello, I am LEESTER KRAUS (customer ID 492). For rental ID 15958, please update the staff_id for payment ID 13275 from 1 to 2. Only this payment record should be modified; no other changes are needed.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 2 WHERE payment_id = 13275 AND customer_id = 492 AND rental_id = 15958;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="79",
      instruction="Hello, I'm LAWRENCE LAWTON with customer ID 361. I believe I returned the movie 'HALF OUTFIELD' (rental ID: 14769, inventory ID: 1800, film ID: 391) on 2006-02-15 at 09:00:00, but it's still marked unreturned. Could you please update the rental record to show it was returned on that date? Also, adjust the payment record (payment ID: 9773) to charge the standard fee of 2.99 on the same date.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 361 AND first_name = 'LAWRENCE' AND last_name = 'LAWTON';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2006-02-15 09:00:00' WHERE rental_id = 14769 AND customer_id = 361;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99, payment_date = '2006-02-15 09:00:00' WHERE payment_id = 9773 AND customer_id = 361;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="80",
      instruction="I am Elizabeth Brown (last name 'BROWN', email 'ELIZABETH.BROWN@sakilacustomer.org'). I recently rented 'GABLES METROPOLIS' but forgot to return it. I have now returned the film. Please update my rental record for rental_id 13209 to set the return_date to '2006-02-17 10:00:00.000'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE last_name = 'BROWN' AND email = 'ELIZABETH.BROWN@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2006-02-17 10:00:00.000' WHERE rental_id = 13209 AND customer_id = 5;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="83",
      instruction="I am RUBY WASHINGTON (CustomerID 90). Please verify my identity by confirming my first name and last name. After verification, update the payment amount for payment ID 2448 (associated with rental ID 7035 and customer ID 90) to $4.99 to correct the overcharge for the 'LOSER HUSTLER' rental.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT first_name, last_name FROM customer WHERE customer_id = 90;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 4.99 WHERE payment_id = 2448 AND customer_id = 90 AND rental_id = 7035;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="84",
      instruction="I am KAREN JACKSON, Customer ID 13, with email KAREN.JACKSON@sakilacustomer.org. For my rental of 'MISSION ZOOLANDER' (rental ID 14252, rented on 2005-08-21 05:44:07.000, inventory ID 2660), currently assigned to staff ID 1, please update the staff to ID 2. Also update the related payment record (payment ID 355) for this rental to staff ID 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET staff_id = 2 WHERE rental_id = 14252 AND customer_id = 13 AND inventory_id = 2660 AND rental_date = '2005-08-21 05:44:07.000' AND staff_id = 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 2 WHERE payment_id = 355 AND customer_id = 13 AND rental_id = 14252;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="85",
      instruction="I am Dave Gardiner. Request deletion of my rental with ID 16025 (inventory 1777, rented on '2005-08-23 21:48:54') and its associated payment (ID 15261, amount 4.99, paid on '2005-08-23 21:48:54', staff ID 2) from my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 15261 AND customer_id = (SELECT customer_id FROM customer WHERE first_name = 'Dave' AND last_name = 'Gardiner') AND amount = 4.99 AND payment_date = '2005-08-23 21:48:54.000' AND staff_id = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 16025 AND customer_id = (SELECT customer_id FROM customer WHERE first_name = 'Dave' AND last_name = 'Gardiner') AND inventory_id = 1777 AND rental_date = '2005-08-23 21:48:54.000';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="90",
      instruction="I am JORDAN ARCHULETA (email: JORDAN.ARCHULETA@sakilacustomer.org). I noticed a charge for renting 'MOVIE SHAKESPEARE' (inventory_id: 2752, rental_id: 14425) that I never picked up. Please remove this rental entirely and reverse the payment. Delete the payment record (payment_id: 15020) and the rental record (rental_id: 14425, inventory_id: 2752) from my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'JORDAN.ARCHULETA@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 15020 AND rental_id = 14425 AND customer_id = 560;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 14425 AND inventory_id = 2752 AND customer_id = 560;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="97",
      instruction="Hello, I'm Vivian Ruiz (email: VIVIAN.RUIZ@sakilacustomer.org, Customer ID: 184). I accidentally rented 'INTENTIONS EMPIRE' (rental ID 7686) and need to switch to 'EVE RESURRECTION' using inventory ID 1310 from store ID 1. Please update rental ID 7686 to inventory ID 1310. After completing the update, share the revised rental details and associated payment records for my reference.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET inventory_id = 1310 WHERE rental_id = 7686 AND customer_id = 184;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT r.rental_id, r.rental_date, r.return_date, r.inventory_id, f.title, p.payment_id, p.amount, p.payment_date FROM rental r JOIN inventory i ON r.inventory_id = i.inventory_id JOIN film f ON i.film_id = f.film_id LEFT JOIN payment p ON p.rental_id = r.rental_id WHERE r.rental_id = 7686 AND r.customer_id = 184;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100",
      instruction="You are Arthur Simpkins (email: ARTHUR.SIMPKINS@sakilacustomer.org, CustomerID: 346). You are polite but firm, and noticed that for your rental of the film 'CHILL LUCK' (rental_id: 10521), you were charged twice. You want to reverse and refund only the payment with payment_id 9358, payment_date '2005-08-01 11:46:17.000', and amount 0.99, to your credit card. Please delete this payment record from the payment table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 9358 AND customer_id = 346 AND rental_id = 10521 AND amount = 0.99 AND payment_date = '2005-08-01 11:46:17.000' AND EXISTS (SELECT 1 FROM customer WHERE customer_id = 346 AND email = 'ARTHUR.SIMPKINS@sakilacustomer.org');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="101",
      instruction="I am KARL SEAL, customer ID 526. Please update my email address to 'karl.seal.new@mail.com' after verifying that my first name is 'KARL' and last name is 'SEAL'. Additionally, for rental ID 16043 (film 'STING PERSONAL', film_id 846), I request a full refund due to a defective DVD. Please set the payment amount to 0 and update the payment date to the current timestamp, ensuring this rental corresponds to film_id 846.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET email = 'karl.seal.new@mail.com' WHERE customer_id = 526 AND first_name = 'KARL' AND last_name = 'SEAL';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 0, payment_date = CURRENT_TIMESTAMP WHERE rental_id = 16043 AND customer_id = 526 AND EXISTS (SELECT 1 FROM rental JOIN inventory ON rental.inventory_id = inventory.inventory_id WHERE rental.rental_id = 16043 AND rental.customer_id = 526 AND inventory.film_id = 846);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="103",
      instruction="I am Pedro Chestnut. My email is PEDRO.CHESTNUT@sakilacustomer.org and customer ID is 475. I request a refund for payment ID 12851 associated with rental ID 8207 due to a faulty disc. Please set the payment amount to zero.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'PEDRO.CHESTNUT@sakilacustomer.org' AND customer_id = 475;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 0 WHERE payment_id = 12851 AND customer_id = 475 AND rental_id = 8207;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="104",
      instruction="I am SHANNON FREEMAN (CustomerID 123). I was charged $8.99 for rental ID 10295 (PaymentID 3328), but the correct amount should have been $4.99. Update the payment record to reflect $4.99 instead of $8.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 4.99 WHERE payment_id = 3328 AND customer_id = 123 AND rental_id = 10295;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="105",
      instruction="I am SHAWN HEATON (CustomerID 390, email SHAWN.HEATON@sakilacustomer.org). I need to void payment 10576 and permanently remove my rental record for 'NIGHTMARE CHILL' (rental_id 12105, inventory_id 2848) from the system. First, delete payment 10576 linked to rental 12105. Then, delete rental 12105 associated with inventory 2848. Execute deletions strictly in this order. Only report back if errors occur.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id=390 AND email='SHAWN.HEATON@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id=10576 AND customer_id=390 AND rental_id=12105;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id=12105 AND customer_id=390 AND inventory_id=2848;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="52",
      instruction="Hello, I'm JULIE SANCHEZ (customer ID 52). I need to permanently delete rental ID 12001 and its associated payment ID 1453 from my records. Please remove both entries.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 52 AND first_name = 'JULIE' AND last_name = 'SANCHEZ';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 1453 AND customer_id = 52;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 12001 AND customer_id = 52;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="108",
      instruction="I am COLLEEN BURTON (authenticating with email COLLEEN.BURTON@sakilacustomer.org). I have not yet returned my rented movie, and the rental ID is 13374. I'd like to process my return today with the exact return timestamp '2006-02-15 10:00:00' and request a refund for the payment of $4.99 made on payment_id 6133 for this rental. Please update the return_date and delete the payment for rental ID 13374 to process my refund.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE email = 'COLLEEN.BURTON@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2006-02-15 10:00:00' WHERE rental_id = 13374 AND customer_id = 227;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 6133 AND customer_id = 227 AND rental_id = 13374;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="109",
      instruction="I'm Edwin Burk (edwin.burk@sakilacustomer.org). I recently rented the film 'PLUTO OLEANDER' (film_id=686). I noticed it’s incorrectly categorized as 'New' (category_id=13). Please update its category to 'Action' (category_id=1) instead, so the next time it's more findable in the right section.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'edwin.burk@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM film_category WHERE film_id = 686;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM film_category WHERE film_id = 686 AND category_id = 13;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO film_category (film_id, category_id, last_update) VALUES (686, 1, CURRENT_TIMESTAMP);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="118",
      instruction="I am Loretta Carpenter with customer ID 189 and email LORETTA.CARPENTER@sakilacustomer.org. I was double-charged for renting 'TELEGRAPH VOYAGE'. Please delete the duplicate rental record (rental_id 10247, inventory_id 4035) and its associated payment (payment_id 5143) from my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id, email FROM customer WHERE customer_id = 189 AND email = 'LORETTA.CARPENTER@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 5143 AND customer_id = 189 AND rental_id = 10247;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 10247 AND customer_id = 189 AND inventory_id = 4035;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="121",
      instruction="Hello, I am Jennie Terry with customer ID 265. Please update my email address to jennie.t.new@gmail.com. Additionally, I mistakenly rented the film 'REEF SALUTE' (rental ID 7414, payment ID 7166) and would like to cancel this rental entirely and issue a refund for its payment. Lastly, for my rental of 'LADY STAGE' (payment ID 7162), I believe I was overcharged—the amount should be corrected from $4.99 to $2.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET email = 'jennie.t.new@gmail.com' WHERE customer_id = 265;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 7166;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 7414;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 7162;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="125",
      instruction="Hello, I'm Suzanne Nichols (email: SUZANNE.NICHOLS@sakilacustomer.org). For my rental of 'DADDY PITTSBURGH', the payment record (payment_id 4174) shows staff_id 1 instead of 2. Please update it to staff_id 2 after confirming it belongs to me.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 2 WHERE payment_id = 4174 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'SUZANNE.NICHOLS@sakilacustomer.org')"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="126",
      instruction="Hello, I'm Charlotte Hunter with customer ID 130. Please update the return date for my rental (rental ID 10645) to '2005-08-06 15:00:00.000'. Also adjust the payment amount to $3.99 for payment ID 3521 due to a $2.00 promotional coupon applied during early return.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET return_date = '2005-08-06 15:00:00.000' WHERE rental_id = 10645 AND customer_id = 130;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 3.99 WHERE payment_id = 3521 AND customer_id = 130;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="129",
      instruction="Verify my identity using my email BRITTANY.RILEY@sakilacustomer.org. For my rental of 'OUTFIELD MASSACRE' (film_id=647, rental_id=4429), I was charged $4.99 instead of the correct $0.99 rate. Update the payment amount to $0.99. Also, change the film's category from 'Music' (category_id=12) to 'Drama' (category_id=7).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'BRITTANY.RILEY@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 0.99 WHERE rental_id = 4429 AND customer_id = 187;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film_category SET category_id = 7 WHERE film_id = 647 AND category_id = 12;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="130",
      instruction="Hello, I am Travis Estep. My customer ID is 417 and my email is TRAVIS.ESTEP@sakilacustomer.org. I need to delete my rental record for rental ID 15795 (associated with the film 'WAIT CIDER') and its payment record for payment ID 11293, as this rental was accidental. Separately, please update the rental rate for the film 'MINE TITANS' (film ID 580) to 2.99 to reflect an ongoing promotion.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE email = 'TRAVIS.ESTEP@sakilacustomer.org' AND customer_id = 417;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 11293 AND rental_id = 15795 AND customer_id = 417;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 15795 AND customer_id = 417;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE film SET rental_rate = 2.99 WHERE film_id = 580;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="132",
      instruction="I am Maurice Crawley (Customer ID: 482). Please reactivate my inactive account and update my email address to 'maurice.crawley2024@example.com'. Additionally, correct the staff assignment for payment ID 13036 (related to rental ID 15879) to reflect staff ID 2 instead of the current one.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customer SET active = '1', email = 'maurice.crawley2024@example.com' WHERE customer_id = 482;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET staff_id = 2 WHERE payment_id = 13036 AND rental_id = 15879 AND customer_id = 482;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="133",
      instruction="Hello, I am GLORIA COOK (customer id 56) with email GLORIA.COOK@sakilacustomer.org. I noticed an unauthorized charge on my account for rental_id 10678 (film: 'WESTWARD SEABISCUIT') that I did not make. Please remove both the rental record (rental_id 10678) and its associated payment (payment_id 1553) from my records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 1553 AND customer_id = 56;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 10678 AND customer_id = 56;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="135",
      instruction="Hello, I'm Audrey Ray. My email is AUDREY.RAY@sakilacustomer.org. For my rental #4904 (film 'HYDE DOCTOR'), I noticed payment #4697 was recorded as $7.99 instead of the correct $2.99 rate. Please update it to $2.99.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 2.99 WHERE payment_id = 4697 AND rental_id = 4904 AND customer_id = (SELECT customer_id FROM customer WHERE email = 'AUDREY.RAY@sakilacustomer.org');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="136",
      instruction="I am Shawn Heaton (customer_id: 390). Please correct the payment for rental_id 9825: update payment_id 10574 from $4.99 to $3.99. Also set the last_update field for rental_id 9825 to today's date.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 3.99 WHERE payment_id = 10574 AND customer_id = 390;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET last_update = CURRENT_DATE WHERE rental_id = 9825 AND customer_id = 390;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="138",
      instruction="Hello, I'm Brent Harkins (Customer ID 493). I’m contacting you about an erroneous charge on my account. I was billed for renting 'BIRDS PERDITION' (rental ID 13675), which I never rented. Please delete this rental record and its associated payment (payment ID 13292). I confirm customer ID 493, rental ID 13675, and payment ID 13292 are accurate. Remove all traces of this transaction.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 493;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 13292 AND customer_id = 493;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 13675 AND customer_id = 493;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="141",
      instruction="I am WAYNE TRUONG (Customer ID: 370). Please authenticate me first. Then, verify that inventory ID 2338 corresponds to the film 'LAMBS CINCINATTI'. Once confirmed, update my payment ID 10004 (linked to rental ID 7152) to $4.99 and change the staff for rental ID 7152 (inventory ID 2338) to staff ID 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 370 AND first_name = 'WAYNE' AND last_name = 'TRUONG';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT film.title FROM inventory INNER JOIN film ON inventory.film_id = film.film_id WHERE inventory.inventory_id = 2338 AND film.title = 'LAMBS CINCINATTI';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE payment SET amount = 4.99 WHERE payment_id = 10004 AND customer_id = 370 AND rental_id = 7152;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE rental SET staff_id = 2 WHERE rental_id = 7152 AND customer_id = 370 AND inventory_id = 2338;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="146",
      instruction="I am Kathy James (CustomerID: 71). First, verify my identity. Then, delete my payment record with payment_id 1930. After that, delete my rental record with rental_id 8783 and inventory_id 2316 to remove all traces of this transaction.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customer WHERE customer_id = 71 AND first_name = 'KATHY' AND last_name = 'JAMES';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 1930 AND customer_id = 71;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 8783 AND customer_id = 71 AND inventory_id = 2316;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="149",
      instruction="Authenticate me using my customer ID 270 and email LEAH.CURTIS@sakilacustomer.org. Once verified, permanently delete my most expensive rental transaction and its associated payment from my account history.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT customer_id FROM customer WHERE customer_id = 270 AND email = 'LEAH.CURTIS@sakilacustomer.org';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT payment_id, rental_id, amount FROM payment WHERE customer_id = 270 ORDER BY amount DESC LIMIT 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM payment WHERE payment_id = 7311 AND customer_id = 270;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM rental WHERE rental_id = 3987 AND customer_id = 270;"
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
