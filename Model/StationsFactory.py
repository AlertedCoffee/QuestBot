from Model.StationModel import StationCard


class StationsFactory:
    cards_first_group = []
    cards_second_group = []
    cards_third_group = []

    questions_1 = ['Кто проживает на дне океана', 'Холл второго этажа', 'Холл третьего этажа', 'Пианино на четвертом этаже',
                'Большой спортивный зал', 'Библиотека', 'Холл перед столовой', 'Лабиринт шкафчиков']
    answers_1 = ['Спанч Боб', 'Потемкин', 'Яновский', 'Ревизор',
               'Алов', 'месяц', 'Пушкин', 'голова']

    questions_2 = ['Кто проживает на дне океана', 'Холл второго этажа', 'Холл третьего этажа', 'Пианино на четвертом этаже',
                  'Большой спортивный зал', 'Библиотека', 'Холл перед столовой', 'Лабиринт шкафчиков']
    answers_2 = ['Спанч Боб', 'Потемкин', 'Яновский', 'Ревизор',
                 'Алов', 'месяц', 'Пушкин', 'голова']

    questions_3 = ['Кто проживает на дне океана', 'Холл второго этажа', 'Холл третьего этажа', 'Пианино на четвертом этаже',
                  'Большой спортивный зал', 'Библиотека', 'Холл перед столовой', 'Лабиринт шкафчиков']
    answers_3 = ['Спанч Боб', 'Потемкин', 'Яновский', 'Ревизор',
                 'Алов', 'месяц', 'Пушкин', 'голова']

    def get_cards_first_group(self) -> list[StationCard]:
        if not self.cards_first_group:
            for i, elem in enumerate(self.questions_1):
                self.cards_first_group.append(StationCard(station_name=elem, answer=self.answers_1[i]))
        return self.cards_first_group

    def get_cards_second_group(self) -> list[StationCard]:
        if not self.cards_second_group:
            for i, elem in enumerate(self.questions_2):
                self.cards_second_group.append(StationCard(station_name=elem, answer=self.answers_2[i]))
        return self.cards_second_group

    def get_cards_third_group(self) -> list[StationCard]:
        if not self.cards_third_group:
            for i, elem in enumerate(self.questions_3):
                self.cards_third_group.append(StationCard(station_name=elem, answer=self.answers_3[i]))
        return self.cards_third_group
