# Infirmatics Day Quest
Worked at the СПбПУ ИСПО

**Functionality:**

The user registers and selects their department. Then, they receive questions (10 from the first category, 5 from the second). The user submits their answers without knowing if they are correct. The results and response times are recorded in the database. Winners are determined by the number of points, and in the case of a tie, the fastest respondent gets an advantage in the leaderboard.

The bot successfully handled a load of 256 users without any issues.

**Admin Commands:**

+ `/open` / `/close` - Open and close the acceptance of responses.
+ `/alert <text>` - Send a notification.
+ `/alert to <id> <text>` - Send a notification to a specific user.
+ `/leaders` - Display the leaderboard.
+ `/finish` / `/cancel_finish` - End the acceptance of responses or cancel the ending.

---

**Compared to the previous version:**
+ The structure has been slightly improved.
+ The database and progress saving algorithm have been reworked.
+ Questions now have categories, and there is only one attempt per question.
+ More admin commands have been added.
