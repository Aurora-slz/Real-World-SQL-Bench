from dysql_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="0",
      instruction="I'm Bailey Hallmark (BowlerID: 29). I noticed an error in my bowling score for MatchID 36, GameNumber 3: the RawScore in Bowler_Scores shows 161 but should be 165. Before correcting it, please archive the current record to Bowler_Scores_Archive. Then update my score to 165.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 36 AND GameNumber = 3 AND BowlerID = 29;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 165 WHERE MatchID = 36 AND GameNumber = 3 AND BowlerID = 29;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1",
      instruction="Authenticate me as Stephanie Viescas with BowlerID 8. After verification, update my RawScore to 152 for MatchID 9 and GameNumber 3 in the Bowler_Scores table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 8 AND BowlerFirstName = 'Stephanie' AND BowlerLastName = 'Viescas';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 152 WHERE BowlerID = 8 AND MatchID = 9 AND GameNumber = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2",
      instruction="I am Ann Patterson (BowlerID 5) living at 16 Maple Lane, Auburn, WA 98002. I recently checked my records for MatchID 26, Game 3, and noticed my RawScore was entered as 160 instead of the correct score, 170. Please update my RawScore to 170 for BowlerID 5.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 5 AND BowlerFirstName = 'Ann' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 170 WHERE BowlerID = 5 AND MatchID = 26 AND GameNumber = 3 AND RawScore = 160;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4",
      instruction="My name is Gary Hallmark (BowlerID: 14), and I want to correct errors in my score records. For MatchID 30, GameNumber 2 at Red Rooster Lanes (TourneyID 8, 2017-10-23), my RawScore should be 158 (not 148). For MatchID 10, GameNumber 2 at Bolero Lanes (TourneyID 3, 2017-09-18), my HandiCapScore should be 207 (not 197). Please update these scores with all given MatchID, GameNumber, BowlerID, and correct values.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 14 AND BowlerFirstName = 'Gary' AND BowlerLastName = 'Hallmark';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 158 WHERE MatchID = 30 AND GameNumber = 2 AND BowlerID = 14;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET HandiCapScore = 207 WHERE MatchID = 10 AND GameNumber = 2 AND BowlerID = 14;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5",
      instruction="Hi, I'm Maria Patterson (BowlerID 34) from the Manatees (TeamID 7). Could you add the Emerald City Invitational tournament? It's scheduled for 2024-07-15 at Rainier Bowl with TourneyID 105. Then, register our team (TeamID 7) as the OddLaneTeam against TeamID 12 (EvenLaneTeam) for match 2001 on lanes 5-6. Lastly, I need to set a placeholder score for myself in game 1: BowlerID 34, RawScore 0, HandiCapScore 0, WonGame false.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 34 AND BowlerFirstName = 'Maria' AND BowlerLastName = 'Patterson' AND TeamID = 7;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tournaments (TourneyID, TourneyDate, TourneyLocation) VALUES (105, '2024-07-15', 'Rainier Bowl');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tourney_Matches (MatchID, TourneyID, Lanes, OddLaneTeamID, EvenLaneTeamID) VALUES (2001, 105, '5-6', 7, 12);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (2001, 1, 34, 0, 0, FALSE);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="7",
      instruction="I am Ann Patterson, living at 16 Maple Lane, Auburn, WA 98002. I discovered a verified scoring error for MatchID 50, GameNumber 1 at Totem Lanes on 2017-11-27. Please update my RawScore for that match from 159 to 165.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 165 WHERE MatchID = 50 AND GameNumber = 1 AND BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Ann' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="27",
      instruction="I am William G. Thompson with BowlerID 27. Please verify my identity by checking my name in your records. Then, for MatchID 50 and GameNumber 1, update my RawScore to 199 and HandiCapScore to 229, keeping WonGame=1 unchanged. Also, archive the original Bowler_Scores record before updating.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerLastName, BowlerFirstName, BowlerMiddleInit FROM Bowlers WHERE BowlerID = 27;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID=50 AND GameNumber=1 AND BowlerID=27;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore=199, HandiCapScore=229 WHERE MatchID=50 AND GameNumber=1 AND BowlerID=27;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9",
      instruction="I am David Cunningham from 4110 Old Redmond Rd., Redmond, WA 98052. I recently checked my match scores and noticed an error. For MatchID 39, GameNumber 2, my raw score is wrongly listed as 146, but it should be 149. Please update my raw score for that entry to 149. Also, I want to archive my score entry for MatchID 5, GameNumber 2 as it was from last season and should be moved out of the current records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'David' AND BowlerLastName = 'Cunningham' AND BowlerAddress = '4110 Old Redmond Rd.' AND BowlerCity = 'Redmond' AND BowlerState = 'WA' AND BowlerZip = '98052';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 149 WHERE MatchID = 39 AND GameNumber = 2 AND BowlerID = 10;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 5 AND GameNumber = 2 AND BowlerID = 10;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 5 AND GameNumber = 2 AND BowlerID = 10;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="11",
      instruction="I am Ben Clothier (BowlerID 31), living at 722 Moss Bay Blvd., Kirkland, WA 98033. I need to correct my recorded score for MatchID 16, GameNumber 1 from RawScore 174 and HandiCapScore 211 to RawScore 178 and HandiCapScore 215. Please archive the original record before making the change.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerAddress, BowlerCity, BowlerState, BowlerZip FROM Bowlers WHERE BowlerID = 31;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID = 31 AND MatchID = 16 AND GameNumber = 1 AND RawScore = 174 AND HandiCapScore = 211;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 178, HandiCapScore = 215 WHERE BowlerID = 31 AND MatchID = 16 AND GameNumber = 1 AND RawScore = 174 AND HandiCapScore = 211;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="29",
      instruction="I am Bailey Hallmark with BowlerID 29. Please verify my identity by confirming my first name and last name. Once verified, archive all my Bowler_Scores records for matches played at Acapulco Lanes in 2017 by moving each matching entry (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) to Bowler_Scores_Archive and remove it from Bowler_Scores.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 29 AND BowlerFirstName = 'Bailey' AND BowlerLastName = 'Hallmark';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE bs.BowlerID = 29 AND t.TourneyLocation = 'Acapulco Lanes' AND strftime('%Y', t.TourneyDate) = '2017';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 29 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Acapulco Lanes' AND strftime('%Y', t.TourneyDate) = '2017');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="13",
      instruction="Hello, I'm Suzanne Viescas (BowlerID 20) from the Dolphins team (TeamID 5). My RawScore for MatchID 36, GameNumber 2 – played at Thunderbird Lanes on 2017-10-30 – is currently 140 but should be 150. Please archive the existing record for BowlerID 20 in this match/game first, then update my RawScore to 150.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 20 AND BowlerFirstName = 'Suzanne' AND BowlerLastName = 'Viescas' AND TeamID = 5"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 36 AND GameNumber = 2 AND BowlerID = 20"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 150 WHERE MatchID = 36 AND GameNumber = 2 AND BowlerID = 20"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="15",
      instruction="I am Maria Patterson (BowlerID 34). Please remove my archived score records for MatchID 52 for GameNumbers 1 and 2 in the Bowler_Scores_Archive table because I was mistakenly listed as a participant.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID, BowlerFirstName, BowlerLastName FROM Bowlers WHERE BowlerID = 34;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores_Archive WHERE BowlerID = 34 AND MatchID = 52 AND (GameNumber = 1 OR GameNumber = 2);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="16",
      instruction="I am Kerry Patterson (BowlerID: 33) from team Manatees (TeamID: 7). I found an error in my bowling scores: for MatchID 105 and GameNumber 2, my RawScore was recorded as 140 instead of 167. Could you please update the Bowler_Scores table to set RawScore to 167 where BowlerID is 33, MatchID is 105, and GameNumber is 2? Additionally, MatchID 105 was never linked to its tournament. Please add a record to the Tourney_Matches table with MatchID 105, TourneyID 15, Lanes '11-12', OddLaneTeamID 7, and EvenLaneTeamID 12.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 33"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 167 WHERE BowlerID = 33 AND MatchID = 105 AND GameNumber = 2"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tourney_Matches (MatchID, TourneyID, Lanes, OddLaneTeamID, EvenLaneTeamID) VALUES (105, 15, '11-12', 7, 12)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="17",
      instruction="Hello, I am Gary Hallmark, BowlerID 14. Please verify my identity. For Game 3 of MatchID 24 (TournamentID 6 at Totem Lanes on 2017-10-09), my recorded RawScore was 163 and HandiCapScore 201, but this is incorrect. The correct RawScore is 180, and HandiCapScore should be 218. All other fields like WonGame (0) remain unchanged. Please archive the original record (MatchID 24, GameNumber 3, BowlerID 14, RawScore 163, HandiCapScore 201, WonGame 0) into Bowler_Scores_Archive, then update the Bowler_Scores row to RawScore 180 and HandiCapScore 218 for the same MatchID, GameNumber, and BowlerID.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (24, 3, 14, 163, 201, 0);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore=180, HandiCapScore=218 WHERE MatchID=24 AND GameNumber=3 AND BowlerID=14;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="26",
      instruction="Please verify my identity. I am Mary K. Thompson with BowlerID 26. After authentication, archive all my bowling score records from tournaments held at 'Thunderbird Lanes'. Specifically, insert each relevant record into Bowler_Scores_Archive (using BowlerID=26 and TourneyLocation='Thunderbird Lanes'), then delete those records from Bowler_Scores.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT 1 FROM Bowlers WHERE BowlerID = 26 AND BowlerFirstName = 'Mary' AND BowlerLastName = 'Thompson' AND BowlerMiddleInit = 'K'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID WHERE bs.BowlerID = 26 AND tm.TourneyID IN (SELECT TourneyID FROM Tournaments WHERE TourneyLocation = 'Thunderbird Lanes')"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 26 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Thunderbird Lanes')"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="21",
      instruction="I am Neil Patterson from Auburn, WA (BowlerID 6). Please update my scores for MatchID 53, GameNumber 2: change RawScore from 179 to 181 and HandiCapScore from 217 to 219 due to an entry error.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID, BowlerFirstName, BowlerLastName, BowlerCity, BowlerState FROM Bowlers WHERE BowlerID = 6;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 181, HandiCapScore = 219 WHERE BowlerID = 6 AND MatchID = 53 AND GameNumber = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22",
      instruction="I am Barbara Fournier (BowlerID 1), and I'd like to archive my game scores for all games I played in the tournament held at Red Rooster Lanes on September 4th, 2017. Please move my Bowler_Scores records from the main table to Bowler_Scores_Archive for that tournament.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Red Rooster Lanes' AND t.TourneyDate = '2017-09-04' AND bs.BowlerID = 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE EXISTS (SELECT 1 FROM Tourney_Matches tm JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE tm.MatchID = Bowler_Scores.MatchID AND t.TourneyLocation = 'Red Rooster Lanes' AND t.TourneyDate = '2017-09-04') AND BowlerID = 1;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2",
      instruction="Authenticate me: My name is David Fournier and my address is 67 Willow Drive. Then, archive all my game scores for matches that happened before 2017-10-01 and remove these archived scores from the current Bowler_Scores table. Only apply these changes to my scores and only for matches in tournaments dated before 2017-10-01.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'David' AND BowlerLastName = 'Fournier' AND BowlerAddress = '67 Willow Drive';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE bs.BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'David' AND BowlerLastName = 'Fournier' AND BowlerAddress = '67 Willow Drive') AND t.TourneyDate < '2017-10-01';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'David' AND BowlerLastName = 'Fournier' AND BowlerAddress = '67 Willow Drive') AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyDate < '2017-10-01');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="24",
      instruction="Verify my identity: I am John Kennedy with middle initial A, and my BowlerID is 3. Then, archive all match scores for BowlerID 3 from tournaments held at 'Acapulco Lanes'. Specifically, move all associated records from the Bowler_Scores table into Bowler_Scores_Archive and delete them from Bowler_Scores.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 3 AND BowlerFirstName = 'John' AND BowlerLastName = 'Kennedy' AND BowlerMiddleInit = 'A';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE bs.BowlerID = 3 AND t.TourneyLocation = 'Acapulco Lanes';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 3 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Acapulco Lanes');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="25",
      instruction="I am Ben Clothier with BowlerID 31 – to confirm my identity. Could you archive all my bowling scores from tournaments before October 1, 2017? Please move only my records (BowlerID 31) linked to pre-2017-10-01 tournaments from the Bowler_Scores table to Bowler_Scores_Archive, then delete them from the active table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE bs.BowlerID = 31 AND t.TourneyDate < '2017-10-01';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 31 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyDate < '2017-10-01');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="27",
      instruction="Hello, I'm Kerry Patterson with Bowler ID 33. I've moved to 122 Pine St, Auburn, WA, 98002 and my new phone number is (206) 555-9211. Please update my bowler profile. Additionally, for Match ID 42, Game Number 3, I scored 176 with a handicap of 0 and did not win—please record this game in my scores.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 33 AND BowlerFirstName = 'Kerry' AND BowlerLastName = 'Patterson';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerAddress = '122 Pine St', BowlerCity = 'Auburn', BowlerState = 'WA', BowlerZip = '98002', BowlerPhoneNumber = '(206) 555-9211' WHERE BowlerID = 33;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (42, 3, 33, 176, 0, FALSE);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="28",
      instruction="Hello, I am Zachary Ehrlich, BowlerID 21. I need to correct an error in my bowling score records. For MatchID 55, GameNumber 1 at Acapulco Lanes on December 4, 2017, my RawScore was entered as 155, but it should be 165. Please update my RawScore to 165 and archive the original entry for audit purposes.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 21;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT * FROM Bowler_Scores WHERE MatchID = 55 AND GameNumber = 1 AND BowlerID = 21;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 165 WHERE MatchID = 55 AND GameNumber = 1 AND BowlerID = 21;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="29",
      instruction="I am Kathryn Patterson (BowlerID 15). I need to correct my score to 193 for MatchID 16, GameNumber 3, as there was a confirmed error in the records for the Imperial Lanes tournament on 2017-09-25. Please archive the previous Bowler_Scores entry before making the update.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 15 AND BowlerFirstName = 'Kathryn' AND BowlerLastName = 'Patterson';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 16 AND GameNumber = 3 AND BowlerID = 15;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 193 WHERE MatchID = 16 AND GameNumber = 3 AND BowlerID = 15;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="31",
      instruction="I am John A. Kennedy with BowlerID 3 from Ballard, WA. First, verify my identity by checking the Bowlers table. Then, archive all records for my performance in MatchID 41, GameNumber 2: Move my Bowler_Scores (MatchID=41, GameNumber=2, BowlerID=3, RawScore=188, HandiCapScore=220, WonGame=1), the Match_Games info (MatchID=41, GameNumber=2, WinningTeamID=6), Tourney_Matches details (MatchID=41, TourneyID=11, Lanes='11-12', OddLaneTeamID=1, EvenLaneTeamID=6), and the associated Tournament (TourneyID=11, TourneyDate='2017-11-13', TourneyLocation='Imperial Lanes') into their respective '_Archive' tables. After archiving, remove the original records from the source tables.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID, BowlerCity, BowlerState FROM Bowlers WHERE BowlerID = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (41, 2, 3, 188, 220, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 41 AND GameNumber = 2 AND BowlerID = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive (MatchID, GameNumber, WinningTeamID) VALUES (41, 2, 6);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE MatchID = 41 AND GameNumber = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tourney_Matches_Archive (MatchID, TourneyID, Lanes, OddLaneTeamID, EvenLaneTeamID) VALUES (41, 11, '11-12', 1, 6);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Tourney_Matches WHERE MatchID = 41;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tournaments_Archive (TourneyID, TourneyDate, TourneyLocation) VALUES (11, '2017-11-13', 'Imperial Lanes');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Tournaments WHERE TourneyID = 11;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="32",
      instruction="I am Maria Patterson (BowlerID=34). Please restore my mistakenly archived score for MatchID=104, GameNumber=2 to the active Bowler_Scores table and remove the archived copy from Bowler_Scores_Archive to prevent duplicate records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID=34 AND BowlerLastName='Patterson' AND BowlerFirstName='Maria';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores_Archive WHERE BowlerID=34 AND MatchID=104 AND GameNumber=2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores_Archive WHERE BowlerID=34 AND MatchID=104 AND GameNumber=2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="34",
      instruction="You are Ann Patterson (BowlerID 5), thorough about your bowling stats. You noticed three duplicate or mis-entered scores in your records and want them cleaned up by moving them from Bowler_Scores to Bowler_Scores_Archive. The records to archive are: - MatchID 6, GameNumber 3, BowlerID 5, RawScore 165, HandiCapScore 212, WonGame 1 - MatchID 26, GameNumber 3, BowlerID 5, RawScore 160, HandiCapScore 206, WonGame 1 - MatchID 14, GameNumber 1, BowlerID 5, RawScore 163, HandiCapScore 207, WonGame 1. After archiving, delete these exact three entries from Bowler_Scores.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (6, 3, 5, 165, 212, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (26, 3, 5, 160, 206, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (14, 1, 5, 163, 207, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 6 AND GameNumber = 3 AND BowlerID = 5;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 26 AND GameNumber = 3 AND BowlerID = 5;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 14 AND GameNumber = 1 AND BowlerID = 5;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="35",
      instruction="Hello, I'm Maria Patterson with BowlerID 34, and I bowl for the Manatees team. I need to resolve a data issue by archiving and deleting my bowling score records for MatchID 101 and GameNumber 2. Please transfer my records from Bowler_Scores to Bowler_Scores_Archive and remove them from the original table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers JOIN Teams ON Bowlers.TeamID = Teams.TeamID WHERE Bowlers.BowlerID = 34 AND Bowlers.BowlerFirstName = 'Maria' AND Bowlers.BowlerLastName = 'Patterson' AND Teams.TeamName = 'Manatees';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 101 AND GameNumber = 2 AND BowlerID = 34;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 101 AND GameNumber = 2 AND BowlerID = 34;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="36",
      instruction="I am David A Viescas with BowlerID 7. Please archive my records for MatchID 38, GameNumbers 1, 2, and 3. Specifically, move my Bowler_Scores for these games, the corresponding Match_Games entries, and the Tourney_Matches record for MatchID 38 to their archive tables.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 7 AND BowlerFirstName = 'David' AND BowlerLastName = 'Viescas' AND BowlerMiddleInit = 'A';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID = 7 AND MatchID = 38 AND GameNumber IN (1,2,3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 7 AND MatchID = 38 AND GameNumber IN (1,2,3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive (MatchID, GameNumber, WinningTeamID) SELECT MatchID, GameNumber, WinningTeamID FROM Match_Games WHERE MatchID = 38 AND GameNumber IN (1,2,3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE MatchID = 38 AND GameNumber IN (1,2,3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tourney_Matches_Archive (MatchID, TourneyID, Lanes, OddLaneTeamID, EvenLaneTeamID) SELECT MatchID, TourneyID, Lanes, OddLaneTeamID, EvenLaneTeamID FROM Tourney_Matches WHERE MatchID = 38;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Tourney_Matches WHERE MatchID = 38;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="39",
      instruction="I'm Suzanne Viescas (BowlerID 20). I've recently moved—please update my profile to address '910 Lakeview Ave', Bellevue, WA 98004, phone '(425) 678-9101' and set my Team affiliation to TeamID 3. Lastly, move all my match scores from the tournament held at Totem Lanes on 2017-11-27 to the archive and remove them from active records, as they reflect my old team.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerAddress = '910 Lakeview Ave', BowlerCity = 'Bellevue', BowlerState = 'WA', BowlerZip = '98004', BowlerPhoneNumber = '(425) 678-9101', TeamID = 3 WHERE BowlerID = 20;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT * FROM Bowler_Scores WHERE BowlerID = 20 AND MatchID IN (SELECT MatchID FROM Tourney_Matches WHERE TourneyID = (SELECT TourneyID FROM Tournaments WHERE TourneyLocation = 'Totem Lanes' AND TourneyDate = '2017-11-27'));"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 20 AND MatchID IN (SELECT MatchID FROM Tourney_Matches WHERE TourneyID = (SELECT TourneyID FROM Tournaments WHERE TourneyLocation = 'Totem Lanes' AND TourneyDate = '2017-11-27'));"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="42",
      instruction="Authenticate me: I am Rachel Patterson with BowlerID 30, living at 16 Maple Lane, Auburn, WA 98002. After authentication, update my MatchID 19 GameNumber 2 result to a loss (set WonGame=0) and archive the previous record with MatchID=19, GameNumber=2, BowlerID=30, RawScore=177, HandiCapScore=214, WonGame=1.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 30 AND BowlerFirstName = 'Rachel' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET WonGame = 0 WHERE BowlerID = 30 AND MatchID = 19 AND GameNumber = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (19, 2, 30, 177, 214, 1);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="43",
      instruction="Please archive my bowling performance records (BowlerID: 3) from the tournament at Sports World Lanes on 2017-11-20. Specifically, copy to archive tables: 1) My Bowler_Scores for MatchID 45, 2) Match_Games for MatchID 45, 3) Tourney_Matches for TourneyID 12, 4) Tournaments record for TourneyID 12.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT * FROM Bowler_Scores WHERE BowlerID = 3 AND MatchID = 45;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive SELECT * FROM Match_Games WHERE MatchID = 45;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tourney_Matches_Archive SELECT * FROM Tourney_Matches WHERE TourneyID = 12;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tournaments_Archive SELECT * FROM Tournaments WHERE TourneyID = 12;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="44",
      instruction="I am Angel Kennedy with BowlerID 11. My first name is Angel and last name is Kennedy. I noticed that my raw score for MatchID 19, GameNumber 3 was incorrectly entered as 149. Please archive the original entry (BowlerID 11, MatchID 19, GameNumber 3, RawScore 149) into Bowler_Scores_Archive for reference. Then, update the RawScore to 159 in the Bowler_Scores table while keeping HandiCapScore and WonGame unchanged.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 11 AND BowlerFirstName = 'Angel' AND BowlerLastName = 'Kennedy';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 19 AND GameNumber = 3 AND BowlerID = 11;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 159 WHERE MatchID = 19 AND GameNumber = 3 AND BowlerID = 11;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="46",
      instruction="My name is Michael L. Viescas and my zip code is 98052. I am retiring from league bowling and wish to archive my achievements. Please: (1) archive all my game records from the Bowler_Scores table into Bowler_Scores_Archive, (2) archive all matches where my team won from the Match_Games table into Match_Games_Archive, and (3) archive all tournaments my team participated in (via Tourney_Matches where my team was on odd or even lanes) into Tournaments_Archive.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT * FROM Bowler_Scores WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Michael' AND BowlerLastName = 'Viescas' AND BowlerMiddleInit = 'L' AND BowlerZip = '98052');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive SELECT * FROM Match_Games WHERE WinningTeamID = (SELECT TeamID FROM Bowlers WHERE BowlerFirstName = 'Michael' AND BowlerLastName = 'Viescas' AND BowlerMiddleInit = 'L' AND BowlerZip = '98052');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tournaments_Archive SELECT * FROM Tournaments WHERE TourneyID IN (SELECT TourneyID FROM Tourney_Matches WHERE OddLaneTeamID = (SELECT TeamID FROM Bowlers WHERE BowlerFirstName = 'Michael' AND BowlerLastName = 'Viescas' AND BowlerMiddleInit = 'L' AND BowlerZip = '98052') OR EvenLaneTeamID = (SELECT TeamID FROM Bowlers WHERE BowlerFirstName = 'Michael' AND BowlerLastName = 'Viescas' AND BowlerMiddleInit = 'L' AND BowlerZip = '98052'));"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="48",
      instruction="I am Michael Hernandez, and my BowlerID is 18. Please authenticate me using my first name, last name, and BowlerID. After authentication, I need to correct an error in my game record for MatchID 36, GameNumber 2. The recorded scores are RawScore: 179, HandiCapScore: 217, and WonGame: 1. However, the correct scores should be RawScore: 165, HandiCapScore: 203, and WonGame: 0 (since I did not win that game). Please first archive the incorrect record and then update Bowler_Scores with the corrected values for BowlerID 18, MatchID 36, and GameNumber 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 18 AND BowlerFirstName = 'Michael' AND BowlerLastName = 'Hernandez';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 36 AND GameNumber = 2 AND BowlerID = 18;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 165, HandiCapScore = 203, WonGame = 0 WHERE MatchID = 36 AND GameNumber = 2 AND BowlerID = 18;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="50",
      instruction="I am Michael Hernandez (BowlerID 18), and I am moving out of state. Please verify my identity. Then, archive all my bowling scores exclusively from matches played at Thunderbird Lanes (TourneyLocation='Thunderbird Lanes') by matching my BowlerID and name. Finally, delete these verified scores from the main Bowler_Scores table. Leave all other records untouched.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID JOIN Tournaments t ON tm.TourneyID = t.TourneyID JOIN Bowlers b ON bs.BowlerID = b.BowlerID WHERE bs.BowlerID = 18 AND t.TourneyLocation = 'Thunderbird Lanes' AND b.BowlerFirstName = 'Michael' AND b.BowlerLastName = 'Hernandez';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 18 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Thunderbird Lanes') AND EXISTS (SELECT 1 FROM Bowlers WHERE BowlerID = 18 AND BowlerFirstName = 'Michael' AND BowlerLastName = 'Hernandez');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="52",
      instruction="I am Alastair Black, BowlerID 9. Please authenticate my identity. After verification, archive all my bowling game scores from tournament matches held prior to October 1, 2017, for historical preservation without removing current records. Separately, update my address to: Street - 9185 Main Street, City - Bellevue, State - WA, ZIP Code - 98004.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 9 AND BowlerFirstName = 'Alastair' AND BowlerLastName = 'Black';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE bs.BowlerID = 9 AND t.TourneyDate < '2017-10-01';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerAddress = '9185 Main Street', BowlerCity = 'Bellevue', BowlerState = 'WA', BowlerZip = '98004' WHERE BowlerID = 9;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="53",
      instruction="I am Michael L. Viescas (first name: Michael, last name: Viescas, middle initial: L) residing in Redmond, WA 98052. Please archive and permanently remove all my game records from matches played at the tournament location 'Imperial Lanes'. Use my personal details to verify my identity before proceeding.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Michael' AND BowlerLastName = 'Viescas' AND BowlerMiddleInit = 'L' AND BowlerCity = 'Redmond' AND BowlerState = 'WA' AND BowlerZip = '98052';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Imperial Lanes' AND bs.BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Michael' AND BowlerLastName = 'Viescas' AND BowlerMiddleInit = 'L' AND BowlerCity = 'Redmond' AND BowlerState = 'WA' AND BowlerZip = '98052');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Michael' AND BowlerLastName = 'Viescas' AND BowlerMiddleInit = 'L' AND BowlerCity = 'Redmond' AND BowlerState = 'WA' AND BowlerZip = '98052') AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Imperial Lanes');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="56",
      instruction="I am Alastair Black (BowlerID: 9). Please archive my individual scores for MatchID 5 GameNumber 1, MatchID 15 GameNumber 2, and MatchID 27 GameNumber 3 into Bowler_Scores_Archive. Also archive the corresponding winning team records for these match-game combinations in Match_Games_Archive. Update my address to: street '900 Rainier Ave', city 'Bellevue', state 'WA', and zip '98005'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID=9 AND ((MatchID=5 AND GameNumber=1) OR (MatchID=15 AND GameNumber=2) OR (MatchID=27 AND GameNumber=3));"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive (MatchID, GameNumber, WinningTeamID) SELECT MatchID, GameNumber, WinningTeamID FROM Match_Games WHERE (MatchID=5 AND GameNumber=1) OR (MatchID=15 AND GameNumber=2) OR (MatchID=27 AND GameNumber=3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerAddress='900 Rainier Ave', BowlerCity='Bellevue', BowlerState='WA', BowlerZip='98005' WHERE BowlerID=9;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="57",
      instruction="Hello, I'm Neil Patterson with BowlerID 6, residing at 16 Maple Lane in Auburn, WA, ZIP 98002. Please verify my identity first. Once confirmed, I need to correct my bowling scores: For MatchID 33, GameNumber 3, my RawScore should be 170 and HandiCapScore 205. Update these values in the system.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID=6 AND BowlerAddress='16 Maple Lane' AND BowlerCity='Auburn' AND BowlerState='WA' AND BowlerZip='98002';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore=170, HandiCapScore=205 WHERE MatchID=33 AND GameNumber=3 AND BowlerID=6;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="58",
      instruction="I am Alaina Hallmark, BowlerID 22. Please update my bowling records for MatchID 8, Game Number 2: Set RawScore to 152, HandiCapScore to 190, and mark WonGame as true since I won that game. Also, update my address to '109 Cherry Lane', city 'Bellevue', state 'WA', zip '98005'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore=152, HandiCapScore=190, WonGame=1 WHERE BowlerID=22 AND MatchID=8 AND GameNumber=2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerAddress='109 Cherry Lane', BowlerCity='Bellevue', BowlerState='WA', BowlerZip='98005' WHERE BowlerID=22;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="59",
      instruction="I am Zachary Ehrlich (BowlerID: 21). Please archive the following records: (1) My Bowler_Scores entry for MatchID 24 and GameNumber 3, (2) The Match_Games record for MatchID 24 and GameNumber 3, and (3) The Tournaments entry for TourneyID 6. Move these to their respective archive tables.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT * FROM Bowler_Scores WHERE BowlerID = 21 AND MatchID = 24 AND GameNumber = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 21 AND MatchID = 24 AND GameNumber = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive SELECT * FROM Match_Games WHERE MatchID = 24 AND GameNumber = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE MatchID = 24 AND GameNumber = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tournaments_Archive SELECT * FROM Tournaments WHERE TourneyID = 6;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Tournaments WHERE TourneyID = 6;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="61",
      instruction="Hello, I'm Michael Hernandez and I live at 47 Harvard Drive, Kirkland, WA. I need to permanently delete my highest bowling score of 180 from MatchID 28, GameNumber 2. After deletion, update my statistics to set total pins to 5945, games bowled to 38, and current average to 156.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 28 AND GameNumber = 2 AND RawScore = 180 AND BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Michael' AND BowlerLastName = 'Hernandez' AND BowlerAddress = '47 Harvard Drive' AND BowlerCity = 'Kirkland' AND BowlerState = 'WA');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerTotalPins = 5945, BowlerGamesBowled = 38, BowlerCurrentAverage = 156 WHERE BowlerFirstName = 'Michael' AND BowlerLastName = 'Hernandez' AND BowlerAddress = '47 Harvard Drive' AND BowlerCity = 'Kirkland' AND BowlerState = 'WA';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="62",
      instruction="Hello, I am Stephanie Viescas. My BowlerID is 8, and I live at 16679 NE 42nd Court, Redmond, WA 98052. During the tournament at Acapulco Lanes on December 4, 2017 (TourneyID 14), for MatchID 53, Game 2, my RawScore was entered as 137 instead of the correct score of 143. Could you archive the current record for this game and update the RawScore to 143?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 8 AND BowlerAddress = '16679 NE 42nd Court' AND BowlerCity = 'Redmond' AND BowlerState = 'WA' AND BowlerZip = '98052';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID = 8 AND MatchID = 53 AND GameNumber = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 143 WHERE BowlerID = 8 AND MatchID = 53 AND GameNumber = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="32",
      instruction="I am Joe Rosales (BowlerID: 32). Please archive my previous RawScore entry for MatchID 49, GameNumber 1 to Bowler_Scores_Archive before updating my score. Set the new RawScore to 145 for this match and game.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 32 AND BowlerLastName = 'Rosales' AND BowlerFirstName = 'Joe';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 49 AND GameNumber = 1 AND BowlerID = 32;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 145 WHERE MatchID = 49 AND GameNumber = 1 AND BowlerID = 32;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="66",
      instruction="Hello, I am Gary Hallmark with BowlerID 14. I have two updates for my records: First, please correct my last name from 'Hallmark' to 'Hallmann'. Second, for Game 2 of MatchID 52 at Totem Lanes on 2017-11-27 (TourneyID 13), update my score (BowlerID 14) to RawScore 146 and HandiCapScore 185.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerLastName = 'Hallmann' WHERE BowlerID = 14;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 146, HandiCapScore = 185 WHERE MatchID = 52 AND GameNumber = 2 AND BowlerID = 14;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="67",
      instruction="I am Gary Hallmark from Woodinville, WA 98072. Please remove all my bowling game records from the Bowler_Scores table that are associated with matches played at Acapulco Lanes due to a suspected scoring error. Ensure only my records from Acapulco Lanes are deleted.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerLastName='Hallmark' AND BowlerFirstName='Gary' AND BowlerCity='Woodinville' AND BowlerState='WA' AND BowlerZip='98072';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID IN (SELECT BowlerID FROM Bowlers WHERE BowlerLastName='Hallmark' AND BowlerFirstName='Gary' AND BowlerCity='Woodinville' AND BowlerState='WA' AND BowlerZip='98072') AND MatchID IN (SELECT TM.MatchID FROM Tourney_Matches TM JOIN Tournaments T ON TM.TourneyID = T.TourneyID WHERE T.TourneyLocation = 'Acapulco Lanes');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="71",
      instruction="Hello, I am Maria Patterson (BowlerID 34, last name Patterson), residing at 16 Maple Lane, Auburn, WA 98002. I need to update my contact phone number to (425) 555-9812. Additionally, as I am taking a break from bowling, please archive all my existing bowler scores from the Bowler_Scores table to Bowler_Scores_Archive and then remove them from Bowler_Scores. Ensure my scores are preserved under BowlerID 34.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 34 AND BowlerFirstName = 'Maria' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerPhoneNumber = '(425) 555-9812' WHERE BowlerID = 34;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID = 34;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 34;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="72",
      instruction="Authenticate as Ann K Patterson (BowlerID 5) living at 16 Maple Lane, Auburn, WA 98002. After authentication, archive all your game scores (BowlerID=5) from the tournament at Bolero Lanes on 2017-09-18 (TourneyID 3) by moving your Bowler_Scores records for matches in this tournament into Bowler_Scores_Archive. Then, delete these records from the main Bowler_Scores table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 5 AND BowlerLastName = 'Patterson' AND BowlerFirstName = 'Ann' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT BS.* FROM Bowler_Scores BS JOIN Tourney_Matches TM ON BS.MatchID = TM.MatchID WHERE BS.BowlerID = 5 AND TM.TourneyID = 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 5 AND MatchID IN (SELECT MatchID FROM Tourney_Matches WHERE TourneyID = 3);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="27",
      instruction="I'm William G. Thompson, BowlerID 27 from Duvall, WA. In Match 26, Game 2 at Acapulco Lanes (TourneyID 7, date 2017-10-16, lanes 15-16), my win was not recorded correctly. Please set my WonGame status to 1 for that record (MatchID=26, GameNumber=2, BowlerID=27). After updating, copy this corrected score (MatchID=26, GameNumber=2, BowlerID=27, RawScore=180, HandiCapScore=212, WonGame=1) to the Bowler_Scores_Archive.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID, BowlerFirstName, BowlerLastName, BowlerMiddleInit, BowlerCity, BowlerState FROM Bowlers WHERE BowlerID = 27;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET WonGame=1 WHERE MatchID=26 AND GameNumber=2 AND BowlerID=27;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (26, 2, 27, 180, 212, 1);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="75",
      instruction="I am Rachel Patterson with BowlerID 30. Please authenticate me. Then update my bowling score for MatchID 43 and GameNumber 2 to a RawScore of 167 as it was incorrectly recorded. Also, add a new game record for MatchID 40 with GameNumber 4: RawScore 155, HandiCapScore 192, and WonGame 0 since I missed recording it.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerFirstName, BowlerLastName FROM Bowlers WHERE BowlerID = 30;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 167 WHERE MatchID = 43 AND GameNumber = 2 AND BowlerID = 30;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (40, 4, 30, 155, 192, 0);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="76",
      instruction="I am Carol M. Viescas (BowlerID 12). Permanently archive all my lost game scores (where WonGame = 0) specifically tied to tournaments held at 'Acapulco Lanes'. After archiving, delete these scores from my active history. This action must only affect my lost games at this location and leave all team and tournament records unchanged.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE bs.BowlerID = 12 AND bs.WonGame = 0 AND t.TourneyLocation = 'Acapulco Lanes';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 12 AND WonGame = 0 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Acapulco Lanes');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="77",
      instruction="You are Michael Hernandez (BowlerID 18). You wish to archive your game records for MatchID 7 and 12. Please move all your Bowler_Scores records (for BowlerID 18, MatchID 7 or 12), as well as corresponding Match_Games records (MatchID 7 or 12, all GameNumbers) to their respective Archive tables.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID = 18 AND (MatchID = 7 OR MatchID = 12);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive (MatchID, GameNumber, WinningTeamID) SELECT MatchID, GameNumber, WinningTeamID FROM Match_Games WHERE MatchID = 7 OR MatchID = 12;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 18 AND (MatchID = 7 OR MatchID = 12);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE MatchID = 7 OR MatchID = 12;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="78",
      instruction="I am Kerry Patterson with BowlerID 33, currently residing in Auburn, WA. I need to update my address to 921 River Rd, Tacoma, WA 98402. Additionally, please archive my match score for MatchID 203 and GameNumber 1, and remove it from active records once archived.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerAddress = '921 River Rd', BowlerCity = 'Tacoma', BowlerState = 'WA', BowlerZip = '98402' WHERE BowlerID = 33;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 203 AND GameNumber = 1 AND BowlerID = 33;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 203 AND GameNumber = 1 AND BowlerID = 33;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="79",
      instruction="Hello, I'm William G. Thompson (Bowler ID 27). I need to request corrections for my scores from the September 18, 2017 tournament at Bolero Lanes (Tourney ID 3). Please update two records in Match ID 11: For Game 2, set my RawScore to 170 instead of 160. For Game 3, change WonGame to 0 (since I did not win) instead of 1.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 170 WHERE MatchID = 11 AND GameNumber = 2 AND BowlerID = 27;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET WonGame = 0 WHERE MatchID = 11 AND GameNumber = 3 AND BowlerID = 27;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="80",
      instruction="I am BowlerID 22. I need to update my RawScore to 150 for MatchID 38, GameNumber 1 and archive my score for MatchID 11, GameNumber 3 with values: RawScore 165, HandiCapScore 205, WonGame 1.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 150 WHERE MatchID = 38 AND GameNumber = 1 AND BowlerID = 22;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (11, 3, 22, 165, 205, 1);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="82",
      instruction="I'm Rachel Patterson (BowlerID 30) from Auburn, WA. Please verify my identity by confirming my first name, last name, city, and state match your records. After verification, I need to correct an error in my bowling record: For MatchID 47, GameNumber 1, my raw score was entered as 152 but should be 158. Update this in the Bowler_Scores table, then show me the updated entry.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerFirstName, BowlerLastName, BowlerCity, BowlerState FROM Bowlers WHERE BowlerID = 30;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 158 WHERE MatchID = 47 AND GameNumber = 1 AND BowlerID = 30;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowler_Scores WHERE MatchID = 47 AND GameNumber = 1 AND BowlerID = 30;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="84",
      instruction="Hello, I'm Bailey Hallmark. I noticed a duplicate entry for my bowling stats in MatchID 12, GameNumber 2. Please move this record to Bowler_Scores_Archive to preserve it and remove it from Bowler_Scores. Additionally, I've relocated to 425 Oak Lane, Bellevue, WA 98005—please update my BowlerAddress, BowlerCity, BowlerState, and BowlerZip in the Bowlers table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 12 AND GameNumber = 2 AND BowlerID = 29;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 12 AND GameNumber = 2 AND BowlerID = 29;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerAddress = '425 Oak Lane', BowlerCity = 'Bellevue', BowlerState = 'WA', BowlerZip = '98005' WHERE BowlerID = 29;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="85",
      instruction="I am Richard Sheskey. For privacy, please archive all of my scores for games I played in matches where the tournament date was before November 1, 2017. That is, move all rows from Bowler_Scores to Bowler_Scores_Archive for me and the related tournament date prior to 2017-11-01. After inserting these into the archive, please delete them from Bowler_Scores.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID INNER JOIN Bowlers b ON bs.BowlerID = b.BowlerID WHERE b.BowlerFirstName = 'Richard' AND b.BowlerLastName = 'Sheskey' AND t.TourneyDate < '2017-11-01';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE (MatchID, GameNumber, BowlerID) IN (SELECT bs.MatchID, bs.GameNumber, bs.BowlerID FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID INNER JOIN Bowlers b ON bs.BowlerID = b.BowlerID WHERE b.BowlerFirstName = 'Richard' AND b.BowlerLastName = 'Sheskey' AND t.TourneyDate < '2017-11-01');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="89",
      instruction="I am Mary K Thompson, BowlerID 26, residing at 122 Spring Valley Drive, Duvall, WA 98019. First, verify my identity using these details. Then, for my record in MatchID 21 and GameNumber 2, archive the current Bowler_Scores entry by copying it to the Bowler_Scores_Archive table. After archiving, update my RawScore to 145 and HandiCapScore to 184 in the Bowler_Scores table. This request applies exclusively to BowlerID 26, MatchID 21, and GameNumber 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT COUNT(*) AS auth_result FROM Bowlers WHERE BowlerID = 26 AND BowlerFirstName = 'Mary' AND BowlerLastName = 'Thompson' AND BowlerMiddleInit = 'K' AND BowlerAddress = '122 Spring Valley Drive' AND BowlerCity = 'Duvall' AND BowlerState = 'WA' AND BowlerZip = '98019';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID = 26 AND MatchID = 21 AND GameNumber = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 145, HandiCapScore = 184 WHERE BowlerID = 26 AND MatchID = 21 AND GameNumber = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="90",
      instruction="Hello, I'm Gary Hallmark with BowlerID=14, residing at Route 2, Box 203B, Woodinville, WA 98072. During the tournament at Sports World Lanes (TourneyID=12) on November 20, 2017, my scores for MatchID=48, GameNumber=2 were recorded incorrectly. Please update my Bowler_Scores record to set RawScore=150 (previously 140) and HandiCapScore=188 (previously 178). After the update, provide the corrected score summary for MatchID=48, GameNumber=2, and BowlerID=14 to verify the changes.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID=14 AND BowlerLastName='Hallmark' AND BowlerFirstName='Gary' AND BowlerAddress='Route 2, Box 203B' AND BowlerCity='Woodinville' AND BowlerState='WA' AND BowlerZip='98072';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore=150, HandiCapScore=188 WHERE MatchID=48 AND GameNumber=2 AND BowlerID=14;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowler_Scores WHERE MatchID=48 AND GameNumber=2 AND BowlerID=14;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="91",
      instruction="Hello, I am Rachel Patterson, residing at 16 Maple Lane, Auburn, WA 98002, phone (206) 555-3487. I need to correct an error in my bowling record for MatchID 49, GameNumber 1. My RawScore should be updated to 150 (currently 145), and HandiCapScore to 190 (currently 184). After updating, please show me the new RawScore and HandiCapScore for that game. Also, recalculate my BowlerTotalPins and BowlerCurrentAverage using my total games bowled (39 unchanged).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Rachel' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002' AND BowlerPhoneNumber = '(206) 555-3487';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 150, HandiCapScore = 190 WHERE MatchID = 49 AND GameNumber = 1 AND BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Rachel' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002' AND BowlerPhoneNumber = '(206) 555-3487');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT RawScore, HandiCapScore FROM Bowler_Scores WHERE MatchID = 49 AND GameNumber = 1 AND BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Rachel' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002' AND BowlerPhoneNumber = '(206) 555-3487');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerTotalPins = (SELECT SUM(RawScore) FROM Bowler_Scores WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Rachel' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002' AND BowlerPhoneNumber = '(206) 555-3487')) WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Rachel' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002' AND BowlerPhoneNumber = '(206) 555-3487');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerCurrentAverage = (SELECT CAST(SUM(RawScore) AS FLOAT) / 39 FROM Bowler_Scores WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Rachel' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002' AND BowlerPhoneNumber = '(206) 555-3487')) WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Rachel' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002' AND BowlerPhoneNumber = '(206) 555-3487');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerTotalPins, BowlerCurrentAverage FROM Bowlers WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Rachel' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002' AND BowlerPhoneNumber = '(206) 555-3487');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="92",
      instruction="Authenticate me as William Thompson with zip 98019 and BowlerID 27. Once confirmed, archive my bowling score for GameNumber 3, MatchID 20 by moving it from Bowler_Scores to Bowler_Scores_Archive and delete it from Bowler_Scores. Parameters: BowlerID=27, MatchID=20, GameNumber=3.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID, BowlerFirstName, BowlerLastName, BowlerZip FROM Bowlers WHERE BowlerID = 27 AND BowlerFirstName = 'William' AND BowlerLastName = 'Thompson' AND BowlerZip = '98019';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 20 AND GameNumber = 3 AND BowlerID = 27;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 20 AND GameNumber = 3 AND BowlerID = 27;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="93",
      instruction="As Suzanne Viescas (BowlerID: 20), I need to archive my records from the Totem Lanes tournament held on 2017-11-27 (TourneyID: 13). Please archive: 1) All my scores from MatchID 52 into the Bowler_Scores_Archive table, 2) All Match_Games records for MatchID 52 into the Match_Games_Archive table, 3) The tournament record for TourneyID 13 into the Tournaments_Archive table, and 4) The Tourney_Matches record for MatchID 52 and TourneyID 13 into the Tourney_Matches_Archive table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID = 20 AND MatchID = 52;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive (MatchID, GameNumber, WinningTeamID) SELECT MatchID, GameNumber, WinningTeamID FROM Match_Games WHERE MatchID = 52;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tournaments_Archive (TourneyID, TourneyDate, TourneyLocation) SELECT TourneyID, TourneyDate, TourneyLocation FROM Tournaments WHERE TourneyID = 13;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tourney_Matches_Archive (MatchID, TourneyID, Lanes, OddLaneTeamID, EvenLaneTeamID) SELECT MatchID, TourneyID, Lanes, OddLaneTeamID, EvenLaneTeamID FROM Tourney_Matches WHERE MatchID = 52 AND TourneyID = 13;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="94",
      instruction="Hello, I'm Ann K. Patterson at 16 Maple Lane, Auburn, WA, 98002, with BowlerID 5. Could you please verify my identity first? After that, for MatchID 14 and GameNumber 3, my raw score shows 142 but should be 150. Archive the current score, then update it to 150 while keeping my original HandiCapScore and WonGame status unchanged.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerFirstName = 'Ann' AND BowlerMiddleInit = 'K' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002' AND BowlerID = 5;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 14 AND GameNumber = 3 AND BowlerID = 5;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 150 WHERE MatchID = 14 AND GameNumber = 3 AND BowlerID = 5;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="95",
      instruction="Hello, I'm Maria Patterson with BowlerID 34. I've moved to 321 Cedar Avenue, Tacoma, WA, 98402. Please update my address. Additionally, for my team, the Manatees (TeamID 7), assign BowlerID 28 as the new captain.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 34 AND BowlerFirstName = 'Maria' AND BowlerLastName = 'Patterson'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerAddress = '321 Cedar Avenue', BowlerCity = 'Tacoma', BowlerState = 'WA', BowlerZip = '98402' WHERE BowlerID = 34"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Teams SET CaptainID = 28 WHERE TeamID = 7"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="96",
      instruction="Hello, I'm Caleb Viescas with BowlerID 23. Please archive all my bowling score records from matches held at 'Bolero Lanes' location. After archiving, remove these records from the active Bowler_Scores table. Finally, update my current handicap to 30 in the Bowlers table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID=23 AND BowlerLastName='Viescas' AND BowlerFirstName='Caleb';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID=tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID=t.TourneyID WHERE bs.BowlerID=23 AND t.TourneyLocation='Bolero Lanes';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID=23 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm INNER JOIN Tournaments t ON tm.TourneyID=t.TourneyID WHERE t.TourneyLocation='Bolero Lanes');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerCurrentHcp=30 WHERE BowlerID=23;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="98",
      instruction="My name is Kathryn Patterson and I currently reside at 16 Maple Lane, Auburn, WA 98002. Please update my bowler profile address to 504 Poplar Street, Auburn, WA 98002. Additionally, archive and remove my erroneous scores for MatchID 6, GameNumbers 2 and 3 from the active records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT bs.* FROM Bowler_Scores bs JOIN Bowlers b ON bs.BowlerID = b.BowlerID WHERE b.BowlerFirstName = 'Kathryn' AND b.BowlerLastName = 'Patterson' AND b.BowlerAddress = '16 Maple Lane' AND b.BowlerCity = 'Auburn' AND b.BowlerState = 'WA' AND b.BowlerZip = '98002' AND bs.MatchID = 6 AND bs.GameNumber IN (2, 3)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE EXISTS (SELECT 1 FROM Bowlers b WHERE b.BowlerID = Bowler_Scores.BowlerID AND b.BowlerFirstName = 'Kathryn' AND b.BowlerLastName = 'Patterson' AND b.BowlerAddress = '16 Maple Lane' AND b.BowlerCity = 'Auburn' AND b.BowlerState = 'WA' AND b.BowlerZip = '98002') AND MatchID = 6 AND GameNumber IN (2, 3)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerAddress = '504 Poplar Street', BowlerCity = 'Auburn', BowlerState = 'WA', BowlerZip = '98002' WHERE BowlerFirstName = 'Kathryn' AND BowlerLastName = 'Patterson' AND BowlerAddress = '16 Maple Lane' AND BowlerCity = 'Auburn' AND BowlerState = 'WA' AND BowlerZip = '98002'"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="100",
      instruction="Authenticate me: I am Stephanie Viescas with BowlerID 8. After authentication, for MatchID 30 and GameNumber 2, update my RawScore in Bowler_Scores to 155. Before updating, archive the current record (MatchID 30, GameNumber 2, BowlerID 8) from Bowler_Scores into Bowler_Scores_Archive.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID, BowlerFirstName, BowlerLastName FROM Bowlers WHERE BowlerID = 8;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 30 AND GameNumber = 2 AND BowlerID = 8;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 155 WHERE MatchID = 30 AND GameNumber = 2 AND BowlerID = 8;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5",
      instruction="I am Ann K Patterson (BowlerID 5). Please move all my scores from matches at 'Imperial Lanes' to Bowler_Scores_Archive and delete them from Bowler_Scores. Confirm archiving and deletion for BowlerID=5 and TourneyLocation='Imperial Lanes'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT BS.MatchID, BS.GameNumber, BS.BowlerID, BS.RawScore, BS.HandiCapScore, BS.WonGame FROM Bowler_Scores BS INNER JOIN Tourney_Matches TM ON BS.MatchID = TM.MatchID INNER JOIN Tournaments T ON TM.TourneyID = T.TourneyID WHERE BS.BowlerID = 5 AND T.TourneyLocation = 'Imperial Lanes';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 5 AND MatchID IN (SELECT TM.MatchID FROM Tourney_Matches TM INNER JOIN Tournaments T ON TM.TourneyID = T.TourneyID WHERE T.TourneyLocation = 'Imperial Lanes');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="15",
      instruction="I am Kathryn Patterson, BowlerID 15. Please verify my identity using my phone number (206) 555-3487. Then, archive my bowling score for MatchID=2, GameNumber=2 where RawScore=155, HandiCapScore=189, and WonGame=0. Also archive the related match result for MatchID=2, GameNumber=2 where WinningTeamID=4.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 15 AND BowlerPhoneNumber = '(206) 555-3487';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID=2 AND GameNumber=2 AND BowlerID=15 AND RawScore=155 AND HandiCapScore=189 AND WonGame=0;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID=2 AND GameNumber=2 AND BowlerID=15 AND RawScore=155 AND HandiCapScore=189 AND WonGame=0;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive (MatchID, GameNumber, WinningTeamID) SELECT MatchID, GameNumber, WinningTeamID FROM Match_Games WHERE MatchID=2 AND GameNumber=2 AND WinningTeamID=4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE MatchID=2 AND GameNumber=2 AND WinningTeamID=4;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="109",
      instruction="I am Kendra Hernandez (BowlerID 17). Please archive all my bowling records from tournaments at 'Bolero Lanes', specifically TourneyID 3 and 10. Include my MatchID 12 (GameNumbers 1,2,3) and MatchID 37 (GameNumbers 1,2,3). Move corresponding records for these items from: 1. Bowler_Scores to Bowler_Scores_Archive2. Match_Games to Match_Games_Archive3. Tournaments to Tournaments_Archive4. Tourney_Matches to Tourney_Matches_Archive",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT * FROM Bowler_Scores WHERE (MatchID=12 AND GameNumber IN (1,2,3) AND BowlerID=17) OR (MatchID=37 AND GameNumber IN (1,2,3) AND BowlerID=17);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE (MatchID=12 AND GameNumber IN (1,2,3) AND BowlerID=17) OR (MatchID=37 AND GameNumber IN (1,2,3) AND BowlerID=17);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive SELECT * FROM Match_Games WHERE (MatchID=12 AND GameNumber IN (1,2,3)) OR (MatchID=37 AND GameNumber IN (1,2,3));"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE (MatchID=12 AND GameNumber IN (1,2,3)) OR (MatchID=37 AND GameNumber IN (1,2,3));"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tourney_Matches_Archive SELECT * FROM Tourney_Matches WHERE MatchID IN (12,37);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Tourney_Matches WHERE MatchID IN (12,37);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tournaments_Archive SELECT * FROM Tournaments WHERE TourneyID IN (3,10);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Tournaments WHERE TourneyID IN (3,10);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="110",
      instruction="I am John L Viescas (BowlerID 19). Archive all my match records from tournament TourneyID 11 held at 'Imperial Lanes' by moving my Bowler_Scores entries to Bowler_Scores_Archive and deleting them from Bowler_Scores. Ensure this only affects BowlerID 19, TourneyID 11, and the location 'Imperial Lanes'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyID = 11 AND t.TourneyLocation = 'Imperial Lanes' AND bs.BowlerID = 19"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 19 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyID = 11 AND t.TourneyLocation = 'Imperial Lanes')"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="111",
      instruction="Hello, I am Ben Clothier with BowlerID 31. Please verify my identity. I need to correct my score for MatchID 16, GameNumber 3 at Imperial Lanes on 2017-09-25. The recorded RawScore is 149, but it should be 159. The old record includes HandiCapScore 186 and WonGame 0. Please archive the original record first, then update the RawScore to 159 while keeping HandiCapScore and WonGame unchanged.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 31 AND BowlerFirstName = 'Ben' AND BowlerLastName = 'Clothier';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 16 AND GameNumber = 3 AND BowlerID = 31 AND RawScore = 149 AND HandiCapScore = 186 AND WonGame = 0;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 159 WHERE MatchID = 16 AND GameNumber = 3 AND BowlerID = 31 AND RawScore = 149 AND HandiCapScore = 186 AND WonGame = 0;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="112",
      instruction="You are Barbara Fournier from ZIP code 98014. You want to archive all your bowling scores (all games, all match numbers) from the tournament with TourneyID 11 held at 'Imperial Lanes' on '2017-11-13' into the Bowler_Scores_Archive table. Archive all your scores using your BowlerID (derived from BowlerLastName 'Fournier', BowlerFirstName 'Barbara', and BowlerZip '98014') and all MatchIDs associated with TourneyID 11.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerLastName = 'Fournier' AND BowlerFirstName = 'Barbara' AND BowlerZip = '98014';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerLastName = 'Fournier' AND BowlerFirstName = 'Barbara' AND BowlerZip = '98014' LIMIT 1) AND MatchID IN (SELECT MatchID FROM Tourney_Matches WHERE TourneyID = 11);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="113",
      instruction="I am William G Thompson, BowlerID 27. My details are: first name 'William', middle initial 'G', last name 'Thompson', address '122 Spring Valley Drive', city 'Duvall', state 'WA', zip '98019', and TeamID 7. Authenticate me, then update my bowling scores for MatchID 31, GameNumber 2 to RawScore 197 and HandiCapScore 229.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 27 AND BowlerFirstName = 'William' AND BowlerMiddleInit = 'G' AND BowlerLastName = 'Thompson' AND BowlerAddress = '122 Spring Valley Drive' AND BowlerCity = 'Duvall' AND BowlerState = 'WA' AND BowlerZip = '98019' AND TeamID = 7;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 197, HandiCapScore = 229 WHERE MatchID = 31 AND GameNumber = 2 AND BowlerID = 27;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="115",
      instruction="Hi, I'm Bailey Hallmark from Woodinville, WA, currently bowling on the Swordfish team. I want to archive all my bowling scores from matches played on October 9, 2017, at Totem Lanes by moving them to Bowler_Scores_Archive and removing them from Bowler_Scores.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Bailey' AND BowlerLastName = 'Hallmark' AND BowlerCity = 'Woodinville' AND BowlerState = 'WA';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID INNER JOIN Bowlers b ON bs.BowlerID = b.BowlerID WHERE b.BowlerFirstName = 'Bailey' AND b.BowlerLastName = 'Hallmark' AND b.BowlerCity = 'Woodinville' AND b.BowlerState = 'WA' AND t.TourneyDate = '2017-10-09' AND t.TourneyLocation = 'Totem Lanes';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE (MatchID, GameNumber, BowlerID) IN (SELECT bs.MatchID, bs.GameNumber, bs.BowlerID FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID INNER JOIN Bowlers b ON bs.BowlerID = b.BowlerID WHERE b.BowlerFirstName = 'Bailey' AND b.BowlerLastName = 'Hallmark' AND b.BowlerCity = 'Woodinville' AND b.BowlerState = 'WA' AND t.TourneyDate = '2017-10-09' AND t.TourneyLocation = 'Totem Lanes');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="116",
      instruction="I am Ben Clothier with zip code 98033. Please archive all my match score records from tournaments held at 'Bolero Lanes' by moving them from Bowler_Scores to Bowler_Scores_Archive.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Ben' AND BowlerLastName = 'Clothier' AND BowlerZip = '98033';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE bs.BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Ben' AND BowlerLastName = 'Clothier' AND BowlerZip = '98033') AND t.TourneyLocation = 'Bolero Lanes';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Ben' AND BowlerLastName = 'Clothier' AND BowlerZip = '98033') AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Bolero Lanes');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="34",
      instruction="I am Maria Patterson from Auburn, WA, and my BowlerID is 34. I bowl for Team 7. I just bowled Game 1 in MatchID 501. My raw score was 178, handicap score 192, and I won. Please add this score and update my bowler record by setting BowlerTotalPins to 178, BowlerGamesBowled to 1, and BowlerCurrentAverage to 178.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerFirstName, BowlerLastName, BowlerCity, TeamID FROM Bowlers WHERE BowlerID = 34;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (501, 1, 34, 178, 192, TRUE);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerTotalPins = 178, BowlerGamesBowled = 1, BowlerCurrentAverage = 178 WHERE BowlerID = 34;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="118",
      instruction="Hello, I am Elizabeth Hallmark with BowlerID 13. For record-keeping purposes, I request the following: First, archive all my existing bowling scores. Second, remove these scores from the active Bowler_Scores table. Finally, insert a corrected score entry for MatchID 44, GameNumber 2 with RawScore 158, HandiCapScore 201, and WonGame status 0. Ensure only this corrected record remains in active storage afterward. Use BowlerID 13 for all steps.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID = 13;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 13;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (44, 2, 13, 158, 201, 0);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="119",
      instruction="I am Kerry Patterson (BowlerID 33) and I confirm I am currently on the Manatees team (TeamID 7). Please authenticate my identity, then process my resignation by removing me from the team, deleting all my bowling score records from current and archive tables, and show my updated profile to confirm.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 33 AND BowlerFirstName = 'Kerry' AND BowlerLastName = 'Patterson' AND TeamID = 7;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET TeamID = NULL WHERE BowlerID = 33;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 33;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores_Archive WHERE BowlerID = 33;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 33;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="120",
      instruction="Hello, I am Sara J Sheskey with BowlerID 4. Please verify my identity. Due to a scorekeeping error, I need to archive my last three games from MatchID 53, specifically GameNumbers 1, 2, and 3. Move these records from the Bowler_Scores table to the Bowler_Scores_Archive table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerFirstName, BowlerLastName FROM Bowlers WHERE BowlerID = 4;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 53 AND BowlerID = 4 AND GameNumber IN (1, 2, 3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 53 AND BowlerID = 4 AND GameNumber IN (1, 2, 3);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5",
      instruction="I am Ann Patterson. My phone number is (206) 555-3487. Please verify my identity for BowlerID 5. Once confirmed, archive all my match scores for games held at 'Thunderbird Lanes' in 2017 by moving them from Bowler_Scores to Bowler_Scores_Archive, then delete those records from Bowler_Scores.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 5 AND BowlerFirstName = 'Ann' AND BowlerLastName = 'Patterson' AND BowlerPhoneNumber = '(206) 555-3487';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE bs.BowlerID = 5 AND t.TourneyLocation = 'Thunderbird Lanes' AND strftime('%Y', t.TourneyDate) = '2017';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 5 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Thunderbird Lanes' AND strftime('%Y', t.TourneyDate) = '2017');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="125",
      instruction="I'm David Cunningham (BowlerID: 10). For MatchID 33, GameNumber 3, my bowling scores were recorded wrong. Could you please verify my identity, archive the original record, then update it to RawScore=159, HandiCapScore=195, and mark WonGame as TRUE?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 10 AND BowlerFirstName = 'David' AND BowlerLastName = 'Cunningham';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 33 AND GameNumber = 3 AND BowlerID = 10;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 159, HandiCapScore = 195, WonGame = 1 WHERE MatchID = 33 AND GameNumber = 3 AND BowlerID = 10;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="126",
      instruction="Hello, my name is Stephanie Viescas and my zip code is 98052. Please archive all my bowling scores for games played at Bolero Lanes, remove them from active records, and update my bowler profile to set my current average to 135.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Bolero Lanes' AND bs.BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Stephanie' AND BowlerLastName = 'Viescas' AND BowlerZip = '98052');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Stephanie' AND BowlerLastName = 'Viescas' AND BowlerZip = '98052') AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Bolero Lanes');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowlers SET BowlerCurrentAverage = 135 WHERE BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Stephanie' AND BowlerLastName = 'Viescas' AND BowlerZip = '98052');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="128",
      instruction="I am William G Thompson (BowlerID: 27). Authenticate my identity, then archive and remove my Bowler_Scores records for these games: MatchID=7, GameNumber=1; MatchID=7, GameNumber=2; and MatchID=35, GameNumber=2. After removal, update my game (MatchID=50, GameNumber=3) to set HandiCapScore to 225.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID, BowlerFirstName, BowlerLastName, BowlerMiddleInit FROM Bowlers WHERE BowlerID = 27;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE (MatchID=7 AND GameNumber=1 AND BowlerID=27) OR (MatchID=7 AND GameNumber=2 AND BowlerID=27) OR (MatchID=35 AND GameNumber=2 AND BowlerID=27);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE (MatchID=7 AND GameNumber=1 AND BowlerID=27) OR (MatchID=7 AND GameNumber=2 AND BowlerID=27) OR (MatchID=35 AND GameNumber=2 AND BowlerID=27);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET HandiCapScore=225 WHERE MatchID=50 AND GameNumber=3 AND BowlerID=27;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="129",
      instruction="Hello, I'm Elizabeth Hallmark from Woodinville, WA (Bowler ID 13). I need to correct a score entry error for my match at Thunderbird Lanes on October 30, 2017. For Match ID 34, Game 3, my RawScore was recorded as 156, but the correct score is 159. Please update only my RawScore to 159 for that specific game.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 159 WHERE BowlerID = 13 AND MatchID = 34 AND GameNumber = 3;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="132",
      instruction="My BowlerID is 2, and I am David Fournier (first name: David, last name: Fournier) residing at 67 Willow Drive, Bothell, WA. I need to correct an error in my bowling record for MatchID 17, GameNumber 3 played on October 2, 2017. The original record shows RawScore: 173, HandiCapScore: 214, and WonGame: 1. However, the HandiCapScore should be 210. Please verify my identity using my provided details, confirm the existing record matches these specifics, then archive the original entry in Bowler_Scores_Archive and update the HandiCapScore to 210 in Bowler_Scores.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID = 2 AND MatchID = 17 AND GameNumber = 3 AND RawScore = 173 AND HandiCapScore = 214 AND WonGame = 1 AND EXISTS (SELECT 1 FROM Bowlers WHERE BowlerID = 2 AND BowlerFirstName = 'David' AND BowlerLastName = 'Fournier' AND BowlerAddress = '67 Willow Drive' AND BowlerCity = 'Bothell' AND BowlerState = 'WA');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET HandiCapScore = 210 WHERE BowlerID = 2 AND MatchID = 17 AND GameNumber = 3 AND RawScore = 173 AND HandiCapScore = 214 AND WonGame = 1 AND EXISTS (SELECT 1 FROM Bowlers WHERE BowlerID = 2 AND BowlerFirstName = 'David' AND BowlerLastName = 'Fournier' AND BowlerAddress = '67 Willow Drive' AND BowlerCity = 'Bothell' AND BowlerState = 'WA');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="133",
      instruction="Hello, my name is Carol M. Viescas and my home address is 16345 NE 32nd Street, Bellevue, WA 98004. Please authenticate me. Once confirmed, I request archiving for my three oldest bowling matches: MatchID 2, MatchID 5, and MatchID 9. This includes moving records from Bowler_Scores, Match_Games, and Tourney_Matches to their archive tables, and moving tournaments with TourneyID 1, 2, and 3 to Tournaments_Archive. Subsequently, remove all these entries from the main tables.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Carol' AND BowlerMiddleInit = 'M' AND BowlerLastName = 'Viescas' AND BowlerAddress = '16345 NE 32nd Street' AND BowlerCity = 'Bellevue' AND BowlerState = 'WA' AND BowlerZip = '98004';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT * FROM Bowler_Scores WHERE BowlerID = 12 AND (MatchID = 2 OR MatchID = 5 OR MatchID = 9);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 12 AND (MatchID = 2 OR MatchID = 5 OR MatchID = 9);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive SELECT * FROM Match_Games WHERE (MatchID = 2 OR MatchID = 5 OR MatchID = 9);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE (MatchID = 2 OR MatchID = 5 OR MatchID = 9);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tourney_Matches_Archive SELECT * FROM Tourney_Matches WHERE (MatchID = 2 OR MatchID = 5 OR MatchID = 9);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Tourney_Matches WHERE (MatchID = 2 OR MatchID = 5 OR MatchID = 9);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tournaments_Archive SELECT * FROM Tournaments WHERE (TourneyID = 1 OR TourneyID = 2 OR TourneyID = 3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Tournaments WHERE (TourneyID = 1 OR TourneyID = 2 OR TourneyID = 3);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="134",
      instruction="Hello, I'm Ben Clothier (Bowler ID: 31) living at 722 Moss Bay Blvd., Kirkland, WA 98033. Please archive my three game records from Match ID 56: Game 1, Game 2, and Game 3. Move them from Bowler_Scores to Bowler_Scores_Archive, then confirm they exist in the archive and are removed from the active scores.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 31 AND BowlerLastName = 'Clothier' AND BowlerFirstName = 'Ben' AND BowlerAddress = '722 Moss Bay Blvd.' AND BowlerCity = 'Kirkland' AND BowlerState = 'WA' AND BowlerZip = '98033';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 56 AND BowlerID = 31 AND GameNumber IN (1, 2, 3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 56 AND BowlerID = 31 AND GameNumber IN (1, 2, 3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowler_Scores_Archive WHERE MatchID = 56 AND BowlerID = 31 AND GameNumber IN (1, 2, 3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowler_Scores WHERE MatchID = 56 AND BowlerID = 31 AND GameNumber IN (1, 2, 3);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="137",
      instruction="I am Bailey Hallmark, living at Route 2, Box 203B, Woodinville, WA 98072, and my BowlerID is 29. For recordkeeping, please move all my bowling scores from tournament games held at 'Thunderbird Lanes' from the Bowler_Scores table to the Bowler_Scores_Archive table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 29 AND BowlerFirstName = 'Bailey' AND BowlerLastName = 'Hallmark' AND BowlerAddress = 'Route 2, Box 203B' AND BowlerCity = 'Woodinville' AND BowlerState = 'WA' AND BowlerZip = '98072';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs INNER JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE bs.BowlerID = 29 AND t.TourneyLocation = 'Thunderbird Lanes';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 29 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm INNER JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Thunderbird Lanes');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="138",
      instruction="Hello, my name is Bailey Hallmark and I live at Route 2, Box 203B. I recently had a scoring dispute resolved for MatchID 47 and Game 1. Please archive both my individual performance for that game and the overall match result, and then remove these records from the main tables.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Bailey' AND BowlerLastName = 'Hallmark' AND BowlerAddress = 'Route 2, Box 203B';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 47 AND GameNumber = 1 AND BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Bailey' AND BowlerLastName = 'Hallmark' AND BowlerAddress = 'Route 2, Box 203B');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive (MatchID, GameNumber, WinningTeamID) SELECT MatchID, GameNumber, WinningTeamID FROM Match_Games WHERE MatchID = 47 AND GameNumber = 1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 47 AND GameNumber = 1 AND BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Bailey' AND BowlerLastName = 'Hallmark' AND BowlerAddress = 'Route 2, Box 203B');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE MatchID = 47 AND GameNumber = 1;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="139",
      instruction="My name is Suzanne Viescas, residing at 218 Main Street, Redmond, WA 98052. I recently noticed that my score for MatchID 55, GameNumber 2 (Acapulco Lanes tournament, TourneyID 14) was incorrectly recorded as 144. Please update it to 150. Additionally, archive all match results for TourneyID 14 for my user account—move them from Bowler_Scores to Bowler_Scores_Archive and remove them from Bowler_Scores after archiving.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Suzanne' AND BowlerLastName = 'Viescas' AND BowlerAddress = '218 Main Street' AND BowlerCity = 'Redmond' AND BowlerState = 'WA' AND BowlerZip = '98052';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 150 WHERE BowlerID IN (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Suzanne' AND BowlerLastName = 'Viescas' AND BowlerAddress = '218 Main Street' AND BowlerCity = 'Redmond' AND BowlerState = 'WA' AND BowlerZip = '98052') AND MatchID = 55 AND GameNumber = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT * FROM Bowler_Scores WHERE BowlerID IN (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Suzanne' AND BowlerLastName = 'Viescas' AND BowlerAddress = '218 Main Street' AND BowlerCity = 'Redmond' AND BowlerState = 'WA' AND BowlerZip = '98052') AND MatchID IN (SELECT MatchID FROM Tourney_Matches WHERE TourneyID = 14);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID IN (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Suzanne' AND BowlerLastName = 'Viescas' AND BowlerAddress = '218 Main Street' AND BowlerCity = 'Redmond' AND BowlerState = 'WA' AND BowlerZip = '98052') AND MatchID IN (SELECT MatchID FROM Tourney_Matches WHERE TourneyID = 14);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22",
      instruction="Hi, I'm Alaina Hallmark with BowlerID 22 from Team 6. My zip code is 98072. I spotted an error in my tournament record for MatchID 35, GameNumber 2—the RawScore shows 155 instead of the correct 165. Could you please update it to 165?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 22 AND BowlerLastName = 'Hallmark' AND BowlerFirstName = 'Alaina' AND TeamID = 6 AND BowlerZip = '98072';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 165 WHERE BowlerID = 22 AND MatchID = 35 AND GameNumber = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="141",
      instruction="Hello, I'm Caleb Viescas (BowlerID 23). On October 16, 2017, at Acapulco Lanes, I bowled a RawScore of 179 in MatchID 27, GameNumber 2. I need this performance permanently archived and removed from active stats. Please archive and delete both my individual score record and the full match game record for this entry. Here are the exact parameters: BowlerID 23, MatchID 27, GameNumber 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 27 AND GameNumber = 2 AND BowlerID = 23;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 27 AND GameNumber = 2 AND BowlerID = 23;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive (MatchID, GameNumber, WinningTeamID) SELECT MatchID, GameNumber, WinningTeamID FROM Match_Games WHERE MatchID = 27 AND GameNumber = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE MatchID = 27 AND GameNumber = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="142",
      instruction="I am Richard Sheskey, BowlerID 16. I need to archive my score for MatchID 6 and GameNumber 1 by moving it from the Bowler_Scores table to the Bowler_Scores_Archive table. Additionally, I found an error in my score for MatchID 44, GameNumber 2 and need to update the RawScore to 150 in the Bowler_Scores table while keeping other fields unchanged.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID=16 AND MatchID=6 AND GameNumber=1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID=16 AND MatchID=6 AND GameNumber=1;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore=150 WHERE BowlerID=16 AND MatchID=44 AND GameNumber=2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="144",
      instruction="I am Ann K Patterson, living in zip code 98002. Archive my score records for MatchID 6, GameNumber 1 and GameNumber 2, to move them from current season stats to the archive.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Ann' AND BowlerLastName = 'Patterson' AND BowlerMiddleInit = 'K' AND BowlerZip = '98002'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Bowlers b ON bs.BowlerID = b.BowlerID WHERE b.BowlerFirstName = 'Ann' AND b.BowlerLastName = 'Patterson' AND b.BowlerMiddleInit = 'K' AND b.BowlerZip = '98002' AND bs.MatchID = 6 AND bs.GameNumber IN (1, 2)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE EXISTS (SELECT 1 FROM Bowlers b WHERE b.BowlerID = Bowler_Scores.BowlerID AND b.BowlerFirstName = 'Ann' AND b.BowlerLastName = 'Patterson' AND b.BowlerMiddleInit = 'K' AND b.BowlerZip = '98002') AND MatchID = 6 AND GameNumber IN (1, 2)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="146",
      instruction="Please verify my identity: I am Karen Lim, BowlerID 28, residing at 218 Main Street, Redmond, WA 98052, and captain of the Manatees team (TeamID 7). Once confirmed, update my scores for MatchID 15 in the Imperial Lanes tournament (TourneyID 4) as follows: for GameNumber 2, set RawScore to 145, HandiCapScore to 196, and WonGame to 1; for GameNumber 3, set RawScore to 144, HandiCapScore to 195, and WonGame to 1.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT 1 FROM Bowlers b JOIN Teams t ON b.TeamID = t.TeamID WHERE b.BowlerID = 28 AND b.BowlerLastName = 'Lim' AND b.BowlerFirstName = 'Karen' AND b.BowlerAddress = '218 Main Street' AND b.BowlerCity = 'Redmond' AND b.BowlerState = 'WA' AND b.BowlerZip = '98052' AND t.TeamID = 7 AND t.CaptainID = 28;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 145, HandiCapScore = 196, WonGame = 1 WHERE MatchID = 15 AND GameNumber = 2 AND BowlerID = 28;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 144, HandiCapScore = 195, WonGame = 1 WHERE MatchID = 15 AND GameNumber = 3 AND BowlerID = 28;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="148",
      instruction="I am Michael Hernandez with BowlerID 18. Please verify my identity. Then, for the game I played on MatchID 28, GameNumber 2 at Acapulco Lanes on 2017-10-16, update my RawScore to 185. Before updating, archive the existing Bowler_Scores record in Bowler_Scores_Archive.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID=18 AND BowlerFirstName='Michael' AND BowlerLastName='Hernandez';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE BowlerID=18 AND MatchID=28 AND GameNumber=2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore=185 WHERE BowlerID=18 AND MatchID=28 AND GameNumber=2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="150",
      instruction="I am Sarah Thompson (BowlerID 24) and need to retire due to a wrist injury. Please archive my tournament participation record for TourneyID 14 held at Acapulco Lanes on 2017-12-04. Specifically: archive all Bowler_Scores records for BowlerID 24 and MatchID 55; archive all Match_Games records for MatchID 55; and archive the Tournaments record for TourneyID 14. Move these to their respective archive tables and delete them from the main tables. Ensure my other scores and matches remain active.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 55 AND BowlerID = 24;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 55 AND BowlerID = 24;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive (MatchID, GameNumber, WinningTeamID) SELECT MatchID, GameNumber, WinningTeamID FROM Match_Games WHERE MatchID = 55;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE MatchID = 55;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tournaments_Archive (TourneyID, TourneyDate, TourneyLocation) SELECT TourneyID, TourneyDate, TourneyLocation FROM Tournaments WHERE TourneyID = 14;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Tournaments WHERE TourneyID = 14;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="153",
      instruction="I am BowlerID 5, Ann K. Patterson. My raw score for MatchID 26, GameNumber 2 was recorded as 139 but should be 149. Please create a backup of the current record in Bowler_Scores_Archive for auditing, then update only the RawScore to 149 in the Bowler_Scores table while retaining the original HandiCapScore and WonGame values.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 26 AND GameNumber = 2 AND BowlerID = 5;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 149 WHERE MatchID = 26 AND GameNumber = 2 AND BowlerID = 5;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="154",
      instruction="I am Bailey Hallmark (BowlerID: 29, TeamID: 8). Please archive the following two Bowler_Scores records for me: first, MatchID 8, GameNumber 2, RawScore 156, HandiCapScore 203, WonGame 1; second, MatchID 19, GameNumber 1, RawScore 144, HandiCapScore 191, WonGame 1. Move both records from Bowler_Scores to Bowler_Scores_Archive.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID, BowlerFirstName, BowlerLastName, TeamID FROM Bowlers WHERE BowlerID = 29;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (8, 2, 29, 156, 203, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 8 AND GameNumber = 2 AND BowlerID = 29;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (19, 1, 29, 144, 191, 1);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 19 AND GameNumber = 1 AND BowlerID = 29;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="156",
      instruction="Hello, my name is David Cunningham and my BowlerID is 10. I need to correct an error in my bowling records for MatchID 19, GameNumber 2. A score of RawScore 161 (HandiCapScore 197, WonGame 0) was recorded under my name on 2017-10-02 at Sports World Lanes, but it belongs to my teammate. Please archive this record first to preserve it, then remove it from my current Bowler_Scores to update my stats. The full record to archive and delete is: MatchID 19, GameNumber 2, BowlerID 10, RawScore 161, HandiCapScore 197, WonGame 0.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 10 AND BowlerLastName = 'Cunningham' AND BowlerFirstName = 'David';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) VALUES (19, 2, 10, 161, 197, 0);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 19 AND GameNumber = 2 AND BowlerID = 10 AND RawScore = 161 AND HandiCapScore = 197 AND WonGame = 0;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="157",
      instruction="I am Ben Clothier, BowlerID 31, with address 722 Moss Bay Blvd., Kirkland, WA 98033. Please authenticate me first. Once confirmed, update my game result for MatchID 47 and GameNumber 2 to RawScore 192, HandiCapScore 227, and keep WonGame as 1.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT 1 FROM Bowlers WHERE BowlerID = 31 AND BowlerFirstName = 'Ben' AND BowlerLastName = 'Clothier' AND BowlerAddress = '722 Moss Bay Blvd.' AND BowlerCity = 'Kirkland' AND BowlerState = 'WA' AND BowlerZip = '98033';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 192, HandiCapScore = 227, WonGame = 1 WHERE MatchID = 47 AND GameNumber = 2 AND BowlerID = 31;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="158",
      instruction="Hello, I'm Ben Clothier with BowlerID 31. Since I'm leaving Swordfish soon, could you archive all my bowling scores from matches hosted at Bolero Lanes? After archiving, please permanently remove those records from the Bowler_Scores table. Ensure both steps use my BowlerID 31 and specifically target Bolero Lanes matches only.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Bolero Lanes' AND bs.BowlerID = 31;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyLocation = 'Bolero Lanes') AND BowlerID = 31;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="163",
      instruction="Hello, my name is David Cunningham and my BowlerID is 10. I need to correct a scoring error from MatchID 9, GameNumber 2. The recorded raw score is 167, but my actual score was 170. Please update it to 170.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowlers WHERE BowlerID = 10 AND BowlerFirstName = 'David' AND BowlerLastName = 'Cunningham';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 170 WHERE MatchID = 9 AND GameNumber = 2 AND BowlerID = 10;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="164",
      instruction="I am Bailey Hallmark (BowlerID 29) from Woodinville, WA 98072. Before my team's stats review, archive my three lowest RawScores from TourneyID 14 at Acapulco Lanes. Move these records from Bowler_Scores to Bowler_Scores_Archive. After archiving, list all my archived scores for TourneyID 14 to confirm.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID, BowlerFirstName, BowlerLastName, BowlerCity, BowlerState, BowlerZip FROM Bowlers WHERE BowlerID = 29;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BS.MatchID, BS.GameNumber, BS.BowlerID, BS.RawScore, BS.HandiCapScore, BS.WonGame FROM Bowler_Scores BS INNER JOIN Tourney_Matches TM ON BS.MatchID = TM.MatchID WHERE BS.BowlerID = 29 AND TM.TourneyID = 14 ORDER BY BS.RawScore ASC, BS.MatchID, BS.GameNumber LIMIT 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT BS.MatchID, BS.GameNumber, BS.BowlerID, BS.RawScore, BS.HandiCapScore, BS.WonGame FROM Bowler_Scores BS INNER JOIN Tourney_Matches TM ON BS.MatchID = TM.MatchID WHERE BS.BowlerID = 29 AND TM.TourneyID = 14 ORDER BY BS.RawScore ASC, BS.MatchID, BS.GameNumber LIMIT 3;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE (MatchID, GameNumber, BowlerID) IN (SELECT BS.MatchID, BS.GameNumber, BS.BowlerID FROM Bowler_Scores BS INNER JOIN Tourney_Matches TM ON BS.MatchID = TM.MatchID WHERE BS.BowlerID = 29 AND TM.TourneyID = 14 ORDER BY BS.RawScore ASC, BS.MatchID, BS.GameNumber LIMIT 3);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Bowler_Scores_Archive WHERE BowlerID = 29 AND MatchID IN (SELECT MatchID FROM Tourney_Matches WHERE TourneyID = 14);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="167",
      instruction="You're Zachary Ehrlich (BowlerID 21, Team Orcas, from Seattle zip 98122) and have decided to retire from the bowling league. You want every record associated with your matches archived: First, move all your bowler scores (identified by BowlerID 21) from Bowler_Scores to Bowler_Scores_Archive. Second, move all match games corresponding to your MatchIDs (derived from your scores) to Match_Games_Archive. Third, move all tournament matches for those same MatchIDs to Tourney_Matches_Archive. Finally, delete your original bowler scores, the archived match games, the archived tournament matches, and your bowler profile (BowlerID 21) from the Bowlers table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT * FROM Bowler_Scores WHERE BowlerID = 21;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive SELECT * FROM Match_Games WHERE MatchID IN (SELECT DISTINCT MatchID FROM Bowler_Scores_Archive WHERE BowlerID = 21);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Tourney_Matches_Archive SELECT * FROM Tourney_Matches WHERE MatchID IN (SELECT DISTINCT MatchID FROM Bowler_Scores_Archive WHERE BowlerID = 21);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 21;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE MatchID IN (SELECT DISTINCT MatchID FROM Bowler_Scores_Archive WHERE BowlerID = 21);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Tourney_Matches WHERE MatchID IN (SELECT DISTINCT MatchID FROM Bowler_Scores_Archive WHERE BowlerID = 21);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowlers WHERE BowlerID = 21;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="169",
      instruction="I am Joe Rosales (BowlerID 32). Please update my Game 2 scores for MatchID 56 at Acapulco Lanes: set RawScore to 144 and HandiCapScore to 196. Then, archive all my bowling score records from tournament matches held before October 1, 2017 by moving them from Bowler_Scores to Bowler_Scores_Archive, and delete them from Bowler_Scores. I want to maintain a neat and accurate record.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET RawScore = 144, HandiCapScore = 196 WHERE MatchID = 56 AND GameNumber = 2 AND BowlerID = 32;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT bs.MatchID, bs.GameNumber, bs.BowlerID, bs.RawScore, bs.HandiCapScore, bs.WonGame FROM Bowler_Scores bs JOIN Tourney_Matches tm ON bs.MatchID = tm.MatchID JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE bs.BowlerID = 32 AND t.TourneyDate < '2017-10-01';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 32 AND MatchID IN (SELECT tm.MatchID FROM Tourney_Matches tm JOIN Tournaments t ON tm.TourneyID = t.TourneyID WHERE t.TourneyDate < '2017-10-01');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="170",
      instruction="My name is Gary Hallmark, living at Route 2, Box 203B, Woodinville, WA 98072. I want to archive all my scores from my oldest match, which was at Red Rooster Lanes on 2017-09-04 (TourneyID=1, MatchID=2). Please move all my Bowler_Scores for that match to Bowler_Scores_Archive, and also move the related Match_Games entries for MatchID=2 to Match_Games_Archive. After copying, remove those records from the original tables.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Gary' AND BowlerLastName = 'Hallmark' AND BowlerAddress = 'Route 2, Box 203B' AND BowlerCity = 'Woodinville' AND BowlerState = 'WA' AND BowlerZip = '98072';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive (MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame) SELECT MatchID, GameNumber, BowlerID, RawScore, HandiCapScore, WonGame FROM Bowler_Scores WHERE MatchID = 2 AND BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Gary' AND BowlerLastName = 'Hallmark' AND BowlerAddress = 'Route 2, Box 203B' AND BowlerCity = 'Woodinville' AND BowlerState = 'WA' AND BowlerZip = '98072');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE MatchID = 2 AND BowlerID = (SELECT BowlerID FROM Bowlers WHERE BowlerFirstName = 'Gary' AND BowlerLastName = 'Hallmark' AND BowlerAddress = 'Route 2, Box 203B' AND BowlerCity = 'Woodinville' AND BowlerState = 'WA' AND BowlerZip = '98072');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive (MatchID, GameNumber, WinningTeamID) SELECT MatchID, GameNumber, WinningTeamID FROM Match_Games WHERE MatchID = 2;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE MatchID = 2;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="171",
      instruction="My name is Ann K. Patterson, and my BowlerID is 5. I bowled in MatchID 53, GameNumber 1 at Acapulco Lanes (TourneyID 14). My HandiCapScore for that game was incorrectly entered as 196, but it should be 198. Please verify my identity and update my HandiCapScore for that specific game.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT BowlerID FROM Bowlers WHERE BowlerID = 5 AND BowlerFirstName = 'Ann' AND BowlerLastName = 'Patterson' AND BowlerMiddleInit = 'K';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Bowler_Scores SET HandiCapScore = 198 WHERE MatchID = 53 AND GameNumber = 1 AND BowlerID = 5;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="30",
      instruction="I am Rachel Patterson (BowlerID 30). I want to archive my three lowest scoring games to focus on future improvements. Please move the following games from the main tables into their respective archives: (1) MatchID 12, GameNumber 1; (2) MatchID 56, GameNumber 1; (3) MatchID 43, GameNumber 1. Ensure all related data from Bowler_Scores for my participation and from Match_Games for these specific games are transferred to Bowler_Scores_Archive and Match_Games_Archive, then remove them from the main tables.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Bowler_Scores_Archive SELECT * FROM Bowler_Scores WHERE BowlerID = 30 AND ((MatchID = 12 AND GameNumber = 1) OR (MatchID = 56 AND GameNumber = 1) OR (MatchID = 43 AND GameNumber = 1));"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Match_Games_Archive SELECT * FROM Match_Games WHERE ((MatchID = 12 AND GameNumber = 1) OR (MatchID = 56 AND GameNumber = 1) OR (MatchID = 43 AND GameNumber = 1));"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Bowler_Scores WHERE BowlerID = 30 AND ((MatchID = 12 AND GameNumber = 1) OR (MatchID = 56 AND GameNumber = 1) OR (MatchID = 43 AND GameNumber = 1));"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Match_Games WHERE ((MatchID = 12 AND GameNumber = 1) OR (MatchID = 56 AND GameNumber = 1) OR (MatchID = 43 AND GameNumber = 1));"
               }
            ),
       ],
       outputs=[]
   ),
]
