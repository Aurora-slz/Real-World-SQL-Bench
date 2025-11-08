from tau_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="0",
      instruction="You're Pirkko Koskitalo (CustomerID: 87) from Wartian Herkku. For your OrderID 10416, please update the quantity of Teatime Chocolate Biscuits (ProductID: 19) from 20 to 35 in order detail 447, and switch the shipper to Federal Shipping (ShipperID: 3) for better reliability.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 35 WHERE OrderDetailID = 447 AND OrderID = 10416 AND ProductID = 19;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 3 WHERE OrderID = 10416 AND CustomerID = 87;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1",
      instruction="I am Fran Wilson from Lonesome Pine Restaurant (CustomerID: 48). For order #10307 under my account, please: (1) assign Andrew Fuller (EmployeeID: 2) as our sales rep, (2) change our shipper to United Package (ShipperID: 2), and (3) update the quantity of Tarte au sucre (ProductID: 62, OrderDetailID: 160) from 10 to 15 pies in this order.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 2 WHERE OrderID = 10307 AND CustomerID = 48;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2 WHERE OrderID = 10307 AND CustomerID = 48;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 15 WHERE OrderDetailID = 160 AND OrderID = 10307 AND ProductID = 62;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2",
      instruction="I am Bernardo Batista from Que Delícia (CustomerID 61). Please remove the 20 units of 'Konbu' (ProductID 13, OrderDetailID 116) from my order #10291 (CustomerID 61) and retain the remaining items. Subsequently, update the shipper for order #10291 to 'United Package' (ShipperID 2) to expedite delivery.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM OrderDetails WHERE OrderDetailID = 116 AND OrderID = 10291 AND ProductID = 13"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2 WHERE OrderID = 10291 AND CustomerID = 61"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7",
      instruction="Hello, this is Elizabeth Lincoln from Bottom-Dollar Markets (CustomerID: 10). I need to update Order #10411 under my account. Please change the assigned shipper to Federal Shipping (ShipperID: 3) and update the responsible sales employee to Anne Dodsworth (EmployeeID: 9). Confirm these changes for my order.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 3 WHERE OrderID = 10411 AND CustomerID = 10;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 9 WHERE OrderID = 10411 AND CustomerID = 10;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="8",
      instruction="Hello, I'm Robert King (EmployeeID=7). I need to modify order #10341 (CustomerID=73, Simons bistro). Please update the quantity of product 'Geitost' (ProductID=33) in order detail ID 250 (belonging to OrderID=10341) to 15 units. Also, change the shipper for this order to ShipperID=3 ('Federal Shipping').",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Employees WHERE EmployeeID=7 AND FirstName='Robert' AND LastName='King';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity=15 WHERE OrderDetailID=250 AND OrderID=10341 AND ProductID=33;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID=3 WHERE OrderID=10341 AND CustomerID=73;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9",
      instruction="I am Elizabeth Brown from Consolidated Holdings (CustomerID: 16). I need to update order #10435: please change its shipper to United Package (ShipperID: 2) and assign Laura Callahan (EmployeeID: 8) as the supervising employee for this order. Confirm both updates are applied to OrderID 10435 under my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 16 AND ContactName = 'Elizabeth Brown';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Orders WHERE OrderID = 10435 AND CustomerID = 16;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2, EmployeeID = 8 WHERE OrderID = 10435 AND CustomerID = 16;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12",
      instruction="I am Paul Henriot (CustomerID 85) from Vins et alcools Chevalier. Please create a new order for me with today's date, assigned to employee Andrew Fuller (EmployeeID 2), using United Package (ShipperID 2). The order should include 12 units of ProductID 1 ('Chai') and 20 units of ProductID 2 ('Chang'). Ensure all details match exactly.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (85, 2, CURRENT_DATE, 2);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT OrderID FROM Orders WHERE CustomerID=85 AND EmployeeID=2 AND OrderDate=CURRENT_DATE AND ShipperID=2 ORDER BY OrderID DESC LIMIT 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES ({new_order_id}, 1, 12);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES ({new_order_id}, 2, 20);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="14",
      instruction="Eduardo Saavedra (CustomerID: 29) from Galería del gastrónomo requests to place a new order for 10 units of 'Gnocchi di nonna Alice' (ProductID: 56) to be processed today. The order should be handled by Margaret Peacock (EmployeeID: 4) and shipped via Speedy Express (ShipperID: 1). Use today's date for the order date. First create the order record, then add the product quantity details.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (29, 4, CURRENT_DATE, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES ((SELECT MAX(OrderID) FROM Orders WHERE CustomerID = 29 AND EmployeeID = 4 AND ShipperID = 1), 56, 10);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="15",
      instruction="Hello, this is Henriette Pfalzheim from Ottilies Käseladen (Customer ID 56). I'd like to place an order for 20 units of 'Queso Cabrales' (Product ID 11). Please ensure Andrew Fuller (Employee ID 2) handles this order and use United Package (Shipper ID 2) for shipping. Confirm the order and item details have been properly recorded.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Orders (CustomerID, EmployeeID, ShipperID) VALUES (56, 2, 2);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES ((SELECT MAX(OrderID) FROM Orders WHERE CustomerID=56 AND EmployeeID=2 AND ShipperID=2), 11, 20);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="16",
      instruction="You are Frédérique Citeaux representing Blondel père et fils (CustomerID:7). Please (1) reduce the quantity of Mozzarella di Giovanni (ProductID:72) in your order #10297 (OrderID:10297, CustomerID:7, OrderDetailID:134) from 20 to 10 units, (2) change the shipping method to United Package (ShipperID:2), and (3) assign Steven Buchanan (EmployeeID:5) as the responsible employee for this order.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 10 WHERE OrderDetailID = 134 AND OrderID = 10297 AND ProductID = 72;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2 WHERE OrderID = 10297 AND CustomerID = 7;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 5 WHERE OrderID = 10297 AND CustomerID = 7;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="17",
      instruction="I am Annette Roulet from 'La maison d'Asie' (Customer ID 41). Please update my order with Order ID 10350 by assigning Michael Suyama (Employee ID 6) as the handling employee, set the shipper to 'United Package' (Shipper ID 2), and for Order Detail ID 274, update the quantity of Product ID 69 to 24 units.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 41 AND ContactName = 'Annette Roulet';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 6, ShipperID = 2 WHERE OrderID = 10350 AND CustomerID = 41;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 24 WHERE OrderDetailID = 274 AND OrderID = 10350 AND ProductID = 69;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="65",
      instruction="You are Paula Wilson, store manager at Rattlesnake Canyon Grocery (CustomerID: 65). Please make the following updates for your order (OrderID: 10316): 1) Change shipping provider to Federal Shipping (ShipperID: 3), 2) Assign Nancy Davolio (EmployeeID: 1) as the responsible employee, and 3) Update quantity to 90 units for Tarte au sucre (ProductID: 62) in order detail line (OrderDetailID: 184).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 3 WHERE OrderID = 10316 AND CustomerID = 65;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 1 WHERE OrderID = 10316 AND CustomerID = 65;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 90 WHERE OrderDetailID = 184 AND OrderID = 10316 AND ProductID = 62;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="20",
      instruction="I am Jose Pavarotti from Save-a-lot Markets (CustomerID 71). For my order (OrderID 10398), please make these updates: 1) Set ShipperID to 3 (Federal Shipping), 2) Assign EmployeeID 2 (Andrew Fuller) as sales representative, and 3) Update quantity to 45 units for OrderDetailID 400 (ProductID 35 - Steeleye Stout). Confirm all changes apply only to CustomerID 71's OrderID 10398.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 3, EmployeeID = 2 WHERE OrderID = 10398 AND CustomerID = 71;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 45 WHERE OrderDetailID = 400 AND OrderID = 10398 AND ProductID = 35;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22",
      instruction="You are Bernardo Batista (CustomerID 61) from Que Delícia. You want to modify your recent order (OrderID 10261). Specifically: 1) Switch the shipping carrier to 'United Package' (ShipperID 2); 2) Reassign the order to employee Margaret Peacock (EmployeeID 4); 3) Adjust the quantity of product 'Steeleye Stout' (ProductID 35) to 25 units for OrderDetailID 40 in this order. Confirm all changes apply to OrderID 10261 under your account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2, EmployeeID = 4 WHERE OrderID = 10261 AND CustomerID = 61;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 25 WHERE OrderDetailID = 40 AND OrderID = 10261 AND ProductID = 35;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="25",
      instruction="You are Patricia McKenna from Hungry Owl All-Night Grocers (CustomerID 37). For your latest order (OrderID 10335), you need to adjust product quantities: increase Mascarpone Fabioli (ProductID 32, OrderDetailID 234) from 6 to 10 units and decrease Gorgonzola Telino (ProductID 31, OrderDetailID 233) from 25 to 20 units. Additionally, update the shipment provider for OrderID 10335 (associated with CustomerID 37) to United Package (ShipperID 2).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 10 WHERE OrderDetailID = 234 AND OrderID = 10335 AND ProductID = 32"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 20 WHERE OrderDetailID = 233 AND OrderID = 10335 AND ProductID = 31"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2 WHERE OrderID = 10335 AND CustomerID = 37"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="27",
      instruction="I am Bernardo Batista from Que Delícia (CustomerID 61). Please update order 10291 to use shipping company 'United Package' (ShipperID 2) and assign employee Michael Suyama (EmployeeID 6) as the responsible representative.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2, EmployeeID = 6 WHERE OrderID = 10291 AND CustomerID = 61;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="28",
      instruction="I am Mary Saveley (CustomerID 84) needing urgent updates for OrderID 10334. Please assign Laura Callahan (EmployeeID 8) as the responsible staff and change the shipper to United Package (ShipperID 2). Confirm both modifications for my order.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 8 WHERE OrderID = 10334 AND CustomerID = 84"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2 WHERE OrderID = 10334 AND CustomerID = 84"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="30",
      instruction="I am Elizabeth Brown from Consolidated Holdings (CustomerID 16). For our order #10435, I request three modifications: (1) Update the quantity of Mozzarella di Giovanni (ProductID 72) from 10 to 20 in the order details; (2) Assign Laura Callahan (EmployeeID 8) as the responsible employee for order #10435; (3) Set United Package (ShipperID 2) as the shipper for order #10435. Please confirm all changes have been applied to order #10435.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 20 WHERE OrderID = 10435 AND ProductID = 72;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 8 WHERE OrderID = 10435;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2 WHERE OrderID = 10435;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="31",
      instruction="I am Hari Kumar from Seven Seas Imports (CustomerID=72). For my order (OrderID=10388 under CustomerID=72), please update the shipper to ShipperID=1 (Speedy Express). For OrderDetailID=373 in this order, change the quantity of ProductID=52 (Filo Mix) from 20 to 25 units.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 1 WHERE OrderID = 10388 AND CustomerID = 72;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 25 WHERE OrderDetailID = 373 AND OrderID = 10388 AND ProductID = 52;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="33",
      instruction="I am Bernardo Batista (CustomerID 61) from Que Delícia. For my order #10261, please update the shipping provider to ShipperID 1 instead of ShipperID 2. Additionally, modify the quantity of Steeleye Stout (ProductID 35) in OrderDetailID 40 of this order from 20 to 30 units.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 61"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 1 WHERE OrderID = 10261 AND CustomerID = 61"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 30 WHERE OrderDetailID = 40 AND OrderID = 10261 AND ProductID = 35"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="34",
      instruction="I'm Roland Mendel from Graz, Austria (CustomerID 20). I want to place a new order today with Nancy Davolio (EmployeeID 1) for 40 units of 'Chang' (ProductID 2) and 30 units of 'Chef Anton's Gumbo Mix' (ProductID 5). Please use Speedy Express (ShipperID 1) for shipping. Confirm the new Order ID and that both product line items have been added.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (20, 1, CURRENT_DATE, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT MAX(OrderID) AS NewOrderID FROM Orders WHERE CustomerID = 20 AND EmployeeID = 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (<NewOrderID>, 2, 40);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (<NewOrderID>, 5, 30);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="37",
      instruction="I am Maria Larsson (ContactName) from Folk och fä HB (CustomerID 24). Please verify my identity. Then, create a new order with EmployeeID 5 (Steven Buchanan) and ShipperID 3 (Federal Shipping). Include 10 units of ProductID 12 and 5 units of ProductID 15. Confirm the OrderID, OrderDate, EmployeeID (with FirstName/LastName), ShipperID (with ShipperName), and all product details after creation.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT CustomerID, ContactName FROM Customers WHERE CustomerID = 24 AND ContactName = 'Maria Larsson';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (24, 5, CURRENT_DATE, 3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT MAX(OrderID) AS NewOrderID FROM Orders WHERE CustomerID = 24;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES ((SELECT MAX(OrderID) FROM Orders WHERE CustomerID = 24), 12, 10);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES ((SELECT MAX(OrderID) FROM Orders WHERE CustomerID = 24), 15, 5);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT o.OrderID, o.OrderDate, e.EmployeeID, e.FirstName || ' ' || e.LastName AS EmployeeName, s.ShipperID, s.ShipperName, p.ProductID, p.ProductName, od.Quantity FROM Orders o JOIN Employees e ON o.EmployeeID = e.EmployeeID JOIN Shippers s ON o.ShipperID = s.ShipperID JOIN OrderDetails od ON o.OrderID = od.OrderID JOIN Products p ON od.ProductID = p.ProductID WHERE o.OrderID = (SELECT MAX(OrderID) FROM Orders WHERE CustomerID = 24);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="40",
      instruction="I am Guillermo Fernández from Pericles Comidas clásicas (CustomerID 58). Please update the shipping carrier for OrderID 10354 to ShipperID 3. Verify that this change applies exclusively to my order 10354 under CustomerID 58.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 58 AND ContactName = 'Guillermo Fernández' AND CustomerName = 'Pericles Comidas clásicas'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 3 WHERE OrderID = 10354 AND CustomerID = 58"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="42",
      instruction="Hello, this is Art Braunschweiger (Contact Name) from Split Rail Beer & Ale (Customer ID 75). For Order ID 10385, please: 1) Update Product ID 68 ('Scottish Longbreads') quantity to 12 units, 2) Assign Shipper ID 2 (United Package), and 3) Set Employee ID 1 (Nancy Davolio) as handling employee.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 75 AND ContactName = 'Art Braunschweiger';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 12 WHERE OrderID = 10385 AND ProductID = 68;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2, EmployeeID = 1 WHERE OrderID = 10385;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="43",
      instruction="I am Carlos González from LILA-Supermercado (Customer ID 46). Today, June 18, 2024, I want to place a new order handled by employee Janet Leverling (Employee ID 3) via Federal Shipping (Shipper ID 3). For Customer ID 46, please add: 15 units of Product ID 12 and 24 units of Product ID 17. Confirm my order placement.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (46, 3, '2024-06-18', 3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT OrderID FROM Orders WHERE CustomerID = 46 AND EmployeeID = 3 AND OrderDate = '2024-06-18' AND ShipperID = 3 ORDER BY OrderID DESC LIMIT 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES ([OrderID from previous step], 12, 15);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES ([OrderID from previous step], 17, 24);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="46",
      instruction="I am Lino Rodriguez from Furia Bacalhau e Frutos do Mar (CustomerID: 28). For my order #10352, please: (1) Update the quantity of Tourtière (ProductID: 54, OrderDetailID: 280) from 20 to 35; (2) Assign Employee Janet Leverling (EmployeeID: 3) as my representative; (3) Set shipping to Federal Shipping (ShipperID: 3). Provide full verification data for OrderDetailID 280 after these changes.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 35 WHERE OrderDetailID = 280 AND OrderID = 10352 AND ProductID = 54"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 3, ShipperID = 3 WHERE OrderID = 10352 AND CustomerID = 28"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT od.OrderDetailID, od.Quantity, o.EmployeeID, o.ShipperID FROM OrderDetails od JOIN Orders o ON od.OrderID = o.OrderID WHERE od.OrderDetailID = 280 AND o.CustomerID = 28"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="49",
      instruction="I am Felipe Izquierdo (ContactName) from LINO-Delicateses (CustomerID 47). I need to update OrderID 10501. Please change the assigned employee to EmployeeID 1 (Nancy Davolio) and switch the shipper to ShipperID 1 (Speedy Express). Confirm these updates apply only to my order.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 47 AND CustomerName = 'LINO-Delicateses' AND ContactName = 'Felipe Izquierdo';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 1, ShipperID = 1 WHERE OrderID = 10501 AND CustomerID = 47;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="50",
      instruction="I am Pirkko Koskitalo from Wartian Herkku (CustomerID 87). Please create a new order for 10 units of ProductID 12, assigned to EmployeeID 8, shipped via ShipperID 1, with order date '2024-06-14'. Confirm my customer details match CustomerID 87 before proceeding.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT CustomerID FROM Customers WHERE CustomerID = 87 AND CustomerName = 'Wartian Herkku' AND ContactName = 'Pirkko Koskitalo';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (87, 8, '2024-06-14', 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT OrderID FROM Orders WHERE CustomerID = 87 AND EmployeeID = 8 AND OrderDate = '2024-06-14' AND ShipperID = 1 ORDER BY OrderID DESC LIMIT 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (<ORDER_ID_FROM_PREVIOUS_STEP>, 12, 10);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="51",
      instruction="You are Pascale Cartrain, the contact for Suprêmes délices (CustomerID 76). You wish to split your existing order (OrderID 10302) so that Alice Mutton (ProductID 17, Quantity 40, OrderDetailID 145) is shipped separately from Ipoh Coffee. Please create a new order under CustomerID 76 with EmployeeID 4 and ShipperID 2 using today's date, move only that item to the new order via OrderDetailID 145, and remove it from the original order.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (76, 4, CURRENT_DATE, 2);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT MAX(OrderID) AS NewOrderID FROM Orders WHERE CustomerID = 76;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET OrderID = {NewOrderID} WHERE OrderDetailID = 145 AND ProductID = 17 AND Quantity = 40;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="54",
      instruction="You are Aria Cruz (ContactName) from Familia Arquibaldo (CustomerID=21). First, confirm my identity. Then for order #10386: 1) Assign Anne Dodsworth (EmployeeID=9) as the responsible employee, 2) Update quantity to 20 for order line item #367 (previously 10 units of 'Sasquatch Ale'), and 3) Use 'Federal Shipping' (ShipperID=3). Process all changes now.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 21"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 9 WHERE OrderID = 10386"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 20 WHERE OrderDetailID = 367"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 3 WHERE OrderID = 10386"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="55",
      instruction="I am Pirkko Koskitalo from Wartian Herkku (CustomerID 87) in Oulu, Finland. I want to place a new order for ProductID 8 with Quantity 25 today (OrderDate '2024-06-12'), managed by Employee Janet Leverling (EmployeeID 3), shipped via Federal Shipping (ShipperID 3). Please process this order and confirm the new OrderID along with the product details.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 87"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (87, 3, '2024-06-12', 3)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT OrderID FROM Orders WHERE CustomerID = 87 AND EmployeeID = 3 AND OrderDate = '2024-06-12' AND ShipperID = 3 ORDER BY OrderID DESC LIMIT 1"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (<OrderID_from_above>, 8, 25)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT o.OrderID, od.ProductID, od.Quantity FROM Orders o JOIN OrderDetails od ON o.OrderID = od.OrderID WHERE o.OrderID = <OrderID_from_above>"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="56",
      instruction="I am Yang Wang from Chop-suey Chinese (CustomerID: 14) located in Bern. Please update my recent order (OrderID: 10254) to decrease 'Longlife Tofu' (ProductID: 74) from 21 units to 11 units (OrderDetailID: 20). Additionally, add 10 units of 'Guaraná Fantástica' (ProductID: 24) to this order. Ensure Steven Buchanan (EmployeeID: 5) is assigned as our sales representative and United Package (ShipperID: 2) handles delivery.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 14 AND City = 'Bern'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 11 WHERE OrderDetailID = 20 AND ProductID = 74 AND OrderID = 10254"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (10254, 24, 10)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 5, ShipperID = 2 WHERE OrderID = 10254 AND CustomerID = 14"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="59",
      instruction="I am Bernardo Batista from Que Delícia (CustomerID 61). For my order #10261, please: 1) Update the handling employee to Margaret Peacock (EmployeeID 4), 2) Set the shipper to United Package (ShipperID 2), and 3) Adjust the quantity of Steeleye Stout (ProductID 35) in OrderDetailID 40 (from order #10261) from 20 to 15 units.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 4 WHERE OrderID = 10261 AND CustomerID = 61;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2 WHERE OrderID = 10261 AND CustomerID = 61;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 15 WHERE OrderDetailID = 40 AND OrderID = 10261 AND ProductID = 35;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="60",
      instruction="I am Jytte Petersen (ContactName) from Simons Bistro (CustomerID 73). Please update the ShipperID to 3 (Federal Shipping) for OrderID 10341 under my account, as the current shipper is unresponsive.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 73 AND ContactName = 'Jytte Petersen';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 3 WHERE OrderID = 10341 AND CustomerID = 73;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="64",
      instruction="I am Art Braunschweiger from Split Rail Beer & Ale (CustomerID 75). For order #10329, I want to know which employee processed the order (EmployeeID) and which shipper was used (ShipperID). Next, perform these updates for order #10329: 1) Change the quantity of 'Gnocchi di nonna Alice' (ProductID 56, OrderDetailID 220) from 12 to 20 units. 2) Remove 'Teatime Chocolate Biscuits' (ProductID 19, OrderDetailID 217). 3) Increase the quantity of 'Nord-Ost Matjeshering' (ProductID 30, OrderDetailID 218) from 8 to 18 units.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT EmployeeID, ShipperID FROM Orders WHERE OrderID = 10329 AND CustomerID = 75;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 20 WHERE OrderDetailID = 220 AND OrderID = 10329 AND ProductID = 56;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM OrderDetails WHERE OrderDetailID = 217 AND OrderID = 10329 AND ProductID = 19;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 18 WHERE OrderDetailID = 218 AND OrderID = 10329 AND ProductID = 30;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="65",
      instruction="This is Mary Saveley (CustomerID: 84) from 'Victuailles en stock'. For order 10334, I require three modifications: 1) Update quantity to 15 for ProductID 68 ('Scottish Longbreads') in the order details, 2) Set ShipperID to 2 ('United Package'), and 3) Assign EmployeeID 8 (Laura Callahan) as the responsible employee. Please execute these changes sequentially.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Customers WHERE CustomerID = 84"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 15 WHERE OrderID = 10334 AND ProductID = 68"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET ShipperID = 2, EmployeeID = 8 WHERE OrderID = 10334"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="66",
      instruction="You are Paula Parente, representing Wellington Importadora (CustomerID 88). You noticed that order #10256 (OrderID 10256), which was handled by employee Janet Leverling (EmployeeID 3) and shipped by United Package (ShipperID 2), incorrectly recorded 15 units of product 'Perth Pasties' (ProductID 53, OrderDetailID 25). You need to update this order detail to 20 units instead of 15. After confirmation of the update, provide a complete summary of this corrected line item including: order date, sales rep name (EmployeeID 3), shipper name (ShipperID 2), product name (ProductID 53), updated quantity (20 units), and total price calculation for OrderDetailID 25 in OrderID 10256.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT CustomerID FROM Customers WHERE ContactName = 'Paula Parente' AND CustomerID = 88;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE OrderDetails SET Quantity = 20 WHERE OrderDetailID = 25 AND OrderID = 10256 AND ProductID = 53;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT o.OrderID, o.OrderDate, CONCAT(e.FirstName, ' ', e.LastName) AS SalesRep, s.ShipperName, p.ProductName, od.Quantity, (od.Quantity * p.Price) AS TotalLinePrice FROM Orders o JOIN Employees e ON o.EmployeeID = e.EmployeeID JOIN Shippers s ON o.ShipperID = s.ShipperID JOIN OrderDetails od ON o.OrderID = od.OrderID JOIN Products p ON od.ProductID = p.ProductID WHERE o.OrderID = 10256 AND od.OrderDetailID = 25;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="67",
      instruction="Hi, this is Pirkko Koskitalo from Wartian Herkku (CustomerID 87). Please create a new order with these details: CustomerID 87, initial EmployeeID 5, ShipperID 1, OrderDate '2024-06-17'. Add 30 units of ProductID 15. Then update this same order to final EmployeeID 8 and ShipperID 2 (United Package). Confirm the final EmployeeID and ShipperID for this new order.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID) VALUES (87, 5, '2024-06-17', 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT MAX(OrderID) AS NewOrderID FROM Orders WHERE CustomerID = 87 AND OrderDate = '2024-06-17';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (NEW_ORDER_ID, 15, 30);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Orders SET EmployeeID = 8, ShipperID = 2 WHERE OrderID = NEW_ORDER_ID;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT EmployeeID, ShipperID FROM Orders WHERE OrderID = NEW_ORDER_ID;"
               }
            ),
       ],
       outputs=[]
   ),
]
