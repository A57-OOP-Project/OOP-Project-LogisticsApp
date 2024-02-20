
from datetime import datetime
#from core.application_data import ApplicationData



class Schedule:
   # dictionary where the keys are truck ids and the values are lists of routes ids assigned to each truck 
   DATA = {}  #{truck_id : [route1_id, route2_id, route3_id]}   
    
    
   @classmethod
   def add_route(cls, truck_id: int, route_id: int): 
        '''
         The method is responsible for adding a route ID to the list of routes assigned to a particular truck ID in the DATA dictionary.
    '''
        if truck_id in cls.DATA:
            cls.DATA[truck_id].append(route_id)
        else:
            cls.DATA[truck_id] = [route_id]    # Q - I do not understand this. What format does it result it? 
       
            
    
   @classmethod
   def info(cls):
       '''
       The method is responsible for generating information about the current schedule of trucks and their assigned routes.
       It returns generated schedule information string.
       '''
       if not cls.DATA:
           return ''
       schedule_info = [f'The schedule for the trucks that are currently involved:']
       for truck_id, route_ids in cls.DATA.items():
            schedule_info.append(f'Truck id #{truck_id} is assigned to the following routes: {", ".join(map(str, route_ids))}')
    
       return "\n".join(schedule_info)  
       
 
#    @classmethod
#    def update_route(cls, truck_id, route_id):
#        if truck_id in cls.DATA and route_id in cls.DATA[truck_id]:
#            cls.DATA[truck_id].remove(route_id)
#        else:
#            raise ValueError('Invalid truck id or route id')            
             
               
           