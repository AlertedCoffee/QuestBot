class StationCard:
    question = ''
    answer = ''

    def __init__(self, station_name: str, answer: str):
        self.question = station_name.strip().lower()
        self.answer = answer.strip().lower()

    def check_answer(self, answer: str):
        if self.answer == answer.strip().lower():
            return True
        else:
            return False

