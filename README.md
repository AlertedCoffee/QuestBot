# Gogol Day Quest
Worked at ГБОУ Лицей № 64. Quest with stations.

**Functionality:**

The user types /start and their data is entered into the database. Then, they are given a location where they need to solve a puzzle and write the answer. Answers are sent to the bot until the correct one is found. The quest is completed after all questions are answered.

During the event, prizes were awarded among those who passed the lottery.

The bot handled the load of 150 people almost without issues, except for problems with the absence of a username for the user (it errors out when attempting to log actions in print(). Be cautious when using it).

**Admin Commands:**

+ `/start_quest` - Open the acceptance of responses.
+ `/alert <text>` - Send a notification.
+ `/finish` / `/cancel_finish` - End the acceptance of responses or cancel the ending.


The project includes a Flask patch [background.py](https://github.com/AlertedCoffee/QuestBot/blob/GogolDayQuest/background.py). It was used to ping the bot every 5 minutes to prevent the host on Repl.it from sleeping.

P.S. Never engage in this nonsense; it's easier to rent a proper VDS/VPS.
