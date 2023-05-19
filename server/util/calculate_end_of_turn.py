
import datetime


def calculate_end_of_turn(self, start_time, duration_turn, format_hours) -> str:    
    
    return str(datetime.datetime.strptime(
                start_time, format_hours) + duration_turn - datetime.datetime(1900, 1, 1))
    pass