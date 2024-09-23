from typing import List
from pytest import fixture

from src.schemas.duties import Duty


@fixture
def duties() -> List[Duty]:
    duties = [
		{
			"duty_id": "1",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "2"
				}
			]
		},
		{
			"duty_id": "2",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "21",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "59"
				}
			]
		},
		{
			"duty_id": "3",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "taxi",
					"start_time": "0.10:28",
					"end_time": "0.10:40",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "4",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "21",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "75"
				}
			]
		},
		{
			"duty_id": "5",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "taxi",
					"start_time": "0.12:22",
					"end_time": "0.12:32",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "6",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.13:13",
					"end_time": "0.13:18",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.13:18",
					"end_time": "0.13:28",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "9"
				}
			]
		},
		{
			"duty_id": "7",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "15"
				}
			]
		},
		{
			"duty_id": "8",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.13:18",
					"end_time": "0.13:23",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.13:23",
					"end_time": "0.13:33",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "37"
				}
			]
		},
		{
			"duty_id": "9",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "19"
				}
			]
		},
		{
			"duty_id": "10",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "47"
				}
			]
		},
		{
			"duty_id": "11",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "taxi",
					"start_time": "0.11:43",
					"end_time": "0.11:58",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "12",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "16"
				}
			]
		},
		{
			"duty_id": "13",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "25"
				}
			]
		},
		{
			"duty_id": "14",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.13:23",
					"end_time": "0.13:28",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.13:28",
					"end_time": "0.14:13",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMSLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "7"
				}
			]
		},
		{
			"duty_id": "15",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "taxi",
					"start_time": "0.11:58",
					"end_time": "0.12:43",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "16",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "87"
				}
			]
		},
		{
			"duty_id": "17",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "taxi",
					"start_time": "0.12:52",
					"end_time": "0.13:02",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "18",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.13:13",
					"end_time": "0.13:18",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.13:18",
					"end_time": "0.13:28",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "52"
				}
			]
		},
		{
			"duty_id": "19",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "35"
				}
			]
		},
		{
			"duty_id": "20",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "88"
				}
			]
		},
		{
			"duty_id": "21",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "37"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "taxi",
					"start_time": "0.13:33",
					"end_time": "0.13:43",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "22",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "54"
				}
			]
		},
		{
			"duty_id": "23",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "taxi",
					"start_time": "0.12:23",
					"end_time": "0.12:35",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "24",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "43"
				}
			]
		},
		{
			"duty_id": "25",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "52"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "taxi",
					"start_time": "0.13:28",
					"end_time": "0.13:38",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "26",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "86"
				}
			]
		},
		{
			"duty_id": "27",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "14"
				}
			]
		},
		{
			"duty_id": "28",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.15:01",
					"end_time": "0.15:06",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.15:06",
					"end_time": "0.15:16",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "36"
				}
			]
		},
		{
			"duty_id": "29",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "57"
				}
			]
		},
		{
			"duty_id": "30",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 34,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 35,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 36,
					"vehicle_id": "42"
				}
			]
		},
		{
			"duty_id": "31",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.15:43",
					"end_time": "0.15:48",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.15:48",
					"end_time": "0.16:03",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 34,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 35,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 36,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 37,
					"vehicle_id": "41"
				}
			]
		},
		{
			"duty_id": "32",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "40"
				}
			]
		},
		{
			"duty_id": "33",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.16:13",
					"end_time": "0.16:18",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.16:18",
					"end_time": "0.16:28",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "45"
				}
			]
		},
		{
			"duty_id": "34",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "89"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "89"
				}
			]
		},
		{
			"duty_id": "35",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.08:59",
					"end_time": "0.09:04",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.09:04",
					"end_time": "0.09:19",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "VaLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "73"
				}
			]
		},
		{
			"duty_id": "36",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.09:10",
					"end_time": "0.09:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.09:15",
					"end_time": "0.09:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "VaLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "34"
				}
			]
		},
		{
			"duty_id": "37",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "56"
				}
			]
		},
		{
			"duty_id": "38",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "67"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "67"
				}
			]
		},
		{
			"duty_id": "39",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "80"
				}
			]
		},
		{
			"duty_id": "40",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "sign_on",
					"start_time": "0.13:28",
					"end_time": "0.13:33",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "taxi",
					"start_time": "0.13:33",
					"end_time": "0.14:03",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiCLO"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "5"
				}
			]
		},
		{
			"duty_id": "41",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "31"
				}
			]
		},
		{
			"duty_id": "42",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "taxi",
					"start_time": "0.10:50",
					"end_time": "0.11:02",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "sign_on",
					"start_time": "0.14:45",
					"end_time": "0.14:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "taxi",
					"start_time": "0.14:50",
					"end_time": "0.15:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "21",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "22",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "44"
				}
			]
		},
		{
			"duty_id": "43",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "73"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "taxi",
					"start_time": "0.09:19",
					"end_time": "0.09:34",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "61"
				}
			]
		},
		{
			"duty_id": "44",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "74"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "74"
				}
			]
		},
		{
			"duty_id": "45",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "75"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "77"
				}
			]
		},
		{
			"duty_id": "46",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "77"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "49"
				}
			]
		},
		{
			"duty_id": "47",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "66"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "66"
				}
			]
		},
		{
			"duty_id": "48",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "78"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "78"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "78"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "78"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "78"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "78"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "78"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "85"
				}
			]
		},
		{
			"duty_id": "49",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "sign_on",
					"start_time": "0.15:37",
					"end_time": "0.15:42",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "taxi",
					"start_time": "0.15:42",
					"end_time": "0.15:52",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "70"
				}
			]
		},
		{
			"duty_id": "50",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "80"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "sign_on",
					"start_time": "0.16:00",
					"end_time": "0.16:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "taxi",
					"start_time": "0.16:05",
					"end_time": "0.16:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "90003"
				}
			]
		},
		{
			"duty_id": "51",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "sign_on",
					"start_time": "0.15:12",
					"end_time": "0.15:17",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "taxi",
					"start_time": "0.15:17",
					"end_time": "0.15:32",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "90115"
				}
			]
		},
		{
			"duty_id": "52",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "taxi",
					"start_time": "0.11:22",
					"end_time": "0.11:32",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "35"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "35"
				}
			]
		},
		{
			"duty_id": "53",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "taxi",
					"start_time": "0.11:16",
					"end_time": "0.11:28",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "64"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "64"
				}
			]
		},
		{
			"duty_id": "54",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "79"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "79"
				}
			]
		},
		{
			"duty_id": "55",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "85"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "sign_on",
					"start_time": "0.14:49",
					"end_time": "0.14:54",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "taxi",
					"start_time": "0.14:54",
					"end_time": "0.15:09",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "VaLO"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "17"
				}
			]
		},
		{
			"duty_id": "56",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "86"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "sign_on",
					"start_time": "0.14:13",
					"end_time": "0.14:18",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "taxi",
					"start_time": "0.14:18",
					"end_time": "0.14:28",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "60"
				}
			]
		},
		{
			"duty_id": "57",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "87"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "65"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "65"
				}
			]
		},
		{
			"duty_id": "58",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "88"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "sign_on",
					"start_time": "0.16:49",
					"end_time": "0.16:54",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "taxi",
					"start_time": "0.16:54",
					"end_time": "0.17:09",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "90002"
				}
			]
		},
		{
			"duty_id": "59",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.07:40",
					"end_time": "0.07:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.07:45",
					"end_time": "0.08:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "taxi",
					"start_time": "0.11:47",
					"end_time": "0.12:02",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "sign_on",
					"start_time": "0.15:07",
					"end_time": "0.15:12",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "taxi",
					"start_time": "0.15:12",
					"end_time": "0.15:32",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "DuDs"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "90111"
				}
			]
		},
		{
			"duty_id": "60",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "taxi",
					"start_time": "0.13:33",
					"end_time": "0.13:48",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "61",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.13:53",
					"end_time": "0.13:58",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.13:58",
					"end_time": "0.14:43",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMSLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "53"
				}
			]
		},
		{
			"duty_id": "62",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "58"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "58"
				}
			]
		},
		{
			"duty_id": "63",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.17:17",
					"end_time": "0.17:22",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.17:22",
					"end_time": "0.17:42",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "DuDs"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "90010"
				}
			]
		},
		{
			"duty_id": "64",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "taxi",
					"start_time": "0.12:43",
					"end_time": "0.13:28",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "65",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "5"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "taxi",
					"start_time": "0.14:03",
					"end_time": "0.14:38",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "66",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "9"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "taxi",
					"start_time": "0.13:28",
					"end_time": "0.13:38",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "67",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "21",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "7"
				},
				{
					"duty_event_sequence": "22",
					"duty_event_type": "taxi",
					"start_time": "0.14:13",
					"end_time": "0.14:58",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "68",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "11"
				}
			]
		},
		{
			"duty_id": "69",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "12"
				}
			]
		},
		{
			"duty_id": "70",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "taxi",
					"start_time": "0.13:16",
					"end_time": "0.13:28",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "71",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "21",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "22",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "23",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "24",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "17"
				},
				{
					"duty_event_sequence": "25",
					"duty_event_type": "taxi",
					"start_time": "0.15:19",
					"end_time": "0.15:34",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "72",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "taxi",
					"start_time": "0.13:56",
					"end_time": "0.14:06",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "73",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "26"
				}
			]
		},
		{
			"duty_id": "74",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "taxi",
					"start_time": "0.13:47",
					"end_time": "0.14:02",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "75",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "taxi",
					"start_time": "0.13:26",
					"end_time": "0.13:56",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "76",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "36"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "taxi",
					"start_time": "0.15:16",
					"end_time": "0.15:26",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "77",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "taxi",
					"start_time": "0.13:13",
					"end_time": "0.13:58",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "78",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "44"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "taxi",
					"start_time": "0.15:00",
					"end_time": "0.15:10",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "79",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "21",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "22",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "41"
				},
				{
					"duty_event_sequence": "23",
					"duty_event_type": "taxi",
					"start_time": "0.16:03",
					"end_time": "0.16:18",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "80",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "42"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "42"
				}
			]
		},
		{
			"duty_id": "81",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "45"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "taxi",
					"start_time": "0.16:28",
					"end_time": "0.16:38",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "82",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "50"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "50"
				}
			]
		},
		{
			"duty_id": "83",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "55"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "55"
				}
			]
		},
		{
			"duty_id": "84",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "53"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "taxi",
					"start_time": "0.14:53",
					"end_time": "0.15:38",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "85",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "60"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "taxi",
					"start_time": "0.14:28",
					"end_time": "0.14:38",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "86",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "63"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "63"
				}
			]
		},
		{
			"duty_id": "87",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "68"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "68"
				}
			]
		},
		{
			"duty_id": "88",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "69"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "69"
				}
			]
		},
		{
			"duty_id": "89",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "70"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "taxi",
					"start_time": "0.15:52",
					"end_time": "0.16:02",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "90",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.10:08",
					"end_time": "0.10:13",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.10:13",
					"end_time": "0.10:28",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "VaLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "3"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 34,
					"vehicle_id": "3"
				}
			]
		},
		{
			"duty_id": "91",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.10:13",
					"end_time": "0.10:18",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.10:18",
					"end_time": "0.10:28",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "21",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "22",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "33"
				}
			]
		},
		{
			"duty_id": "92",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.10:30",
					"end_time": "0.10:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.10:35",
					"end_time": "0.10:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "VaLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "72"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "72"
				}
			]
		},
		{
			"duty_id": "93",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.10:56",
					"end_time": "0.11:01",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.11:01",
					"end_time": "0.11:16",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "VaLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "83"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "83"
				}
			]
		},
		{
			"duty_id": "94",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.11:07",
					"end_time": "0.11:12",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.11:12",
					"end_time": "0.11:22",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "81"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "81"
				}
			]
		},
		{
			"duty_id": "95",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.11:08",
					"end_time": "0.11:13",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.11:13",
					"end_time": "0.11:58",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMSLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "29"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "29"
				}
			]
		},
		{
			"duty_id": "96",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.11:23",
					"end_time": "0.11:28",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.11:28",
					"end_time": "0.11:43",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "23"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "23"
				}
			]
		},
		{
			"duty_id": "97",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "51"
				}
			]
		},
		{
			"duty_id": "98",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "21"
				}
			]
		},
		{
			"duty_id": "99",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.11:53",
					"end_time": "0.11:58",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.11:58",
					"end_time": "0.12:43",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMSLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "4"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "4"
				}
			]
		},
		{
			"duty_id": "100",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.12:03",
					"end_time": "0.12:08",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.12:08",
					"end_time": "0.12:23",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "VaLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "39"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "39"
				}
			]
		},
		{
			"duty_id": "101",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "19"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "19"
				}
			]
		},
		{
			"duty_id": "102",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.12:07",
					"end_time": "0.12:12",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.12:12",
					"end_time": "0.12:22",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 34,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "21",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 35,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "22",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 36,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "23",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 37,
					"vehicle_id": "10"
				},
				{
					"duty_event_sequence": "24",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 38,
					"vehicle_id": "10"
				}
			]
		},
		{
			"duty_id": "103",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "82"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "82"
				}
			]
		},
		{
			"duty_id": "104",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.12:23",
					"end_time": "0.12:28",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.12:28",
					"end_time": "0.13:13",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMSLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "38"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 34,
					"vehicle_id": "38"
				}
			]
		},
		{
			"duty_id": "105",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "25"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 34,
					"vehicle_id": "25"
				}
			]
		},
		{
			"duty_id": "106",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "2"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "2"
				}
			]
		},
		{
			"duty_id": "107",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.12:37",
					"end_time": "0.12:42",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.12:42",
					"end_time": "0.12:52",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 31,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 32,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 33,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 34,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "21",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 35,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "22",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 36,
					"vehicle_id": "32"
				},
				{
					"duty_event_sequence": "23",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 37,
					"vehicle_id": "32"
				}
			]
		},
		{
			"duty_id": "108",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.12:41",
					"end_time": "0.12:46",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.12:46",
					"end_time": "0.13:26",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PHMLO"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 29,
					"vehicle_id": "28"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 30,
					"vehicle_id": "28"
				}
			]
		},
		{
			"duty_id": "109",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "15"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "15"
				}
			]
		},
		{
			"duty_id": "110",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "1"
				}
			]
		},
		{
			"duty_id": "111",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "taxi",
					"start_time": "0.08:44",
					"end_time": "0.08:59",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "sign_on",
					"start_time": "0.11:27",
					"end_time": "0.11:32",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "taxi",
					"start_time": "0.11:32",
					"end_time": "0.11:47",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "taxi",
					"start_time": "0.14:00",
					"end_time": "0.14:15",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "112",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "taxi",
					"start_time": "0.08:00",
					"end_time": "0.08:15",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "sign_on",
					"start_time": "0.10:06",
					"end_time": "0.10:11",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "taxi",
					"start_time": "0.10:11",
					"end_time": "0.10:31",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "DuDs"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "taxi",
					"start_time": "0.13:43",
					"end_time": "0.13:58",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "113",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "taxi",
					"start_time": "0.09:20",
					"end_time": "0.09:35",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "sign_on",
					"start_time": "0.13:31",
					"end_time": "0.13:36",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "taxi",
					"start_time": "0.13:36",
					"end_time": "0.13:56",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "DuDs"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "taxi",
					"start_time": "0.17:08",
					"end_time": "0.17:23",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "114",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "sign_on",
					"start_time": "0.12:48",
					"end_time": "0.12:53",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "taxi",
					"start_time": "0.12:53",
					"end_time": "0.13:08",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "taxi",
					"start_time": "0.17:09",
					"end_time": "0.17:24",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "115",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "sign_on",
					"start_time": "0.10:07",
					"end_time": "0.10:12",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "taxi",
					"start_time": "0.10:12",
					"end_time": "0.10:27",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "taxi",
					"start_time": "0.13:56",
					"end_time": "0.14:16",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "116",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "taxi",
					"start_time": "0.09:20",
					"end_time": "0.09:40",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "sign_on",
					"start_time": "0.13:40",
					"end_time": "0.13:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "taxi",
					"start_time": "0.13:45",
					"end_time": "0.14:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "90003"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "taxi",
					"start_time": "0.16:20",
					"end_time": "0.16:35",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "117",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "14"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "90111"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "taxi",
					"start_time": "0.15:32",
					"end_time": "0.15:52",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "118",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "13"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "13"
				}
			]
		},
		{
			"duty_id": "119",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "16"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "90115"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "taxi",
					"start_time": "0.15:32",
					"end_time": "0.15:47",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "120",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "26"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "26"
				}
			]
		},
		{
			"duty_id": "121",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "21"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "78"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "78"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "78"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "78"
				}
			]
		},
		{
			"duty_id": "122",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "sign_on",
					"start_time": "0.13:20",
					"end_time": "0.13:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "taxi",
					"start_time": "0.13:25",
					"end_time": "0.13:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "taxi",
					"start_time": "0.17:41",
					"end_time": "0.17:56",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "123",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "31"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "sign_on",
					"start_time": "0.12:56",
					"end_time": "0.13:01",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "taxi",
					"start_time": "0.13:01",
					"end_time": "0.13:16",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "VaLO"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "18"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "18"
				}
			]
		},
		{
			"duty_id": "124",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "34"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "taxi",
					"start_time": "0.09:30",
					"end_time": "0.09:45",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "sign_on",
					"start_time": "0.13:23",
					"end_time": "0.13:28",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "taxi",
					"start_time": "0.13:28",
					"end_time": "0.13:43",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "taxi",
					"start_time": "0.17:56",
					"end_time": "0.18:11",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "125",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "40"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "30"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "30"
				}
			]
		},
		{
			"duty_id": "126",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "43"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "sign_on",
					"start_time": "0.12:16",
					"end_time": "0.12:21",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "taxi",
					"start_time": "0.12:21",
					"end_time": "0.12:36",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "taxi",
					"start_time": "0.17:42",
					"end_time": "0.18:02",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "127",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "taxi",
					"start_time": "0.10:27",
					"end_time": "0.10:42",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "48"
				}
			]
		},
		{
			"duty_id": "128",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "46"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "46"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "46"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "46"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "46"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "46"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "46"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "46"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "12"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "12"
				}
			]
		},
		{
			"duty_id": "129",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "47"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "11"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "11"
				}
			]
		},
		{
			"duty_id": "130",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "48"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "6"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "6"
				}
			]
		},
		{
			"duty_id": "131",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "taxi",
					"start_time": "0.10:31",
					"end_time": "0.10:51",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "8"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "8"
				}
			]
		},
		{
			"duty_id": "132",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "49"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "20"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "20"
				}
			]
		},
		{
			"duty_id": "133",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "51"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "sign_on",
					"start_time": "0.13:13",
					"end_time": "0.13:18",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "taxi",
					"start_time": "0.13:18",
					"end_time": "0.13:33",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTCLO"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "22"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "22"
				}
			]
		},
		{
			"duty_id": "134",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "54"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "62"
				}
			]
		},
		{
			"duty_id": "135",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "56"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "84"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "84"
				}
			]
		},
		{
			"duty_id": "136",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "57"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "71"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "71"
				}
			]
		},
		{
			"duty_id": "137",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "59"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "19",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "76"
				},
				{
					"duty_event_sequence": "20",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "76"
				}
			]
		},
		{
			"duty_id": "138",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "61"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "sign_on",
					"start_time": "0.13:41",
					"end_time": "0.13:46",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "taxi",
					"start_time": "0.13:46",
					"end_time": "0.13:56",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTCLO"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "24"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "24"
				}
			]
		},
		{
			"duty_id": "139",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "62"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "sign_on",
					"start_time": "0.13:27",
					"end_time": "0.13:32",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "taxi",
					"start_time": "0.13:32",
					"end_time": "0.13:47",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTCLO"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "27"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "27"
				}
			]
		},
		{
			"duty_id": "140",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.08:24",
					"end_time": "0.08:29",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.08:29",
					"end_time": "0.08:44",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "90002"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "taxi",
					"start_time": "0.13:08",
					"end_time": "0.13:23",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "sign_on",
					"start_time": "0.17:21",
					"end_time": "0.17:26",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "taxi",
					"start_time": "0.17:26",
					"end_time": "0.17:41",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "90008"
				}
			]
		},
		{
			"duty_id": "141",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.08:55",
					"end_time": "0.09:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.09:00",
					"end_time": "0.09:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "DuDs"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "90010"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "taxi",
					"start_time": "0.12:36",
					"end_time": "0.12:51",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "sign_on",
					"start_time": "0.16:48",
					"end_time": "0.16:53",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "taxi",
					"start_time": "0.16:53",
					"end_time": "0.17:08",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "90052"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "90052"
				}
			]
		},
		{
			"duty_id": "142",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "sign_on",
					"start_time": "0.09:00",
					"end_time": "0.09:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "taxi",
					"start_time": "0.09:05",
					"end_time": "0.09:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "90008"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "taxi",
					"start_time": "0.13:40",
					"end_time": "0.13:55",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "sign_on",
					"start_time": "0.17:36",
					"end_time": "0.17:41",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "taxi",
					"start_time": "0.17:41",
					"end_time": "0.17:56",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "90057"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "90057"
				}
			]
		},
		{
			"duty_id": "143",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 0,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 1,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 2,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 3,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 4,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 5,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 6,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 7,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 8,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 9,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "33"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "taxi",
					"start_time": "0.10:28",
					"end_time": "0.10:38",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Pomona"
				}
			]
		},
		{
			"duty_id": "144",
			"duty_events": [
				{
					"duty_event_sequence": "0",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 10,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "1",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 11,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "2",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 12,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "3",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 13,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "4",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 14,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "5",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 15,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "6",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 16,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "7",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 17,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "8",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 18,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "9",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 19,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "10",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 20,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "11",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 21,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "12",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 22,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "13",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 23,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "14",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 24,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "15",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 25,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "16",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 26,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "17",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 27,
					"vehicle_id": "1"
				},
				{
					"duty_event_sequence": "18",
					"duty_event_type": "vehicle_event",
					"vehicle_event_sequence": 28,
					"vehicle_id": "1"
				}
			]
		}
	]

    return [Duty(**duty) for duty in duties]
