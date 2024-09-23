from typing import List

from fixtures.duty import duties
from fixtures.vehicle import vehicles
from src.schemas.duties import Duty
from src.schemas.vehicles import Vehicle
from src.step_1 import get_duty_start_time, get_duty_end_time


def test_get_duty_start_time_when_first_event_has_start_time_then_format_and_return_it(duties: List[Duty], vehicles: List[Vehicle]):
    # arrange
    duty_mock = duties[5]
    vehicles_mock = vehicles
    expected_start_time = "13:13"

    # act
    duty_start_time = get_duty_start_time(duty_mock, vehicles_mock)

    # assert
    assert duty_start_time == expected_start_time


def test_get_duty_start_time_when_first_event_does_not_have_start_time_then_search_in_vehicle_events(duties: List[Duty], vehicles: List[Vehicle]):
    # arrange
    duty_mock = duties[0]
    vehicles_mock = vehicles
    expected_start_time = "03:25"

    # act
    duty_start_time = get_duty_start_time(duty_mock, vehicles_mock)

    # assert
    assert duty_start_time == expected_start_time


def test_get_duty_end_time_when_event_has_end_time_then_format_and_return_it(duties: List[Duty], vehicles: List[Vehicle]):
    # arrange
    duty_mock = duties[2]
    vehicles_mock = vehicles
    expected_end_time = "10:40"

    # act
    duty_end_time = get_duty_end_time(duty_mock, vehicles_mock)

    # assert
    assert duty_end_time == expected_end_time


def test_get_duty_end_time_when_first_event_does_not_have_end_time_then_search_in_vehicle_events(duties: List[Duty], vehicles: List[Vehicle]):
    # arrange
    duty_mock = duties[0]
    vehicles_mock = vehicles
    expected_end_time = "11:39"

    # act
    duty_end_time = get_duty_end_time(duty_mock, vehicles_mock)

    # assert
    assert duty_end_time == expected_end_time
