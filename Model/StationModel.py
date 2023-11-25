class StationCard:
    question = ''
    answer = ''
    group: int
    id: int

    def __init__(self, station_name: str, answer: str, group: int, id: int):
        self.question = station_name
        self.answer = answer.strip().lower()
        self.group = group
        self.id = id

    def check_answer(self, answer: str):
        if self.answer == answer.strip().lower():
            return True
        else:
            return False

