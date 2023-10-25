from QuestionModel import QuestionCard


class QuestionsFactory:
    cards = []

    questions = ['Да?', 'Нет?']
    answers = ['Да', 'Нет']

    def get_cards(self):
        for i, elem in enumerate(self.questions):
            self.cards.append(QuestionCard(question=elem, answer=self.answers[i]))
        return self.cards

