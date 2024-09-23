import csv

from json import load
from typing import Dict, List, Optional, Union

from schemas.duties import Duty, DutyEvent
from schemas.schedules import Break, Report, Schedule
from schemas.stops import Stop
from schemas.trips import Trip
from schemas.vehicles import Vehicle, VehicleEvent

from datetime import datetime, time, timedelta


def get_stop_name(stop_id: str, stops: List[Stop]) -> str:
    stop_query = lambda stop: stop.stop_id == stop_id
    return list(filter(stop_query, stops))[0].stop_name


def get_vehicle(vehicle_id: str, vehicles: List[Vehicle]) -> Vehicle:
    vehicle_query = lambda vehicle: vehicle.vehicle_id == vehicle_id
    return list(filter(vehicle_query, vehicles))[0]


def get_vehicle_events(query: filter, vehicle_events: List[VehicleEvent]) -> List[VehicleEvent]:
    return list(filter(query, vehicle_events))


def get_break_time(event_time: str) -> time:
    event_time = event_time.split(".")
    event_time_day_offset = int(event_time[0])
    event_time = datetime.strptime(event_time[1], '%H:%M')
    
    if event_time_day_offset > 0:
        event_time += timedelta(days=1)

    return event_time.time()

def get_duty_breaks(duty: Duty, vehicles: List[Vehicle], stops: List[Stop]) -> List[Dict]:
    breaks = []
    
    for event in duty.duty_events:
        if event.duty_event_type != "vehicle_event":
            continue

        vehicle = get_vehicle(event.vehicle_id, vehicles)
        vehicle_event_query = lambda vehicle_event: vehicle_event.vehicle_event_type == "deadhead" and vehicle_event.duty_id == duty.duty_id
        deadhead_events = get_vehicle_events(vehicle_event_query, vehicle.vehicle_events)

        for event in deadhead_events:
            start_time = get_break_time(event.start_time)
            end_time = get_break_time(event.end_time)
            
            duration = (datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), start_time)).total_seconds() / 60
            
            if duration > 15:
                breaks.append(Break(**{
                    "start_time": start_time,
                    "duration": duration,
                    "stop_name": get_stop_name(event.origin_stop_id, stops)
                }))

    return breaks


def get_stop_description(duty: Duty, vehicles: List[Vehicle], trips: List[Trip], index: int, stops: List[Stop]):
    for event in duty.duty_events:
        if event.duty_event_type in ["taxi", "sign_on"]:
            continue

        vehicle = get_vehicle(event.vehicle_id, vehicles)

        vehicle_event_query = lambda vehicle_event: vehicle_event.vehicle_event_type == "service_trip" and vehicle_event.duty_id == duty.duty_id
        service_trip_events = get_vehicle_events(vehicle_event_query, vehicle.vehicle_events)

        if service_trip_events:
            aux_index = 0 if index > 0 else -1
            service_trip_event = service_trip_events[aux_index]

            trip_query = lambda trip: trip.trip_id == service_trip_event.trip_id
            trip = list(filter(trip_query, trips))[aux_index]

            desired_stop_id = trip.origin_stop_id if index > 0 else trip.destination_stop_id
            
            return get_stop_name(desired_stop_id, stops)


def get_vehicle_event_from_duty(duty_event: DutyEvent, vehicles: List[Vehicle]) -> Optional[Union[VehicleEvent, DutyEvent]]:
    if duty_event.duty_event_type == "service_trip":
        return None
    elif duty_event.duty_event_type in ["sign_on", "taxi"]:
        return duty_event

    vehicle_query = lambda vehicle: vehicle.vehicle_id == duty_event.vehicle_id
    vehicle = list(filter(vehicle_query, vehicles))[0]

    vehicle_event_query = lambda vehicle_event: vehicle_event.vehicle_event_sequence == duty_event.vehicle_event_sequence

    event = get_vehicle_events(vehicle_event_query, vehicle.vehicle_events)[0]

    if not event.start_time or not event.end_time:
        return None

    return event


def get_duty_report(duty: Duty, vehicles: List[Vehicle], stops: List[Stop], trips: List[Trip]) -> Report:
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

    return Report(**
        {
            "start_time": start_time, 
            "end_time": end_time, 
            "start_stop_description": get_stop_description(duty, vehicles, trips, start_index, stops), 
            "end_stop_description": get_stop_description(duty, vehicles, trips, end_index, stops), 
            "breaks": get_duty_breaks(duty, vehicles, stops)
        }
    )


def generate_report() -> None:
    with open("fixtures/mini_json_dataset.json", "r") as file:
        data = load(file)

    schedule = Schedule(**data)

    with open("./results/step_3.csv", "w+") as file:
        writer = csv.writer(file)

        writer.writerow(["Duty ID", "Start time", "End time", "Start stop description", "End stop description", "Break start time", "Break duration", "Break stop name"])

        for duty in schedule.duties:
            duty_report = get_duty_report(duty, schedule.vehicles, schedule.stops, schedule.trips)
            
            writer.writerow(
                [
                    duty.duty_id, 
                    duty_report.start_time, 
                    duty_report.end_time, 
                    duty_report.start_stop_description, 
                    duty_report.end_stop_description
                ]
            )

            if duty_report.breaks:
                [
                    writer.writerow(
                            [
                                duty.duty_id, 
                                duty_report.start_time, 
                                duty_report.end_time, 
                                duty_report.start_stop_description, 
                                duty_report.end_stop_description, 
                                duty_break.start_time,
                                duty_break.duration,
                                duty_break.stop_name
                            ]
                        )
                    for duty_break in duty_report.breaks
                ]
                return


if __name__ == '__main__':
    generate_report()