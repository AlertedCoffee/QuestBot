from Model.StationModel import StationCard


class StationsFactory:
    cards = []

    stations = ['Актовый зал', 'Холл второго этажа', 'Холл третьего этажа', 'Пианино на четвертом этаже',
                'Большой спортивный зал', 'Библиотека', 'Холл перед столовой', 'Лабиринт шкафчиков']
    answers = ['сорочинцы', 'Потемкин', 'Яновский', 'Ревизор',
               'Алов', 'месяц', 'Пушкин', 'голова']

    def get_cards(self) -> list[StationCard]:
        for i, elem in enumerate(self.stations):
            self.cards.append(StationCard(station_name=elem, answer=self.answers[i]))
        return self.cards
