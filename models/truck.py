class Truck:
   SCANIA_CAPACITY = 42000
   SCANIA_MAX_RANGE = 8000
   SCANIA_IDS_MIN = 1001
   SCANIA_IDS_MAX = 1010

   MAN_CAPACITY = 37000
   MAN_MAX_RANGE = 10000
   MAN_IDS_MIN = 1011
   MAN_IDS_MAX = 1025

   ACTROS_CAPACITY = 26000
   ACTROS_MAX_RANGE = 13000
   ACTROS_IDS_MIN = 1026
   ACTROS_IDS_MAX = 1040

   def __init__(self, name: str, truck_id: int):
      if name.lower() == "scania":
         if Truck.SCANIA_IDS_MIN <= truck_id <= Truck.SCANIA_IDS_MAX:
             self._truck_id = truck_id
         else:
            raise ValueError("Invalid ID for Scania truck")
         self._name = name
         self._capacity = Truck.SCANIA_CAPACITY
         self._max_range = Truck.SCANIA_MAX_RANGE
      elif name.lower() == "man":
         if Truck.MAN_IDS_MIN <= truck_id <= Truck.MAN_IDS_MAX:
             self._truck_id = truck_id
         else:
            raise ValueError("Invalid ID for Man truck")
         self._name = name
         self._capacity = Truck.MAN_CAPACITY
         self._max_range = Truck.MAN_MAX_RANGE
      elif name.lower() == "actros":
         if Truck.ACTROS_IDS_MIN <= truck_id <= Truck.ACTROS_IDS_MAX:
             self._truck_id = truck_id
         else:
            raise ValueError("Invalid ID for Actros truck")
         self._name = name
         self._capacity = Truck.ACTROS_CAPACITY
         self._max_range = Truck.ACTROS_MAX_RANGE
      else:
         raise ValueError("Invalid name of truck")
      
   @property
   def name(self):
      return self._name

   @property
   def truck_id(self):
        return self._truck_id
   
   @property
   def capacity(self):
      return self._capacity
   
   @property
   def max_range(self):
      return self._max_range


         
         