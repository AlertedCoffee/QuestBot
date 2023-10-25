from Model.QuestionModel import QuestionCard


class QuestionsFactory:
    cards = []

    questions = ['Станция 1', 'Станция 2', 'Станция 3']
    answers = ['Да', 'Нет', 'Нет']

    def get_cards(self) -> list[QuestionCard]:
        for i, elem in enumerate(self.questions):
            self.cards.append(QuestionCard(question=elem, answer=self.answers[i]))
        return self.cards

