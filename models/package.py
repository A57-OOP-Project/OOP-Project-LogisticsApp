#from customer import Customer

class Package:
   
    def __init__(self, id: int, start_location: str, end_location: str, weight: int, contact_info: str):
       self._id = id
       self.start_location = start_location
       self.end_location = end_location
       self._weight = weight
       self.contact_info = contact_info
       self.route = None # the attribute self.route is initially None(before the package is assigned to some route)
       self.expected_arrival_time = None
    
    @property
    def id(self) -> int:
        return self._id

    @property
    def weight(self) -> int:
        return self._weight

    @property
    def start_location(self) ->str:
        return self._start_location

    @start_location.setter
    def start_location(self, value):
        self._start_location = value

    @property
    def end_location(self) ->str:
        return self._end_location

    @end_location.setter
    def end_location(self, value):
        self._end_location = value

    @property
    def contact_info(self) -> str:
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        self._contact_info = value

    @property
    def expected_arrival_time(self) -> str:
        return self._expected_arrival_time

    @expected_arrival_time.setter
    def expected_arrival_time(self, value):
        self._expected_arrival_time = value
        
    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, value):
        self._route = value
    
    
    def info(self):
        
        '''
        The method generates and returns a formatted string containing information about a package
        
        '''
        if (self.route is not None) and (self.expected_arrival_time is not None):
            expected_arrival_info = f"Expected Arrival Time: {self.expected_arrival_time}"
        else:
            expected_arrival_info = f"Currently the package id #{self._id} is not assigned to any route"
            
        return f"Package ID: {self._id}\n" \
               f"Start Location: {self.start_location}\n" \
               f"End Location: {self.end_location}\n" \
               f"Weight: {self.weight} kg\n" \
               f"Contact Info: {self.contact_info}\n" \
               f"{expected_arrival_info}"
    
    