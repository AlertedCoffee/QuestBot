# QuestBot 
### Репозиторий тг бота для квестов на aiogram 

В репозитории три ветки, в каждой из который есть свой README.md: 
+ [master](https://github.com/AlertedCoffee/QuestBot/tree/master) - особо ничего не скажешь главная ветка, либо буду дальше плясать от нее, либо от других; 
+ [GogolDayQuest](https://github.com/AlertedCoffee/QuestBot/tree/GogolDayQuest) - квет посвященный Дню Гоголя завуалированный Halloween ([@gogol_quest_bot](https://t.me/gogol_quest_bot) скорее всего не запущен сейчас);
+ [InformaticsDayQuest](https://github.com/AlertedCoffee/QuestBot/tree/InformaticsDayQuest) - квест ко Дню Информатики, по сути викторина ([@informatics_quest_bot](https://t.me/informatics_quest_bot) скорее всего не запущен сейчас).

<br>

Чтобы собрать сие творения в корень нужны файлы:
+ _userbase.db_ <br> Инициализация чистой базы происходит через [DB.py](https://github.com/AlertedCoffee/QuestBot/blob/master/DB.py) и метод `create_table()`  
+ _.env_ <br>
`TEST_TOKEN='yourtesttoken'` <br>
`MASTER_TOKEN='yourprodtoken'`
+ ну и окружение с библиотеками в зависимости от ветки

<br>
_________________________________________________________________________

### Repository for a quest Telegram bot using aiogram 

There are three branches in the repository, each with its own README.md: 
+ [master](https://github.com/AlertedCoffee/QuestBot/tree/master) - Not much to say here, this is the main branch. I might continue from this one or from others; 
+ [GogolDayQuest](https://github.com/AlertedCoffee/QuestBot/tree/GogolDayQuest) - A quest dedicated to Gogol Day, disguised as Halloween ([@gogol_quest_bot](https://t.me/gogol_quest_bot) is likely not running now);
+ [InformaticsDayQuest](https://github.com/AlertedCoffee/QuestBot/tree/InformaticsDayQuest) - A quest for Informatics Day, essentially a quiz ([@informatics_quest_bot](https://t.me/informatics_quest_bot) is likely not running now).

<br>

To assemble these creations in the root, the following files are needed:
+ _userbase.db_ <br> The initialization of a clean database is done through [DB.py](https://github.com/AlertedCoffee/QuestBot/blob/master/DB.py) and the method `create_table()`  
+ _.env_ <br>
`TEST_TOKEN='yourtesttoken'` <br>
`MASTER_TOKEN='yourprodtoken'`
+ And the environment with libraries depending on the branch

