from tau_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="0",
      instruction="I am Kenneth Charles (SSN: 555-56-5555). Requesting transfer from Boston office (locationID: 2) to New York office (locationID: 3) and promotion to Manager position (positionID: 2). Please update my employee record - set locationID to 3 and positionID to 2 using my SSN: 555-56-5555.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '555-56-5555';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 3, positionID = 2 WHERE ssn = '555-56-5555';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="sasha_lin_la_manager",
      instruction="I'm Sasha Lin, office manager at our Los Angeles branch (locationID 8, address 1400 Main St, zip 94235). Please onboard two new team members: 1) Jordan Lee with SSN 112233445 as positionID 2 starting 2024-07-01 at $52k salary (Male, performance Pending). 2) Priya Patel with SSN 998877665 as positionID 3 starting same date at $58k salary (Female, performance Pending). After confirmation, please generate a current roster showing all employees assigned to locationID 8.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('112233445', 'Lee', 'Jordan', '2024-07-01', 52000, 'M', 'Pending', 2, 8);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('998877665', 'Patel', 'Priya', '2024-07-01', 58000, 'F', 'Pending', 3, 8);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT ssn, lastname, firstname, hiredate, salary, gender, performance, positionID FROM employee WHERE locationID = 8;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="locationID_5",
      instruction="As the HR administrator for the NYC office (locationID: 5, address: 1650 Washington Blvd, NY 15648), first update the office phone number to '(518)256-3150'. Then create a new Manager record for Steven Brown with: SSN '882-99-7766', first name 'Steven', last name 'Brown', hire date 6/17/24, salary 'US$72,000.00', gender 'M', performance 'Good', assigned to positionID 2 at locationID 5. Use only the exact values provided.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone='(518)256-3150' WHERE locationID=5;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('882-99-7766', 'Brown', 'Steven', '6/17/24', 'US$72,000.00', 'M', 'Good', 2, 5);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="000-02-2222",
      instruction="My name is Sandy Adams, SSN 000-02-2222. As an approved career advancement, please update my employee record: Change from current Position ID 3 (Trainee) to Position ID 1 (Account Representative), and assign me to Location ID 1 (450 Peachtree Rd, Atlanta, 30316). Confirm my current position is Trainee before updating.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '000-02-2222' AND firstname = 'Sandy' AND lastname = 'Adams' AND positionID = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 1, locationID = 1 WHERE ssn = '000-02-2222' AND positionID = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6",
      instruction="You are Patricia Milgrom (SSN: 000-01-0000), Manager at Boston office (locationID: 2). First verify your identity. Transfer Kenneth Charles (SSN: 555-56-5555) from current locationID 2 to new locationID 3, updating his position to positionID 2 (Manager). Confirm the updated employee record after making these changes.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '000-01-0000';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 3, positionID = 2 WHERE ssn = '555-56-5555' AND locationID = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '555-56-5555';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="location_manager_los_angeles",
      instruction="As manager of the Los Angeles office at 1400 Main St, CA 94235 (locationID 8), I need to: (1) Update our office phone number to '(213)123-4567' specifically for locationID 8, (2) Permanently remove all employees currently assigned to locationID 8, and (3) After confirming successful deletion of employees from locationID 8, delete the location record for ID 8. Please execute these actions sequentially and confirm completion after each step.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone = '(213)123-4567' WHERE locationID = 8;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM employee WHERE locationID = 8;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM location WHERE locationID = 8;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="8",
      instruction="You are Sandy Adams (SSN: 000-02-2222) working as a Trainee (positionID 3) at the Atlanta office (locationID 1). Request a promotion to Account Representative (positionID 1) at the same location by updating your positionID and setting your salary to US$30,000.00. Keep your existing locationID (1) unchanged.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 1, salary = 'US$30,000.00' WHERE ssn = '000-02-2222' AND lastname = 'Adams' AND firstname = 'Sandy' AND positionID = 3 AND locationID = 1;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="123-45-6789",
      instruction="I am Tracy Coulter (SSN: 123-45-6789), manager at Atlanta office (LocationID: 1). Please execute the following for Sandy Adams (SSN: 000-02-2222): 1) Update her position to Account Representative (PositionID: 1) 2) Set salary to US$28,000.00 3) Return verification of her current position title and exact salary amount. Confirm all changes were applied successfully.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 1, salary = 'US$28,000.00' WHERE ssn = '000-02-2222';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT position.positiontitle, employee.salary FROM employee JOIN position ON employee.positionID = position.positionID WHERE employee.ssn = '000-02-2222';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="10",
      instruction="My name is Tracy Coulter with SSN 123-45-6789 (manager of Atlanta office locationID 1). First verify my identity and authorization. Then: 1) Update locationID 1's address to '1234 New Horizon Ave', zipcode 30316, and office phone '(404)333-5555'. 2) Set all employees at locationID 1 to 'Pending Review' performance status for relocation notifications.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT locationID FROM location WHERE locationID = 1 AND manager_ssn = '123-45-6789';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET address = '1234 New Horizon Ave', zipcode = 30316, officephone = '(404)333-5555' WHERE locationID = 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET performance = 'Pending Review' WHERE locationID = 1;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="123-45-6789",
      instruction="You are Tracy Coulter (SSN: 123-45-6789), manager at the Atlanta office (locationID: 1, positionID: 2). Update the performance rating for trainee Marietta Brown (SSN: 333-66-1234, locationID: 1) from 'Poor' to 'Good' based on documented improvements in her work quality.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '123-45-6789' AND positionID = 2 AND locationID = 1"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '333-66-1234' AND locationID = 1"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET performance = 'Good' WHERE ssn = '333-66-1234'"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="HR_admin_021",
      instruction="As HR administrator, I need to process William Martin's promotion from Trainee (positionID 3) to Manager (positionID 2) at locationID 5. His SSN is 767-74-7373. Update his salary to US$65,000.00 and verify the changes apply ONLY to the record matching SSN '767-74-7373' AND locationID 5. Confirm success by checking his updated position and salary.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 2, salary = 'US$65,000.00' WHERE ssn = '767-74-7373' AND locationID = 5;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT firstname, lastname, positionID, salary FROM employee WHERE ssn = '767-74-7373' AND locationID = 5;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="16",
      instruction="I’m the HR manager and need to update our Los Angeles office (locationID 8). First, update its address to '1500 Sunset Blvd' and office phone to '(213)123-4567'. Then, add a new employee with ssn='999-99-1234', lastname='Doe', firstname='John', hiredate='2024-06-24', salary=95000, gender='M', performance='Excellent', positionID=2, and assign them to locationID 8.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET address='1500 Sunset Blvd', officephone='(213)123-4567' WHERE locationID=8;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('999-99-1234', 'Doe', 'John', '2024-06-24', 95000, 'M', 'Excellent', 2, 8);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="18",
      instruction="You are Alex Rivera, HR manager at the Salt Lake City office (locationID 7). Add a new employee record for Emily Thompson with social security number 589-17-3421. Details: first name 'Emily', last name 'Thompson', position ID 1, hire date 2024-05-15, starting salary 54000, gender F, performance rating 'Excellent', assigned to location ID 7.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('589-17-3421', 'Thompson', 'Emily', '2024-05-15', 54000, 'F', 'Excellent', 1, 7);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="555-22-3333",
      instruction="My name is Patricia Rubin, SSN 555-22-3333. I request a transfer from Boston office (locationID: 2) to a new office at these details: Address - 200 Liberty St, City - New York, State - NY, Zip Code - 10281, Office Phone - (212)555-5678. Additionally, update my performance rating to 'Excellent' due to recent achievements.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO location (locationcity, address, state, zipcode, officephone) VALUES ('New York', '200 Liberty St', 'NY', 10281, '(212)555-5678');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = (SELECT locationID FROM location WHERE address = '200 Liberty St' AND state = 'NY' AND zipcode = 10281) WHERE ssn = '555-22-3333';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET performance = 'Excellent' WHERE ssn = '555-22-3333';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="21",
      instruction="My name is Sandy Johanson with SSN 245-67-8910. I've been approved to transfer to locationID 8. Please confirm my current location is 6 and update my employee record to locationID 8 immediately.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '245-67-8910' AND locationID = 6;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 8 WHERE ssn = '245-67-8910' AND locationID = 6;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="SaltLakeMgr2024",
      instruction="As Melanie Griggs managing locationID 7 (316 S. State St, Salt Lake City), add: 1) Administrative Assistant Sam Keller (SSN 488-27-4312, M) hired 2024-06-10 at position's minimum salary with 'Satisfactory' rating. 2) Manager Olivia Pierce (SSN 592-34-1128, F) hired 2024-06-11 at position's maximum salary with 'Excellent' rating. Use EXACT position titles 'Administrative Assistant' and 'Manager' to retrieve official positionIDs and salary ranges from the position table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT positionID, minsalary FROM position WHERE positiontitle = 'Administrative Assistant';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT positionID, maxsalary FROM position WHERE positiontitle = 'Manager';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('488-27-4312', 'Keller', 'Sam', '2024-06-10', [minsalary_found], 'M', 'Satisfactory', [admin_positionID], 7);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('592-34-1128', 'Pierce', 'Olivia', '2024-06-11', [maxsalary_found], 'F', 'Excellent', [manager_positionID], 7);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="25",
      instruction="Authenticate me as David Adamson with SSN 776-67-6666. Update locationID 3's address to '600 Lakeview Ave'. Also update the salary for employee SSN 777-78-7777 to 45000.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '776-67-6666';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET address = '600 Lakeview Ave' WHERE locationID = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET salary = 45000 WHERE ssn = '777-78-7777';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="28",
      instruction="I am Holly Jones (SSN: 335-55-5533), Manager at the New York City office (locationID: 5). I have completed my executive MBA and request a promotion to Regional Manager (positionID: 4). Please update my employee record to set positionID = 4 and salary = 'US$100,000.00'. Additionally, update the office phone number for locationID 5 to '(212)555-1999' as the current number is outdated.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 4, salary = 'US$100,000.00' WHERE ssn = '335-55-5533';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone = '(212)555-1999' WHERE locationID = 5;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="29",
      instruction="My name is Dana Cho (SSN 987654321), hiring manager at the Los Angeles office (locationID 8). I want to add a new employee: SSN 534216879, First Name: Michael, Last Name: Nguyen, Gender: Male, Hire Date: 2024-06-14, Salary: 82000, Performance: Excellent. He will fill a new position we're creating: Position Title: Data Analyst, Education Required: Bachelor's, Minimum Salary: 70000, Maximum Salary: 90000. Please verify my identity first, then add the new position and assign Michael Nguyen to it at our office.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '987654321' AND locationID = 8;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO position (positiontitle, educationrequired, minsalary, maxsalary) VALUES ('Data Analyst', 'Bachelor''s', 70000, 90000);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, firstname, lastname, gender, hiredate, salary, performance, positionID, locationID) VALUES ('534216879', 'Michael', 'Nguyen', 'Male', '2024-06-14', 82000, 'Excellent', (SELECT positionID FROM position WHERE positiontitle = 'Data Analyst' AND educationrequired = 'Bachelor''s' AND minsalary = 70000 AND maxsalary = 90000), 8);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="31",
      instruction="As Vernon Frank (SSN: 444-45-4444) from the Miami office (locationID: 4), I need to make two updates: First, change our Miami office phone number to (305)777-1010 at locationID 4. Second, update my employee performance review status to 'Excellent' using my SSN 444-45-4444. Both updates should be tied to my verified credentials.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone = '(305)777-1010' WHERE locationID = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET performance = 'Excellent' WHERE ssn = '444-45-4444';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="manager123",
      instruction="As the office administrator, I need to transfer all employees from locationID 8 (Los Angeles office) to locationID 10 (new San Francisco branch). First, generate a list of affected employees with their SSN, first name, and last name for verification. Then proceed to update their locationID from 8 to 10.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT ssn, firstname, lastname FROM employee WHERE locationID = 8;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 10 WHERE locationID = 8;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="35",
      instruction="Hello, this is David Whitehead (SSN: 925-45-7116). I've been approved for a transfer and need my office location updated to branch locationID=3. Please confirm the update of my employee record's locationID field to 3 first. Once updated, could you provide me specifically with the physical address and direct office phone number associated with locationID=3?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 3 WHERE ssn = '925-45-7116';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT address, officephone FROM location WHERE locationID = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="39",
      instruction="I am Holly Jones (SSN: 335-55-5533), Manager at the New York City office (locationID 5). I have transferred to a new branch assigned to locationID 10 and need my employee record updated accordingly. Additionally, please update the office phone number for locationID 5 to '(518)999-9999' due to a recent phone line upgrade at my previous location.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 10 WHERE ssn = '335-55-5533';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone = '(518)999-9999' WHERE locationID = 5;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="LaurenSanchez_001",
      instruction="As Lauren Sanchez, HR Manager for the Los Angeles office (locationID=8), first confirm my authorization by verifying my employee record. Then create a new Marketing Director position with positionID=3, requiring an MBA, minimum salary $120,000 and maximum $180,000. Subsequently, onboard Sam Patterson (SSN: 982-66-1542) with salary $145,000 starting 2024-06-10 - Excellent performance rating, assigned to positionID=3 at locationID=8.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE lastname = 'Sanchez' AND firstname = 'Lauren' AND positionID = (SELECT positionID FROM position WHERE positiontitle = 'HR Manager') AND locationID = 8;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO position (positionID, positiontitle, educationrequired, minsalary, maxsalary) VALUES (3, 'Marketing Director', 'MBA', 120000, 180000);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('982-66-1542', 'Patterson', 'Sam', '2024-06-10', 145000, 'M', 'Excellent', 3, 8);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="41",
      instruction="I need to transfer Holly Holmes (SSN: 625-62-6262) from the Miami office (locationID:4) to the Atlanta office (locationID:5). After completing the transfer, display Holly's full employee record to verify the location update.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 5 WHERE ssn = '625-62-6262' AND locationID = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '625-62-6262';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="42",
      instruction="I am Melissa Roberts (SSN: 612-99-1111). Update Kelly Marder's (SSN: 777-78-7777) performance review to 'Excellent' and assign her to locationID 2. Then provide the office phone number for locationID 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '612-99-1111';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET performance = 'Excellent' WHERE ssn = '777-78-7777';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 2 WHERE ssn = '777-78-7777';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT officephone FROM location WHERE locationID = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="43",
      instruction="I am Emily Wood (SSN 109-87-6543), Manager at the New York City office (locationID 5). Please update my performance review from 'Average' to 'Excellent' in the employee records. Also, change the office phone number for locationID 5 from (518)256-3100 to (212)333-1234.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '109-87-6543' AND firstname = 'Emily' AND lastname = 'Wood' AND locationID = 5;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET performance = 'Excellent' WHERE ssn = '109-87-6543';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone = '(212)333-1234' WHERE locationID = 5;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="45",
      instruction="As Emily Wood (SSN: 109-87-6543), Manager at New York City locationID 5, I need to: 1) Verify my current Manager status (positionID: 2) at locationID 5. 2) Upon confirmation, promote employee William Martin (SSN: 767-74-7373) from positionID 3 (Trainee) to positionID 2 (Manager), set salary to 'US$70,000.00', and maintain his locationID 5 assignment.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT ssn FROM employee WHERE ssn = '109-87-6543' AND positionID = 2 AND locationID = 5"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 2, salary = 'US$70,000.00', locationID = 5 WHERE ssn = '767-74-7373'"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="47",
      instruction="This is Jose Rodriguez (SSN 500-50-0505), Regional Manager (positionID 4) at New York City office (locationID 5). Process my retirement by deleting my employee record. Subsequently, promote Holly Jones (SSN 335-55-5533) from Manager (positionID 2) to Regional Manager (positionID 4) at locationID 5.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '500-50-0505';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM employee WHERE ssn = '500-50-0505';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 4, locationID = 5 WHERE ssn = '335-55-5533';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="48",
      instruction="Authenticate as David Whitehead (SSN: 925-45-7116), Regional Manager in Boston. After authentication, promote Patricia Rubin (SSN: 555-22-3333) from Account Representative to Regional Manager (positionID: 4) at locationID 2. Set her salary to US$120,000.00 while maintaining her current locationID 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '925-45-7116';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 4, salary = 'US$120,000.00', locationID = 2 WHERE ssn = '555-22-3333';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="53",
      instruction="As Kimberly Allen (SSN 910-28-4662), please complete my onboarding to the Los Angeles office (locationID 8) with these details: Last name 'Allen', first name 'Kimberly', hire date June 10, 2024, salary $81,000, gender Female, performance rating 'Excellent', positionID 3. Also correct the office phone number for locationID 8 to (213)555-3011 as my documentation contained an error.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('910-28-4662', 'Allen', 'Kimberly', '2024-06-10', 81000, 'F', 'Excellent', 3, 8);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone = '(213)555-3011' WHERE locationID = 8;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Sarah Thompson",
      instruction="This is Sarah Thompson. Please execute these updates: For employee Mary Smith (SSN: 222-52-5555), set positionID to 2 and salary to 'US$60,000.00'. For the Chicago office (locationID: 3), set address to '700 Tech Parkway', zipcode to 60616, and officephone to '(312)333-5555'. The city remains Chicago and state remains IL.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 2, salary = 'US$60,000.00' WHERE ssn = '222-52-5555';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET address = '700 Tech Parkway', zipcode = 60616, officephone = '(312)333-5555' WHERE locationID = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="123-45-6789",
      instruction="I am Tracy Coulter (SSN: 123-45-6789), Manager at locationID 1 in Atlanta. Please update employee Frank Smith (SSN: 333-43-4444) with these changes: 1) Set performance rating to 'Excellent', 2) Assign to Manager position (positionID 2), 3) Update salary to 'US$110,000.00', 4) Maintain current location (locationID 1). Confirm implementation of all specified changes.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET performance = 'Excellent', positionID = 2, salary = 'US$110,000.00' WHERE ssn = '333-43-4444' AND locationID = 1"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="57",
      instruction="Please update employee Holly Holmes' (SSN: 625-62-6262) work assignment to location Miami (locationID 4) and set her performance rating to 'Excellent' in the employee database.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 4, performance = 'Excellent' WHERE ssn = '625-62-6262';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="606-78-4532",
      instruction="You are Kevin Turner (SSN: 606-78-4532). Please update your office location to Salt Lake City using location ID 7 and increase your annual salary from $65,000 to $72,000, effective immediately.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '606-78-4532';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 7 WHERE ssn = '606-78-4532';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET salary = 72000 WHERE ssn = '606-78-4532';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="123-45-6789",
      instruction="My name is Dana Moore with SSN 123-45-6789. I manage and work at the Salt Lake City office located at 316 S. State St (locationID 7). Update our office phone from '(801)459-6652' to '(801)123-9876' for this exact address and city. After updating, display all current details for locationID 7 to confirm.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '123-45-6789' AND firstname = 'Dana' AND lastname = 'Moore' AND locationid = 7"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone = '(801)123-9876' WHERE locationID = 7 AND address = '316 S. State St' AND locationcity = 'Salt Lake City' AND officephone = '(801)459-6652'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM location WHERE locationID = 7"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="61",
      instruction="As the HR manager for the Miami office (locationID 4), I need to: 1) Promote Vernon Frank (ssn '444-45-4444') from Account Representative (positionID 1) to Manager (positionID 2) at the same location (locationID 4), updating his salary to 'US$58,000.00'. 2) Terminate Holly Holmes (ssn '625-62-6262') currently assigned to the Miami office (locationID 4) by removing her employee record. Use the explicitly provided parameters including ssn and locationID values for both actions.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 2, salary = 'US$58,000.00' WHERE ssn = '444-45-4444' AND locationID = 4"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM employee WHERE ssn = '625-62-6262' AND locationID = 4"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="manager_saltlake_316SState",
      instruction="I am the manager for the Salt Lake City office (locationID: 7, 316 S. State St, UT 84125). Please update the HR record for our employee (ssn: '987-65-4321', current locationID: 7): promote them from positionID 2 to positionID 4 and set salary to 72000. After updating, confirm by displaying their first name, last name, new positionID, and updated salary from our location records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 4, salary = 72000 WHERE ssn = '987-65-4321' AND locationID = 7"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT firstname, lastname, positionID, salary FROM employee WHERE ssn = '987-65-4321' AND locationID = 7"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="444-45-4444",
      instruction="I am Vernon Frank (SSN 444-45-4444), Account Representative at locationID 4. First verify my identity. Then update my employee address to '125 Ocean Drive'. Separately, update the office phone number for locationID 4 to '(305)000-8888'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '444-45-4444';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET address = '125 Ocean Drive' WHERE ssn = '444-45-4444';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone = '(305)000-8888' WHERE locationID = 4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Simone Lee",
      instruction="My name is Simone Lee. Please: 1) Verify my identity, 2) Update the Salt Lake City office (locationID 7) phone number from '(801)459-6652' to '(801)500-8001', and 3) Move all employees from other locations to locationID 7.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT ssn FROM employee WHERE firstname = 'Simone' AND lastname = 'Lee';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone='(801)500-8001' WHERE locationID=7 AND officephone='(801)459-6652';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID=7 WHERE locationID <> 7;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="66",
      instruction="I am Sandy Johanson, SSN 245-67-8910. Please update my employee record to positionID 1 and change the Denver office (locationID 6) phone number to (303)123-4567.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '245-67-8910';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 1 WHERE ssn = '245-67-8910';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET officephone = '(303)123-4567' WHERE locationID = 6;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="67",
      instruction="Hello, this is Sandra McGregor, HR Manager for the Los Angeles office at 1400 Main St, CA 94235 (locationID 8). We are expanding our team and need to: 1) Create a new position with positionID 301, titled 'Data Analyst', requiring Bachelor's Degree, minimum salary 65000 and maximum salary 95000. 2) Hire Jordan Blake (SSN: 988-76-4503) with hire date 2024-06-18, salary 72000, gender M, performance Excellent, assigned to positionID 301 at our verified locationID 8.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO position (positionID, positiontitle, educationrequired, minsalary, maxsalary) VALUES (301, 'Data Analyst', 'Bachelor''s Degree', 65000, 95000);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('988-76-4503', 'Blake', 'Jordan', '2024-06-18', 72000, 'M', 'Excellent', 301, 8);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="69",
      instruction="You are Patricia Milgrom (ssn: '000-01-0000'), manager of locationID 2 in Boston. Update Emily Manin (ssn: '333-34-3333') and Patricia Rubin (ssn: '555-22-3333') from positionID 1 to 4, but only if they currently hold positionID 1 at your location (locationID 2). First confirm that positionID 4 exists in the system.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '000-01-0000';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM position WHERE positionID = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 4 WHERE ssn = '333-34-3333' AND positionID = 1 AND locationID = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET positionID = 4 WHERE ssn = '555-22-3333' AND positionID = 1 AND locationID = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="71",
      instruction="My name is Melissa Roberts, SSN 612-99-1111, manager at Chicago office (locationID 3). Please: 1. Verify my identity. 2. Add new Seattle office (locationID: 4) at 1200 Pacific Ave, Seattle, WA 98101 with phone (206)888-5555. 3. Transfer employee Harold Foster (SSN 109-87-6544) from locationID 3 to locationID 4.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '612-99-1111';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO location (locationID, locationcity, address, state, zipcode, officephone) VALUES (4, 'Seattle', '1200 Pacific Ave', 'WA', 98101, '(206)888-5555');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 4 WHERE ssn = '109-87-6544' AND locationID = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="333-43-4444",
      instruction="I am Frank Smith (ssn: 333-43-4444). Please update my profile with: 1) New office location (locationID 2) - Miami at 310 Biscayne Blvd, FL 33132, phone (305)444-7777. 2) New position (positionID 4) - Regional Manager requiring 4-year degree, salary range US$55,000.00-US$95,000.00. Set my location to ID 2, position to ID 4, and salary to US$70,000.00.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '333-43-4444';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO location (locationID, locationcity, address, state, zipcode, officephone) VALUES (2, 'Miami', '310 Biscayne Blvd', 'FL', 33132, '(305)444-7777');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO position (positionID, positiontitle, educationrequired, minsalary, maxsalary) VALUES (4, 'Regional Manager', '4 year degree', 'US$55,000.00', 'US$95,000.00');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 2, positionID = 4, salary = 'US$70,000.00' WHERE ssn = '333-43-4444';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="hr_manager_ca",
      instruction="My name is Evelyn Chen, newly hired HR manager for our Los Angeles office. Please complete these setup tasks: 1) Create location record with locationID 8, city 'Los Angeles', address '1400 Main St', state 'CA', zip code 94235. 2) Add positionID 1 titled 'Sales Manager' requiring Bachelor's Degree ($65k-$95k range). 3) Hire Luis Gonzalez (SSN 901-23-4567) starting 2024-07-10 as male employee with $70k salary in position 1 at location 8.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO location (locationID, locationcity, address, state, zipcode) VALUES (8, 'Los Angeles', '1400 Main St', 'CA', 94235);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO position (positionID, positiontitle, educationrequired, minsalary, maxsalary) VALUES (1, 'Sales Manager', 'Bachelor''s Degree', 65000, 95000);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO employee (ssn, lastname, firstname, hiredate, salary, gender, performance, positionID, locationID) VALUES ('901-23-4567', 'Gonzalez', 'Luis', '2024-07-10', 70000, 'M', 'N/A', 1, 8);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="75",
      instruction="My name is Samantha Tran, SSN 888222777, HR manager. Verify my identity. Then, create a new office with locationID 12 in San Jose at 900 Tech Avenue, California, zip code 95112, office phone (408)555-1000. Transfer employee William Chen (SSN 111334555) to this location by updating his work location.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM employee WHERE ssn = '888222777'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO location (locationID, locationcity, address, state, zipcode, officephone) VALUES (12, 'San Jose', '900 Tech Avenue', 'CA', 95112, '(408)555-1000')"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE employee SET locationID = 12 WHERE ssn = '111334555'"
               }
            ),
       ],
       outputs=[]
   ),
]
