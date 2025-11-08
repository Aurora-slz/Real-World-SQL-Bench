from tau_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="0",
      instruction="Hi, I'm Kyle Wilson (ELITEID: 11750) and I need to update my draft information in the PlayerInfo record. Please change my draft round from 9 to 7 and update the 'overallby' team from 'Minnesota Wild' to 'Columbus Blue Jackets' for my player profile.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET draftround = 7, overallby = 'Columbus Blue Jackets' WHERE ELITEID = 11750;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1",
      instruction="I am Shane Sims (ELITEID 12278). Please create a new weight record with ID 197 containing 91 kg (200 lbs). Then update my PlayerInfo profile to link this new weight_id (197) as my current weight measurement.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO weight_info (weight_id, weight_in_kg, weight_in_lbs) VALUES (197, 91, 200);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 197 WHERE ELITEID = 12278;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2",
      instruction="This is Philippe Paquet (ELITEID 15055). Please process these updates to my player records: 1) Update draft round to 5 and overall draft pick to 190 in PlayerInfo for PlayerName 'Philippe Paquet' (ELITEID 15055). 2) Correct my height in the height_info table to 188 cm specifically for height_id 75. Confirmation details: ELITEID=15055, PlayerName=Philippe Paquet, new_draft_round=5, new_overall_pick=190, target_height_id=75, new_height_cm=188.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET draftround = 5, overall = 190 WHERE ELITEID = 15055 AND PlayerName = 'Philippe Paquet';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE height_info SET height_in_cm = 188 WHERE height_id = 75;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3",
      instruction="I am Nick Tuzzolino (ELITEID 11327). After an official measurement, please: 1) Add a new weight_info record with weight_id 228, 103 kg (228 lbs) 2) Update my PlayerInfo profile weight from 225 to 228 lbs using ELITEID 11327",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO weight_info (weight_id, weight_in_kg, weight_in_lbs) VALUES (228, 103, 228);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 228 WHERE ELITEID = 11327;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4",
      instruction="You are Jason Lynch (ELITEID: 11634). You found some mistakes in your profile and want them corrected: please update your height to height_id 77 (195 cm), your weight to weight_id 215 (100 kg), your draft round to 5, and your overall selection number to 150 in your PlayerInfo record. Confirm all parameters are explicitly provided for the database update.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET height = 77, weight = 215, draftround = 5, overall = 150 WHERE ELITEID = 11634"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6",
      instruction="My name is Tomas Linhart with ELITEID 15831. I authorize corrections to my PlayerInfo record: Update birthyear from 1983 to 1984, adjust height from 74 inches to 75 inches, and correct weight from 227 lbs to 220 lbs. Verify my identity using ELITEID 15831 before making changes.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET birthyear = 1984 WHERE ELITEID = 15831 AND birthyear = 1983"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET height = 75 WHERE ELITEID = 15831 AND height = 74"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 220 WHERE ELITEID = 15831 AND weight = 227"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="analytics_manager_1",
      instruction="Please execute these updates for Maxim Shchevyev (ELITEID 48284): 1) Insert new weight record with weight_id=202 containing 92kg/202lbs. 2) Update his PlayerInfo.weight to reference the new weight_id 202. 3) Add 2002-2003 season stats for Elektrostal in RUS-JR league (Regular Season): 12 GP, 3G, 7A, 10P, 6 PIM, +5. Confirm all values match exactly: SEASON='2002-2003', TEAM='Elektrostal', LEAGUE='RUS-JR', GAMETYPE='Regular Season'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO weight_info (weight_id, weight_in_kg, weight_in_lbs) VALUES (202, 92, 202);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 202 WHERE ELITEID = 48284;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (48284, '2002-2003', 'Elektrostal', 'RUS-JR', 'Regular Season', 12, 3, 7, 10, 6, 5);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="8",
      instruction="I am Ben Winnett (ELITEID 12537). I need to update my draft information in the system: Please change my draft year from 2007 to 2008, draft round from 4 to 3, and overall pick number from 104 to 87 for my account.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM PlayerInfo WHERE ELITEID = 12537;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET draftyear = 2008, draftround = 3, overall = 87 WHERE ELITEID = 12537;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="9",
      instruction="I am Sergei Verenikin (ELITEID: 83453). Update my PlayerInfo record: set position_info to 'C', shoots to 'R', and weight to 198 (referencing weight_id). Add new weight entry with weight_id=198 containing 90 kg and 198 lbs. Verify updates apply only to ELITEID 83453.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO weight_info (weight_id, weight_in_kg, weight_in_lbs) VALUES (198, 90, 198);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET position_info = 'C', shoots = 'R', weight = 198 WHERE ELITEID = 83453;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="10",
      instruction="I am Yevgeni Fyodorov with ELITEID 18377. Please verify my identity first. I need to update my weight to 90 kg (198 lbs) by: 1) Creating a new weight_info entry with weight_id=198, weight_in_kg=90, weight_in_lbs=198. 2) Updating my PlayerInfo weight reference to weight_id=198. Confirm the update by showing my PlayerName, nation, height details (cm/inch), and new weight metrics (kg/lbs).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM PlayerInfo WHERE ELITEID = 18377"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO weight_info (weight_id, weight_in_kg, weight_in_lbs) VALUES (198, 90, 198)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 198 WHERE ELITEID = 18377"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT pi.PlayerName, pi.nation, hi.height_in_cm, hi.height_in_inch, wi.weight_in_kg, wi.weight_in_lbs FROM PlayerInfo pi JOIN height_info hi ON pi.height = hi.height_id JOIN weight_info wi ON pi.weight = wi.weight_id WHERE pi.ELITEID = 18377"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1662",
      instruction="This is Tore Vikingstad (ELITEID:1662). I need to update my player profile with my new verified weight of 100 kg (220 lbs). Please: 1) Create a new weight record (weight_id=220, weight_in_kg=100, weight_in_lbs=220) in the weight_info table. 2) Update my PlayerInfo entry to reference this new weight record. Confirm these changes apply exclusively to my profile (ELITEID:1662).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO weight_info (weight_id, weight_in_kg, weight_in_lbs) VALUES (220, 100, 220);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 220 WHERE ELITEID = 1662;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="12",
      instruction="I am an agent managing Tomas Skvaridlo (ELITEID 27219). Please update his profile: set his shooting style to 'R', draft year to 2000, and update his height reference to height_id 75. Then add a new season record for him: season '1999-2000', team 'Pittsburgh Penguins', league 'NHL', gametype 'Preseason', 3 games played, 2 goals, 1 assist, 3 points, 4 penalty minutes, plus/minus 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET shoots = 'R', draftyear = 2000, height = 75 WHERE ELITEID = 27219"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (27219, '1999-2000', 'Pittsburgh Penguins', 'NHL', 'Preseason', 3, 2, 1, 3, 4, 2)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="13",
      instruction="I'm Nathan Davis (ELITEID 9211) and need to register my participation in the 2024-2025 season. Please add my entry for Team Milwaukee Admirals in the AHL league, playing Regular games. Initialize my stats to: GP=0, G=0, A=0, P=0, PIM=0, PLUSMINUS=0.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM PlayerInfo WHERE ELITEID = 9211;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (9211, '2024-2025', 'Milwaukee Admirals', 'AHL', 'Regular', 0, 0, 0, 0, 0, 0);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="14",
      instruction="You are Jonathan Ericsson (ELITEID: 1346). Update your draft year to 2003 and draft round to 8 in PlayerInfo. Insert/update weight_id 225 with 102 kg (225 lbs) in weight_info, then set your weight reference to 225 in PlayerInfo. Add a 2003-2004 season record for Detroit Red Wings (NHL Regular season: 6 GP, 0 G, 2 A, 2 P, 4 PIM, +1).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET draftyear = 2003, draftround = 8 WHERE ELITEID = 1346;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT OR REPLACE INTO weight_info (weight_id, weight_in_kg, weight_in_lbs) VALUES (225, 102, 225);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 225 WHERE ELITEID = 1346;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (1346, '2003-2004', 'Detroit Red Wings', 'NHL', 'Regular', 6, 0, 2, 2, 4, 1);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="15",
      instruction="My name is Tomi Maki (ELITEID 3215, birthdate 1983-08-19). I need to update my profile: Set height_in_cm to 181 cm for height_id 71, weight_in_kg to 89 kg (195 lbs) for weight_id 192, and change birthplace to 'Helsinki, Finland'. Confirm my identity using ELITEID 3215 and birthdate 1983-08-19, then update PlayerInfo (ELITEID 3215) to reference height_id 71, weight_id 192, and the new birthplace.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT ELITEID FROM PlayerInfo WHERE ELITEID = 3215 AND birthdate = '1983-08-19';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE height_info SET height_in_cm = 181 WHERE height_id = 71;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE weight_info SET weight_in_kg = 89, weight_in_lbs = 195 WHERE weight_id = 192;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET height = 71, weight = 192, birthplace = 'Helsinki, Finland' WHERE ELITEID = 3215;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="16",
      instruction="You are the authorized manager for Marc Cavosie, ELITEID 9452. Update Marc's PlayerInfo: set height to 185 cm and weight to 90 kg. Then, create a new SeasonStatus entry with SEASON '2006-2007', TEAM 'Albany River Rats', LEAGUE 'AHL', GAMETYPE 'regular', GP 40, G 12, A 15, P 27, PIM 20, PLUSMINUS -5.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET height = 185, weight = 90 WHERE ELITEID = 9452;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (9452, '2006-2007', 'Albany River Rats', 'AHL', 'regular', 40, 12, 15, 27, 20, -5);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="17",
      instruction="My name is Oak Hewer (ELITEID 81623). Update my player weight to 220 lbs in my profile. Then, add my 2023-2024 season performance: TEAM 'Ottawa Cyclones', LEAGUE 'OHL', GAMETYPE 'Regular', GP 15, G 2, A 7, P 9, PIM 4, PLUSMINUS 3. Use ELITEID 81623 for both updates.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 220 WHERE ELITEID = 81623"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (81623, '2023-2024', 'Ottawa Cyclones', 'OHL', 'Regular', 15, 2, 7, 9, 4, 3)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="18",
      instruction="I'd like to update Steven Kampfer's profile. First, modify weight record 192 to set weight_in_kg = 88 and weight_in_lbs = 195. Second, add his 2023-2024 season stats: TEAM 'Kazan Bars', LEAGUE 'KHL', GAMETYPE 'Regular', GP 55, G 4, A 15, P 19, PIM 32, PLUSMINUS 11, ELITEID 12530, SEASON '2023-2024'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE weight_info SET weight_in_kg = 88, weight_in_lbs = 195 WHERE weight_id = 192"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (12530, '2023-2024', 'Kazan Bars', 'KHL', 'Regular', 55, 4, 15, 19, 32, 11)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="18885",
      instruction="You are Katherine Johnson, assistant coach and stats administrator for Joe Gleason (ELITEID 18885). Execute these updates: 1) In PlayerInfo, set draftyear = 2009 and overall draft pick = 200 for ELITEID 18885. 2) Update weight_id 181 in weight_info to 85 kg / 187 lbs. 3) Add a 2024-25 season record in SeasonStatus for ELITEID 18885: Team='Edina Eagles', League='USHL', GAMETYPE='Regular', GP=34, G=5, A=16, P=21, PIM=18, PLUSMINUS=7.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET draftyear = 2009, overall = 200 WHERE ELITEID = 18885"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE weight_info SET weight_in_kg = 85, weight_in_lbs = 187 WHERE weight_id = 181"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (18885, '2024-25', 'Edina Eagles', 'USHL', 'Regular', 34, 5, 16, 21, 18, 7)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="20",
      instruction="As the team manager, I need to update Travis Morin's player record (ELITEID 11446). Set his height to ID 74 and weight to ID 195 in the PlayerInfo table. After confirmation, display his full name, updated height in centimeters, updated weight in kilograms, draft year, and drafting team to validate the changes.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET height = 74, weight = 195 WHERE ELITEID = 11446"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT PlayerInfo.PlayerName, height_info.height_in_cm, weight_info.weight_in_kg, PlayerInfo.draftyear, PlayerInfo.overallby FROM PlayerInfo JOIN height_info ON PlayerInfo.height = height_info.height_id JOIN weight_info ON PlayerInfo.weight = weight_info.weight_id WHERE PlayerInfo.ELITEID = 11446"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="21",
      instruction="Authenticate as ELITEID=18024. Update records for Maxim Semyonov: 1) In PlayerInfo table - Set nation='Russia' WHERE ELITEID=18024; 2) In SeasonStatus table - Set A=2 WHERE ELITEID=18024 AND SEASON='2003-2004' AND TEAM='Lada Togliatti-2' AND LEAGUE='Russia3' AND GAMETYPE='Regular Season'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET nation = 'Russia' WHERE ELITEID = 18024;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE SeasonStatus SET A = 2 WHERE ELITEID = 18024 AND SEASON = '2003-2004' AND TEAM = 'Lada Togliatti-2' AND LEAGUE = 'Russia3' AND GAMETYPE = 'Regular Season';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22",
      instruction="Update Jakub Klepis's profile (ELITEID 9609) with the following changes: 1) Set height=74 and height_id=74 in PlayerInfo based on his updated 186 cm measurement. 2) Create new weight_info entry (weight_id=204, 94 kg/207 lbs) then update PlayerInfo with weight=204 and weight_id=204. 3) Update position_info to 'C/LW' in PlayerInfo. 4) Add new SeasonStatus record: SEASON='2023-2024', TEAM='HC Sparta Praha', LEAGUE='Extraliga', GAMETYPE='Regular Season', GP=54, G=17, A=30, P=47, PIM=42, PLUSMINUS=8.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET height = 74, height_id = 74 WHERE ELITEID = 9609"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO weight_info (weight_id, weight_in_kg, weight_in_lbs) VALUES (204, 94, 207)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 204, weight_id = 204 WHERE ELITEID = 9609"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET position_info = 'C/LW' WHERE ELITEID = 9609"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (9609, '2023-2024', 'HC Sparta Praha', 'Extraliga', 'Regular Season', 54, 17, 30, 47, 42, 8)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="23",
      instruction="I'm John Flatters (ELITEID: 11646). My profile has incorrect height and weight entries. Please update my height to 188 cm and weight to 82 kg in the PlayerInfo table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM PlayerInfo WHERE ELITEID = 11646 AND PlayerName = 'John Flatters';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT height_id FROM height_info WHERE height_in_cm = 188;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT weight_id FROM weight_info WHERE weight_in_kg = 82;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET height = (SELECT height_id FROM height_info WHERE height_in_cm = 188), weight = (SELECT weight_id FROM weight_info WHERE weight_in_kg = 82) WHERE ELITEID = 11646;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="24",
      instruction="You are Will Engasser, born 1985-09-25. Your player profile currently lists your height as 74 inches and weight as 225 lbs. Please update your profile in PlayerInfo to reflect your current height of 76 inches and weight of 228 lbs. Additionally, add your 2004-2005 season stats to SeasonStatus with the following details: SEASON '2004-2005', TEAM 'Tri-City Storm', LEAGUE 'USHL', GAMETYPE 'Regular Season', GP 52, G 9, A 14, P 23, PIM 38, PLUSMINUS 2.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT ELITEID FROM PlayerInfo WHERE PlayerName = 'Will Engasser' AND birthdate = '1985-09-25';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET height = 76, weight = 228 WHERE ELITEID = 15314;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (15314, '2004-2005', 'Tri-City Storm', 'USHL', 'Regular Season', 52, 9, 14, 23, 38, 2);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="25",
      instruction="I am Nigel Williams (ELITEID 9310). I've recently switched my role to forward and now shoot right-handed. Please update my profile: set position_info to 'F', shoots to 'R', and weight to 232 lbs in my PlayerInfo. Additionally, update my weight record (weight_id 232) to reflect 105 kg / 232 lbs in the weight_info table. All changes apply to ELITEID 9310.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET position_info = 'F', shoots = 'R', weight = 232 WHERE ELITEID = 9310;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE weight_info SET weight_in_kg = 105, weight_in_lbs = 232 WHERE weight_id = 232;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="26",
      instruction="I am Jonas Ronnqvist (ELITEID 510). Please add my 2000-2001 NHL Regular Season stats for Anaheim Ducks: 25 games played, 2 goals, 7 assists, 9 points, 6 penalty minutes, plus-minus of 1. Ensure my existing height (74 inches) and weight (201 lbs) from PlayerInfo are referenced.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM PlayerInfo WHERE ELITEID=510 AND PlayerName='Jonas Ronnqvist'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (510, '2000-2001', 'Anaheim Ducks', 'NHL', 'Regular Season', 25, 2, 7, 9, 6, 1)"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="27",
      instruction="You are Jake Brenk (ELITEID 12079, birthdate 1982-04-16, nation USA). To prepare for your team review, please execute the following updates: 1) Retrieve your current PlayerInfo data. 2) Update your weight to 185 lbs. 3) Modify your draft round to 4 and set 'overallby' to 'Updated Oilers Committee'. 4) Add a new 2024 season entry to SeasonStatus with TEAM 'Detroit Lakes Eagles', LEAGUE 'Minnesota Minor', GAMETYPE 'Regular', 5 GP, 2 G, 3 A, 5 P, 4 PIM, and +2. Finally, confirm all updates by returning your revised PlayerInfo and the new SeasonStatus row.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM PlayerInfo WHERE ELITEID = 12079"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 185, draftround = 4, overallby = 'Updated Oilers Committee' WHERE ELITEID = 12079"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (12079, '2024', 'Detroit Lakes Eagles', 'Minnesota Minor', 'Regular', 5, 2, 3, 5, 4, 2)"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM PlayerInfo WHERE ELITEID = 12079"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM SeasonStatus WHERE ELITEID = 12079 AND SEASON = '2024'"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="29",
      instruction="Roman Polak (ELITEID 9621) requests to update his height entry (height_id 74) to 190 cm and his weight entry (weight_id 236) to 110 kg following a recent physical assessment. Additionally, he needs to add a new 2004-2005 season record with the St. Louis Blues in the NHL Regular Season, including 75 games played, 2 goals, 10 assists, 12 points, 65 penalty minutes, and a +5 plus-minus rating.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE height_info SET height_in_cm = 190 WHERE height_id = 74;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE weight_info SET weight_in_kg = 110 WHERE weight_id = 236;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (9621, '2004-2005', 'St. Louis Blues', 'NHL', 'Regular Season', 75, 2, 10, 12, 65, 5);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="31",
      instruction="My name is Matt Foy (ELITEID 9158). I want to update my official weight from 225 lbs (102 kg) to 215 lbs (98 kg). Please create a new weight entry with weight_id 215 containing 215 lbs/98 kg, then update my PlayerInfo record to use this new weight_id. Confirm both changes are completed.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO weight_info (weight_id, weight_in_kg, weight_in_lbs) VALUES (215, 98, 215);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 215 WHERE ELITEID = 9158;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="32",
      instruction="You are Jyri Niemi (ELITEID=12570) requesting a profile update. Please: 1) Change birthplace to 'Tampere, FIN' 2) Update position to 'LW' 3) Set height to 189 cm using existing height_id=74 (remove inches) 4) Set weight to 96 kg using existing weight_id=207 (remove pounds). Ensure both PlayerInfo and the corresponding height_info/weight_info entries are updated.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM PlayerInfo WHERE ELITEID = 12570;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET birthplace = 'Tampere, FIN', position_info = 'LW' WHERE ELITEID = 12570;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE height_info SET height_in_cm = 189, height_in_inch = NULL WHERE height_id = 74;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET height = 74 WHERE ELITEID = 12570;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE weight_info SET weight_in_kg = 96, weight_in_lbs = NULL WHERE weight_id = 207;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 207 WHERE ELITEID = 12570;"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="10406",
      instruction="You are Brett Carson (ELITEID 10406). Your weight is incorrectly listed as 227 lbs. Please: (1) Insert a new weight_info entry with weight_id=225, weight_in_kg=102, and weight_in_lbs=225. (2) Update your PlayerInfo record to set weight=225. (3) Add a 2004-2005 season record with TEAM='Calgary Hitmen', LEAGUE='WHL', GAMETYPE='Regular', GP=60, G=5, A=17, P=22, PIM=58, PLUSMINUS=7 under your ELITEID 10406.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO weight_info (weight_id, weight_in_kg, weight_in_lbs) VALUES (225, 102, 225);"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET weight = 225 WHERE ELITEID = 10406;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (10406, '2004-2005', 'Calgary Hitmen', 'WHL', 'Regular', 60, 5, 17, 22, 58, 7);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="36",
      instruction="As Alex Conrad, first verify that ELITEID 15451 corresponds to Matt Generous. Then update his height to 191 cm using height_id 75, update weight to 89 kg using weight_id 194, and add a new 2024-2025 season entry for TEAM 'Bridgeport Sound Tigers', LEAGUE 'AHL', GAMETYPE 'Regular' with GP=0, G=0, A=0, P=0, PIM=0, PLUSMINUS=0.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT PlayerName FROM PlayerInfo WHERE ELITEID = 15451;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE height_info SET height_in_cm = 191 WHERE height_id = 75;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE weight_info SET weight_in_kg = 89 WHERE weight_id = 194;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO SeasonStatus (ELITEID, SEASON, TEAM, LEAGUE, GAMETYPE, GP, G, A, P, PIM, PLUSMINUS) VALUES (15451, '2024-2025', 'Bridgeport Sound Tigers', 'AHL', 'Regular', 0, 0, 0, 0, 0, 0);"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="38",
      instruction="I am Ryan Peterson, a sports statistician. Authenticate my access using ELITEID 8724. Update Adam Hall's profile: 1) Set birthyear to 1981 (ELITEID 8724), 2) Adjust height to 188 cm (height_id 74), 3) Update weight to 97 kg (weight_id 212), and 4) Change 1998-1999 season team to 'USA National U20 Team' (ELITEID 8724, SEASON '1998-1999'). All parameters are explicitly provided for each modification.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM PlayerInfo WHERE ELITEID = 8724;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE PlayerInfo SET birthyear = 1981 WHERE ELITEID = 8724;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE height_info SET height_in_cm = 188 WHERE height_id = 74;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE weight_info SET weight_in_kg = 97 WHERE weight_id = 212;"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE SeasonStatus SET TEAM = 'USA National U20 Team' WHERE ELITEID = 8724 AND SEASON = '1998-1999';"
               }
            ),
       ],
       outputs=[]
   ),
]
