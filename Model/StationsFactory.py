from Model.StationModel import StationCard


class StationsFactory:
    cards_first_group = []
    cards_second_group = []
    cards_third_group = []

    questions_1 = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7']
    answers_1 = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7']

    questions_2 = ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7']
    answers_2 = ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7']

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
