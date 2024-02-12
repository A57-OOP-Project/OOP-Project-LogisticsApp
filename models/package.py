from customer import Customer

class Package:
   
    def __init__(self, id, start_location, end_location, weight, contact_info):
       self._id = id
       self.start_location = start_location
       self.end_location = end_location
       self._weight = weight
       self.contact_info = contact_info
       self.expected_arrival_time = None
    
    @property
    def id(self):
        return self._id

    @property
    def weight(self):
        return self._weight

    @property
    def start_location(self):
        return self._start_location

    @start_location.setter
    def start_location(self, value):
        self._start_location = value

    @property
    def end_location(self):
        return self._end_location

    @end_location.setter
    def end_location(self, value):
        self._end_location = value

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        self._contact_info = value

    @property
    def expected_arrival_time(self):
        return self._expected_arrival_time

    @expected_arrival_time.setter
    def expected_arrival_time(self, value):
        self._expected_arrival_time = value
    
    
    def info(self):
        expected_arrival_info = f"Expected Arrival Time: {self.expected_arrival_time}" if self.expected_arrival_time is not None else ""
        return f"Package ID: {self._id}\n" \
               f"Start Location: {self.start_location}\n" \
               f"End Location: {self.end_location}\n" \
               f"Weight: {self.weight} kg\n" \
               f"Contact Info: {self.contact_info}\n" \
               f"{expected_arrival_info}"
    
    