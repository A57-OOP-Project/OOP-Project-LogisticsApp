#       SYD	    MEL	    ADL	    ASP	    BRI	    DAR	    PER
# SYD	        877	    1376	2762	909	    3935	4016
# MEL	877		        725	    2255	1765	3752	3509
# ADL	1376	725		        1530	1927	3027	2785
# ASP	2762	2255	1530	        2993	1497	2481
# BRI	909	    1765	1927	2993	        3426	4311
# DAR	3935	3752	3027	1497	3426	        4025
# PER	4016	3509	2785	2481	4311	4025    0 
# SYD = SYDNEY
# MEL = MELBOURNE
# ADL = ADELAIDE
# ASP = ALICE SPRINGS
# BRI = BRISBANE
# DAR = DARWIN
# PER = PERTH

class Distances:
  
    distances = {
    'SYD': {'SYD': 0, 'MEL': 877, 'ADL': 1376, 'ASP': 2762, 'BRI': 909, 'DAR': 3935, 'PER': 4016},
    'MEL': {'SYD': 877, 'MEL': 0, 'ADL': 725, 'ASP': 2255, 'BRI': 1765, 'DAR': 3752, 'PER': 3509},
    'ADL': {'SYD': 1376, 'MEL': 725, 'ADL': 0, 'ASP': 1530, 'BRI': 1927, 'DAR': 3027, 'PER': 2785},
    'ASP': {'SYD': 2762, 'MEL': 2255, 'ADL': 1530, 'ASP': 0, 'BRI': 2993, 'DAR': 1497, 'PER': 2481},
    'BRI': {'SYD': 909, 'MEL': 1765, 'ADL': 1927, 'ASP': 2993, 'BRI': 0, 'DAR': 3426, 'PER': 4311},
    'DAR': {'SYD': 3935, 'MEL': 3752, 'ADL': 3027, 'ASP': 1497, 'BRI': 3426, 'DAR': 0, 'PER': 4025},
    'PER': {'SYD': 4016, 'MEL': 3509, 'ADL': 2785, 'ASP': 2481, 'BRI': 4311, 'DAR': 4025, 'PER': 0}
    }
    
    @classmethod
    def calculate_distance(cls, locations: list[str]):
        distance = 0
        for i in range(len(locations) - 1):
            distance += cls.distances[locations[i]][locations[i + 1]]
        
        return distance
