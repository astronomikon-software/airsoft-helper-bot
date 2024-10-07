import datetime


def int_time_to_str(int_time: int) -> str:
    datetime_time = int_to_datetime(int_time)
    return datetime_to_str(datetime_time)


def str_time_to_int(str_time: str) -> int:
    datetime_time = str_to_datetime(str_time)
    return datetime_to_int(datetime_time)


def str_to_datetime(str_time: str) -> datetime:
    return datetime.datetime.strptime(str_time, '%d.%m.%Y')


def datetime_to_int(datetime_time: datetime) -> int:
    return int(round(datetime_time.timestamp()))

def int_to_datetime(int_time: int) -> datetime:
    return datetime.datetime.fromtimestamp(int_time)


def datetime_to_str(datetime_time: datetime) -> str:
    return datetime_time.strftime('%d.%m.%Y')
