import datetime 
import os 
from collections import defaultdict

def parse_log_line(line):
    timestamp, plate, vehicle_type, action = line.strip().split(",")
    return datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f"), plate, vehicle_type, action

def calculate_parking_time(entry_time, exit_time):
    return(exit_time - entry_time).total_seconds() /3600

def analyze_parking_log(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File  '{file_path}' not found.")
        return
    
    if os.path.getsize(file_path) == 0:
        print(f"The file '{file_path}' is empty.")
        
    car_parking_times = {}
    max_count = 0
    most_frequent_car = None
    
    with open(file_path, "r") as f:
        for line in f:
            print("Line:", line.strip())
            timestamp, plate, vehicle_type, action = parse_log_line(line)
            
            if vehicle_type == "Car":
                if action == "Entry":
                    if plate in car_parking_times and isinstance(car_parking_times[plate], datetime.datetime):
                        print(f"Error: Duplicate entry for car {plate} at {timestamp}")
                        
                    else:
                        car_parking_times[plate] = timestamp
                        
                elif action == "Exit":
                    if plate in car_parking_times and isinstance(car_parking_times[plate], datetime.datetime):
                        exit_time = timestamp
                        parking_time = calculate_parking_time(car_parking_times[plate], exit_time)
                        car_parking_times[plate] = parking_time
                        
                        if parking_time > max_count:
                            max_count = parking_time
                            most_frequent_car = plate
    
    if max_count > 0:
        print(f"Car {most_frequent_car} has been parked the most, {max_count:.2f} hours")
    else:
        print("No cars found in the log")
        
    total_parking_time = 0
    car_count = 0
        
    for plate, time in car_parking_times.items():
        if isinstance(time, float):
            total_parking_time += time
            car_count += 1
        
    if car_count > 0:
        average_parking_time = total_parking_time / car_count
        print(f"Average parking time for cars: {average_parking_time:.2f} hours")
    else:
        print("No cars found to calculate average time")
            
file_path = "parking_log.txt"
analyze_parking_log(file_path)