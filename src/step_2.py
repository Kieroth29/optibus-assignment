import csv

from json import load
from typing import List, Optional, Union

from schemas.duties import Duty, DutyEvent
from schemas.schedules import Schedule
from schemas.stops import Stop
from schemas.trips import Trip
from schemas.vehicles import Vehicle, VehicleEvent


def get_stop_description(duty: Duty, vehicles: List[Vehicle], trips: List[Trip], index: int, stops: List[Stop]):
    for event in duty.duty_events:
        if event.duty_event_type in ["taxi", "sign_on"]:
            continue

        vehicle_query = lambda vehicle: vehicle.vehicle_id == event.vehicle_id
        vehicle = list(filter(vehicle_query, vehicles))[0]

        vehicle_event_query = lambda vehicle_event: vehicle_event.vehicle_event_type == "service_trip" and vehicle_event.duty_id == duty.duty_id
        service_trip_events = list(filter(vehicle_event_query, vehicle.vehicle_events))

        if service_trip_events:
            aux_index = 0 if index > 0 else -1
            service_trip_event = service_trip_events[aux_index]

            trip_query = lambda trip: trip.trip_id == service_trip_event.trip_id
            trip = list(filter(trip_query, trips))[aux_index]

            desired_stop_id = trip.origin_stop_id if index > 0 else trip.destination_stop_id
            stop_query = lambda stop: stop.stop_id == desired_stop_id
            return list(filter(stop_query, stops))[0].stop_name


def get_vehicle_event_from_duty(duty_event: DutyEvent, vehicles: List[Vehicle]) -> Optional[Union[VehicleEvent, DutyEvent]]:
    if duty_event.duty_event_type == "service_trip":
        return None
    elif duty_event.duty_event_type in ["sign_on", "taxi"]:
        return duty_event

    vehicle_query = lambda vehicle: vehicle.vehicle_id == duty_event.vehicle_id
    vehicle = list(filter(vehicle_query, vehicles))[0]

    vehicle_event_query = lambda vehicle_event: vehicle_event.vehicle_event_sequence == duty_event.vehicle_event_sequence

    event = list(filter(vehicle_event_query, vehicle.vehicle_events))[0]

    if not event.start_time or not event.end_time:
        return None

    return event


def get_duty_events(duty: Duty, vehicles: List[Vehicle], stops: List[Stop], trips: List[Trip]) -> List[str]:
    start_event, end_event = (None, None)
    start_index, end_index = (0, -1)

    while start_event is None:
        start_event = get_vehicle_event_from_duty(duty.duty_events[start_index], vehicles)
        start_index += 1

    start_time = start_event.start_time.split(".")[1]

    while end_event is None:
        end_event = get_vehicle_event_from_duty(duty.duty_events[end_index], vehicles)
        end_index -= 1

    end_time = end_event.end_time.split(".")[1]

    return [start_time, end_time, get_stop_description(duty, vehicles, trips, start_index, stops), get_stop_description(duty, vehicles, trips, end_index, stops)]


def generate_report() -> None:
    with open("fixtures/mini_json_dataset.json", "r") as file:
        data = load(file)

    schedule = Schedule(**data)

    with open("./results/step_2.csv", "w+") as file:
        writer = csv.writer(file)

        writer.writerow(["Duty ID", "Start time", "End time", "Start stop description", "End stop description"])
        [writer.writerow([duty.duty_id] + get_duty_events(duty, schedule.vehicles, schedule.stops, schedule.trips)) for duty in schedule.duties]


if __name__ == '__main__':
    generate_report()