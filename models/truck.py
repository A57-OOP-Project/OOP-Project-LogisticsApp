from models.constants.truck_types import TruckTypes

class Truck:
   
   def __init__(self, name: str, truck_id: int):
        truck_info = TruckTypes.DATA.get(name.upper())
        if truck_info != None:
            if truck_info['ids_min'] <= truck_id <= truck_info['ids_max']:
                self._id = truck_id
            else:
                raise ValueError(f"Invalid ID for {name} truck")
            self._name = name
            self._capacity = truck_info['capacity']
            self._max_range = truck_info['max_range']
        else:
            raise ValueError("Invalid name of truck")
      
   @property
   def name(self):
      return self._name

   @property
   def id(self):
        return self._id
   
   @property
   def max_range(self):
      return self._max_range
   
   @property
   def capacity(self):
      return self._capacity
   
   # """  @capacity.setter
   # def capacity(self, value):
   #    if value >= 0:
   #       self._capacity = value
   #    else:
   #       raise ValueError("Invalid value for the capacity of the truck") """
      
   def info(self):
      return f"Truck ID: {self.id}\nName: {self.name}\nCapacity: {self.capacity} kg\nMax Range: {self.max_range} km"
   

