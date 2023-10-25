from Model.StationModel import StationCard


class StationsFactory:
    cards = []

    questions = ['Станция 1', 'Станция 2', 'Станция 3', 'Станция 4', 'Станция 5']
    answers = ['Да', 'Нет', 'Нет', 'Нет', 'Нет']

    def get_cards(self) -> list[StationCard]:
        for i, elem in enumerate(self.questions):
            self.cards.append(StationCard(question=elem, answer=self.answers[i]))
        return self.cards

