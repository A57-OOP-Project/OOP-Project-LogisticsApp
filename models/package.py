class Package:
    def __init__(self, id, start_location, end_location, weight, contact_info):
        self._id = id
        self._start_location = start_location
        self._end_location = end_location
        self._weight = weight
        self._contact_info = contact_info
        self._expected_arrival_time = None

    @property
    def id(self):
        return self._id

    @property
    def start_location(self):
        return self._start_location

    @property
    def end_location(self):
        return self._end_location

    @property
    def weight(self):
        return self._weight

    @property
    def contact_info(self):
        return self._contact_info

    @property
    def get_expected_arrival_time(self):
        return self._expected_arrival_time

    def set_expected_arrival_time(self, expected_arrival_time):
        self._expected_arrival_time = expected_arrival_time
        
    def info(self):
        return f"Package ID: {self._id}\nStart Location: {self._start_location}\nEnd Location: {self._end_location}\nWeight: {self._weight}\nContact Info: {self._contact_info}\nExpected Arrival Time: {self._expected_arrival_time}"