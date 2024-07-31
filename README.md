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

