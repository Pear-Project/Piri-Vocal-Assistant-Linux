from datetime import date
from datetime import datetime

getmonth = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

getday = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"
}

getsuffix = {
    0 : "th",
    1 : "st",
    2 : "nd",
    3 : "rd",
    4 : "th",
    5 : "th",
    6 : "th",
    7 : "th",
    8 : "th",
    9 : "th",
    12: "th"
}

TimeArr = {
    13 : 1,
    14 : 2,
    15 : 3,
    16 : 4,
    17 : 5,
    18 : 6,
    19 : 7,
    20 : 8,
    21 : 9,
    22 : 10,
    23 : 11,
    24 : 12,
    00 : 12.
}


def assignSuffix(num):
    x = str(num)
    lastint = x[len(x) - 1]
    return getsuffix.get(int(lastint), "")




def getDate():
    month = getmonth.get(datetime.now().month, "")
    day = str(datetime.now().day)
    suffix = lambda b : "th" if b == 12 else assignSuffix(int(day))
    year = datetime.now().year
    return f"{month} {day}{suffix(int(day))} {year}"

def getTime():
    hr = convHour(datetime.now().hour)
    mn = datetime.now().minute
    pref = lambda : str(f"0{mn}") if mn < 10 else str(mn) 
    suffix = lambda : "PM" if int(datetime.now().hour) > 12 else "AM"

    return str(f"{hr} : {pref()} {suffix()}")

def convHour(integer):
    if integer <= 12:
        return integer
    else:
        return TimeArr.get(integer, "")


