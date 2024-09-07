import datetime
import re

# to think

def datetime_to_int(current_datetime: datetime) -> int:
    format_str = '%d%m%Y%H%M%S' # here, here it is
    date_str = current_datetime.strftime(format_str)
    date_int = int(date_str)
    return date_int

def int_to_datetime(current_datetime: int) -> datetime:
    date_str = str(current_datetime)
    format_str = '%d%m%Y%H%M%S' # and here
    date_obj = datetime.datetime.strptime(date_str, format_str)
    return date_obj

def int_datetime_to_str(int_datetime: int) -> str:
    primary_str = str(int_datetime)
    secondary_str = primary_str[:2] + '-' + primary_str[2:4] + '-' + primary_str[4:8] + ' ' + primary_str[8:10] + ':' + primary_str[10:12] + ':' + primary_str[12:len(primary_str)]
    return secondary_str

def str_datetime_to_int(str_datetime: str) -> int:
    int_datetime = int(str_datetime[0:2] + str_datetime[3:5] + str_datetime[6:10] + str_datetime[11:13] + str_datetime[14:17] + '00')
    return int_datetime

def check_datetime_format(datetime_str: str) -> bool:
    pattern = r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}'
    if re.match(pattern, datetime_str):
        return True
    else:
        return False
