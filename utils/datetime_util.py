import re


def check_datetime_format(datetime_str: str) -> bool:
    pattern = r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}'
    if re.match(pattern, datetime_str):
        return True
    else:
        return False
