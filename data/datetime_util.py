import datetime


def datetime_to_int(current_datetime: datetime) -> int:
    format_str = '%Y%m%d%H%M%S'
    date_str = current_datetime.strftime(format_str)
    date_int = int(date_str)
    return date_int

def int_to_datetime(current_datetime: int) -> datetime:
    date_str = str(current_datetime)
    format_str = '%Y%m%d%H%M%S'
    date_obj = datetime.datetime.strptime(date_str, format_str)
    return date_obj
