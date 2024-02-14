from datetime import datetime


class Location:
    def __init__(self, city: str, time: datetime):
        self._city = city 
        self._time = time
        self.capacity = None
        
    
    @property
    def city(self):
        return self._city
    
    @property
    def time(self):
        return self._time
    
    
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value
        
        
    