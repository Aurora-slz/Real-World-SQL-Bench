from tau_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="0",
      instruction="Hi, I'm user 125. My profile currently shows my gender as Male, but I need to update it to 'Other'. After making that change, could you please fetch the Reach and Sentiment metrics from my latest tweet so I can review its performance?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Other' WHERE user_id = 125;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT Reach, Sentiment FROM twitter WHERE user_id = 125 ORDER BY Day DESC, Hour DESC LIMIT 1;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="user2371",
      instruction="I am user2371 and would like to update my gender to 'Unisex'. Additionally, please set the language to Spanish ('es') for my tweets with IDs 3201, 3202, and 3203.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Unisex' WHERE user_id = 'user2371';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET language = 'es' WHERE user_id = 'user2371' AND tweet_id IN (3201, 3202, 3203);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2",
      instruction="I am your registered user with UserID 'U2023123'. Due to personal privacy concerns, I would like my gender information permanently deleted from my account profile. Please confirm removal of all gender associations from my records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = NULL WHERE user_id = 'U2023123';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12345",
      instruction="Hello, my user ID is 12345. First, please update my gender from Male to Female in your records. After confirming this change, I'd like to see a list of all my English-language tweets showing both the full text and the exact day each was posted.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Female' WHERE UserID = '12345';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT tweetid, text, Day FROM twitter WHERE UserID = '12345' AND Lang = 'en';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6",
      instruction="I am Chloe Miller (UserID: U1002) and want to delete all my tweets posted from Austin city. Using my UserID U1002, please permanently remove all tweets from the twitter table that are associated with LocationIDs corresponding to 'Austin' city in the location table, regardless of weekday or hour.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT LocationID FROM location WHERE City = 'Austin';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 'U1002' AND LocationID IN (SELECT LocationID FROM location WHERE City = 'Austin');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7",
      instruction="Confirm your user ID as 'M104' and gender as 'Male'. Check how many of your tweets were posted on Sundays (Weekday = 'Sunday'), then permanently delete all tweets matching this criteria.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT COUNT(*) FROM user WHERE UserID = 'M104' AND Gender = 'Male';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT COUNT(*) FROM twitter WHERE UserID = 'M104' AND Weekday = 'Sunday';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 'M104' AND Weekday = 'Sunday';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="8",
      instruction="My name is Priya Singh and my user ID is U341. I live in New York, NY with location ID 1043. I want to update my gender to 'Female' in my user profile. Additionally, I need to edit my tweet with tweet ID T903, which I posted from location ID 1043, to change its text to 'Excited for spring in NY!' and set the sentiment score to 0.8. Please process these updates.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE user_id = 'U341'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Female' WHERE user_id = 'U341'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET text = 'Excited for spring in NY!', Sentiment = 0.8 WHERE tweet_id = 'T903' AND user_id = 'U341' AND location_id = 1043"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9",
      instruction="Hello, my name is Adam with User ID 42. I noticed an error in my profile - could you please correct my gender to 'Male' in the user records? Additionally, I would like to permanently delete all my tweets posted on Sundays from the twitter table to protect my privacy. Please confirm these changes are made specifically for UserID 42 where Weekday equals 'Sunday'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE UserID = 42"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Male' WHERE UserID = 42"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 42 AND Weekday = 'Sunday'"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12",
      instruction="You are Alex Chen (UserID: 10235), and your gender is Unisex. You want to delete all tweets written in Spanish (Lang = 'es') that were posted on Saturdays (Weekday = 'Saturday') as part of revising your social media strategy. Please remove only these tweets from your account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = '10235' AND Lang = 'es' AND Weekday = 'Saturday';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="13",
      instruction="I want to permanently delete my social media account and all activity. My account is the only one registered with Gender 'Male'. Please (1) confirm my UserID using my Gender, (2) delete all my tweets, and (3) fully remove my user profile.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT UserID FROM user WHERE Gender = 'Male';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = '<UserID from previous step>';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM user WHERE UserID = '<UserID from previous step>';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="14",
      instruction="I am James Miller (UserID: 42, Gender: Male). Please permanently delete my tweet ID 1025 that was posted on Monday at 10 (24-hour format) in English (language code 'en'), which has a negative sentiment score (Sentiment < 0).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT user_id FROM user WHERE user_id = 42 AND Gender = 'Male';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE tweet_id = 1025 AND user_id = 42 AND Weekday = 'Monday' AND Hour = 10 AND language = 'en' AND Sentiment < 0;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="16",
      instruction="My user ID is U35719. Please update my gender to 'Unisex' in my profile and delete all tweets I posted on Saturday or Sunday.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Unisex' WHERE UserID = 'U35719';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 'U35719' AND (Weekday = 'Saturday' OR Weekday = 'Sunday');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="789",
      instruction="As an administrator with UserID 789, I need to permanently delete all tweets posted by users where Gender is exactly 'Female' and Weekday is either 'Saturday' or 'Sunday'. First verify my account exists, then execute the deletion.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT UserID FROM user WHERE UserID = '789';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE Weekday IN ('Saturday', 'Sunday') AND UserID IN (SELECT UserID FROM user WHERE Gender = 'Female');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="18",
      instruction="I'm Michael Thompson (UserID: U312). First, update my profile gender to 'Other'. Second, create a tweet with text='Excited to announce my consulting services now available nationwide!', language='en', scheduled for Monday at 10:00 (Day 1) from New York, NY, USA. Ensure location parameters: City='New York', State='NY', Country='USA'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Other' WHERE UserID = 'U312';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT LocationID FROM location WHERE City = 'New York' AND State = 'NY' AND Country = 'USA';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO twitter (Weekday, Hour, Day, Lang, IsReshare, Reach, RetweetCount, Likes, Klout, Sentiment, text, LocationID, UserID) VALUES ('Monday', 10, 1, 'en', 'False', 0, 0, 0, 0, 0.0, 'Excited to announce my consulting services now available nationwide!', <LocationID>, 'U312');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="19",
      instruction="I am Taylor West with UserID TW10032. Update all my Spanish-language tweets (lang = 'es') posted on Saturdays or Sundays to set their Reach to 5000. Only modify these specific tweets.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE user_id = 'TW10032';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET Reach = 5000 WHERE UserID = 'TW10032' AND Lang = 'es' AND (Weekday = 'Saturday' OR Weekday = 'Sunday');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="20",
      instruction="My name is Casey Lee (user ID 3248). Please update my gender to 'Nonbinary' in your records. Additionally, I request that all my historical tweets showing negative sentiment (those with sentiment values below 0) be updated to a positive sentiment score of 1.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Nonbinary' WHERE user_id = 3248;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET Sentiment = 1 WHERE user_id = 3248 AND Sentiment < 0;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="21",
      instruction="My name is Chris Burton and my user ID is 1. I need to update my profile gender to 'Female'. After that, please post a new tweet for me with these details: Weekday='Wednesday', Hour=14 (2 PM), Day=7, Language='en', not a reshare, Reach=150 followers, RetweetCount=2, Likes=10, Klout score=45, Sentiment=0.95, and text content 'Excited to update my profile!'. Ensure this tweet is associated with my account (UserID 1).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Female' WHERE UserID = 1"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO twitter (Weekday, Hour, Day, Lang, IsReshare, Reach, RetweetCount, Likes, Klout, Sentiment, text, UserID) VALUES ('Wednesday', 14, 7, 'en', 'No', 150, 2, 10, 45, 0.95, 'Excited to update my profile!', 1)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22",
      instruction="I am Michael Carter with user ID M123456. Please update all my tweets posted from Chicago (city) that are currently marked as language 'en' to 'es'. This should apply specifically to records where UserID is M123456, existing language is 'en', and location corresponds to Chicago.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE user_id = 'M123456';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT locationid FROM location WHERE city = 'Chicago';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET Lang = 'es' WHERE userid = 'M123456' AND Lang = 'en' AND locationid IN (SELECT locationid FROM location WHERE city = 'Chicago');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="A123",
      instruction="I am Ashley and my current profile indicates female gender, but I need it updated to male. Please change my gender to 'Male'. Also, remove all my tweets posted in Spanish on Mondays (language = 'Spanish', Weekday = 'Monday'). My user ID is A123.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Male' WHERE UserID = 'A123' AND Gender = 'Female';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 'A123' AND Lang = 'Spanish' AND Weekday = 'Monday';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="25",
      instruction="You are Ethan Torres (UserID: 10123) requesting account updates. First, delete all Spanish-language tweets ('es') posted on Saturdays/Sundays with fewer than 10 likes. Second, update my registered city from Miami (LocationID: 551) to Coral Gables (LocationID: 552). Please confirm and execute both actions sequentially.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 10123 AND Lang = 'es' AND (Weekday = 'Saturday' OR Weekday = 'Sunday') AND Likes < 10;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET LocationID = 552 WHERE UserID = 10123;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="201",
      instruction="My name is Amira Hassan (UserID 201), a Female user. Please update my tweets with TweetIDs 345 and 346 posted from LocationID 22 to mark 'is reshare' as 'True'. After confirmation, provide the total count of tweets marked as reshare from LocationID 22 that were posted by Female users.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE user_id = 201 AND gender = 'Female';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET is_reshare = 'True' WHERE tweet_id IN (345, 346) AND location_id = 22 AND user_id = 201;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT COUNT(*) FROM twitter t INNER JOIN user u ON t.user_id = u.user_id WHERE u.gender = 'Female' AND t.location_id = 22 AND t.is_reshare = 'True';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="27",
      instruction="Please register me as a new user with user id U10045, gender Male. My primary location is United States/Pennsylvania/PA/Philadelphia (LocationID L20012). Then post: 1) Tweet T30011 on Monday at 9:00 (Day 3) in English: 'Excited to join Twitter!' with Reach=150, Retweets=0, Likes=5, Klout=40, Sentiment=0.8, location L20012. 2) Tweet T30012 on Tuesday at 18:00 (Day 4) in Spanish: '¡Feliz de estar aquí!' as a reshare with Reach=100, Retweets=1, Likes=3, Klout=38, Sentiment=0.9, location L20012. Ensure all parameters are explicitly included.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO user (UserID, Gender) VALUES ('U10045', 'Male');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO location (LocationID, Country, State, StateCode, City) VALUES ('L20012', 'United States', 'Pennsylvania', 'PA', 'Philadelphia');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO twitter (TweetID, Weekday, Hour, Day, Lang, IsReshare, Reach, RetweetCount, Likes, Klout, Sentiment, text, LocationID, UserID) VALUES ('T30011', 'Monday', 9, 3, 'en', 'No', 150, 0, 5, 40, 0.8, 'Excited to join Twitter!', 'L20012', 'U10045');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO twitter (TweetID, Weekday, Hour, Day, Lang, IsReshare, Reach, RetweetCount, Likes, Klout, Sentiment, text, LocationID, UserID) VALUES ('T30012', 'Tuesday', 18, 4, 'es', 'Yes', 100, 1, 3, 38, 0.9, '¡Feliz de estar aquí!', 'L20012', 'U10045');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="u9831",
      instruction="Hi, I'm Marcus Yu (user id: u9831). Please update my gender to 'Male' in my account. Also, update all my English-language tweets (language: 'en') currently under temporary user id 'temp_id' to my permanent user id 'u9831'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Male' WHERE UserID = 'u9831';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET UserID = 'u9831' WHERE Lang = 'en' AND UserID = 'temp_id';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="32",
      instruction="I am Hailey Chan (User ID: U3625, Gender: Female). Please permanently delete all my tweets posted in San Diego specifically on Saturdays or Sundays. Verify my identity using User ID U3625 and Female gender before proceeding with removal.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE UserID = 'U3625' AND Gender = 'Female';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT t.tweetID FROM twitter t JOIN location l ON t.LocationID = l.LocationID WHERE t.UserID = 'U3625' AND l.City = 'San Diego' AND (t.Weekday = 'Saturday' OR t.Weekday = 'Sunday');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 'U3625' AND LocationID IN (SELECT LocationID FROM location WHERE City = 'San Diego') AND (Weekday = 'Saturday' OR Weekday = 'Sunday');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12345",
      instruction="As user 12345, first authenticate me. Then: 1) Update my tweet ID 5678 - set text to 'Excited about privacy!', weekday to 'Tuesday', and language to 'en'. 2) Change my profile gender from 'Male' to 'Other'. Confirm both updates.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE user_id = 12345;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET text = 'Excited about privacy!', Weekday = 'Tuesday', language = 'en' WHERE tweet_id = 5678 AND user_id = 12345;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Other' WHERE user_id = 12345 AND Gender = 'Male';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="36",
      instruction="I am user with ID 12. Please first verify my identity by confirming my account details. After confirmation, update my gender to 'Non-binary' and permanently delete all tweets I posted from the city of 'Seattle'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE UserID = 12;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Non-binary' WHERE UserID = 12;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT LocationID FROM location WHERE City = 'Seattle';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 12 AND LocationID IN (SELECT LocationID FROM location WHERE City = 'Seattle');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="u10234",
      instruction="I am user u10234. Please delete all my tweets posted from Brooklyn. Confirm deletion using my UserID 'u10234' and city name 'Brooklyn'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE user_id = 'u10234';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT locationid FROM location WHERE City = 'Brooklyn';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE userID = 'u10234' AND locationid IN (SELECT locationid FROM location WHERE City = 'Brooklyn');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="38",
      instruction="My UserID is tw-465925216 and I am a Male user. I need to permanently delete my tweet posted on Day 21 at 8AM containing the exact phrase 'Export existing AWS resources to @terraformsf'. Please verify my identity and remove all matching tweets from the twitter table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE UserID = 'tw-465925216' AND Gender = 'Male';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 'tw-465925216' AND Day = 21 AND Hour = 8 AND text LIKE '%Export existing AWS resources to @terraformsf%';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="JL2024",
      instruction="I am Jordan Lee (user id JL2024). Please update my gender to 'Unisex' in your records. Then, delete all my tweets where the language is exactly 'Spanish' and the 'IsReshare' field equals 'Yes'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE user_id = 'JL2024';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Unisex' WHERE user_id = 'JL2024';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 'JL2024' AND Lang = 'Spanish' AND IsReshare = 'Yes';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="44",
      instruction="You are Olivia Chen, a diligent social media manager. First authenticate user1003's identity, then (1) count how many Spanish-language tweets (Lang='es') were posted by user1003 on Sundays (Weekday='Sunday') during June (Day between 1 and 30), and (2) delete them all. Explicitly specify user_id='user1003', Lang='es', Weekday='Sunday', and Day >=1 AND Day <=30 in all relevant SQL operations. Proceed strictly in this sequence.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT Gender FROM user WHERE UserID = 'user1003';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT COUNT(*) FROM twitter WHERE UserID = 'user1003' AND Lang = 'es' AND Weekday = 'Sunday' AND Day >= 1 AND Day <= 30;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 'user1003' AND Lang = 'es' AND Weekday = 'Sunday' AND Day >= 1 AND Day <= 30;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Find female user",
      instruction="I'm the only female user in the system. Please change the language of my tweet (tweet ID 145) to English ('en').",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT user_id FROM user WHERE Gender = 'Female';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET language = 'en' WHERE tweet_id = 145 AND user_id = (SELECT user_id FROM user WHERE Gender = 'Female');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="46",
      instruction="My name is Sam Rivera. My user id is 'user_1928'. Please update my gender to 'Other'. For my user id 'user_1928', change the language to 'es' and sentiment to 'positive' for my tweet with tweet id 'tweet_3881'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Other' WHERE user_id = 'user_1928';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET language = 'es', Sentiment = 'positive' WHERE tweet_id = 'tweet_3881' AND user_id = 'user_1928';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="47",
      instruction="As the user with ID 'tw-26753143', I need to update my tweet (TweetID: 'tw-701484415034249218') posted at LocationID 2228 on day 21 during hour 12. Change the language to 'no', set sentiment score to 0.5, and update the text to 'Oppdatert applikasjon er drevet av aws, #threejs og nginx i Oslo.'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE UserID = 'tw-26753143';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET Lang = 'no', Sentiment = 0.5, text = 'Oppdatert applikasjon er drevet av aws, #threejs og nginx i Oslo.' WHERE TweetID = 'tw-701484415034249218' AND UserID = 'tw-26753143' AND LocationID = 2228 AND Day = 21 AND Hour = 12;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="48",
      instruction="You are user 456 (male) and want to delete all tweets posted on Saturdays or Sundays with fewer than 5 likes. First confirm your identity, then locate and remove all qualifying tweets from your account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT user_id FROM user WHERE user_id = '456' AND Gender = 'Male';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT tweet_id FROM twitter WHERE user_id = '456' AND (Weekday = 'Saturday' OR Weekday = 'Sunday') AND Likes < 5;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE user_id = '456' AND (Weekday = 'Saturday' OR Weekday = 'Sunday') AND Likes < 5;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="50",
      instruction="I am a user with user ID 47. I want to permanently delete all of my tweets from the platform. Please confirm my account and remove every tweet associated with user ID 47.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT user_id FROM user WHERE user_id = 47"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE user_id = 47"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="51",
      instruction="I am user U12749 and need to update my profile gender to 'Non-binary'. Additionally, schedule a new tweet with the following details: tweet id T60293, to be posted on Friday at 15:00 (hour 15), day 12 of the month, in Spanish (language 'es'), not a reshare (is_reshare 'False'). The tweet should have a reach of 425, retweet count 2, likes 25, klout score 67, sentiment 0.7, text '¡Día productivo en el trabajo!', and originate from location id 483.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE UserID = 'U12749';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Non-binary' WHERE UserID = 'U12749';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO twitter (TweetID, Weekday, Hour, Day, Lang, IsReshare, Reach, RetweetCount, Likes, Klout, Sentiment, text, LocationID, UserID) VALUES ('T60293', 'Friday', 15, 12, 'es', 'False', 425, 2, 25, 67, 0.7, '¡Día productivo en el trabajo!', 483, 'U12749');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="u5678",
      instruction="You are Dalia Morgan (user u5678) requesting to permanently delete all your English-language ('en') tweets posted on Saturdays or Sundays to maintain a professional social media presence. First verify how many tweets meet these criteria (language: 'en', weekdays: Saturday/Sunday) before proceeding with deletion.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT COUNT(*) FROM twitter WHERE UserID = 'u5678' AND Lang = 'en' AND (Weekday = 'Saturday' OR Weekday = 'Sunday');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM twitter WHERE UserID = 'u5678' AND Lang = 'en' AND (Weekday = 'Saturday' OR Weekday = 'Sunday');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="55",
      instruction="I am a male user with ID 'U12345'. Please authenticate me, find all my tweets posted on Monday at 15:00 hour, then update their location to LocationID 100 with Country 'USA', State 'California', StateCode 'CA', and City 'San Francisco'. Ensure the location entry exists with these details before updating the tweets.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE Gender = 'Male' AND UserID = 'U12345';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT tweetid FROM twitter WHERE UserID = 'U12345' AND Weekday = 'Monday' AND Hour = 15;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT OR REPLACE INTO location (LocationID, Country, State, StateCode, City) VALUES (100, 'USA', 'California', 'CA', 'San Francisco');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE twitter SET LocationID = 100 WHERE UserID = 'U12345' AND Weekday = 'Monday' AND Hour = 15;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="56",
      instruction="Please verify my identity as Alex Morgan using UserID 7 and email alex.morgan915@example.com. After confirmation, update my profile's gender from 'Unisex' to 'Male' and modify my location record (LocationID: 12) with City='Austin', State='Texas', StateCode='TX'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM user WHERE UserID = 7 AND Email = 'alex.morgan915@example.com';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE location SET City = 'Austin', State = 'Texas', StateCode = 'TX' WHERE LocationID = 12;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE user SET Gender = 'Male' WHERE UserID = 7;"
               }
            ),
       ],
       outputs=[]
   ),
]
