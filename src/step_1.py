import csv

from json import load
from typing import List

from schemas.duties import Duty
from schemas.vehicles import Vehicle, VehicleEvent


def get_duty_start_time(duty: Duty, vehicles: List[Vehicle]) -> str:
    first_event = duty.duty_events[0]

    if first_event.start_time:
        return first_event.start_time.split('.')[1]
    
    vehicle_query = lambda vehicle: vehicle.vehicle_id == first_event.vehicle_id
    vehicle = list(filter(vehicle_query, vehicles))[0]

    vehicle_event_query = lambda vehicle_event: vehicle_event.vehicle_event_sequence == first_event.vehicle_event_sequence
    vehicle_event: VehicleEvent = list(filter(vehicle_event_query, vehicle.vehicle_events))[0]

    return vehicle_event.start_time.split('.')[1]


def get_duty_end_time(duty: Duty, vehicles: List[Vehicle]) -> str:
    last_event = duty.duty_events[-1]

    if last_event.end_time:
        return last_event.end_time.split('.')[1]
    
    vehicle_query = lambda vehicle: vehicle.vehicle_id == last_event.vehicle_id
    vehicle = list(filter(vehicle_query, vehicles))[0]

    vehicle_event_query = lambda vehicle_event: vehicle_event.vehicle_event_sequence == last_event.vehicle_event_sequence
    vehicle_event: VehicleEvent = list(filter(vehicle_event_query, vehicle.vehicle_events))[0]

    return vehicle_event.end_time.split('.')[1]


def generate_report() -> None:
    with open('fixtures/mini_json_dataset.json', 'r') as file:
        data = load(file)

    duties = [Duty(**duty) for duty in data['duties']]
    vehicles = [Vehicle(**vehicle) for vehicle in data['vehicles']]

    with open('./results/step_1.csv', 'w+') as file:
        writer = csv.writer(file)

        writer.writerow(['Duty ID', 'Start time', 'End time'])
        [writer.writerow([duty.duty_id, get_duty_start_time(duty, vehicles), get_duty_end_time(duty, vehicles)]) for duty in duties]


if __name__ == '__main__':
    generate_report()