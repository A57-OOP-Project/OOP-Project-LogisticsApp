
class TruckTypes:
    
    DATA = {
        'SCANIA': {
            'capacity': 42000,
            'max_range': 8000,
            'ids_min': 1001,
            'ids_max': 1010
        },
        'MAN': {
            'capacity': 37000,
            'max_range': 10000,
            'ids_min': 1011,
            'ids_max': 1025
        },
        'ACTROS': {
            'capacity': 26000,
            'max_range': 13000,
            'ids_min': 1026,
            'ids_max': 1040
        }
    }
    
    @classmethod
    def format_truck_info(cls, suitable_trucks: list, unsuitable_trucks: set):
        truck_info = []
        for truck_type, ids_range in [('Scania', (1001, 1011)), ('Man', (1011, 1026)), ('Actros', (1026, 1041))]:
            if truck_type.upper() in unsuitable_trucks:
                continue
            truck_ids = [truck_id for truck_id in suitable_trucks if truck_id in range(*ids_range)]
            truck_info.append(f"Name: {truck_type}, Capacity: {cls.DATA[truck_type.upper()]['capacity']} kg, Max Range: {cls.DATA[truck_type.upper()]['max_range']} km\nTruck IDs: {', '.join(map(str, truck_ids))}")
        return f"Available trucks with appropriate capacity and range:\n{'\n'.join(truck_info)}"