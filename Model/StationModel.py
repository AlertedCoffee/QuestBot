class StationCard:
    station_name = ''
    answer = ''

    def __init__(self, station_name: str, answer: str):
        self.station_name = station_name.strip().lower()
        self.answer = answer.strip().lower()

    def check_answer(self, answer: str):
        if self.answer == answer.strip().lower():
            return True
        else:
            return False

