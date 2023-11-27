from Model.StationModel import StationCard


class StationsFactory:
    cards_first_group = []
    cards_second_group = []
    cards_third_group = []

    questions_1 = ["""Информацию, изложенную на доступном для получателя языке, называют…
a)      понятной;
b)      актуальной;
c)      достоверной;
d)      полной.
""",
                   """Наибольший объем информации человек получает при помощи…
a)      вкусовых рецепторов;
b)      органов осязания;
c)      органов зрения;
d)      органов слуха;
e)      органов обоняния.
""",
                   """К формальным языкам можно отнести…
a)      язык программирования;
b)      русский язык;
c)      китайский язык;
d)      язык жестов.
""",
                   """Материальный объект, предназначенный для хранения информации, называется…
a)      носитель информации;
b)      получатель информации;
c)      хранитель информации;
d)      канал связи.
""",
                   """В какой из последовательностей единицы измерения указаны в порядке возрастания
a)      мегабайт, килобайт, байт, гигабайт;
b)      байт, килобайт, мегабайт, гигабайт;
c)      гигабайт, килобайт, мегабайт, байт;
d)      гигабайт, мегабайт, килобайт, байт.
""",
                   """Процесс представления информации (сообщения) в виде кода называется… 
a)      декодированием;
b)      дешифрованием;
c)      кодированием;
d)      дискретизацией.
""",
                   'Является ли верным утверждение: "В позиционной системе счисления количественный '
                   'Эквивалент цифры зависит от места цифры в записи числа"? да/нет?',
                   'Алфавит системы счисления 0, 1, 2, 3, 4, 5. Какая это система счисления?',
                   """Двоичное число 1001 соответствует десятичному числу… 
a)      1001;
b)      6;
c)      9;
d)      8.
""",
                   """Найти двоичный эквивалент числа Х, представленного в десятичной системе счисления, если Х = 5. 
a)      110;
b)      101;
c)      1001;
d)      11.
""",
                   """Укажите самое большое число (в  скобках система счисления).
a)      144 (16);
b)      144 (10);
c)      144 (6);
d)      144 (8).
""",
                   """Изображение представляющее собой совокупность точек (пикселей) разных цветов называется…
a)      векторным;
b)      цветным;
c)      аналоговым;
d)      растровым.
""",
                   """Многопроходная линия для информационного обмена между устройствами компьютера называется… 
a)      модемом;
b)      контроллером;
c)      магистралью;
d)      провайдером.
""",
                   """Устройством ввода информации является…
a)      сканер;
b)      дисковод;
c)      принтер;
d)      клавиатура.
""",
                   """Комплекс взаимосвязанных программ, обеспечивающий пользователю удобный способ общения с программами, называется…
a)      утилитой;
b)      драйвером;
c)      интерпретатором;
d)      интерфейсом.
""",
                   """Расширение имени файла характеризует…
a)      время создания файла;
b)      тип информации, содержащейся в файле;
c)      объем файла;
d)      место, занимаемое файлом на диске.
""",
                   """Архивный файл представляет собой… 
a)      файл, которым долго не пользовались;
b)      файл, защищенный от несанкционированного доступа;
c)      файл, защищенный от копирования;
d)      файл, сжатый с помощью архиватора.
""",
                   """По среде обитания компьютерные вирусы классифицируют на… 
a)      неопасные, опасные и очень опасные;
b)      паразиты, репликаторы, невидимки, мутанты, троянские;
c)      сетевые, файловые, загрузочные, макровирусы.
""",
                   """К антивирусным программам не относятся…
a)      интерпретаторы;
b)      фаги;
c)      ревизоры;
d)      сторожа.
""",
                   """В каком году появилась первая ЭВМ? 
a)      1823;
b)      1951;
c)      1980;
d)      1905.
""",
                   """На какой электронной основе созданы ЭВМ I поколения? 
a)      транзисторы;
b)      электронно-вакуумные лампы;
c)      зубчатые колеса;
d)      реле.
""",
                   """Плоттер – это разновидность...
a) клавиатуры
b) принтера
c) монитора
d) сканера
""",
                   """Выберите неверный ответ. Принтер может быть подключён к компьютеру…
a) с помощью кабеля USB
b) через беспроводную сеть Wi-Fi
c) через локальную сеть
d) с помощью тонера
"""]
    answers_1 = ['a', 'c', 'a', 'a', 'b', 'c', 'да', 'шестеричная', 'c', 'b', 'a', 'd', 'c', 'd', 'd', 'b', 'd', 'c',
                 'a', 'b', 'b', 'b', 'd']

    questions_2 = ["""1) Термин «алгоритм» происходит от имени выдающегося учёного…
a) Авиценны
b) Аль-Бируни
c) Аль-Хорезми
d) Улугбека
""",
                   'Если X>2 и X<8, то Y=X+2, иначе Y=X–2. Чему равен Y, если X=4?',
                   """Один из мостов – контроллеров материнской платы компьютера называют...
a) северным
b) восточным
c) вычислительным
d) транспортным
""",
                   """Какое расширение имеют исполняемые файлы в операционных системах семейства Windows? (ответ без точки)""",
                   """Какой из ответов представляет из себя IP-адрес
a) 87.236.19.119
b) 34.89.45
c) ааа@ааа.ru
d) www.ааа.ru
""",
                   """Сообщение, уменьшающее неопределенность знаний в два раза, несет…
a)      1 бит;
b)      4 бита;
c)      1 байт;
d)      2 бита.
""",
                   """Сколько информации несет сообщение длиной 32 символа, если алфавит языка состоит из 16 знаков? 
a)      16 бит;
b)      128 бит;
c)      256 бит;
d)      80 бит.
""",
                   """Сколько байт в словах «информационные технологии» (без учета кавычек)?
a)      24 байта;
b)      192 байт;
c)      25 байт;
d)      2 байта.
""",
                   """Сколько байт в 4 Мбайт?
a)      4000;
b)      2^22;
c)      2^12;
d)      4^20.
""",
                   """Какое число лишнее? (в скобках система счисления)
a)      11111111 (2);
b)      377 (8);
c)      FF (16);
d)      226 (10).
""",
                   """Сложите числа 5А(16)+43(8)+111(2)+5(10), результат получите в двоичной системе счисления (в скобках система счисления).
a)      11110001;
b)      10000011;
c)      10001001;
d)      10011101.
""",
                   """Пусть небольшая книжка, сделанная с помощью компьютера, содержит 15 страниц; на каждой странице — 40 строк, в каждой строке — 60 символов. Сколько информации она содержит?
a)      36000 байт;
b)      19200 байт;
c)      256 бит;
d)      2400 байт
""",
                   """Задано 2 функции: min(a, b) возвращает минимальное значение из a и b, и max(a, b) возвращает максимальное значение из a и b. Какое из выражений возвращает минимальное значение для любых a, b, c?
a) min(min(max(a, b), min(b, c)), min(а, c))
b) min(min(a, b), max(b, c))
c) max(min(a, b), min(b, c))
d) min(max(a, b), max(b, c))
""",
                   """Трехзначное число состоит из цифр 1, 2, 3. У данного числа и у чисел 231 и 312 одинаковых цифр в совпадающих разрядах нет. какое это число?""",
                   """В детском саду на завтрак готовят 3 разные каши: гречневая, манная и овсяная. В группе из 31 детей, каждый ест одну или все 3 каши. Гречневую едят 17 человек, манную – 15 человек, овсяную – 11 человек. Сколько детей любят все 3 каши """,
                   """Спутник навигации может определить расстояние до пользователя, тем самым может определить положение пользователя на земном шаре. 
Какое минимальное количество спутников необходимо в общем случае для определения положения пользователя, находящегося в поле видимости каждого из них?""",
                   """По правилам игры необходимо задумывать трёхзначное число из цифр 1, 2, 3, где каждая цифра обязана быть использована по одному разу. Игрок пытается отгадать это число, называя свои варианты чисел и получая после каждого ответ о числе разрядов, в которых у задуманного и предложенного чисел стоят одинаковые цифры. 
За какое минимальное количество попыток можно гарантированно определит задуманное число?""",
                   """Автор алгоритма сжатия RAR:
a) Чарльз Бэббидж
b) Евгений Рошал
c) Билл Гейтс
d) Евгений Касперский
""",
                   """Первый программист
a) Ада Лавлейс
b) Стив Джобс
c) Уильям Билл Гейтс
d) Дуглас Карл
"""]

    answers_2 = ['c', '6', 'a', 'exe', 'a', 'a', 'b', 'c', 'b', 'd', 'c', 'a', 'a', '123', '6', '3', '3', 'b', 'a']

    questions_3 = ['2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7']
    answers_3 = ['2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7']

    def get_cards_first_group(self) -> list[StationCard]:
        if not self.cards_first_group:
            for i, elem in enumerate(self.questions_1):
                self.cards_first_group.append(StationCard(station_name=elem, answer=self.answers_1[i], group=0, id=i))
        return self.cards_first_group

    def get_cards_second_group(self) -> list[StationCard]:
        if not self.cards_second_group:
            for i, elem in enumerate(self.questions_2):
                self.cards_second_group.append(StationCard(station_name=elem, answer=self.answers_2[i], group=1, id=i))
        return self.cards_second_group

    def get_cards_third_group(self) -> list[StationCard]:
        if not self.cards_third_group:
            for i, elem in enumerate(self.questions_3):
                self.cards_third_group.append(StationCard(station_name=elem, answer=self.answers_3[i], group=2, id=i))
        return self.cards_third_group
