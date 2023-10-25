class QuestionCard:
    question = ''
    answer = ''

    def __init__(self, question: str, answer: str):
        self.question = question.strip().lower()
        self.answer = answer.strip().lower()

    def check_answer(self, answer: str):
        if self.answer == answer.strip().lower():
            return True
        else:
            return False

