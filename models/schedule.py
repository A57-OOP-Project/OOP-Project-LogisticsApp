
from datetime import datetime
#from core.application_data import ApplicationData



class Schedule:
   # dictionary where the keys are truck ids and the values are lists of routes ids assigned to each truck 
   DATA = {}  #{truck_id : [route1_id, route2_id, route3_id]}   
    
    
   @classmethod
   def add_route(cls, truck_id, route_id): 
        if truck_id in cls.DATA:
            cls.DATA[truck_id].append(route_id)
        else:
            cls.DATA[truck_id] = [route_id]    
       
        
#    @classmethod
#    def update_route(cls, truck_id, route_id):
#        if truck_id in cls.DATA and route_id in cls.DATA[truck_id]:
#            cls.DATA[truck_id].remove(route_id)
#        else:
#            raise ValueError('Invalid truck id or route id') 
      
    
#    @classmethod
#    def is_conflict(cls, truck_id, route_id_number) -> bool:
#        if truck_id not in cls.DATA or route_id_number not in cls.DATA[truck_id]:
#            raise ValueError('Invalid truck id or route id')
#        new_route = ApplicationData.find_route_by_id(route_id_number)
#        start_time_new_route = new_route.locations[0].time
#        end_time_new_route = new_route.locations[-1].time
            
#        for route_id in cls.DATA[truck_id]:
#            route_in_schedule = ApplicationData.find_route_by_id(route_id)
#            start_time_route_in_schedule = route_in_schedule.locations[0].time
#            end_time_route_in_schedule = route_in_schedule.locations[-1].time
#            if start_time_route_in_schedule <= end_time_new_route and end_time_route_in_schedule >= start_time_new_route:
#                return True
           
#        return False
    
   @classmethod
   def info(cls):
       if not cls.DATA:
           return ''
       schedule_info = [f'The schedule for the trucks that are currently involved:']
       for truck_id, route_ids in cls.DATA.items():
            schedule_info.append(f'Truck id #{truck_id} is assigned to the following routes: {", ".join(map(str, route_ids))}')
    
       return "\n".join(schedule_info)  
       
            
             
               
           