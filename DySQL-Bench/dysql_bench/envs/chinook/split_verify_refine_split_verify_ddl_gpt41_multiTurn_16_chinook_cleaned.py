from tau_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="0",
      instruction="Hello, I'm Jack Smith with Customer ID 17 and email jacksmith@microsoft.com. Please update my company's address in your system to: Address: 300 Bellevue Way NE, City: Bellevue, State: WA, Postal Code: 98004, Country: USA. Also update the billing address for Invoice ID 298 to match this new address.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET Address='300 Bellevue Way NE', City='Bellevue', State='WA', Country='USA', PostalCode='98004' WHERE CustomerId=17 AND Email='jacksmith@microsoft.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE invoices SET BillingAddress='300 Bellevue Way NE', BillingCity='Bellevue', BillingState='WA', BillingCountry='USA', BillingPostalCode='98004' WHERE InvoiceId=298 AND CustomerId=17;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1",
      instruction="Hello, I'm Daan Peeters with email daan_peeters@apple.be. Please remove the track 'Sister Awake' from the 'Music' playlist and update my company information to 'GreenTech Belgium' for future invoices.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM playlist_track WHERE PlaylistId = (SELECT PlaylistId FROM playlists WHERE Name = 'Music') AND TrackId = (SELECT TrackId FROM tracks WHERE Name = 'Sister Awake');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET Company = 'GreenTech Belgium' WHERE CustomerId = (SELECT CustomerId FROM customers WHERE Email = 'daan_peeters@apple.be');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4",
      instruction="Hello, I'm Aaron Mitchell (aaronmitchell@yahoo.ca). I've moved to 220 Grant Avenue, Winnipeg, MB, Canada, R3C 1P8. Please update my customer profile address to this new location and ensure all my past invoice billing addresses reflect this change too.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE Email = 'aaronmitchell@yahoo.ca'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET Address='220 Grant Avenue', City='Winnipeg', State='MB', Country='Canada', PostalCode='R3C 1P8' WHERE CustomerId=32"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE invoices SET BillingAddress='220 Grant Avenue', BillingCity='Winnipeg', BillingState='MB', BillingCountry='Canada', BillingPostalCode='R3C 1P8' WHERE CustomerId=32"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4",
      instruction="I am Bjørn Hansen (email: bjorn.hansen@yahoo.no), and I want to modify my invoice #197. First, authenticate me. Then, remove the track with InvoiceLineId 1065 (TrackId: 2995) and replace it with 'Rock & Roll' (TrackId: 1662) at a unit price of 0.99 and quantity 1. Confirm the update by showing the revised items for Invoice #197.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT CustomerId FROM customers WHERE Email = 'bjorn.hansen@yahoo.no';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT InvoiceId FROM invoices WHERE InvoiceId = 197 AND CustomerId = (SELECT CustomerId FROM customers WHERE Email = 'bjorn.hansen@yahoo.no');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT InvoiceLineId FROM invoice_items WHERE InvoiceLineId = 1065 AND InvoiceId = 197 AND TrackId = 2995;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM invoice_items WHERE InvoiceLineId = 1065 AND InvoiceId = 197 AND TrackId = 2995;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO invoice_items (InvoiceId, TrackId, UnitPrice, Quantity) VALUES (197, 1662, 0.99, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE invoices SET Total = (SELECT SUM(UnitPrice * Quantity) FROM invoice_items WHERE InvoiceId = 197) WHERE InvoiceId = 197;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT invoice_items.InvoiceLineId, invoice_items.TrackId, tracks.Name FROM invoice_items JOIN tracks ON invoice_items.TrackId = tracks.TrackId WHERE invoice_items.InvoiceId = 197;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="34",
      instruction="Hello, my name is João Fernandes and my CustomerID is 34. I need to update the BillingCity from 'Lisbon' to 'Lisboa' in all my invoices where BillingCity is currently 'Lisbon' and Total exceeds 5.00. After the update, list all tracks and their corresponding artist names for these updated invoices.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE invoices SET BillingCity = 'Lisboa' WHERE CustomerId = 34 AND BillingCity = 'Lisbon' AND Total > 5.00;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT tracks.Name AS TrackName, artists.Name AS ArtistName FROM invoice_items INNER JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId INNER JOIN tracks ON invoice_items.TrackId = tracks.TrackId INNER JOIN albums ON tracks.AlbumId = albums.AlbumId INNER JOIN artists ON albums.ArtistId = artists.ArtistId WHERE invoices.CustomerId = 34 AND invoices.BillingCity = 'Lisboa' AND invoices.Total > 5.00;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="8",
      instruction="I am Edward Francis (edfrancis@yachoo.ca). Verify my identity and confirm ownership of invoice ID 333. Then modify this invoice by: removing tracks 'When I Come Around' (TrackID 473) and 'Surrender' (TrackID 461), adding 'The Number Of The Beast' (TrackID 1367) with UnitPrice 0.99 and Quantity 1, and updating the total amount.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT CustomerId FROM customers WHERE Email = 'edfrancis@yachoo.ca';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT i.InvoiceId FROM invoices i JOIN customers c ON i.CustomerId = c.CustomerId WHERE c.Email = 'edfrancis@yachoo.ca' AND i.InvoiceId = 333;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM invoice_items WHERE InvoiceId = 333 AND TrackId IN (473, 461);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO invoice_items (InvoiceId, TrackId, UnitPrice, Quantity) VALUES (333, 1367, 0.99, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE invoices SET Total = (SELECT SUM(UnitPrice * Quantity) FROM invoice_items WHERE InvoiceId = 333) WHERE InvoiceId = 333;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9",
      instruction="I am Stanisław Wójcik (Email: stanisław.wójcik@wp.pl). Please update the billing address for invoice 356 to: street 'Nowy Świat 22', city 'Warsaw', postal code '00-373', country 'Poland'. Then, add the track 'Hallowed Be Thy Name' (TrackID 1321) to the '90’s Music' playlist (PlaylistID 5).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM customers WHERE Email = 'stanisław.wójcik@wp.pl';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE invoices SET BillingAddress = 'Nowy Świat 22', BillingCity = 'Warsaw', BillingPostalCode = '00-373', BillingCountry = 'Poland' WHERE InvoiceId = 356 AND CustomerId = (SELECT CustomerId FROM customers WHERE Email = 'stanisław.wójcik@wp.pl');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO playlist_track (PlaylistId, TrackId) VALUES (5, 1321);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22",
      instruction="Hi, I'm Heather Leacock. I recently moved and need to update my billing address for invoice #375 to '4528 N Main St', Tampa, FL 33610. Also, please change my support representative to Erin Harper.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT CustomerId FROM customers WHERE FirstName='Heather' AND LastName='Leacock';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT EmployeeId FROM employees WHERE FirstName='Erin' AND LastName='Harper';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE invoices SET BillingAddress='4528 N Main St', BillingCity='Tampa', BillingState='FL', BillingPostalCode='33610' WHERE InvoiceId=375 AND CustomerId=22;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET SupportRepId=7 WHERE CustomerId=22;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="11",
      instruction="Hello, I am Tim Goyer with email tgoyer@apple.com from Apple Inc. I need a refund for the track 'Dream Of Mirrors' on Invoice #255 due to a corrupted download. The specific line item is InvoiceLineId 1375. Please remove this item and update my invoice total. The original total was $5.94, and the track's unit price was $0.99, so the new total should be $4.95.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT CustomerId FROM customers WHERE FirstName = 'Tim' AND LastName = 'Goyer' AND Email = 'tgoyer@apple.com' AND Company = 'Apple Inc.';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM invoice_items WHERE InvoiceLineId = 1375 AND InvoiceId = 255;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE invoices SET Total = 4.95 WHERE InvoiceId = 255;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="13",
      instruction="Hello, I'm Hannah Schneider (Customer ID 36, email hannah.schneider@yahoo.de). I accidentally purchased 'The Number Of The Beast' (Track ID 1367) twice under Invoice ID 40. Please remove the duplicate entry with Invoice Line ID 224 and refund $0.99. Then, add 'Children Of The Damned' (Track ID 1380) as a replacement at $0.99 for one copy to the same invoice (ID 40). Update the invoice total to reflect these changes. Also, assign Steve Johnson (Employee ID 5) as my support representative.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM invoice_items WHERE InvoiceLineId = 224 AND TrackId = 1367 AND InvoiceId = 40;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE invoices SET Total = Total - 0.99 WHERE InvoiceId = 40 AND CustomerId = 36;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO invoice_items (InvoiceId, TrackId, UnitPrice, Quantity) VALUES (40, 1380, 0.99, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE invoices SET Total = Total + 0.99 WHERE InvoiceId = 40 AND CustomerId = 36;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE customers SET SupportRepId = 5 WHERE CustomerId = 36;"
               }
            ),
       ],
       outputs=[]
   ),
]
