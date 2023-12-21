from datetime import datetime, timedelta, date

today = datetime.now()

def get_offset():
    h = int(today.strftime("%H"))
    if h % 3 == 0:
        return 0
    elif h % 3 == 1:
        return 1
    else:
        return -1


def reference_day():
    return today + timedelta(days=get_offset())


def spelled_out_value(value):
    if value in value_map:
        return value_map[value]
    elif 20 < value < 30:
        return f"twenty {value_map[value - 20]}"
    elif 30 < value < 40:
        return f"thirty {value_map[value - 30]}"
    elif 40 < value < 50:
        return f"forty {value_map[value - 40]}"
    elif 50 < value < 60:
        return f"fifty {value_map[value - 50]}"
    else:
        return "Invalid value"


value_map = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
}

weekday = reference_day().strftime("%A").lower()
month = reference_day().strftime("%B").lower()
day = spelled_out_value(int(reference_day().strftime("%d")))
hour = spelled_out_value(int(reference_day().strftime("%H")))
minute = spelled_out_value(int(reference_day().strftime("%M")))
year = spelled_out_value(int(reference_day().strftime("%y")[-1]))
am_pm = reference_day().strftime("%p").lower()


def join_date_parts(*args):
    return ' '.join(map(str, args))


date_key = join_date_parts(weekday, month, day, year, am_pm)