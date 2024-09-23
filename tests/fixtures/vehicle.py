from typing import List
from pytest import fixture

from src.schemas.vehicles import Vehicle


@fixture
def vehicles() -> List[Vehicle]:
    vehicles = [
		{
			"vehicle_id": "1",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:15",
					"end_time": "0.03:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "110"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.03:35",
					"end_time": "0.04:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "110"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301431",
					"duty_id": "110"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:22",
					"end_time": "0.05:24",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "110"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:43",
					"end_time": "0.05:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "110"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301533",
					"duty_id": "110"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:04",
					"end_time": "0.07:09",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "GrPR",
					"duty_id": "110"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302243",
					"sub_trip_index": "1",
					"duty_id": "110"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302243",
					"sub_trip_index": "2",
					"duty_id": "110"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:55",
					"end_time": "0.09:50",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "110"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.12:00",
					"end_time": "0.12:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.12:20",
					"end_time": "0.12:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301891",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:41",
					"end_time": "0.13:45",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:14",
					"end_time": "0.14:15",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301813",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:26",
					"end_time": "0.15:37",
					"origin_stop_id": "PTC",
					"destination_stop_id": "VaLO",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:23",
					"end_time": "0.16:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302034",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:15",
					"end_time": "0.17:19",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:24",
					"end_time": "0.17:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301826",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:13",
					"end_time": "0.18:17",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:33",
					"end_time": "0.18:35",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302043",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:38",
					"end_time": "0.19:40",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:48",
					"end_time": "0.19:50",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301614",
					"duty_id": "144"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:49",
					"end_time": "0.21:04",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "144"
				}
			]
		},
		{
			"vehicle_id": "2",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:25",
					"end_time": "0.03:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.03:45",
					"end_time": "0.04:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301688",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:12",
					"end_time": "0.05:47",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "EMSLO",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:58",
					"end_time": "0.06:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301535",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:37",
					"end_time": "0.07:39",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:58",
					"end_time": "0.08:00",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301731",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:50",
					"end_time": "0.08:52",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:28",
					"end_time": "0.09:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302166",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302173",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.11:29",
					"end_time": "0.11:39",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "1"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.12:35",
					"end_time": "0.12:55",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.12:55",
					"end_time": "0.14:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301626",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:29",
					"end_time": "0.15:46",
					"origin_stop_id": "MTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:58",
					"end_time": "0.16:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301916",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:55",
					"end_time": "0.16:57",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:33",
					"end_time": "0.17:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301766",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:18",
					"end_time": "0.19:20",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:28",
					"end_time": "0.19:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301612",
					"duty_id": "106"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:06",
					"end_time": "0.21:21",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "106"
				}
			]
		},
		{
			"vehicle_id": "3",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:30",
					"end_time": "0.03:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.03:50",
					"end_time": "0.04:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301844",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.04:58",
					"end_time": "0.05:02",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:44",
					"end_time": "0.05:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302133",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:22",
					"end_time": "0.06:24",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:31",
					"end_time": "0.06:33",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301541",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:36",
					"end_time": "0.07:40",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:00",
					"end_time": "0.08:02",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302000",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:06",
					"end_time": "0.09:08",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:13",
					"end_time": "0.09:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301565",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:16",
					"end_time": "0.10:20",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "attendance",
					"start_time": "0.10:20",
					"end_time": "0.10:28",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "VaLO",
					"duty_id": "3"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:28",
					"end_time": "0.10:30",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302013",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:33",
					"end_time": "0.11:35",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:18",
					"end_time": "0.12:20",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302267",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:05",
					"end_time": "0.14:07",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:28",
					"end_time": "0.14:30",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301754",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:20",
					"end_time": "0.15:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:58",
					"end_time": "0.16:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301914",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:28",
					"end_time": "0.17:32",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:49",
					"end_time": "0.17:50",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301828",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:23",
					"end_time": "0.19:25",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:33",
					"end_time": "0.19:35",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301934",
					"duty_id": "90"
				},
				{
					"vehicle_event_sequence": "34",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:17",
					"end_time": "0.20:32",
					"origin_stop_id": "RiVa",
					"destination_stop_id": "Pomona",
					"duty_id": "90"
				}
			]
		},
		{
			"vehicle_id": "4",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:40",
					"end_time": "0.04:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:00",
					"end_time": "0.04:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301689",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:27",
					"end_time": "0.06:02",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "EMSLO",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:13",
					"end_time": "0.06:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301538",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:29",
					"end_time": "0.07:35",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:27",
					"end_time": "0.08:35",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301440",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:00",
					"end_time": "0.10:02",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:13",
					"end_time": "0.10:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302201",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:16",
					"end_time": "0.11:20",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:28",
					"end_time": "0.11:30",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302018",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:34",
					"end_time": "0.12:36",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "attendance",
					"start_time": "0.12:36",
					"end_time": "0.12:43",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMSLO",
					"duty_id": "64"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:43",
					"end_time": "0.12:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302211",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:49",
					"end_time": "0.13:53",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:58",
					"end_time": "0.14:00",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302195",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:05",
					"end_time": "0.15:07",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:28",
					"end_time": "0.15:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302222",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:38",
					"end_time": "0.16:42",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:25",
					"end_time": "0.18:11",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301671",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:46",
					"end_time": "0.20:00",
					"origin_stop_id": "SDPR",
					"destination_stop_id": "PTC",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301935",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301404",
					"duty_id": "99"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:52",
					"end_time": "0.22:02",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "99"
				}
			]
		},
		{
			"vehicle_id": "5",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:50",
					"end_time": "0.04:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:10",
					"end_time": "0.04:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301690",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:49",
					"end_time": "0.05:51",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:03",
					"end_time": "0.06:05",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302102",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:49",
					"end_time": "0.06:53",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:09",
					"end_time": "0.07:10",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301785",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:28",
					"end_time": "0.08:30",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:28",
					"end_time": "0.09:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301876",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:25",
					"end_time": "0.10:27",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:33",
					"end_time": "0.10:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301743",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:10",
					"end_time": "0.12:12",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:28",
					"end_time": "0.12:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301574",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:57",
					"end_time": "0.14:03",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "65"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:03",
					"end_time": "0.14:11",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301447",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:55",
					"end_time": "0.15:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:08",
					"end_time": "0.16:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302119",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:02",
					"end_time": "0.17:06",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:19",
					"end_time": "0.17:20",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302178",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:53",
					"end_time": "0.19:03",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "40"
				}
			]
		},
		{
			"vehicle_id": "6",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:55",
					"end_time": "0.04:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:15",
					"end_time": "0.05:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMS",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301529",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:01",
					"end_time": "0.06:05",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:15",
					"end_time": "0.06:30",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "CoTC",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302237",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.07:30",
					"end_time": "0.08:25",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:35",
					"end_time": "0.13:55",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.13:55",
					"end_time": "0.14:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMS",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302219",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:53",
					"end_time": "0.15:57",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:14",
					"end_time": "0.17:00",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302234",
					"sub_trip_index": "1",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302234",
					"sub_trip_index": "2",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:09",
					"end_time": "0.18:39",
					"origin_stop_id": "GrPR",
					"destination_stop_id": "Pomona",
					"duty_id": "130"
				}
			]
		},
		{
			"vehicle_id": "7",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:55",
					"end_time": "0.04:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:15",
					"end_time": "0.04:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301691",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:42",
					"end_time": "0.06:32",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "IMPR",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302180",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:42",
					"end_time": "0.08:19",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "PHMLO",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:12",
					"end_time": "0.09:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302146",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:53",
					"end_time": "0.09:55",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:08",
					"end_time": "0.10:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302110",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:56",
					"end_time": "0.11:00",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:12",
					"end_time": "0.11:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302152",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:55",
					"end_time": "0.11:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:08",
					"end_time": "0.12:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302112",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:00",
					"end_time": "0.13:04",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:12",
					"end_time": "0.13:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302156",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:55",
					"end_time": "0.13:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "attendance",
					"start_time": "0.13:57",
					"end_time": "0.14:13",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMSLO",
					"duty_id": "67"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:13",
					"end_time": "0.14:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301579",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:42",
					"end_time": "0.15:48",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:37",
					"end_time": "0.17:00",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "PTC",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301922",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:28",
					"end_time": "0.18:32",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:44",
					"end_time": "0.18:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301832",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:15",
					"end_time": "0.20:17",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:28",
					"end_time": "0.20:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301938",
					"duty_id": "14"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:37",
					"end_time": "0.22:17",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "14"
				}
			]
		},
		{
			"vehicle_id": "8",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:55",
					"end_time": "0.04:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:15",
					"end_time": "0.04:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "IMPR",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302164",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:41",
					"end_time": "0.06:18",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "PHMLO",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:34",
					"end_time": "0.06:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301783",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301408",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:16",
					"end_time": "0.08:56",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.15:10",
					"end_time": "0.15:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.15:30",
					"end_time": "0.15:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302030",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:50",
					"end_time": "0.16:52",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:59",
					"end_time": "0.17:01",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301595",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:09",
					"end_time": "0.18:24",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "131"
				}
			]
		},
		{
			"vehicle_id": "9",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:55",
					"end_time": "0.04:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:15",
					"end_time": "0.04:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "GrPR",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302253",
					"sub_trip_index": "1",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302253",
					"sub_trip_index": "2",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:48",
					"end_time": "0.06:28",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "CiCLO",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:42",
					"end_time": "0.06:50",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301436",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:15",
					"end_time": "0.08:38",
					"origin_stop_id": "EMS",
					"destination_stop_id": "RiVa",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301957",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:12",
					"end_time": "0.10:14",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:28",
					"end_time": "0.10:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302167",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302174",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:29",
					"end_time": "0.12:31",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "attendance",
					"start_time": "0.12:31",
					"end_time": "0.13:28",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTCLO",
					"duty_id": "66"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:28",
					"end_time": "0.13:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302170",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:25",
					"end_time": "0.15:20",
					"origin_stop_id": "CTC",
					"destination_stop_id": "Fi9t",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301632",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:50",
					"end_time": "0.16:52",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:59",
					"end_time": "0.17:01",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301764",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:51",
					"end_time": "0.17:53",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:33",
					"end_time": "0.18:35",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301929",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:22",
					"end_time": "0.19:25",
					"origin_stop_id": "RiVa",
					"destination_stop_id": "TeSC",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302045",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:27",
					"end_time": "0.20:29",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:38",
					"end_time": "0.20:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301619",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:37",
					"end_time": "0.21:41",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:53",
					"end_time": "0.21:55",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302051",
					"duty_id": "6"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:53",
					"end_time": "0.23:45",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "6"
				}
			]
		},
		{
			"vehicle_id": "10",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:00",
					"end_time": "0.04:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:20",
					"end_time": "0.04:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301845",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:38",
					"end_time": "0.06:00",
					"origin_stop_id": "PHM",
					"destination_stop_id": "EMSLO",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:19",
					"end_time": "0.06:21",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301539",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:23",
					"end_time": "0.07:27",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:11",
					"end_time": "0.08:13",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302001",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:17",
					"end_time": "0.09:19",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:28",
					"end_time": "0.09:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301567",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:08",
					"end_time": "0.11:10",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:28",
					"end_time": "0.11:30",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301745",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:20",
					"end_time": "0.12:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "5"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:22",
					"end_time": "0.12:24",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301892",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:25",
					"end_time": "0.13:30",
					"origin_stop_id": "MTC",
					"destination_stop_id": "CTC",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302176",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:29",
					"end_time": "0.14:39",
					"origin_stop_id": "PTC",
					"destination_stop_id": "VaLO",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:53",
					"end_time": "0.14:55",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302265",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:45",
					"end_time": "0.15:49",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:42",
					"end_time": "0.16:43",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302145",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:29",
					"end_time": "0.17:31",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:38",
					"end_time": "0.17:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302122",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:32",
					"end_time": "0.18:36",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:43",
					"end_time": "0.18:44",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302160",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:28",
					"end_time": "0.19:30",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:38",
					"end_time": "0.19:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "34",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302126",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "35",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:27",
					"end_time": "0.20:31",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "36",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:44",
					"end_time": "0.20:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "37",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301839",
					"duty_id": "102"
				},
				{
					"vehicle_event_sequence": "38",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:51",
					"end_time": "0.22:01",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "102"
				}
			]
		},
		{
			"vehicle_id": "11",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:00",
					"end_time": "0.04:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:20",
					"end_time": "0.05:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PHM",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302132",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:37",
					"end_time": "0.05:39",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:45",
					"end_time": "0.05:47",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301534",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:46",
					"end_time": "0.06:50",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:33",
					"end_time": "0.07:35",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301997",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:39",
					"end_time": "0.08:41",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:58",
					"end_time": "0.09:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301563",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:38",
					"end_time": "0.10:40",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:47",
					"end_time": "0.11:00",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301884",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301395",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.12:52",
					"end_time": "0.13:02",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "68"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.15:11",
					"end_time": "0.15:31",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.15:31",
					"end_time": "0.16:42",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301649",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:01",
					"end_time": "0.18:31",
					"origin_stop_id": "SDPR",
					"destination_stop_id": "Pomona",
					"duty_id": "129"
				}
			]
		},
		{
			"vehicle_id": "12",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:05",
					"end_time": "0.04:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:25",
					"end_time": "0.05:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PHM",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301778",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:04",
					"end_time": "0.06:20",
					"origin_stop_id": "PTC",
					"destination_stop_id": "GrPR",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302254",
					"sub_trip_index": "1",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302254",
					"sub_trip_index": "2",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:40",
					"end_time": "0.08:40",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "CTC",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302171",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:29",
					"end_time": "0.09:31",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:28",
					"end_time": "0.10:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301882",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:39",
					"end_time": "0.11:43",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:14",
					"end_time": "0.12:15",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301805",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.13:35",
					"end_time": "0.13:45",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "69"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:05",
					"end_time": "0.14:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:25",
					"end_time": "0.15:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301448",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:25",
					"end_time": "0.16:27",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:44",
					"end_time": "0.16:46",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301593",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.17:54",
					"end_time": "0.18:09",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "128"
				}
			]
		},
		{
			"vehicle_id": "13",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:10",
					"end_time": "0.04:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:30",
					"end_time": "0.05:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMS",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301530",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:17",
					"end_time": "0.06:21",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:31",
					"end_time": "0.06:33",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301991",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:34",
					"end_time": "0.07:36",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:46",
					"end_time": "0.07:48",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301553",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:51",
					"end_time": "0.09:06",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.12:30",
					"end_time": "0.12:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.12:50",
					"end_time": "0.13:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301750",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:41",
					"end_time": "0.14:43",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:55",
					"end_time": "0.15:35",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301634",
					"duty_id": "118"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.17:06",
					"end_time": "0.17:21",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "118"
				}
			]
		},
		{
			"vehicle_id": "14",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:10",
					"end_time": "0.04:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:30",
					"end_time": "0.05:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "IMPR",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301678",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:56",
					"end_time": "0.06:46",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "IMPR",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301683",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.07:58",
					"end_time": "0.08:53",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.15:00",
					"end_time": "0.15:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.15:20",
					"end_time": "0.15:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301911",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:25",
					"end_time": "0.16:27",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:33",
					"end_time": "0.16:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301763",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:16",
					"end_time": "0.18:18",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:28",
					"end_time": "0.18:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301606",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:15",
					"end_time": "0.20:17",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:13",
					"end_time": "0.21:15",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301776",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:41",
					"end_time": "0.22:43",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.23:03",
					"end_time": "0.23:05",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302131",
					"duty_id": "27"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.23:46",
					"end_time": "1.00:26",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "27"
				}
			]
		},
		{
			"vehicle_id": "15",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:10",
					"end_time": "0.04:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:30",
					"end_time": "0.04:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301692",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:59",
					"end_time": "0.06:39",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "CiCLO",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:22",
					"end_time": "0.07:30",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301438",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:55",
					"end_time": "0.08:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:08",
					"end_time": "0.09:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302108",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:56",
					"end_time": "0.10:00",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:12",
					"end_time": "0.10:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302150",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.10:53",
					"end_time": "0.11:38",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "7"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.12:50",
					"end_time": "0.13:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.13:10",
					"end_time": "0.14:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMS",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301578",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:45",
					"end_time": "0.15:47",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:58",
					"end_time": "0.16:00",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301760",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:50",
					"end_time": "0.16:52",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:57",
					"end_time": "0.16:59",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301920",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:54",
					"end_time": "0.17:56",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:33",
					"end_time": "0.18:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301769",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:09",
					"end_time": "0.20:11",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:28",
					"end_time": "0.20:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301618",
					"duty_id": "109"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:04",
					"end_time": "0.22:19",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "109"
				}
			]
		},
		{
			"vehicle_id": "16",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:10",
					"end_time": "0.04:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:30",
					"end_time": "0.04:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301693",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:09",
					"end_time": "0.06:37",
					"origin_stop_id": "EMS",
					"destination_stop_id": "SDPR",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301977",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.07:56",
					"end_time": "0.08:51",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:20",
					"end_time": "0.13:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.13:40",
					"end_time": "0.13:55",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302263",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:44",
					"end_time": "0.14:48",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:56",
					"end_time": "0.15:33",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301633",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:50",
					"end_time": "0.17:40",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "Fi9t",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302258",
					"sub_trip_index": "1",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302258",
					"sub_trip_index": "2",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:25",
					"end_time": "0.19:30",
					"origin_stop_id": "GrPR",
					"destination_stop_id": "CiGL",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301455",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:49",
					"end_time": "0.20:51",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:58",
					"end_time": "0.21:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301620",
					"duty_id": "12"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:16",
					"end_time": "0.22:48",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "Pomona",
					"duty_id": "12"
				}
			]
		},
		{
			"vehicle_id": "17",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:10",
					"end_time": "0.04:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:30",
					"end_time": "0.04:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301983",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:40",
					"end_time": "0.05:42",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:56",
					"end_time": "0.05:58",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301536",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:57",
					"end_time": "0.07:01",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:23",
					"end_time": "0.07:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301998",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:12",
					"end_time": "0.08:16",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:24",
					"end_time": "0.08:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301790",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:08",
					"end_time": "0.09:12",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:58",
					"end_time": "0.10:00",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302011",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:03",
					"end_time": "0.11:05",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:28",
					"end_time": "0.11:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302206",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:32",
					"end_time": "0.12:36",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:43",
					"end_time": "0.12:45",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302190",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:49",
					"end_time": "0.13:51",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:58",
					"end_time": "0.14:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302216",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:05",
					"end_time": "0.15:09",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "71"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:09",
					"end_time": "0.15:11",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302029",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:15",
					"end_time": "0.16:19",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:24",
					"end_time": "0.16:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301822",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:13",
					"end_time": "0.17:17",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:29",
					"end_time": "0.18:15",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301672",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:43",
					"end_time": "0.19:58",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "55"
				}
			]
		},
		{
			"vehicle_id": "18",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:00",
					"end_time": "0.04:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:20",
					"end_time": "0.04:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "GrPR",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302236",
					"sub_trip_index": "1",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302236",
					"sub_trip_index": "2",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:03",
					"end_time": "0.06:38",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "EMSLO",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:43",
					"end_time": "0.06:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301542",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:07",
					"end_time": "0.08:13",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:08",
					"end_time": "0.09:30",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "PTC",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301877",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:40",
					"end_time": "0.11:10",
					"origin_stop_id": "PHM",
					"destination_stop_id": "VaLO",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:23",
					"end_time": "0.11:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302019",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:13",
					"end_time": "0.12:17",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:24",
					"end_time": "0.12:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301806",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:12",
					"end_time": "0.13:16",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "70"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:16",
					"end_time": "0.13:18",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302023",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:12",
					"end_time": "0.14:16",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:24",
					"end_time": "0.14:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301814",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:13",
					"end_time": "0.15:17",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:36",
					"end_time": "0.16:22",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301643",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.17:41",
					"end_time": "0.18:11",
					"origin_stop_id": "SDPR",
					"destination_stop_id": "Pomona",
					"duty_id": "123"
				}
			]
		},
		{
			"vehicle_id": "19",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:15",
					"end_time": "0.04:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:35",
					"end_time": "0.05:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301432",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:23",
					"end_time": "0.06:25",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:38",
					"end_time": "0.06:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302103",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:24",
					"end_time": "0.07:28",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:39",
					"end_time": "0.07:40",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301788",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:00",
					"end_time": "0.09:02",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:58",
					"end_time": "0.10:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301879",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301394",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.11:52",
					"end_time": "0.12:02",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "9"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.12:05",
					"end_time": "0.12:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.12:25",
					"end_time": "0.12:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301893",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301961",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:14",
					"end_time": "0.14:24",
					"origin_stop_id": "PTC",
					"destination_stop_id": "VaLO",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:13",
					"end_time": "0.15:15",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302027",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:20",
					"end_time": "0.16:22",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:29",
					"end_time": "0.16:31",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301591",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:39",
					"end_time": "0.17:43",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:53",
					"end_time": "0.17:55",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302040",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:00",
					"end_time": "0.19:02",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:08",
					"end_time": "0.19:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301611",
					"duty_id": "101"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:29",
					"end_time": "0.21:01",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "Pomona",
					"duty_id": "101"
				}
			]
		},
		{
			"vehicle_id": "20",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:15",
					"end_time": "0.04:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:35",
					"end_time": "0.05:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMS",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302101",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:06",
					"end_time": "0.06:10",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:24",
					"end_time": "0.06:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301782",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:05",
					"end_time": "0.07:09",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:20",
					"end_time": "0.07:22",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301996",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:26",
					"end_time": "0.08:28",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:34",
					"end_time": "0.08:36",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301561",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.09:37",
					"end_time": "0.09:52",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:00",
					"end_time": "0.14:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:20",
					"end_time": "0.14:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301903",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:54",
					"end_time": "0.15:58",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:12",
					"end_time": "0.16:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302141",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:59",
					"end_time": "0.17:01",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:14",
					"end_time": "0.17:16",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301597",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:23",
					"end_time": "0.18:38",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "132"
				}
			]
		},
		{
			"vehicle_id": "21",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:20",
					"end_time": "0.04:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:40",
					"end_time": "0.05:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "BeLH",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301406",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:14",
					"end_time": "0.06:18",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:39",
					"end_time": "0.06:40",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301784",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:50",
					"end_time": "0.07:52",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:58",
					"end_time": "0.08:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301867",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301392",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.09:52",
					"end_time": "0.10:02",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.11:50",
					"end_time": "0.12:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.12:10",
					"end_time": "0.13:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMS",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302212",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:04",
					"end_time": "0.14:08",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:13",
					"end_time": "0.14:15",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302196",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:20",
					"end_time": "0.15:22",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:40",
					"end_time": "0.15:42",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301586",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:09",
					"end_time": "0.17:15",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:56",
					"end_time": "0.18:15",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "TeSC",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302041",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:20",
					"end_time": "0.19:22",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:28",
					"end_time": "0.19:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301613",
					"duty_id": "98"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:31",
					"end_time": "0.20:46",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "98"
				}
			]
		},
		{
			"vehicle_id": "22",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:20",
					"end_time": "0.04:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:40",
					"end_time": "0.05:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMS",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301531",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:03",
					"end_time": "0.07:05",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:16",
					"end_time": "0.07:18",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301724",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:52",
					"end_time": "0.09:37",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "VaLO",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:13",
					"end_time": "0.10:15",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302012",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:18",
					"end_time": "0.11:20",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:38",
					"end_time": "0.11:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302268",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:22",
					"end_time": "0.13:24",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "attendance",
					"start_time": "0.13:24",
					"end_time": "0.13:33",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTCLO",
					"duty_id": "60"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:33",
					"end_time": "0.13:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301752",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:11",
					"end_time": "0.15:13",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:28",
					"end_time": "0.15:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301585",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.17:16",
					"end_time": "0.17:31",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "133"
				}
			]
		},
		{
			"vehicle_id": "23",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:21",
					"end_time": "0.04:41",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:41",
					"end_time": "0.05:11",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "SDPR",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301968",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:07",
					"end_time": "0.06:42",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "EMSLO",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:55",
					"end_time": "0.06:57",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301544",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:02",
					"end_time": "0.08:06",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:43",
					"end_time": "0.08:45",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302005",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:48",
					"end_time": "0.09:50",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:58",
					"end_time": "0.10:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301568",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:41",
					"end_time": "0.11:43",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "11"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:43",
					"end_time": "0.11:45",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301747",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:40",
					"end_time": "0.13:42",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:13",
					"end_time": "0.14:35",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301627",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:02",
					"end_time": "0.16:04",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:03",
					"end_time": "0.17:05",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301765",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:48",
					"end_time": "0.18:50",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:58",
					"end_time": "0.19:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301609",
					"duty_id": "96"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:36",
					"end_time": "0.20:51",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "96"
				}
			]
		},
		{
			"vehicle_id": "24",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:25",
					"end_time": "0.04:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:45",
					"end_time": "0.05:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMS",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301532",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:34",
					"end_time": "0.06:38",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:56",
					"end_time": "0.06:58",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301994",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:01",
					"end_time": "0.08:03",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:28",
					"end_time": "0.08:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301559",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:54",
					"end_time": "0.10:00",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:40",
					"end_time": "0.11:00",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "PTC",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301885",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:22",
					"end_time": "0.12:26",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:44",
					"end_time": "0.12:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301808",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:54",
					"end_time": "0.13:56",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "72"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:56",
					"end_time": "0.14:56",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301629",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:17",
					"end_time": "0.16:35",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "PHM",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301823",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301418",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:23",
					"end_time": "0.19:03",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "138"
				}
			]
		},
		{
			"vehicle_id": "25",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:25",
					"end_time": "0.04:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:45",
					"end_time": "0.05:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301694",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:17",
					"end_time": "0.06:54",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "PHMLO",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:43",
					"end_time": "0.07:44",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302140",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:27",
					"end_time": "0.08:29",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:38",
					"end_time": "0.08:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302107",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:26",
					"end_time": "0.09:30",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:42",
					"end_time": "0.09:43",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302148",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:23",
					"end_time": "0.10:25",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:43",
					"end_time": "0.10:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302203",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.11:46",
					"end_time": "0.12:01",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "13"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.12:35",
					"end_time": "0.12:55",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.12:55",
					"end_time": "0.13:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301445",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:55",
					"end_time": "0.14:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:10",
					"end_time": "0.15:12",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301584",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:39",
					"end_time": "0.16:45",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:24",
					"end_time": "0.17:32",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301453",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:57",
					"end_time": "0.18:59",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:08",
					"end_time": "0.19:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302125",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:57",
					"end_time": "0.20:01",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:19",
					"end_time": "0.20:20",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302151",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:58",
					"end_time": "0.21:00",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:08",
					"end_time": "0.21:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302129",
					"duty_id": "105"
				},
				{
					"vehicle_event_sequence": "34",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:52",
					"end_time": "0.22:32",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "105"
				}
			]
		},
		{
			"vehicle_id": "26",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:25",
					"end_time": "0.04:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:45",
					"end_time": "0.05:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301984",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:55",
					"end_time": "0.05:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:08",
					"end_time": "0.06:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301537",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:10",
					"end_time": "0.07:30",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "MTCLO",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:44",
					"end_time": "0.07:46",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301729",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:18",
					"end_time": "0.09:41",
					"origin_stop_id": "EMS",
					"destination_stop_id": "RiVa",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301958",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:13",
					"end_time": "0.11:15",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:28",
					"end_time": "0.11:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302168",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302175",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.13:29",
					"end_time": "0.13:39",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "73"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:05",
					"end_time": "0.14:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:25",
					"end_time": "0.14:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301904",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301963",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:15",
					"end_time": "0.16:17",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:27",
					"end_time": "0.16:29",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301917",
					"duty_id": "120"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.17:24",
					"end_time": "0.17:39",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "120"
				}
			]
		},
		{
			"vehicle_id": "27",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:26",
					"end_time": "0.04:46",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:46",
					"end_time": "0.05:16",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "IMPR",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302179",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:12",
					"end_time": "0.06:52",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "CiCLO",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:02",
					"end_time": "0.07:10",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301437",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:35",
					"end_time": "0.08:37",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:46",
					"end_time": "0.08:48",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301562",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:49",
					"end_time": "0.09:53",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:43",
					"end_time": "0.10:45",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302015",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:48",
					"end_time": "0.11:50",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:58",
					"end_time": "0.12:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301573",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:45",
					"end_time": "0.13:47",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "74"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:47",
					"end_time": "0.13:49",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301753",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:43",
					"end_time": "0.15:45",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:58",
					"end_time": "0.16:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301587",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:50",
					"end_time": "0.17:52",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:59",
					"end_time": "0.18:01",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301767",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:51",
					"end_time": "0.19:01",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "139"
				}
			]
		},
		{
			"vehicle_id": "28",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:30",
					"end_time": "0.04:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:50",
					"end_time": "0.05:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301695",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:29",
					"end_time": "0.06:31",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:43",
					"end_time": "0.06:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301543",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:49",
					"end_time": "0.08:00",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "IMPR",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301686",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:11",
					"end_time": "0.09:48",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "PHMLO",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:39",
					"end_time": "0.10:40",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301800",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:48",
					"end_time": "0.11:50",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:58",
					"end_time": "0.12:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301890",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:22",
					"end_time": "0.13:26",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "75"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:26",
					"end_time": "0.13:27",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302157",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:25",
					"end_time": "0.14:27",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:38",
					"end_time": "0.14:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302116",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:30",
					"end_time": "0.15:34",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:44",
					"end_time": "0.15:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301820",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:09",
					"end_time": "0.17:11",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:58",
					"end_time": "0.18:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301926",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:24",
					"end_time": "0.19:28",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:34",
					"end_time": "0.19:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301835",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301421",
					"duty_id": "108"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:15",
					"end_time": "0.21:55",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "108"
				}
			]
		},
		{
			"vehicle_id": "29",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:30",
					"end_time": "0.04:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:50",
					"end_time": "0.05:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301846",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.05:59",
					"end_time": "0.06:03",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:09",
					"end_time": "0.06:10",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301781",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:20",
					"end_time": "0.07:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:33",
					"end_time": "0.07:35",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301866",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:23",
					"end_time": "0.08:30",
					"origin_stop_id": "RiVa",
					"destination_stop_id": "PTC",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301872",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:25",
					"end_time": "0.09:27",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:03",
					"end_time": "0.10:05",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301741",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:40",
					"end_time": "0.11:42",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "attendance",
					"start_time": "0.11:42",
					"end_time": "0.11:58",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMSLO",
					"duty_id": "15"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:58",
					"end_time": "0.12:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302208",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:04",
					"end_time": "0.13:08",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:13",
					"end_time": "0.13:15",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302192",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:20",
					"end_time": "0.14:22",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:33",
					"end_time": "0.14:35",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301581",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:02",
					"end_time": "0.16:08",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:54",
					"end_time": "0.17:02",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301452",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:27",
					"end_time": "0.18:29",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:38",
					"end_time": "0.18:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302124",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:30",
					"end_time": "0.19:34",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:44",
					"end_time": "0.19:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301836",
					"duty_id": "95"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:56",
					"end_time": "0.21:06",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "95"
				}
			]
		},
		{
			"vehicle_id": "30",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:30",
					"end_time": "0.04:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "122"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:50",
					"end_time": "0.05:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CoTC",
					"duty_id": "122"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302241",
					"duty_id": "122"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:23",
					"end_time": "0.07:13",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "IMPR",
					"duty_id": "122"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301684",
					"duty_id": "122"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:21",
					"end_time": "0.09:16",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "122"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:50",
					"end_time": "0.14:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:10",
					"end_time": "0.14:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MoHa",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302185",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301429",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:49",
					"end_time": "0.15:51",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:58",
					"end_time": "0.16:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301913",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301400",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.17:55",
					"end_time": "0.18:05",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "125"
				}
			]
		},
		{
			"vehicle_id": "31",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:34",
					"end_time": "0.04:54",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:54",
					"end_time": "0.05:24",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "SDPR",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301969",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:21",
					"end_time": "0.07:11",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "SDPR",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301979",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:23",
					"end_time": "0.09:18",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "123"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.15:00",
					"end_time": "0.15:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.15:20",
					"end_time": "0.15:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CTC",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301430",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:19",
					"end_time": "0.16:21",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:28",
					"end_time": "0.17:28",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301662",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:03",
					"end_time": "0.19:18",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "41"
				}
			]
		},
		{
			"vehicle_id": "32",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:35",
					"end_time": "0.04:55",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:55",
					"end_time": "0.05:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PHM",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301779",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301407",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:14",
					"end_time": "0.07:18",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:24",
					"end_time": "0.07:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301786",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:08",
					"end_time": "0.08:12",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:19",
					"end_time": "0.08:21",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302002",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:25",
					"end_time": "0.09:56",
					"origin_stop_id": "EMS",
					"destination_stop_id": "BeLH",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301411",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:23",
					"end_time": "0.11:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:39",
					"end_time": "0.11:40",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301804",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:50",
					"end_time": "0.12:52",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "17"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:52",
					"end_time": "0.12:54",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301895",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:23",
					"end_time": "0.14:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:42",
					"end_time": "0.14:43",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302161",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:26",
					"end_time": "0.15:28",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:38",
					"end_time": "0.15:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302118",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:31",
					"end_time": "0.16:35",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:34",
					"end_time": "0.17:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301827",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301419",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:19",
					"end_time": "0.19:23",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:43",
					"end_time": "0.19:44",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302143",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:24",
					"end_time": "0.20:26",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:38",
					"end_time": "0.20:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302128",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "34",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:23",
					"end_time": "0.21:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "35",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:44",
					"end_time": "0.21:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "36",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301841",
					"duty_id": "107"
				},
				{
					"vehicle_event_sequence": "37",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:47",
					"end_time": "0.22:57",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "107"
				}
			]
		},
		{
			"vehicle_id": "33",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:40",
					"end_time": "0.05:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:00",
					"end_time": "0.05:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301433",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:51",
					"end_time": "0.06:53",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:08",
					"end_time": "0.07:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302104",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:56",
					"end_time": "0.08:00",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:09",
					"end_time": "0.08:10",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301789",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:32",
					"end_time": "0.09:34",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "attendance",
					"start_time": "0.09:34",
					"end_time": "0.10:28",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTCLO",
					"duty_id": "143"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:28",
					"end_time": "0.10:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301881",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:25",
					"end_time": "0.11:27",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:33",
					"end_time": "0.11:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301746",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:09",
					"end_time": "0.13:11",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:28",
					"end_time": "0.13:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301576",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:57",
					"end_time": "0.15:03",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:56",
					"end_time": "0.16:15",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "TeSC",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302032",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:21",
					"end_time": "0.17:23",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:29",
					"end_time": "0.17:31",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301599",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:38",
					"end_time": "0.18:42",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:53",
					"end_time": "0.18:55",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302044",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:58",
					"end_time": "0.20:00",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:08",
					"end_time": "0.20:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302127",
					"duty_id": "91"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:53",
					"end_time": "0.21:33",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "91"
				}
			]
		},
		{
			"vehicle_id": "34",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:40",
					"end_time": "0.05:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:00",
					"end_time": "0.05:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PHM",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301780",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:47",
					"end_time": "0.06:57",
					"origin_stop_id": "PTC",
					"destination_stop_id": "VaLO",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:08",
					"end_time": "0.07:10",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301995",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:14",
					"end_time": "0.08:16",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:22",
					"end_time": "0.08:24",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301558",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:26",
					"end_time": "0.09:30",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:30",
					"end_time": "0.09:32",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302010",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:48",
					"end_time": "0.10:50",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:13",
					"end_time": "0.11:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302205",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:16",
					"end_time": "0.12:20",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:28",
					"end_time": "0.12:30",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302189",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:34",
					"end_time": "0.13:36",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:43",
					"end_time": "0.13:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302215",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:50",
					"end_time": "0.14:54",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:45",
					"end_time": "0.16:31",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301651",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:53",
					"end_time": "0.18:43",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "Fi9t",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301676",
					"duty_id": "36"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:52",
					"end_time": "0.20:22",
					"origin_stop_id": "SDPR",
					"destination_stop_id": "Pomona",
					"duty_id": "36"
				}
			]
		},
		{
			"vehicle_id": "35",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:40",
					"end_time": "0.05:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:00",
					"end_time": "0.05:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301985",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:11",
					"end_time": "0.06:13",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:28",
					"end_time": "0.06:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301540",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:07",
					"end_time": "0.08:09",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:03",
					"end_time": "0.09:05",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301738",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:40",
					"end_time": "0.10:42",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:58",
					"end_time": "0.11:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301571",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.12:42",
					"end_time": "0.12:57",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "19"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:30",
					"end_time": "0.14:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:50",
					"end_time": "0.15:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301757",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:43",
					"end_time": "0.16:45",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:58",
					"end_time": "0.17:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301594",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:50",
					"end_time": "0.19:05",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "52"
				}
			]
		},
		{
			"vehicle_id": "36",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:42",
					"end_time": "0.05:02",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:02",
					"end_time": "0.05:17",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301697",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:34",
					"end_time": "0.07:34",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "CTC",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301426",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:25",
					"end_time": "0.08:27",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:33",
					"end_time": "0.08:35",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301873",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:28",
					"end_time": "0.09:35",
					"origin_stop_id": "RiVa",
					"destination_stop_id": "PTC",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301878",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:12",
					"end_time": "0.11:15",
					"origin_stop_id": "RiVa",
					"destination_stop_id": "TeSC",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302017",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:19",
					"end_time": "0.12:21",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:38",
					"end_time": "0.12:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302266",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:25",
					"end_time": "0.14:30",
					"origin_stop_id": "MTC",
					"destination_stop_id": "CTC",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301428",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:14",
					"end_time": "0.15:16",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "76"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:16",
					"end_time": "0.15:18",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301912",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301964",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:17",
					"end_time": "0.17:19",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:58",
					"end_time": "0.18:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301927",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:55",
					"end_time": "0.18:57",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:03",
					"end_time": "0.19:05",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301771",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:36",
					"end_time": "0.20:38",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:58",
					"end_time": "0.21:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301621",
					"duty_id": "28"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:34",
					"end_time": "0.22:49",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "28"
				}
			]
		},
		{
			"vehicle_id": "37",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:44",
					"end_time": "0.05:04",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:04",
					"end_time": "0.05:34",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "IMPR",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301679",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:30",
					"end_time": "0.07:14",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "PTCLO",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:28",
					"end_time": "0.07:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301863",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:56",
					"end_time": "0.09:00",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:09",
					"end_time": "0.09:10",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301793",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:32",
					"end_time": "0.10:34",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:33",
					"end_time": "0.11:35",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301888",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301960",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:13",
					"end_time": "0.13:15",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "attendance",
					"start_time": "0.13:15",
					"end_time": "0.13:33",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTCLO",
					"duty_id": "21"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:33",
					"end_time": "0.13:35",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301898",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301962",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:15",
					"end_time": "0.15:17",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:24",
					"end_time": "0.16:24",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301644",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:02",
					"end_time": "0.18:19",
					"origin_stop_id": "MTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:58",
					"end_time": "0.19:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301932",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:55",
					"end_time": "0.19:57",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:03",
					"end_time": "0.20:05",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301774",
					"duty_id": "8"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:31",
					"end_time": "0.22:23",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "8"
				}
			]
		},
		{
			"vehicle_id": "38",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:50",
					"end_time": "0.05:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:10",
					"end_time": "0.05:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301699",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:49",
					"end_time": "0.06:51",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:03",
					"end_time": "0.07:05",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301546",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:29",
					"end_time": "0.08:35",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:27",
					"end_time": "0.09:35",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301441",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:00",
					"end_time": "0.11:02",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:08",
					"end_time": "0.11:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302111",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:00",
					"end_time": "0.12:04",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:12",
					"end_time": "0.12:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302154",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:55",
					"end_time": "0.12:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "attendance",
					"start_time": "0.12:57",
					"end_time": "0.13:13",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMSLO",
					"duty_id": "77"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:13",
					"end_time": "0.13:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302213",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:19",
					"end_time": "0.14:23",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:28",
					"end_time": "0.14:30",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302197",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:35",
					"end_time": "0.15:37",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:00",
					"end_time": "0.16:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302256",
					"sub_trip_index": "1",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302256",
					"sub_trip_index": "2",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:25",
					"end_time": "0.18:30",
					"origin_stop_id": "GrPR",
					"destination_stop_id": "CiGL",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301454",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:55",
					"end_time": "0.19:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:08",
					"end_time": "0.20:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301617",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:08",
					"end_time": "0.21:12",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:23",
					"end_time": "0.21:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302050",
					"duty_id": "104"
				},
				{
					"vehicle_event_sequence": "34",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:25",
					"end_time": "0.23:17",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "104"
				}
			]
		},
		{
			"vehicle_id": "39",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:50",
					"end_time": "0.05:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:10",
					"end_time": "0.05:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301847",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:30",
					"end_time": "0.06:34",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:44",
					"end_time": "0.06:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302136",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:26",
					"end_time": "0.07:28",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:38",
					"end_time": "0.08:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "CiGL",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301439",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:25",
					"end_time": "0.09:27",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:38",
					"end_time": "0.09:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302109",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:26",
					"end_time": "0.10:30",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:24",
					"end_time": "0.11:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301802",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:12",
					"end_time": "0.12:16",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "attendance",
					"start_time": "0.12:16",
					"end_time": "0.12:23",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "VaLO",
					"duty_id": "23"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:23",
					"end_time": "0.12:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302022",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:12",
					"end_time": "0.13:16",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:34",
					"end_time": "0.13:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301811",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301415",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:23",
					"end_time": "0.15:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:14",
					"end_time": "0.16:15",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301821",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:42",
					"end_time": "0.17:44",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:50",
					"end_time": "0.18:05",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301768",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:39",
					"end_time": "0.19:41",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:58",
					"end_time": "0.20:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301615",
					"duty_id": "100"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:34",
					"end_time": "0.21:49",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "100"
				}
			]
		},
		{
			"vehicle_id": "40",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:52",
					"end_time": "0.05:12",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:12",
					"end_time": "0.05:27",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301701",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:44",
					"end_time": "0.07:34",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "SDPR",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301981",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:53",
					"end_time": "0.09:48",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "125"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.16:05",
					"end_time": "0.16:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.16:25",
					"end_time": "0.16:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301919",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301965",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:16",
					"end_time": "0.18:18",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:28",
					"end_time": "0.18:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301928",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:42",
					"end_time": "0.19:46",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:14",
					"end_time": "0.20:15",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301837",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:20",
					"end_time": "0.21:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:58",
					"end_time": "0.22:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301943",
					"duty_id": "32"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.23:05",
					"end_time": "0.23:45",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "32"
				}
			]
		},
		{
			"vehicle_id": "41",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:55",
					"end_time": "0.05:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:15",
					"end_time": "0.05:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301700",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:20",
					"end_time": "0.06:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:27",
					"end_time": "0.06:29",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301856",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:25",
					"end_time": "0.07:30",
					"origin_stop_id": "CTC",
					"destination_stop_id": "MTC",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301727",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:20",
					"end_time": "0.08:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:28",
					"end_time": "0.08:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302165",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302172",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:29",
					"end_time": "0.10:31",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:28",
					"end_time": "0.11:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301887",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:40",
					"end_time": "0.12:44",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:14",
					"end_time": "0.13:15",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301809",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:35",
					"end_time": "0.14:37",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:58",
					"end_time": "0.15:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301908",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:55",
					"end_time": "0.15:57",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "attendance",
					"start_time": "0.15:57",
					"end_time": "0.16:03",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTCLO",
					"duty_id": "79"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:03",
					"end_time": "0.16:05",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301761",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:46",
					"end_time": "0.17:48",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:58",
					"end_time": "0.18:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301602",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:45",
					"end_time": "0.19:47",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:58",
					"end_time": "0.20:00",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301773",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:50",
					"end_time": "0.20:52",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:28",
					"end_time": "0.21:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301941",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "34",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:34",
					"end_time": "0.22:38",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "35",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:54",
					"end_time": "0.22:55",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "36",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301842",
					"duty_id": "31"
				},
				{
					"vehicle_event_sequence": "37",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.23:55",
					"end_time": "1.00:05",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "31"
				}
			]
		},
		{
			"vehicle_id": "42",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:55",
					"end_time": "0.05:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:15",
					"end_time": "0.05:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301848",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:20",
					"end_time": "0.06:25",
					"origin_stop_id": "MTC",
					"destination_stop_id": "CTC",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301424",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:15",
					"end_time": "0.07:17",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:28",
					"end_time": "0.07:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301864",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:25",
					"end_time": "0.08:30",
					"origin_stop_id": "CTC",
					"destination_stop_id": "MTC",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301736",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:20",
					"end_time": "0.09:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:58",
					"end_time": "0.10:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301880",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:22",
					"end_time": "0.11:26",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:34",
					"end_time": "0.11:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301803",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301413",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:23",
					"end_time": "0.13:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:44",
					"end_time": "0.13:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301812",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.15:05",
					"end_time": "0.15:15",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "80"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.15:35",
					"end_time": "0.15:55",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.15:55",
					"end_time": "0.16:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301451",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:55",
					"end_time": "0.17:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:13",
					"end_time": "0.18:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301604",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:38",
					"end_time": "0.19:44",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:22",
					"end_time": "0.20:30",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301456",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:46",
					"end_time": "0.21:48",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:01",
					"end_time": "0.22:25",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "TeSC",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302052",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "33",
					"vehicle_event_type": "deadhead",
					"start_time": "0.23:20",
					"end_time": "0.23:22",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "34",
					"vehicle_event_type": "deadhead",
					"start_time": "0.23:28",
					"end_time": "0.23:50",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "PHM",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "35",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302155",
					"duty_id": "30"
				},
				{
					"vehicle_event_sequence": "36",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "1.00:28",
					"end_time": "1.01:13",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "30"
				}
			]
		},
		{
			"vehicle_id": "43",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:55",
					"end_time": "0.05:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:15",
					"end_time": "0.05:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "RiVa",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301953",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:09",
					"end_time": "0.06:25",
					"origin_stop_id": "PTC",
					"destination_stop_id": "IMPR",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301682",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.07:27",
					"end_time": "0.08:22",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:55",
					"end_time": "0.15:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.15:15",
					"end_time": "0.15:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302028",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:35",
					"end_time": "0.16:37",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:43",
					"end_time": "0.16:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301592",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:10",
					"end_time": "0.18:16",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:07",
					"end_time": "0.19:30",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "PTC",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301933",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:38",
					"end_time": "0.20:42",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:49",
					"end_time": "0.20:50",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302162",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:28",
					"end_time": "0.21:30",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:38",
					"end_time": "0.21:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301624",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:37",
					"end_time": "0.22:41",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:53",
					"end_time": "0.22:55",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302053",
					"duty_id": "24"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.23:50",
					"end_time": "1.00:42",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "24"
				}
			]
		},
		{
			"vehicle_id": "44",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:55",
					"end_time": "0.05:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:15",
					"end_time": "0.05:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301986",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:27",
					"end_time": "0.06:49",
					"origin_stop_id": "EMS",
					"destination_stop_id": "GrPR",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302238",
					"sub_trip_index": "1",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302238",
					"sub_trip_index": "2",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:05",
					"end_time": "0.08:49",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "PTCLO",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:58",
					"end_time": "0.09:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301875",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:26",
					"end_time": "0.10:30",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:09",
					"end_time": "0.11:10",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301801",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:30",
					"end_time": "0.12:32",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:58",
					"end_time": "0.13:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301894",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301397",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:52",
					"end_time": "0.14:54",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "attendance",
					"start_time": "0.14:54",
					"end_time": "0.15:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTCLO",
					"duty_id": "78"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:00",
					"end_time": "0.16:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302233",
					"sub_trip_index": "1",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302233",
					"sub_trip_index": "2",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:16",
					"end_time": "0.17:35",
					"origin_stop_id": "GrPR",
					"destination_stop_id": "PTC",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301924",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301966",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:13",
					"end_time": "0.19:23",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "42"
				}
			]
		},
		{
			"vehicle_id": "45",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.04:58",
					"end_time": "0.05:18",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:18",
					"end_time": "0.05:48",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "SDPR",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301971",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:47",
					"end_time": "0.07:22",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "EMSLO",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:28",
					"end_time": "0.07:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301550",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:09",
					"end_time": "0.09:11",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:28",
					"end_time": "0.09:30",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301739",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:20",
					"end_time": "0.10:38",
					"origin_stop_id": "PTC",
					"destination_stop_id": "CiCLO",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:27",
					"end_time": "0.11:35",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301443",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:00",
					"end_time": "0.13:02",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:28",
					"end_time": "0.13:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301577",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:15",
					"end_time": "0.15:17",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:28",
					"end_time": "0.15:30",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301758",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:20",
					"end_time": "0.16:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "attendance",
					"start_time": "0.16:22",
					"end_time": "0.16:28",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTCLO",
					"duty_id": "81"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:28",
					"end_time": "0.16:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301918",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:58",
					"end_time": "0.18:02",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:19",
					"end_time": "0.18:20",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301829",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:50",
					"end_time": "0.19:52",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:58",
					"end_time": "0.20:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301937",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:55",
					"end_time": "0.20:57",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:43",
					"end_time": "0.21:45",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301777",
					"duty_id": "33"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.23:11",
					"end_time": "1.00:03",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "33"
				}
			]
		},
		{
			"vehicle_id": "46",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:00",
					"end_time": "0.05:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:20",
					"end_time": "0.05:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CTC",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301422",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:15",
					"end_time": "0.06:29",
					"origin_stop_id": "PTC",
					"destination_stop_id": "SDPR",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301975",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:37",
					"end_time": "0.08:27",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "IMPR",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301687",
					"duty_id": "128"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.09:37",
					"end_time": "0.10:32",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "128"
				}
			]
		},
		{
			"vehicle_id": "47",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:04",
					"end_time": "0.05:24",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:24",
					"end_time": "0.05:59",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301434",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:20",
					"end_time": "0.07:22",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:34",
					"end_time": "0.07:36",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301551",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:39",
					"end_time": "0.08:43",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:58",
					"end_time": "0.09:00",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302006",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.10:03",
					"end_time": "0.10:48",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "129"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:18",
					"end_time": "0.13:38",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.13:38",
					"end_time": "0.14:48",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301628",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:14",
					"end_time": "0.17:14",
					"origin_stop_id": "SDPR",
					"destination_stop_id": "Fi9t",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301658",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:51",
					"end_time": "0.18:53",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:33",
					"end_time": "0.19:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301772",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:06",
					"end_time": "0.21:08",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:28",
					"end_time": "0.21:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301623",
					"duty_id": "10"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.23:04",
					"end_time": "0.23:19",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "10"
				}
			]
		},
		{
			"vehicle_id": "48",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:04",
					"end_time": "0.05:24",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:24",
					"end_time": "0.05:54",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "IMPR",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301680",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:50",
					"end_time": "0.07:35",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "VaLO",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:47",
					"end_time": "0.07:49",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301999",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:53",
					"end_time": "0.09:33",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "130"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:30",
					"end_time": "0.14:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:50",
					"end_time": "0.15:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301906",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:28",
					"end_time": "0.16:32",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:39",
					"end_time": "0.16:40",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301824",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:09",
					"end_time": "0.18:19",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "127"
				}
			]
		},
		{
			"vehicle_id": "49",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:05",
					"end_time": "0.05:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:25",
					"end_time": "0.05:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301849",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:22",
					"end_time": "0.06:25",
					"origin_stop_id": "RiVa",
					"destination_stop_id": "TeSC",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301992",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:08",
					"end_time": "0.07:43",
					"origin_stop_id": "PHM",
					"destination_stop_id": "IMPR",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301685",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:45",
					"end_time": "0.09:40",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "132"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:00",
					"end_time": "0.14:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:20",
					"end_time": "0.14:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301902",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:25",
					"end_time": "0.15:27",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:33",
					"end_time": "0.15:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301759",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:13",
					"end_time": "0.17:15",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:28",
					"end_time": "0.17:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301598",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:20",
					"end_time": "0.19:35",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "46"
				}
			]
		},
		{
			"vehicle_id": "50",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:06",
					"end_time": "0.05:26",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:26",
					"end_time": "0.05:41",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301704",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:06",
					"end_time": "0.07:56",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "SDPR",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301982",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:13",
					"end_time": "0.09:50",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "PHMLO",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:34",
					"end_time": "0.10:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301799",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301412",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:23",
					"end_time": "0.12:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:24",
					"end_time": "0.13:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301810",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:11",
					"end_time": "0.14:15",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:24",
					"end_time": "0.15:00",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "EMS",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301583",
					"duty_id": "82"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.16:46",
					"end_time": "0.17:01",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "82"
				}
			]
		},
		{
			"vehicle_id": "51",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:05",
					"end_time": "0.05:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:25",
					"end_time": "0.06:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "BMTC",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301389",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:52",
					"end_time": "0.07:06",
					"origin_stop_id": "PTC",
					"destination_stop_id": "SDPR",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301980",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:39",
					"end_time": "0.09:34",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "133"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.11:40",
					"end_time": "0.12:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.12:00",
					"end_time": "0.12:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301444",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:00",
					"end_time": "0.14:02",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:13",
					"end_time": "0.14:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302217",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:20",
					"end_time": "0.15:24",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:09",
					"end_time": "0.16:55",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302251",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:17",
					"end_time": "0.18:35",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "PHM",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301831",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301420",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:15",
					"end_time": "0.20:19",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:34",
					"end_time": "0.20:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301838",
					"duty_id": "97"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:11",
					"end_time": "0.21:56",
					"origin_stop_id": "BeLH",
					"destination_stop_id": "Pomona",
					"duty_id": "97"
				}
			]
		},
		{
			"vehicle_id": "52",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:10",
					"end_time": "0.05:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:30",
					"end_time": "0.05:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301703",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:09",
					"end_time": "0.07:11",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:22",
					"end_time": "0.07:24",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301548",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:28",
					"end_time": "0.08:32",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:13",
					"end_time": "0.09:15",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302007",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:19",
					"end_time": "0.10:21",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:28",
					"end_time": "0.10:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301570",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:11",
					"end_time": "0.12:13",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:28",
					"end_time": "0.12:30",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301748",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:20",
					"end_time": "0.13:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "attendance",
					"start_time": "0.13:22",
					"end_time": "0.13:28",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTCLO",
					"duty_id": "25"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:28",
					"end_time": "0.13:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301896",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:42",
					"end_time": "0.14:46",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:14",
					"end_time": "0.15:15",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301817",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:29",
					"end_time": "0.16:31",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:28",
					"end_time": "0.17:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301923",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:57",
					"end_time": "0.19:01",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:13",
					"end_time": "0.19:14",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302134",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:54",
					"end_time": "0.19:56",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:03",
					"end_time": "0.20:05",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301616",
					"duty_id": "18"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:21",
					"end_time": "0.21:53",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "Pomona",
					"duty_id": "18"
				}
			]
		},
		{
			"vehicle_id": "53",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:10",
					"end_time": "0.05:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:30",
					"end_time": "0.05:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301850",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:50",
					"end_time": "0.06:54",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:12",
					"end_time": "0.07:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302138",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:56",
					"end_time": "0.07:58",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:03",
					"end_time": "0.08:05",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301556",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:29",
					"end_time": "0.09:35",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:27",
					"end_time": "0.10:35",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301442",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:00",
					"end_time": "0.12:02",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:13",
					"end_time": "0.12:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302209",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:19",
					"end_time": "0.13:23",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:28",
					"end_time": "0.13:30",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302193",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:35",
					"end_time": "0.14:37",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "attendance",
					"start_time": "0.14:37",
					"end_time": "0.14:53",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMSLO",
					"duty_id": "84"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:53",
					"end_time": "0.14:55",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "61"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301582",
					"duty_id": "61"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:22",
					"end_time": "0.16:28",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "61"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:33",
					"end_time": "0.17:35",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "61"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302252",
					"duty_id": "61"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:49",
					"end_time": "0.19:19",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "Pomona",
					"duty_id": "61"
				}
			]
		},
		{
			"vehicle_id": "54",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:10",
					"end_time": "0.05:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:30",
					"end_time": "0.05:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301987",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:44",
					"end_time": "0.06:46",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:58",
					"end_time": "0.07:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301545",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:39",
					"end_time": "0.08:54",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:10",
					"end_time": "0.14:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:30",
					"end_time": "0.14:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302025",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:50",
					"end_time": "0.15:52",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:58",
					"end_time": "0.16:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302224",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:08",
					"end_time": "0.17:12",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:23",
					"end_time": "0.17:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302038",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:15",
					"end_time": "0.18:19",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:24",
					"end_time": "0.18:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301830",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:11",
					"end_time": "0.19:15",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:53",
					"end_time": "0.19:55",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302047",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:56",
					"end_time": "0.20:58",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:08",
					"end_time": "0.21:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301622",
					"duty_id": "22"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:07",
					"end_time": "0.22:22",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "22"
				}
			]
		},
		{
			"vehicle_id": "55",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:10",
					"end_time": "0.05:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:30",
					"end_time": "0.06:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "GrPR",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302242",
					"sub_trip_index": "1",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302242",
					"sub_trip_index": "2",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:05",
					"end_time": "0.07:55",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "IMPR",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302261",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:57",
					"end_time": "0.09:34",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "PHMLO",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:54",
					"end_time": "0.09:55",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302262",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:42",
					"end_time": "0.10:46",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:58",
					"end_time": "0.12:00",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302021",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:04",
					"end_time": "0.13:06",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:38",
					"end_time": "0.13:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302114",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:30",
					"end_time": "0.14:34",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:44",
					"end_time": "0.14:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301816",
					"duty_id": "83"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.16:07",
					"end_time": "0.16:17",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "83"
				}
			]
		},
		{
			"vehicle_id": "56",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:15",
					"end_time": "0.05:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:35",
					"end_time": "0.06:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PHM",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302135",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:56",
					"end_time": "0.06:58",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:10",
					"end_time": "0.07:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "CoTC",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302239",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:30",
					"end_time": "0.09:25",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:44",
					"end_time": "0.14:04",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:04",
					"end_time": "0.15:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301631",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:42",
					"end_time": "0.17:00",
					"origin_stop_id": "SDPR",
					"destination_stop_id": "PTC",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301921",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301401",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:55",
					"end_time": "0.19:05",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "37"
				}
			]
		},
		{
			"vehicle_id": "57",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:18",
					"end_time": "0.05:38",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:38",
					"end_time": "0.05:53",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301706",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:25",
					"end_time": "0.08:10",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "VaLO",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:23",
					"end_time": "0.08:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302004",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:12",
					"end_time": "0.09:16",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:24",
					"end_time": "0.09:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301794",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.10:12",
					"end_time": "0.10:27",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.15:25",
					"end_time": "0.15:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.15:45",
					"end_time": "0.16:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302031",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:06",
					"end_time": "0.17:08",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:13",
					"end_time": "0.17:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301596",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:39",
					"end_time": "0.18:45",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:06",
					"end_time": "0.19:25",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "TeSC",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302046",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:13",
					"end_time": "0.20:17",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:14",
					"end_time": "0.21:15",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301840",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:18",
					"end_time": "0.22:20",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:28",
					"end_time": "0.22:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301944",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.23:35",
					"end_time": "0.23:39",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.23:54",
					"end_time": "0.23:55",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301843",
					"duty_id": "29"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "1.00:55",
					"end_time": "1.01:05",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "29"
				}
			]
		},
		{
			"vehicle_id": "58",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:22",
					"end_time": "0.05:42",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:42",
					"end_time": "0.06:12",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "SDPR",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301973",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:12",
					"end_time": "0.07:47",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "EMSLO",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:58",
					"end_time": "0.08:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301555",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:38",
					"end_time": "0.09:55",
					"origin_stop_id": "MTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:33",
					"end_time": "0.10:35",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301883",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301959",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:13",
					"end_time": "0.12:15",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:28",
					"end_time": "0.12:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302169",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301427",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:44",
					"end_time": "0.14:46",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:58",
					"end_time": "0.15:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301905",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301399",
					"duty_id": "62"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.16:55",
					"end_time": "0.17:05",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "62"
				}
			]
		},
		{
			"vehicle_id": "59",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:22",
					"end_time": "0.05:42",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:42",
					"end_time": "0.05:57",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301988",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:57",
					"end_time": "0.06:59",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:10",
					"end_time": "0.07:12",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301547",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:16",
					"end_time": "0.08:20",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:31",
					"end_time": "0.08:33",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302003",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.09:37",
					"end_time": "0.10:17",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:00",
					"end_time": "0.13:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.13:20",
					"end_time": "0.13:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301897",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:25",
					"end_time": "0.14:27",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:33",
					"end_time": "0.14:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301755",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:13",
					"end_time": "0.16:15",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:28",
					"end_time": "0.16:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301590",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:20",
					"end_time": "0.18:22",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:58",
					"end_time": "0.19:00",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301770",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:50",
					"end_time": "0.19:52",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:58",
					"end_time": "0.20:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301936",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:04",
					"end_time": "0.21:08",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:19",
					"end_time": "0.21:20",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302147",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:58",
					"end_time": "0.22:00",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:08",
					"end_time": "0.22:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301625",
					"duty_id": "2"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.23:06",
					"end_time": "0.23:21",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "2"
				}
			]
		},
		{
			"vehicle_id": "60",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:23",
					"end_time": "0.05:43",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:43",
					"end_time": "0.05:53",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301851",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:48",
					"end_time": "0.06:50",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:58",
					"end_time": "0.07:00",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301721",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:50",
					"end_time": "0.07:52",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:58",
					"end_time": "0.08:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301870",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:55",
					"end_time": "0.08:57",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:33",
					"end_time": "0.09:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301740",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:10",
					"end_time": "0.11:12",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:18",
					"end_time": "0.11:20",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302269",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:02",
					"end_time": "0.13:04",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:28",
					"end_time": "0.13:30",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301751",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:20",
					"end_time": "0.14:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "attendance",
					"start_time": "0.14:22",
					"end_time": "0.14:28",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTCLO",
					"duty_id": "85"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:28",
					"end_time": "0.14:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301901",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:25",
					"end_time": "0.16:20",
					"origin_stop_id": "CTC",
					"destination_stop_id": "Fi9t",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302255",
					"sub_trip_index": "1",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302255",
					"sub_trip_index": "2",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:41",
					"end_time": "0.18:00",
					"origin_stop_id": "GrPR",
					"destination_stop_id": "PTC",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301925",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301402",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:52",
					"end_time": "0.20:02",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "56"
				}
			]
		},
		{
			"vehicle_id": "61",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:24",
					"end_time": "0.05:44",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:44",
					"end_time": "0.06:14",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "IMPR",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301681",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:11",
					"end_time": "0.07:46",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "EMSLO",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:58",
					"end_time": "0.08:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301554",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.09:03",
					"end_time": "0.09:18",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "138"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:30",
					"end_time": "0.13:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.13:50",
					"end_time": "0.14:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301900",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:23",
					"end_time": "0.15:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:42",
					"end_time": "0.15:43",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302137",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:29",
					"end_time": "0.16:31",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:38",
					"end_time": "0.16:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302120",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:32",
					"end_time": "0.17:36",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:43",
					"end_time": "0.17:44",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302153",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:30",
					"end_time": "0.19:10",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "43"
				}
			]
		},
		{
			"vehicle_id": "62",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:25",
					"end_time": "0.05:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:45",
					"end_time": "0.06:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301707",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:50",
					"end_time": "0.06:52",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:58",
					"end_time": "0.07:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301860",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301391",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:52",
					"end_time": "0.09:02",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "139"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:03",
					"end_time": "0.13:23",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.13:23",
					"end_time": "0.14:33",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302225",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:49",
					"end_time": "0.16:39",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "Fi9t",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301648",
					"duty_id": "134"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:16",
					"end_time": "0.18:31",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "134"
				}
			]
		},
		{
			"vehicle_id": "63",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:30",
					"end_time": "0.05:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:50",
					"end_time": "0.06:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CTC",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301423",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:45",
					"end_time": "0.06:47",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.06:58",
					"end_time": "0.07:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301861",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:26",
					"end_time": "0.08:30",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:39",
					"end_time": "0.08:40",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301792",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:02",
					"end_time": "0.10:12",
					"origin_stop_id": "PTC",
					"destination_stop_id": "VaLO",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:23",
					"end_time": "0.10:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302014",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:12",
					"end_time": "0.11:16",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:34",
					"end_time": "0.12:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301807",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301414",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:23",
					"end_time": "0.14:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:13",
					"end_time": "0.15:50",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301636",
					"duty_id": "86"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.17:24",
					"end_time": "0.17:39",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "86"
				}
			]
		},
		{
			"vehicle_id": "64",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:30",
					"end_time": "0.05:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:50",
					"end_time": "0.06:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301435",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:47",
					"end_time": "0.07:49",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:08",
					"end_time": "0.08:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302106",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:56",
					"end_time": "0.09:36",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "40"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:25",
					"end_time": "0.14:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:45",
					"end_time": "0.15:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302026",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:05",
					"end_time": "0.16:07",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:12",
					"end_time": "0.16:14",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301588",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:41",
					"end_time": "0.18:09",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "EMSLO",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:30",
					"end_time": "0.18:32",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301607",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:36",
					"end_time": "0.19:51",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "53"
				}
			]
		},
		{
			"vehicle_id": "65",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:30",
					"end_time": "0.05:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:50",
					"end_time": "0.06:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301709",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:31",
					"end_time": "0.07:33",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:43",
					"end_time": "0.07:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301552",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.09:09",
					"end_time": "0.09:49",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "Pomona",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:29",
					"end_time": "0.14:49",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:49",
					"end_time": "0.16:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301637",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:27",
					"end_time": "0.17:36",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "TeSC",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302039",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:41",
					"end_time": "0.18:43",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:48",
					"end_time": "0.18:50",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301608",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:52",
					"end_time": "0.20:07",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "57"
				}
			]
		},
		{
			"vehicle_id": "66",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:30",
					"end_time": "0.05:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:50",
					"end_time": "0.06:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301710",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:37",
					"end_time": "0.08:16",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "RiVa",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301956",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.09:11",
					"end_time": "0.09:21",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "37"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.15:00",
					"end_time": "0.15:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.15:20",
					"end_time": "0.15:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301909",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:50",
					"end_time": "0.16:54",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:08",
					"end_time": "0.17:45",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301666",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:18",
					"end_time": "0.19:33",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "47"
				}
			]
		},
		{
			"vehicle_id": "67",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:30",
					"end_time": "0.05:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:50",
					"end_time": "0.06:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301852",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301390",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:52",
					"end_time": "0.07:54",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:05",
					"end_time": "0.08:07",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301869",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:56",
					"end_time": "0.09:11",
					"origin_stop_id": "CTC",
					"destination_stop_id": "Pomona",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:29",
					"end_time": "0.13:49",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.13:49",
					"end_time": "0.15:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302232",
					"sub_trip_index": "1",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302232",
					"sub_trip_index": "2",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:15",
					"end_time": "0.16:30",
					"origin_stop_id": "GrPR",
					"destination_stop_id": "TeSC",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302033",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:37",
					"end_time": "0.17:39",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:45",
					"end_time": "0.17:47",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301601",
					"duty_id": "38"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:54",
					"end_time": "0.19:09",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "38"
				}
			]
		},
		{
			"vehicle_id": "68",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:30",
					"end_time": "0.05:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:50",
					"end_time": "0.06:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301853",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301425",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:45",
					"end_time": "0.07:47",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:58",
					"end_time": "0.08:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301868",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:27",
					"end_time": "0.09:31",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:39",
					"end_time": "0.09:40",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301796",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:53",
					"end_time": "0.10:55",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:58",
					"end_time": "0.12:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301889",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301396",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:52",
					"end_time": "0.13:54",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:02",
					"end_time": "0.14:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "EMS",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301580",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:15",
					"end_time": "0.16:17",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:28",
					"end_time": "0.16:30",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301762",
					"duty_id": "87"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.17:20",
					"end_time": "0.17:30",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "87"
				}
			]
		},
		{
			"vehicle_id": "69",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:30",
					"end_time": "0.05:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:50",
					"end_time": "0.06:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301854",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:19",
					"end_time": "0.07:23",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:34",
					"end_time": "0.07:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301787",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301409",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:23",
					"end_time": "0.09:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:34",
					"end_time": "0.09:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301795",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:16",
					"end_time": "0.11:45",
					"origin_stop_id": "BeLH",
					"destination_stop_id": "EMS",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302207",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:49",
					"end_time": "0.12:53",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:58",
					"end_time": "0.13:00",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302191",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:04",
					"end_time": "0.14:06",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:25",
					"end_time": "0.15:05",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301630",
					"duty_id": "88"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.16:35",
					"end_time": "0.16:50",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "88"
				}
			]
		},
		{
			"vehicle_id": "70",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:34",
					"end_time": "0.05:54",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:54",
					"end_time": "0.06:09",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301989",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:09",
					"end_time": "0.07:11",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:23",
					"end_time": "0.07:25",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301549",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:49",
					"end_time": "0.09:29",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "Pomona",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.10:30",
					"end_time": "0.10:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.10:50",
					"end_time": "0.11:05",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301744",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:39",
					"end_time": "0.12:41",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:58",
					"end_time": "0.13:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301575",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:45",
					"end_time": "0.14:47",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:58",
					"end_time": "0.15:00",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301756",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:50",
					"end_time": "0.15:52",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "89"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:52",
					"end_time": "0.15:54",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301915",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:00",
					"end_time": "0.17:55",
					"origin_stop_id": "CTC",
					"destination_stop_id": "Fi9t",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301668",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:27",
					"end_time": "0.19:42",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "49"
				}
			]
		},
		{
			"vehicle_id": "71",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:42",
					"end_time": "0.06:02",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:02",
					"end_time": "0.06:17",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301712",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:49",
					"end_time": "0.08:26",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "PHMLO",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:34",
					"end_time": "0.08:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301791",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301410",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.10:23",
					"end_time": "0.11:03",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "41"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:30",
					"end_time": "0.14:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:50",
					"end_time": "0.15:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301907",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:59",
					"end_time": "0.16:54",
					"origin_stop_id": "CTC",
					"destination_stop_id": "Fi9t",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301653",
					"duty_id": "136"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:32",
					"end_time": "0.18:47",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "136"
				}
			]
		},
		{
			"vehicle_id": "72",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:46",
					"end_time": "0.06:06",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:06",
					"end_time": "0.06:21",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301990",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:22",
					"end_time": "0.07:24",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:38",
					"end_time": "0.07:40",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302105",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:26",
					"end_time": "0.08:30",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:42",
					"end_time": "0.08:43",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302144",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:28",
					"end_time": "0.09:30",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:43",
					"end_time": "0.09:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302199",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:46",
					"end_time": "0.10:50",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "42"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:50",
					"end_time": "0.10:52",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302016",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:04",
					"end_time": "0.12:06",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:28",
					"end_time": "0.12:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302210",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:34",
					"end_time": "0.13:38",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:43",
					"end_time": "0.13:45",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302194",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:50",
					"end_time": "0.14:52",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:58",
					"end_time": "0.15:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302220",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:08",
					"end_time": "0.16:12",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:17",
					"end_time": "0.18:03",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301669",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:12",
					"end_time": "0.19:23",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "RiVa",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301967",
					"duty_id": "92"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:13",
					"end_time": "0.20:23",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "92"
				}
			]
		},
		{
			"vehicle_id": "73",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:50",
					"end_time": "0.06:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:10",
					"end_time": "0.06:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301713",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:51",
					"end_time": "0.07:53",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:10",
					"end_time": "0.08:12",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301557",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:15",
					"end_time": "0.09:19",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "43"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:19",
					"end_time": "0.09:21",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302008",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:33",
					"end_time": "0.10:35",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:58",
					"end_time": "0.11:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302204",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:01",
					"end_time": "0.12:05",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:13",
					"end_time": "0.12:15",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302188",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:19",
					"end_time": "0.13:21",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:28",
					"end_time": "0.13:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302214",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:34",
					"end_time": "0.14:38",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:34",
					"end_time": "0.16:20",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301647",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:43",
					"end_time": "0.18:33",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "Fi9t",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301674",
					"duty_id": "35"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:42",
					"end_time": "0.20:12",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "Pomona",
					"duty_id": "35"
				}
			]
		},
		{
			"vehicle_id": "74",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:50",
					"end_time": "0.06:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:10",
					"end_time": "0.06:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301855",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:15",
					"end_time": "0.07:17",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:25",
					"end_time": "0.07:27",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301725",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:59",
					"end_time": "0.09:01",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:28",
					"end_time": "0.09:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302198",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.10:31",
					"end_time": "0.10:46",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.15:00",
					"end_time": "0.15:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.15:20",
					"end_time": "0.15:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301910",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:38",
					"end_time": "0.17:33",
					"origin_stop_id": "CTC",
					"destination_stop_id": "Fi9t",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301663",
					"duty_id": "44"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:49",
					"end_time": "0.19:19",
					"origin_stop_id": "SDPR",
					"destination_stop_id": "Pomona",
					"duty_id": "44"
				}
			]
		},
		{
			"vehicle_id": "75",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:50",
					"end_time": "0.06:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:10",
					"end_time": "0.06:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302177",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:39",
					"end_time": "0.07:43",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:54",
					"end_time": "0.07:55",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302249",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:38",
					"end_time": "0.08:42",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:49",
					"end_time": "0.09:00",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "PTC",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301874",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301393",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.10:52",
					"end_time": "0.11:02",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:00",
					"end_time": "0.13:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.13:20",
					"end_time": "0.14:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMS",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302115",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:00",
					"end_time": "0.15:04",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:12",
					"end_time": "0.15:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302163",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:59",
					"end_time": "0.16:01",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:13",
					"end_time": "0.16:15",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301589",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:23",
					"end_time": "0.17:27",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:23",
					"end_time": "0.18:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302042",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:15",
					"end_time": "0.19:19",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:24",
					"end_time": "0.19:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301834",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:09",
					"end_time": "0.20:13",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:23",
					"end_time": "0.20:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302048",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "29",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:25",
					"end_time": "0.21:27",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "30",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:32",
					"end_time": "0.22:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "PTC",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "31",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301942",
					"duty_id": "4"
				},
				{
					"vehicle_event_sequence": "32",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:48",
					"end_time": "0.23:23",
					"origin_stop_id": "BMTC",
					"destination_stop_id": "Pomona",
					"duty_id": "4"
				}
			]
		},
		{
			"vehicle_id": "76",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:55",
					"end_time": "0.06:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:15",
					"end_time": "0.06:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301715",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:20",
					"end_time": "0.07:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:28",
					"end_time": "0.07:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301865",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:25",
					"end_time": "0.08:27",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:43",
					"end_time": "0.08:45",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301737",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.10:18",
					"end_time": "0.11:03",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "47"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:50",
					"end_time": "0.14:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:10",
					"end_time": "0.14:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302024",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:15",
					"end_time": "0.15:19",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:24",
					"end_time": "0.15:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301818",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:15",
					"end_time": "0.16:19",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:34",
					"end_time": "0.17:20",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302257",
					"sub_trip_index": "1",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302257",
					"sub_trip_index": "2",
					"duty_id": "137"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:29",
					"end_time": "0.18:59",
					"origin_stop_id": "GrPR",
					"destination_stop_id": "Pomona",
					"duty_id": "137"
				}
			]
		},
		{
			"vehicle_id": "77",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:55",
					"end_time": "0.06:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:15",
					"end_time": "0.06:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "RiVa",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301954",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:09",
					"end_time": "0.07:11",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:16",
					"end_time": "0.07:31",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301726",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.09:05",
					"end_time": "0.10:00",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "46"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:05",
					"end_time": "0.14:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:25",
					"end_time": "0.15:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "EMS",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302221",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:23",
					"end_time": "0.16:27",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:43",
					"end_time": "0.16:45",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302035",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:53",
					"end_time": "0.17:55",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:01",
					"end_time": "0.18:03",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301603",
					"duty_id": "45"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:10",
					"end_time": "0.19:25",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "45"
				}
			]
		},
		{
			"vehicle_id": "78",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:58",
					"end_time": "0.06:18",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:18",
					"end_time": "0.06:33",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301716",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:06",
					"end_time": "0.08:43",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "PHMLO",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:54",
					"end_time": "0.08:55",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302250",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.09:41",
					"end_time": "0.09:56",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:32",
					"end_time": "0.14:52",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:52",
					"end_time": "0.16:03",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301639",
					"duty_id": "121"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.17:39",
					"end_time": "0.17:54",
					"origin_stop_id": "MTC",
					"destination_stop_id": "Pomona",
					"duty_id": "121"
				}
			]
		},
		{
			"vehicle_id": "79",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.06:05",
					"end_time": "0.06:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:25",
					"end_time": "0.06:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301857",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301955",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:11",
					"end_time": "0.08:13",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:28",
					"end_time": "0.08:30",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301871",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:57",
					"end_time": "0.10:01",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:09",
					"end_time": "0.10:10",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301797",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.11:29",
					"end_time": "0.11:39",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "49"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.15:05",
					"end_time": "0.15:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.15:25",
					"end_time": "0.16:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301450",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:25",
					"end_time": "0.17:27",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:43",
					"end_time": "0.17:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301600",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:09",
					"end_time": "0.19:54",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "Pomona",
					"duty_id": "54"
				}
			]
		},
		{
			"vehicle_id": "80",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.06:10",
					"end_time": "0.06:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:30",
					"end_time": "0.06:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301858",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:59",
					"end_time": "0.08:03",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:12",
					"end_time": "0.08:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302142",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:58",
					"end_time": "0.09:00",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:28",
					"end_time": "0.09:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301566",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.10:54",
					"end_time": "0.11:34",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "Pomona",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:14",
					"end_time": "0.14:34",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:34",
					"end_time": "0.15:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301635",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:04",
					"end_time": "0.17:18",
					"origin_stop_id": "SDPR",
					"destination_stop_id": "TeSC",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302037",
					"duty_id": "39"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:24",
					"end_time": "0.19:04",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "39"
				}
			]
		},
		{
			"vehicle_id": "81",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.06:11",
					"end_time": "0.06:31",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:31",
					"end_time": "0.06:46",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301718",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:12",
					"end_time": "0.08:14",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:28",
					"end_time": "0.08:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301560",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:08",
					"end_time": "0.10:10",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:28",
					"end_time": "0.10:30",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301742",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:20",
					"end_time": "0.11:22",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "52"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:22",
					"end_time": "0.11:24",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301886",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:25",
					"end_time": "0.12:27",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:33",
					"end_time": "0.12:35",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301749",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:10",
					"end_time": "0.14:12",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:28",
					"end_time": "0.14:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302218",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:36",
					"end_time": "0.15:40",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:29",
					"end_time": "0.17:15",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302248",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:40",
					"end_time": "0.19:00",
					"origin_stop_id": "IMPR",
					"destination_stop_id": "PTC",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301931",
					"duty_id": "94"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:12",
					"end_time": "0.20:52",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "94"
				}
			]
		},
		{
			"vehicle_id": "82",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.06:11",
					"end_time": "0.06:31",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:31",
					"end_time": "0.06:46",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301993",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:48",
					"end_time": "0.07:50",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:10",
					"end_time": "0.08:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "CoTC",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302240",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.09:30",
					"end_time": "0.10:25",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.12:20",
					"end_time": "0.12:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.12:40",
					"end_time": "0.12:55",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "TeSC",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302264",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:42",
					"end_time": "0.13:46",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:34",
					"end_time": "0.14:35",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301815",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301416",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:23",
					"end_time": "0.16:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:12",
					"end_time": "0.17:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302149",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:59",
					"end_time": "0.18:01",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:08",
					"end_time": "0.18:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302123",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:00",
					"end_time": "0.19:04",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:14",
					"end_time": "0.19:15",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301833",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:26",
					"end_time": "0.20:28",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:58",
					"end_time": "0.21:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301939",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301405",
					"duty_id": "103"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:52",
					"end_time": "0.23:02",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "103"
				}
			]
		},
		{
			"vehicle_id": "83",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.06:13",
					"end_time": "0.06:33",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:33",
					"end_time": "0.06:48",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301719",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:21",
					"end_time": "0.09:06",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "VaLO",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:23",
					"end_time": "0.09:25",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302009",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:12",
					"end_time": "0.10:16",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:24",
					"end_time": "0.10:25",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301798",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:12",
					"end_time": "0.11:16",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "53"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:16",
					"end_time": "0.11:18",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302020",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:49",
					"end_time": "0.12:51",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:08",
					"end_time": "0.13:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302113",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:00",
					"end_time": "0.14:04",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:12",
					"end_time": "0.14:13",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302159",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "deadhead",
					"start_time": "0.14:56",
					"end_time": "0.14:58",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:08",
					"end_time": "0.15:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302117",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:01",
					"end_time": "0.16:05",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:59",
					"end_time": "0.17:00",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301825",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:33",
					"end_time": "0.18:35",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:58",
					"end_time": "0.19:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "26",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301930",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "27",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301403",
					"duty_id": "93"
				},
				{
					"vehicle_event_sequence": "28",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:52",
					"end_time": "0.21:02",
					"origin_stop_id": "PTC",
					"destination_stop_id": "Pomona",
					"duty_id": "93"
				}
			]
		},
		{
			"vehicle_id": "84",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.06:17",
					"end_time": "0.06:37",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:37",
					"end_time": "0.06:47",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301859",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:42",
					"end_time": "0.07:44",
					"origin_stop_id": "MTC",
					"destination_stop_id": "MTCLO",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.07:53",
					"end_time": "0.07:55",
					"origin_stop_id": "MTCLO",
					"destination_stop_id": "MTC",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301730",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:29",
					"end_time": "0.10:04",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "EMSLO",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:28",
					"end_time": "0.10:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302202",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.11:31",
					"end_time": "0.11:46",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "54"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:30",
					"end_time": "0.13:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.13:50",
					"end_time": "0.14:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301899",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301398",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:55",
					"end_time": "0.15:57",
					"origin_stop_id": "PTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:03",
					"end_time": "0.17:03",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301656",
					"duty_id": "135"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.18:22",
					"end_time": "0.18:52",
					"origin_stop_id": "SDPR",
					"destination_stop_id": "Pomona",
					"duty_id": "135"
				}
			]
		},
		{
			"vehicle_id": "85",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.06:30",
					"end_time": "0.06:50",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:50",
					"end_time": "0.07:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PTC",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301862",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:00",
					"end_time": "0.08:05",
					"origin_stop_id": "CTC",
					"destination_stop_id": "MTC",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301732",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:38",
					"end_time": "0.09:40",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:58",
					"end_time": "0.10:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302200",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.11:01",
					"end_time": "0.11:16",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "55"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.13:59",
					"end_time": "0.14:19",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:19",
					"end_time": "0.15:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302260",
					"sub_trip_index": "1",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302260",
					"sub_trip_index": "2",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:46",
					"end_time": "0.17:01",
					"origin_stop_id": "GrPR",
					"destination_stop_id": "TeSC",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302036",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:08",
					"end_time": "0.18:10",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:15",
					"end_time": "0.18:17",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301605",
					"duty_id": "48"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:23",
					"end_time": "0.19:38",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "48"
				}
			]
		},
		{
			"vehicle_id": "86",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.06:31",
					"end_time": "0.06:51",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:51",
					"end_time": "0.07:06",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301723",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.08:40",
					"end_time": "0.09:35",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "Pomona",
					"duty_id": "56"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:33",
					"end_time": "0.14:53",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:53",
					"end_time": "0.16:04",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Fi9t",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301638",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:35",
					"end_time": "0.18:35",
					"origin_stop_id": "SDPR",
					"destination_stop_id": "Fi9t",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301675",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:01",
					"end_time": "0.20:18",
					"origin_stop_id": "MTC",
					"destination_stop_id": "PTCLO",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:58",
					"end_time": "0.21:00",
					"origin_stop_id": "PTCLO",
					"destination_stop_id": "PTC",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301940",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:05",
					"end_time": "0.22:09",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:19",
					"end_time": "0.22:20",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302139",
					"duty_id": "26"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:58",
					"end_time": "0.23:50",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "26"
				}
			]
		},
		{
			"vehicle_id": "87",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.06:32",
					"end_time": "0.06:52",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.06:52",
					"end_time": "0.07:07",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301722",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:39",
					"end_time": "0.08:41",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:58",
					"end_time": "0.09:00",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301564",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.10:01",
					"end_time": "0.10:16",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "Pomona",
					"duty_id": "57"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:35",
					"end_time": "0.14:55",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:55",
					"end_time": "0.15:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CiGL",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301449",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:55",
					"end_time": "0.16:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:08",
					"end_time": "0.17:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302121",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:02",
					"end_time": "0.18:06",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:13",
					"end_time": "0.18:14",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "PHM",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302158",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "deadhead",
					"start_time": "0.18:58",
					"end_time": "0.19:00",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.19:08",
					"end_time": "0.19:10",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301610",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:12",
					"end_time": "0.20:16",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:53",
					"end_time": "0.20:55",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "TeSC",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302049",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "deadhead",
					"start_time": "0.21:55",
					"end_time": "0.21:57",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "deadhead",
					"start_time": "0.22:03",
					"end_time": "0.22:05",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "24",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302130",
					"duty_id": "16"
				},
				{
					"vehicle_event_sequence": "25",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:46",
					"end_time": "0.23:26",
					"origin_stop_id": "PHM",
					"destination_stop_id": "Pomona",
					"duty_id": "16"
				}
			]
		},
		{
			"vehicle_id": "88",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.07:05",
					"end_time": "0.07:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.07:25",
					"end_time": "0.07:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "CTC",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302186",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.08:16",
					"end_time": "0.08:25",
					"origin_stop_id": "MoHa",
					"destination_stop_id": "MTC",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301735",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:58",
					"end_time": "0.10:00",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.10:28",
					"end_time": "0.10:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301569",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.11:54",
					"end_time": "0.12:34",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "Pomona",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.14:35",
					"end_time": "0.14:55",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "20"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.14:55",
					"end_time": "0.15:35",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "PHM",
					"duty_id": "20"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301819",
					"duty_id": "20"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301417",
					"duty_id": "20"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:23",
					"end_time": "0.17:27",
					"origin_stop_id": "PHM",
					"destination_stop_id": "PHMLO",
					"duty_id": "20"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:53",
					"end_time": "0.18:30",
					"origin_stop_id": "PHMLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "20"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302259",
					"sub_trip_index": "1",
					"duty_id": "20"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302259",
					"sub_trip_index": "2",
					"duty_id": "20"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "deadhead",
					"start_time": "0.20:18",
					"end_time": "0.20:40",
					"origin_stop_id": "GrPR",
					"destination_stop_id": "MTC",
					"duty_id": "20"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301775",
					"duty_id": "20"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:06",
					"end_time": "0.22:58",
					"origin_stop_id": "EMS",
					"destination_stop_id": "Pomona",
					"duty_id": "20"
				}
			]
		},
		{
			"vehicle_id": "89",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.07:47",
					"end_time": "0.08:07",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.08:07",
					"end_time": "0.08:22",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "MTC",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301734",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "deadhead",
					"start_time": "0.09:55",
					"end_time": "0.10:30",
					"origin_stop_id": "9thHo",
					"destination_stop_id": "EMSLO",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "deadhead",
					"start_time": "0.11:28",
					"end_time": "0.11:30",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301572",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "deadhead",
					"start_time": "0.12:55",
					"end_time": "0.13:01",
					"origin_stop_id": "CiGL",
					"destination_stop_id": "CiCLO",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "deadhead",
					"start_time": "0.13:52",
					"end_time": "0.14:00",
					"origin_stop_id": "CiCLO",
					"destination_stop_id": "CiGL",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301446",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:25",
					"end_time": "0.15:27",
					"origin_stop_id": "EMS",
					"destination_stop_id": "EMSLO",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "deadhead",
					"start_time": "0.15:43",
					"end_time": "0.15:45",
					"origin_stop_id": "EMSLO",
					"destination_stop_id": "EMS",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302223",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "deadhead",
					"start_time": "0.16:53",
					"end_time": "0.16:57",
					"origin_stop_id": "TeSC",
					"destination_stop_id": "VaLO",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "deadhead",
					"start_time": "0.17:14",
					"end_time": "0.18:00",
					"origin_stop_id": "VaLO",
					"destination_stop_id": "Fi9t",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302235",
					"sub_trip_index": "1",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302235",
					"sub_trip_index": "2",
					"duty_id": "34"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:09",
					"end_time": "0.19:39",
					"origin_stop_id": "GrPR",
					"destination_stop_id": "Pomona",
					"duty_id": "34"
				}
			]
		},
		{
			"vehicle_id": "90002",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:20",
					"end_time": "0.03:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "111"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.03:40",
					"end_time": "0.04:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "DuDs",
					"duty_id": "111"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301471",
					"duty_id": "111"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302056",
					"duty_id": "111"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301476",
					"duty_id": "111"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302231",
					"duty_id": "111"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301482",
					"duty_id": "111"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "attendance",
					"start_time": "0.08:44",
					"end_time": "0.09:00",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302063",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301488",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302069",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301495",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "attendance",
					"start_time": "0.12:53",
					"end_time": "0.13:08",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302077",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301503",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302083",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301511",
					"duty_id": "114"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "attendance",
					"start_time": "0.17:09",
					"end_time": "0.17:24",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302088",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301519",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302096",
					"duty_id": "58"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:24",
					"end_time": "0.20:44",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "Pomona",
					"duty_id": "58"
				}
			]
		},
		{
			"vehicle_id": "90003",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:25",
					"end_time": "0.03:45",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.03:45",
					"end_time": "0.04:00",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302054",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301473",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302227",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301479",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "attendance",
					"start_time": "0.07:43",
					"end_time": "0.08:00",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302182",
					"duty_id": "59"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301485",
					"duty_id": "59"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302066",
					"duty_id": "59"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301491",
					"duty_id": "59"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "attendance",
					"start_time": "0.11:47",
					"end_time": "0.12:04",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "111"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302073",
					"duty_id": "111"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301499",
					"duty_id": "111"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "attendance",
					"start_time": "0.14:00",
					"end_time": "0.14:12",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302081",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301507",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "attendance",
					"start_time": "0.16:08",
					"end_time": "0.16:20",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302085",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301515",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302092",
					"duty_id": "50"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:14",
					"end_time": "0.19:34",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "Pomona",
					"duty_id": "50"
				}
			]
		},
		{
			"vehicle_id": "90008",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:50",
					"end_time": "0.04:10",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:10",
					"end_time": "0.04:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "DuDs",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301472",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302057",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301477",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302187",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301483",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "attendance",
					"start_time": "0.09:04",
					"end_time": "0.09:20",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302064",
					"duty_id": "142"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301489",
					"duty_id": "142"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302071",
					"duty_id": "142"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301497",
					"duty_id": "142"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "attendance",
					"start_time": "0.13:26",
					"end_time": "0.13:40",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "142"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302079",
					"duty_id": "122"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301505",
					"duty_id": "122"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302084",
					"duty_id": "122"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301513",
					"duty_id": "122"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "attendance",
					"start_time": "0.17:41",
					"end_time": "0.17:56",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302090",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301521",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302097",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301526",
					"duty_id": "140"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.21:44",
					"end_time": "0.21:59",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona",
					"duty_id": "140"
				}
			]
		},
		{
			"vehicle_id": "90010",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.03:55",
					"end_time": "0.04:15",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.04:15",
					"end_time": "0.04:30",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302055",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301474",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302226",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301480",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302061",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "attendance",
					"start_time": "0.09:08",
					"end_time": "0.09:20",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "DuDs",
					"duty_id": "116"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301486",
					"duty_id": "141"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302067",
					"duty_id": "141"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301493",
					"duty_id": "141"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "attendance",
					"start_time": "0.12:19",
					"end_time": "0.12:36",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "141"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302075",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301501",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302082",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301509",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302086",
					"duty_id": "126"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "attendance",
					"start_time": "0.17:42",
					"end_time": "0.17:56",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "DuDs",
					"duty_id": "63"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301517",
					"duty_id": "63"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302094",
					"duty_id": "63"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301524",
					"duty_id": "63"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302099",
					"duty_id": "63"
				},
				{
					"vehicle_event_sequence": "22",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301528",
					"duty_id": "63"
				},
				{
					"vehicle_event_sequence": "23",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:44",
					"end_time": "0.22:59",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona",
					"duty_id": "63"
				}
			]
		},
		{
			"vehicle_id": "90052",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:00",
					"end_time": "0.05:20",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:20",
					"end_time": "0.05:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "DuDs",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301475",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302059",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301481",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302062",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301487",
					"duty_id": "127"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "attendance",
					"start_time": "0.10:27",
					"end_time": "0.10:40",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302068",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301494",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302076",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "attendance",
					"start_time": "0.13:43",
					"end_time": "0.13:56",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "DuDs",
					"duty_id": "115"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301502",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302228",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301510",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "attendance",
					"start_time": "0.16:54",
					"end_time": "0.17:08",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "113"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302087",
					"duty_id": "141"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301518",
					"duty_id": "141"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302095",
					"duty_id": "141"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301525",
					"duty_id": "141"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302100",
					"duty_id": "141"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:12",
					"end_time": "0.22:32",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "Pomona",
					"duty_id": "141"
				}
			]
		},
		{
			"vehicle_id": "90057",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.05:05",
					"end_time": "0.05:25",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.05:25",
					"end_time": "0.05:40",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302058",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301478",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302060",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301484",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302065",
					"duty_id": "131"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "attendance",
					"start_time": "0.10:31",
					"end_time": "0.10:40",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "DuDs",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301490",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302072",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301498",
					"duty_id": "112"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "attendance",
					"start_time": "0.13:43",
					"end_time": "0.13:56",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302080",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "13",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301506",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "14",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302183",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "15",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301514",
					"duty_id": "124"
				},
				{
					"vehicle_event_sequence": "16",
					"vehicle_event_type": "attendance",
					"start_time": "0.17:56",
					"end_time": "0.18:12",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "142"
				},
				{
					"vehicle_event_sequence": "17",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302091",
					"duty_id": "142"
				},
				{
					"vehicle_event_sequence": "18",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301522",
					"duty_id": "142"
				},
				{
					"vehicle_event_sequence": "19",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302098",
					"duty_id": "142"
				},
				{
					"vehicle_event_sequence": "20",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301527",
					"duty_id": "142"
				},
				{
					"vehicle_event_sequence": "21",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.22:14",
					"end_time": "0.22:29",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona",
					"duty_id": "142"
				}
			]
		},
		{
			"vehicle_id": "90111",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.10:36",
					"end_time": "0.10:56",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.10:56",
					"end_time": "0.11:16",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "DuDs",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301492",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302074",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301500",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302229",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "attendance",
					"start_time": "0.15:18",
					"end_time": "0.15:32",
					"origin_stop_id": "DuDs",
					"destination_stop_id": "DuDs",
					"duty_id": "117"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301508",
					"duty_id": "59"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302184",
					"duty_id": "59"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301516",
					"duty_id": "59"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302093",
					"duty_id": "59"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301523",
					"duty_id": "59"
				},
				{
					"vehicle_event_sequence": "12",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.20:27",
					"end_time": "0.20:42",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona",
					"duty_id": "59"
				}
			]
		},
		{
			"vehicle_id": "90115",
			"vehicle_events": [
				{
					"vehicle_event_sequence": "0",
					"vehicle_event_type": "pre_trip",
					"start_time": "0.10:41",
					"end_time": "0.11:01",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "Pomona",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "1",
					"vehicle_event_type": "depot_pull_out",
					"start_time": "0.11:01",
					"end_time": "0.11:16",
					"origin_stop_id": "Pomona",
					"destination_stop_id": "ToMa",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "2",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302070",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "3",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301496",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "4",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302078",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "5",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301504",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "6",
					"vehicle_event_type": "attendance",
					"start_time": "0.15:20",
					"end_time": "0.15:32",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "ToMa",
					"duty_id": "119"
				},
				{
					"vehicle_event_sequence": "7",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302230",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "8",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301512",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "9",
					"vehicle_event_type": "service_trip",
					"trip_id": "5302089",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "10",
					"vehicle_event_type": "service_trip",
					"trip_id": "5301520",
					"duty_id": "51"
				},
				{
					"vehicle_event_sequence": "11",
					"vehicle_event_type": "depot_pull_in",
					"start_time": "0.19:32",
					"end_time": "0.19:47",
					"origin_stop_id": "ToMa",
					"destination_stop_id": "Pomona",
					"duty_id": "51"
				}
			]
		}
	]

    return [Vehicle(**vehicle) for vehicle in vehicles]