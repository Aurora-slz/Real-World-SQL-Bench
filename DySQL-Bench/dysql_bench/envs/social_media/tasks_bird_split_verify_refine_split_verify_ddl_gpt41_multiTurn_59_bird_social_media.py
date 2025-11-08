from tau_bench.types import Task, Action

TASKS_TEST = [
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
]
