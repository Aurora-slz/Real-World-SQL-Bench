from dysql_bench.types import Task, Action

TASKS_TEST = [
   Task(
      user_id="casting_coordinator_2024",
      instruction="As the casting coordinator, I need to update the role for person ID 'nm0176681' working on episode 'tt0629391' in the Art Department category. Their current role is listed as 'set dresser' - please change this to 'stand-by set dresser'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'stand-by set dresser' WHERE episode_id = 'tt0629391' AND person_id = 'nm0176681' AND role = 'set dresser' AND category = 'Art Department';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="1",
      instruction="My name is Greg Ross with email greg.ross7732@example.com. Please update Constantine Makris (person_id: nm0538744) to credited status 'true' for the director role in episode 'Refuge: Part 1' (episode_id: tt0629397). Also set his nickname to 'Gus' in the Person records.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited='true' WHERE episode_id='tt0629397' AND person_id='nm0538744' AND role='director';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET nickname='Gus' WHERE person_id='nm0538744';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="2",
      instruction="I am Cindy Lee (person_id nm0514445). Please record my Writers Guild of America Award for Best Episodic Drama in 1999. Add an entry with organization 'Writers Guild of America', year 1999, award_category 'Best Episodic Drama', award 'Winner', series 'Law and Order', episode_id 'tt0629146', person_id 'nm0514445', role 'teleplay writer', and result 'Won' to the Award table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Award (organization, year, award_category, award, series, episode_id, person_id, role, result) VALUES ('Writers Guild of America', 1999, 'Best Episodic Drama', 'Winner', 'Law and Order', 'tt0629146', 'nm0514445', 'teleplay writer', 'Won');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="3",
      instruction="As Lynne Whitlock (person_id 'nm0926104'), update my credited status in the Credit table from 'false' to 'true' for my role as 'assistant editor' (category 'Editorial Department') in Law & Order Season 9 Episode 14 titled 'Sideshow' (episode_id 'tt0629422'). Confirm the update where currently credited = 'false'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629422' AND person_id = 'nm0926104' AND category = 'Editorial Department' AND role = 'assistant editor' AND credited = 'false';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="4",
      instruction="As Jane Lee (jane.lee123@email.com), production assistant for Law and Order, I need to update credits for episode 'Refuge: Part 1' (ID: tt0629397). First, add a new credit: Paul Rivers (ID nm9999999) in category 'Produced by' as 'line producer' with credited status 'true'. Second, remove the existing credit: Anthony Azzara (ID nm2190130) in category 'Additional Crew' for role 'first assistant accountant' marked as credited 'false'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Credit (episode_id, person_id, category, role, credited) VALUES ('tt0629397', 'nm9999999', 'Produced by', 'line producer', 'true');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Credit WHERE episode_id='tt0629397' AND person_id='nm2190130' AND category='Additional Crew' AND role='first assistant accountant' AND credited='false';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="5",
      instruction="This is Stewart J. Zully (person_id: nm0958597, birthdate: August 23, 1955). I need to correct my credited role in the Law & Order episode 'Scrambled' (episode_id: tt0629409). Specifically, in the Cast category, my role currently shows as 'Tom Bublitz' but should be updated to 'Officer Tom Bublitz'. Please verify my identity using my birthdate and ensure the update applies exclusively to episode tt0629409, person nm0958597, in the Cast category, where the role currently lists 'Tom Bublitz'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Person WHERE person_id = 'nm0958597' AND name = 'Stewart J. Zully' AND birthdate = '1955-08-23';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Credit WHERE episode_id = 'tt0629409' AND person_id = 'nm0958597' AND category = 'Cast' AND role = 'Tom Bublitz';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'Officer Tom Bublitz' WHERE episode_id = 'tt0629409' AND person_id = 'nm0958597' AND category = 'Cast' AND role = 'Tom Bublitz';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="6",
      instruction="As William N. Fordes (person_id 'nm0285969'), co-producer of Law & Order, I need to formally request a correction to Steven Zirnkilton's (person_id 'nm0007064') credit status. For episode 'Disciple' (episode_id 'tt0629239'), update his 'Cast' category entry for the 'Narrator' role to reflect proper credited status (change from uncredited to credited).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629239' AND person_id = 'nm0007064' AND category = 'Cast' AND role = 'Narrator';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="casting_manager_jones",
      instruction="As casting manager Alex Jones, I need to correct the credit status for Sharon Ziman (person ID: nm0956539) in Law and Order Season 9 Episode 14 (episode ID: tt0629422). Her role as 'Naomi' in the 'Cast' category is currently uncredited. Please update this record to officially credit her participation.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE person_id = 'nm0956539' AND episode_id = 'tt0629422' AND category = 'Cast' AND role = 'Naomi';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="prod.coordinator1856@example.com",
      instruction="As production coordinator, please process two credit updates for episode 'tt0629146' (Law and Order S09E22: Admissions):1. Set credited status to TRUE for:- Person: nm2190130- Category: Additional Crew- Role: first assistant accountant2. Modify existing role from 'Melissa Slater' to 'Lead Forensics Technician' for:- Person: nm0180025- Category: Cast",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited='true' WHERE episode_id='tt0629146' AND person_id='nm2190130' AND category='Additional Crew' AND role='first assistant accountant';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role='Lead Forensics Technician' WHERE episode_id='tt0629146' AND person_id='nm0180025' AND category='Cast' AND role='Melissa Slater';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="11",
      instruction="Hi, I'm Gene Ritchings (person_id: nm0728643). I need to update my credit for the Law & Order episode 'Shield' (episode_id: tt0629420). Please change my role from 'production coordinator' to 'unit production manager' in the 'Additional Crew' category and mark me as credited.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Person WHERE person_id = 'nm0728643' AND name = 'Gene Ritchings';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'unit production manager', credited = 'true' WHERE episode_id = 'tt0629420' AND person_id = 'nm0728643' AND category = 'Additional Crew' AND role = 'production coordinator';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="fan_editor_8327",
      instruction="As wiki editor (user_id: fan_editor_8327), I request two updates: 1) Update Jerry Orbach's record (person_id: nm0001583) to set height_meters = 1.89 in the Person table. 2) For episode tt0629292, mark Steven Zirnkilton (person_id: nm0007064) as credited='true' in the Cast category for his Narrator role in the Credit table.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET height_meters = 1.89 WHERE person_id = 'nm0001583';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629292' AND person_id = 'nm0007064' AND category = 'Cast' AND role = 'Narrator';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Erica Ray, Detroit",
      instruction="I am Erica Ray from Detroit, MI. After reviewing the credits for Law and Order Season 9 Episode 13 (episode_id: tt0629306), I confirm that C.J. Simpson (person_id: nm0800929) was not actually credited as 'art director' under the 'General' category. Please update their credited status to 'false' for this specific entry in the database.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited='false' WHERE episode_id='tt0629306' AND person_id='nm0800929' AND category='General' AND role='art director';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="18",
      instruction="Hi, my name is Samuel Lee and my person_id is nm3000123. As associate producer for episode 'Punk' (episode_id: tt0629391), please: 1) Create a Credit record with episode_id 'tt0629391', person_id 'nm3000123', category 'Produced by', role 'associate producer', and credited 'true'. 2) Then update this specific record (episode_id 'tt0629391', person_id 'nm3000123', category 'Produced by', role 'associate producer') to set credited to 'false' to reflect no on-screen credit.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Person WHERE person_id = 'nm3000123' AND name = 'Samuel Lee'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Credit (episode_id, person_id, category, role, credited) VALUES ('tt0629391', 'nm3000123', 'Produced by', 'associate producer', 'true')"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'false' WHERE episode_id = 'tt0629391' AND person_id = 'nm3000123' AND category = 'Produced by' AND role = 'associate producer'"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="19",
      instruction="I am Anthony Azzara (person_id: nm2190130) requesting to update my uncredited role as 'first assistant accountant' under the 'Additional Crew' category for episode 'Venom' (episode_id: tt0629487). Please verify my identity, set the credited status to 'true' for this specific role, and display the updated record.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Person WHERE person_id = 'nm2190130' AND name = 'Anthony Azzara';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629487' AND person_id = 'nm2190130' AND category = 'Additional Crew' AND role = 'first assistant accountant';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Credit WHERE episode_id = 'tt0629487' AND person_id = 'nm2190130' AND category = 'Additional Crew' AND role = 'first assistant accountant';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="21",
      instruction="First, in the Credit table, update Steven Zirnkilton (person_id: nm0007064) for episode tt0629391 (role: 'Narrator') to set credited='true'. Then, insert a new record in the Award table with award_id 999999, organization 'Emmy Awards', year 1999, award_category 'Outstanding Voice-Over Performance', award 'Nominated', series 'Law and Order', episode_id 'tt0629391', person_id 'nm0007064', role 'Narrator', and result 'Nominated'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited='true' WHERE episode_id='tt0629391' AND person_id='nm0007064' AND role='Narrator';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Award (award_id, organization, year, award_category, award, series, episode_id, person_id, role, result) VALUES (999999, 'Emmy Awards', 1999, 'Outstanding Voice-Over Performance', 'Nominated', 'Law and Order', 'tt0629391', 'nm0007064', 'Narrator', 'Nominated');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="22",
      instruction="You are Daniel Fisher (person_id 'nm0279437'). You noticed your role in the 'Art Department' category for Law and Order episode 'tt0629204' (episode_id 'tt0629204') was incorrectly listed as 'stand-by set dresser'. Please update this credit entry to reflect your correct role as 'lead set dresser' and ensure it is marked as 'credited' (credited='true'). The existing record to modify has: episode_id='tt0629204', person_id='nm0279437', current role='stand-by set dresser', category='Art Department'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'lead set dresser', credited = 'true' WHERE episode_id = 'tt0629204' AND person_id = 'nm0279437' AND role = 'stand-by set dresser' AND category = 'Art Department';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="23",
      instruction="I'm Lewis Gould (person ID: nm0332434), born in USA. I worked as a 'unit production manager' in the Law and Order episode 'Harm' (episode_id tt0629289). Please update my credit role to 'executive unit production manager' for this episode. Also, correct my birth_place to 'Brooklyn' and birth_region to 'New York' in my profile.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Person WHERE person_id = 'nm0332434' AND name = 'Lewis Gould' AND birth_country = 'USA'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'executive unit production manager' WHERE episode_id = 'tt0629289' AND person_id = 'nm0332434' AND role = 'unit production manager'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET birth_place = 'Brooklyn', birth_region = 'New York' WHERE person_id = 'nm0332434'"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="casting_assistant_23",
      instruction="As a verified casting assistant, please execute these updates: 1) Add a 'Cast' credit for person nm1000001 as 'Nurse Kelly' in episode tt0629289 with credited status 'true'. 2) Set Boston as the birth place for nm1000001 in their profile. Confirm completion.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Credit (episode_id, person_id, category, role, credited) VALUES ('tt0629289', 'nm1000001', 'Cast', 'Nurse Kelly', 'true');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET birth_place = 'Boston' WHERE person_id = 'nm1000001';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="26",
      instruction="I am Terry Beaver (person_id: nm0064777). Please update my credited status to 'false' for the role of Defense Attorney Manning in the Law and Order episode 'tt0629398', as it is incorrect. Additionally, record that I won Screen Actors Guild's 'Best Guest Actor' award (award_id: 90001) in 2000 for this role - award category: 'Best Guest Actor', award name: 'Best Guest Actor', result: 'Won', series: 'Law and Order', episode_id: 'tt0629398', person_id: nm0064777, role: Defense Attorney Manning.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'false' WHERE episode_id = 'tt0629398' AND person_id = 'nm0064777' AND role = 'Defense Attorney Manning';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Award (award_id, organization, year, award_category, award, series, episode_id, person_id, role, result) VALUES (90001, 'Screen Actors Guild', 2000, 'Best Guest Actor', 'Best Guest Actor', 'Law and Order', 'tt0629398', 'nm0064777', 'Defense Attorney Manning', 'Won');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="27",
      instruction="My name is Jasmine Tang (assistant_producer_jtang@example.com), assistant producer for Law and Order. For episode ID 'tt0629170' (titled 'Bait', Season 9 Episode 3), update all 'Art Department' crew entries in the Credit table to set their 'credited' status to 'true'. Additionally, update John W. Farraday's record (person_id = 'nm0268082') in the Person table to set 'birth_place' to 'Philadelphia'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629170' AND category = 'Art Department';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET birth_place = 'Philadelphia' WHERE person_id = 'nm0268082';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="28",
      instruction="You are Park Dietz (person_id: nm0226352). For episode 'Punk' (episode_id: tt0629391), please: 1) Change the role for person_id nm0226352 in Credit from 'technical advisor' to 'forensic psychiatrist consultant' specifically for episode_id tt0629391. 2) Update the birth_region for person_id nm0226352 in Person from 'Pennsylvania' to 'California'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'forensic psychiatrist consultant' WHERE episode_id = 'tt0629391' AND person_id = 'nm0226352' AND role = 'technical advisor';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET birth_region = 'California' WHERE person_id = 'nm0226352' AND birth_region = 'Pennsylvania';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="29",
      instruction="You are Alice Hargreaves, a researcher. Update the Person table record for Teresa Carriker-Thayer (person_id 'nm0140457') to set birth_place = 'Denver' and nickname = 'Carriker, Terri'. All required parameters are provided: person_id, birth_place, and nickname.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET birth_place = 'Denver' WHERE person_id = 'nm0140457';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET nickname = 'Carriker, Terri' WHERE person_id = 'nm0140457';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="30",
      instruction="Hello, this is Angie Harmon (person_id: nm0004990). I recently won the Screen Actors Guild's 1999 Outstanding Supporting Actress award ('Winner' category) for my role as A.D.A. Abbie Carmichael in the Law & Order episode 'True North' (episode_id: tt0629477). Could you please add this award to the system with these official details: organization='Screen Actors Guild', year=1999, award_category='Outstanding Supporting Actress', award='Winner', series='Law and Order', episode_id='tt0629477', person_id='nm0004990', role='A.D.A. Abbie Carmichael', result='won'?",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Person WHERE person_id = 'nm0004990';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Credit WHERE episode_id = 'tt0629477' AND person_id = 'nm0004990';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Award (organization, year, award_category, award, series, episode_id, person_id, role, result) VALUES ('Screen Actors Guild', 1999, 'Outstanding Supporting Actress', 'Winner', 'Law and Order', 'tt0629477', 'nm0004990', 'A.D.A. Abbie Carmichael', 'won');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="31",
      instruction="I am updating my biographical records. For Angie Harmon (person_id = 'nm0004990', birth name = 'Angela Michelle Harmon'), update her birth_country in the Person table to 'United States of America'. For Jerry Orbach (person_id = 'nm0001583', birth name = 'Jerome Bernard Orbach'), update his birth_country to 'United States of America'. After updates, list all awards from the Award table associated with either person_id 'nm0004990' or 'nm0001583', including award_id, organization, year, award_category, award, series, episode_id, person_id, role, and result for verification.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET birth_country = 'United States of America' WHERE person_id = 'nm0004990';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET birth_country = 'United States of America' WHERE person_id = 'nm0001583';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT award_id, organization, year, award_category, award, series, episode_id, person_id, role, result FROM Award WHERE person_id = 'nm0004990' OR person_id = 'nm0001583';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="Television Academy",
      instruction="As a representative of the Television Academy, I need to correct our records for Law and Order episode 'tt0629292'. Currently, Sam Waterston (person_id: 'nm0001832') is mistakenly recorded as the recipient of the 'Best Cinematographer' award for this episode. The correct recipient should be Constantine Makris (person_id: 'nm0538744'). Please: (1) Verify the award record WHERE organization='Television Academy', episode_id='tt0629292', award_category='Best Cinematographer', AND person_id='nm0001832'; (2) Update the person_id to 'nm0538744' for the record WHERE organization='Television Academy', episode_id='tt0629292', award_category='Best Cinematographer', AND person_id='nm0001832'; (3) Confirm the correction by retrieving the record WHERE organization='Television Academy', episode_id='tt0629292', award_category='Best Cinematographer', AND person_id='nm0538744'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Award WHERE organization = 'Television Academy' AND episode_id = 'tt0629292' AND award_category = 'Best Cinematographer' AND person_id = 'nm0001832';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Award SET person_id = 'nm0538744' WHERE organization = 'Television Academy' AND episode_id = 'tt0629292' AND award_category = 'Best Cinematographer' AND person_id = 'nm0001832';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Award WHERE organization = 'Television Academy' AND episode_id = 'tt0629292' AND award_category = 'Best Cinematographer' AND person_id = 'nm0538744';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="production_coordinator_law_and_order",
      instruction="As the production coordinator for Law & Order, I require two updates in our production database. First, in the Credit table (episode_id: 'tt0629448', person_id: 'nm0279437'), set the 'credited' field to 'false' for Daniel Fisher's involvement in 'Tabula Rasa'. Second, update Daniel Fisher's biographical data in the Person table (person_id: 'nm0279437') with birth_place: 'New York', birth_region: 'New York', and birth_country: 'USA'. Both updates must be processed immediately per studio requirements.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'false' WHERE episode_id = 'tt0629448' AND person_id = 'nm0279437';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET birth_place = 'New York', birth_region = 'New York', birth_country = 'USA' WHERE person_id = 'nm0279437';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="37",
      instruction="As Olivia Torres, after verifying your identity, update Deborah Devgan (person_id 'nm0223375')'s credit record in episode 'tt0629321' ('Juvenile', Law and Order S9E18) to mark 'credited' as 'true' for her role 'assistant: Ed Sherin'. Also, set her nickname to 'Debbie' in her Person profile.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629321' AND person_id = 'nm0223375' AND role = 'assistant: Ed Sherin';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET nickname = 'Debbie' WHERE person_id = 'nm0223375';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="40",
      instruction="Hello, I'm Rachel Li (user ID: researcher_rli), an archival researcher for TV productions. Please correct the credited status for crew member John W. Farraday (person ID: nm0268082) in your database records. For episode tt0629266 (Law and Order S09E04), his role as 'set dresser' should have the 'credited' field updated from false to true to reflect the on-screen credit. This is an official correction to the existing record.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629266' AND person_id = 'nm0268082' AND role = 'set dresser';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="41",
      instruction="As the Law and Order production coordinator, update Daniel Fisher's credit (person_id: nm0279437) for episode tt0629149 in the Art Department category. Change role from 'stand-by set dresser' to 'lead set dresser'. Required parameters: episode_id=tt0629149, person_id=nm0279437, category=Art Department, new_role=lead set dresser.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'lead set dresser' WHERE episode_id = 'tt0629149' AND person_id = 'nm0279437' AND category = 'Art Department';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="42",
      instruction="As the content manager for Law and Order, I need to make two updates for episode 'Ambitious' (episode_id=tt0629153). First, update the existing Credit entry where person_id=nm1250384 works in category='Produced by' with current role='co-executive producer' to set role='producer' and credited='true'. Then, create a new Award record with award_id=6001: organization='Producers Guild', year=1999, award_category='Outstanding Producer', award='Outstanding Producer', series='Law and Order', linked to episode_id=tt0629153 and person_id=nm1250384 as role='producer' with result='won'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role='producer', credited='true' WHERE episode_id='tt0629153' AND person_id='nm1250384' AND category='Produced by' AND role='co-executive producer';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Award (award_id, organization, year, award_category, award, series, episode_id, person_id, role, result) VALUES (6001, 'Producers Guild', 1999, 'Outstanding Producer', 'Outstanding Producer', 'Law and Order', 'tt0629153', 'nm1250384', 'producer', 'won');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="assistant_to_production_law_and_order",
      instruction="Update Patrick Cousins' (person_id: nm0184112) credit record in the Camera and Electrical Department category for role 'best boy' in Episode 'Haven' (episode_id: tt0629292) from uncredited to credited.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629292' AND person_id = 'nm0184112' AND category = 'Camera and Electrical Department' AND role = 'best boy';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="editor_law_and_order_01",
      instruction="First authenticate as the episode editor for Law & Order. After verification: 1) Insert a new Credit record for Lisa Frank (person_id 'nm1234567') in episode 'tt0629487' with category 'Production Management', role 'line producer', and credited status 'true'. 2) Display current Production Management credits for this episode showing name, role, and credited status.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Credit (episode_id, person_id, category, role, credited) VALUES ('tt0629487', 'nm1234567', 'Production Management', 'line producer', 'true');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT Person.name, Credit.role, Credit.credited FROM Credit JOIN Person ON Credit.person_id = Person.person_id WHERE Credit.episode_id = 'tt0629487' AND Credit.category = 'Production Management';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="nm0566552",
      instruction="Hello, this is Kathy McCormick (person_id: nm0566552). I need to update two credits for Law and Order episode 'Scrambled' (episode_id: tt0629409, season 9 episode 6). First, please set my existing 'Produced by' credit as co-executive producer to uncredited (credited='false'). Second, ensure Jeffrey L. Hayes (person_id: nm1250384) is properly credited as 'true' for the same episode under 'Produced by' category with co-executive producer role.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'false' WHERE episode_id = 'tt0629409' AND person_id = 'nm0566552' AND category = 'Produced by' AND role = 'co-executive producer';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629409' AND person_id = 'nm1250384' AND category = 'Produced by' AND role = 'co-executive producer';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="archivist001",
      instruction="As the Law & Order series archivist, please update the credit record for John W. Farraday (person_id='nm0268082') in Episode 'Disciple' (episode_id='tt0629239'). Specifically, set his credited status to 'true' for the Art Department category where his role is listed as set dresser.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited='true' WHERE episode_id='tt0629239' AND person_id='nm0268082' AND category='Art Department' AND role='set dresser';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="51",
      instruction="Authenticate user lawandorderfan123. For episode 'Harm' (episode_id='tt0629289'): 1) Remove director credit for Richard Dobbs (person_id='nm0229650', role='director') from this episode; 2) Update Don Ohlmeyer's credit (person_id='nm0645048') from 'president of NBC West Coast' to 'executive consultant' for this episode; 3) Add Emmy Award record: Park Dietz (person_id='nm0226352') as 'technical advisor', organization='Emmy', year=1999, category='Outstanding Technical Contribution', award='Nominee', result='Nominated' for 'Law and Order' episode 'tt0629289'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Credit WHERE episode_id = 'tt0629289' AND person_id = 'nm0229650' AND role = 'director';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'executive consultant' WHERE episode_id = 'tt0629289' AND person_id = 'nm0645048' AND role = 'president of NBC West Coast';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Award (organization, year, award_category, award, series, episode_id, person_id, role, result) VALUES ('Emmy', 1999, 'Outstanding Technical Contribution', 'Nominee', 'Law and Order', 'tt0629289', 'nm0226352', 'technical advisor', 'Nominated');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="52",
      instruction="As Billy Fox (person_id: nm0288886), I need to correct my role credit for the Law and Order episode 'Admissions' (episode_id: tt0629146) in the Credit table. Please update my existing role entry from 'producer' to 'executive producer' for this specific episode.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'executive producer' WHERE episode_id = 'tt0629146' AND person_id = 'nm0288886' AND role = 'producer';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="54",
      instruction="You are Kathy O'Connell (person_id: nm0640107). Update your credit for episode 'Shield' (episode_id: tt0629420) from category 'Production Management' to 'Produced by' and role from 'post-production supervisor' to 'Producer'. Additionally, record your Primetime Emmy Award (organization: Primetime Emmy Award) won in 2000 for 'Outstanding Producer of a Drama Series' (award_category) as 'Producer' (role) on series 'Law and Order' episode 'Shield' (episode_id: tt0629420), with award name 'Emmy' and result 'Won'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET category = 'Produced by', role = 'Producer' WHERE person_id = 'nm0640107' AND episode_id = 'tt0629420';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Award (organization, year, award_category, award, series, episode_id, person_id, role, result) VALUES ('Primetime Emmy Award', 2000, 'Outstanding Producer of a Drama Series', 'Emmy', 'Law and Order', 'tt0629420', 'nm0640107', 'Producer', 'Won');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="55",
      instruction="Hello, my name is Nora Elcar-Verdon (person_id: 'nm6214567'). For the Law and Order episode 'Venom' (episode_id: 'tt0629487'), I need my role in the 'Script and Continuity Department' category updated from 'script co-ordinator' to 'script supervisor'. Please ensure the credited status remains 'true'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'script supervisor' WHERE episode_id = 'tt0629487' AND person_id = 'nm6214567' AND category = 'Script and Continuity Department';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="db_editor_jane_3152",
      instruction="As Jane Doe, database editor: 1) Delete the Art Department credit entry for person nm0268082 in episode tt0629409. 2) Change the Production Management role to 'production supervisor' for person nm0640107 in the same episode tt0629409.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Credit WHERE episode_id = 'tt0629409' AND person_id = 'nm0268082' AND category = 'Art Department';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'production supervisor' WHERE episode_id = 'tt0629409' AND person_id = 'nm0640107' AND category = 'Production Management';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="58",
      instruction="As Allison Kent from the production team responsible for 'Law and Order', verify and correct the credit record for Jeremy Schroeder (person_id 'nm0775493') in episode 'tt0629477'. Update his role from 'best boy grip' to 'key grip' and ensure he's marked as credited (credited='true') in the database to reflect accurate production credits.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Credit WHERE episode_id = 'tt0629477' AND person_id = 'nm0775493';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'key grip', credited = 'true' WHERE episode_id = 'tt0629477' AND person_id = 'nm0775493';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="59",
      instruction="For episode 'Refuge: Part 2' (episode_id: 'tt0629398') of 'Law and Order', please make these credit updates: 1) Update Nora Elcar-Verdon (person_id: 'nm6214567') to credited='false' for their 'script co-ordinator' role. 2) Update Wendy M. Roberts (person_id: 'nm1059316') to credited='true' for their 'casting associate' role. Confirm changes specifically for episode_id 'tt0629398'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'false' WHERE episode_id = 'tt0629398' AND person_id = 'nm6214567' AND role = 'script co-ordinator';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629398' AND person_id = 'nm1059316' AND role = 'casting associate';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="60",
      instruction="Authenticate as Margaret Wu (margaret.wu82@example.com). I need to officially update the credited status for Anthony Azzara (person ID: nm2190130) working as 'first assistant accountant' in the 'Additional Crew' category on Episode 'Shield' (ID: tt0629420) from 'false' to 'true'. Confirm all identifiers: episode_id=tt0629420, person_id=nm2190130, category='Additional Crew', role='first assistant accountant'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629420' AND person_id = 'nm2190130' AND category = 'Additional Crew' AND role = 'first assistant accountant';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="61",
      instruction="I am Steven Hill (person_id: nm0384696). Please update my credited status for Law & Order episode 'tt0629397' (series: Law & Order, season: 16, episode: 13) from current 'true' to 'false' as I was incorrectly listed. First confirm my identity and existing credit entry details including current credited status.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Person WHERE person_id = 'nm0384696' AND name = 'Steven Hill';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT episode_id, person_id, credited FROM Credit WHERE episode_id = 'tt0629397' AND person_id = 'nm0384696';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'false' WHERE episode_id = 'tt0629397' AND person_id = 'nm0384696';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="62",
      instruction="I am Evelyn Kennedy, crew manager for 'Law and Order.' Please update Anthony Azzara's credit (person_id: nm2190130) in episode 'Venom' (episode_id: tt0629487). Modify his entry in the 'Additional Crew' category where his current role is 'first assistant accountant' - change the role to 'production accountant' and mark his credited status as 'true'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'production accountant', credited = 'true' WHERE episode_id = 'tt0629487' AND person_id = 'nm2190130' AND category = 'Additional Crew' AND role = 'first assistant accountant';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="63",
      instruction="In episode 'tt0629391', update the credit role for person 'nm0176681' from 'set dresser' to 'assistant property master', and update person 'nm1094224' from 'assistant property master' to 'set dresser'. Both changes apply to episode 'tt0629391'. All person IDs and their current/new roles are explicitly provided.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'assistant property master' WHERE episode_id = 'tt0629391' AND person_id = 'nm0176681' AND role = 'set dresser';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'set dresser' WHERE episode_id = 'tt0629391' AND person_id = 'nm1094224' AND role = 'assistant property master';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="65",
      instruction="You are E. Monique Floyd (person_id: nm0283251). Please submit two updates: 1) Correct your credit role to 'co-producer' for the Law and Order episode 'True North' (episode_id: tt0629477), and 2) Update your official database name from 'E. Monique Floyd' to 'Monique Floyd'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'co-producer' WHERE episode_id = 'tt0629477' AND person_id = 'nm0283251';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Person SET name = 'Monique Floyd' WHERE person_id = 'nm0283251';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="68",
      instruction="As the production coordinator for 'Law and Order', I need to update Nicholas Albanese's (person_id: nm2240611) Art Department credit for episode tt0629292 (season 9 episode 12). Please modify his existing entry to set his role specifically as 'carpenter' and ensure his credited status is marked 'true' in the Art Department category.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'carpenter', credited = 'true' WHERE episode_id = 'tt0629292' AND person_id = 'nm2240611' AND category = 'Art Department';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="69",
      instruction="You are Richard Sweren (person_id: nm0842478), co-producer (category: 'Produced by') on Law & Order episode 'Venom' (episode_id: 'tt0629487'), credited as 'true'. Please update the Credit entry for cast member Matt Keeslar (person_id: nm0444832) in category 'Cast' by changing his role from 'Dennis Pollock' to 'Dennis Pollack' where he is credited as 'true'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Credit WHERE episode_id = 'tt0629487' AND person_id = 'nm0842478' AND category = 'Produced by' AND credited = 'true'"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'Dennis Pollack' WHERE episode_id = 'tt0629487' AND person_id = 'nm0444832' AND category = 'Cast' AND role = 'Dennis Pollock' AND credited = 'true'"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="70",
      instruction="My name is David Shore, person_id nm0794914. Please update my existing credit on episode tt0629153 (Ambitious) in the 'Produced by' category from 'supervising producer' to 'co-executive producer' while keeping category='Produced by' and credited='true'. Additionally, create a new Person entry for Alex Harper with person_id nm9999999, name 'Alex Harper', birth name 'Alexander R. Harper' (no birthdate/location available), then add a credit for them on episode tt0629153 in category='Produced by' as 'associate producer' with credited='true'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET role = 'co-executive producer' WHERE episode_id = 'tt0629153' AND person_id = 'nm0794914' AND category = 'Produced by' AND role = 'supervising producer';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Person (person_id, name, birth_name) VALUES ('nm9999999', 'Alex Harper', 'Alexander R. Harper');"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Credit (episode_id, person_id, category, role, credited) VALUES ('tt0629153', 'nm9999999', 'Produced by', 'associate producer', 'true');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="71",
      instruction="You are Lewis Gould (person_id: nm0332434), director for episode 'Juvenile' (episode_id: tt0629321) of the series 'Law and Order'. Please confirm your identity, then update your credit for episode_id 'tt0629321' (category: 'General', role: 'director') to set credited = 'true'. Additionally, add an award entry with organization = 'Directors Guild of America', year = 1999, award_category = 'Best Direction', award = 'Nominee', series = 'Law and Order', episode_id = 'tt0629321', person_id = 'nm0332434', role = 'director', result = 'Nominated'.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Person WHERE person_id = 'nm0332434';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'true' WHERE episode_id = 'tt0629321' AND person_id = 'nm0332434' AND category = 'General' AND role = 'director';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Award (organization, year, award_category, award, series, episode_id, person_id, role, result) VALUES ('Directors Guild of America', 1999, 'Best Direction', 'Nominee', 'Law and Order', 'tt0629321', 'nm0332434', 'director', 'Nominated');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="prod_2127",
      instruction="I need to authenticate as Jenna Lucas first. Then update Daniel Fisher's (person_id: nm0279437) credit status to uncredited for his 'stand-by set dresser' role in the Art Department category on episode 'Ramparts' (tt0629394). Finally, show me all currently credited crew members for this episode with their names, roles, and departments.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT person_id FROM Person WHERE name = 'Jenna Lucas';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "UPDATE Credit SET credited = 'false' WHERE episode_id = 'tt0629394' AND person_id = 'nm0279437' AND category = 'Art Department' AND role = 'stand-by set dresser';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT Person.name, Credit.role, Credit.category FROM Credit JOIN Person ON Credit.person_id = Person.person_id WHERE Credit.episode_id = 'tt0629394' AND Credit.credited = 'true';"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="committee_coordinator_002",
      instruction="As the awards committee coordinator, I need to create a new award record. Please verify: 1) That Angie Harmon (name: 'Angie Harmon') is officially credited as 'A.D.A. Abbie Carmichael' in Episode 8 of Season 9 of 'Law and Order' titled 'Punk'. 2) If confirmed, insert an Emmy Awards 1999 entry for 'Outstanding Supporting Actress in a Drama Series' with award 'Nominee' and result 'Nominated'. Ensure validation uses current database records for person_id and episode_id before insertion.",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT person_id FROM Person WHERE name = 'Angie Harmon';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT episode_id FROM Episode WHERE series = 'Law and Order' AND season = 9 AND episode = 8 AND title = 'Punk';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "SELECT * FROM Credit WHERE person_id = (SELECT person_id FROM Person WHERE name = 'Angie Harmon') AND episode_id = (SELECT episode_id FROM Episode WHERE series = 'Law and Order' AND season = 9 AND episode = 8 AND title = 'Punk') AND role = 'A.D.A. Abbie Carmichael' AND credited = 'true';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "INSERT INTO Award (organization, year, award_category, award, series, episode_id, person_id, role, result) VALUES ('Emmy Awards', 1999, 'Outstanding Supporting Actress in a Drama Series', 'Nominee', 'Law and Order', (SELECT episode_id FROM Episode WHERE series = 'Law and Order' AND season = 9 AND episode = 8 AND title = 'Punk'), (SELECT person_id FROM Person WHERE name = 'Angie Harmon'), 'A.D.A. Abbie Carmichael', 'Nominated');"
               }
            ),
       ],
       outputs=[]
   ),
   Task(
      user_id="74",
      instruction="You are the series database administrator. Please remove the 'camera operator' credit under the 'Camera and Electrical Department' category for Richard Dobbs (person_id: nm0229650) from episode 'Sideshow' (episode_id: tt0629422) in Law and Order. If this was his only credit in this episode, also delete his record from the Person table (person_id: nm0229650).",
       actions=[
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Credit WHERE episode_id = 'tt0629422' AND person_id = 'nm0229650' AND category = 'Camera and Electrical Department' AND role = 'camera operator';"
               }
            ),
            Action(
               name="sql",
               kwargs={
               "sql": "DELETE FROM Person WHERE person_id = 'nm0229650' AND NOT EXISTS (SELECT 1 FROM Credit WHERE person_id = 'nm0229650');"
               }
            ),
       ],
       outputs=[]
   ),
]
