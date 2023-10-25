class StationCard:
    station_name = ''
    answer = ''

    def __init__(self, question: str, answer: str):
        self.station_name = question.strip().lower()
        self.answer = answer.strip().lower()

    def check_answer(self, answer: str):
        if self.answer == answer.strip().lower():
            return True
        else:
            return False

