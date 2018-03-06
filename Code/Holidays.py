import pandas as pd

def getHolidayDates(filepath):

    HolidaysFile = open(filepath)
    lines = HolidaysFile.readlines()
    lines = [line.split(" ")[:3] for line in lines]
    lines = ["{} {} {}".format(line[0], line[1], line[2]) for line in lines]
    lines = pd.to_datetime(lines)
    return pd.DataFrame({"Date": lines})


def getHolidayNames(filepath):

    HolidaysNameFile = open(filepath)
    lines = HolidaysNameFile.readlines()
    lines = [line.strip().split(" ")[:4] for line in lines]
    lines_dt = ["{} {} {}".format(line[0], line[1], line[2]) for line in lines]
    lines_dt = pd.to_datetime(lines_dt)
    lines_hol = [line[3] for line in lines]
    return pd.DataFrame({"Date": lines_dt, "Holiday Name": lines_hol})

holidays = getHolidayDates('holidays.txt')
print (holidays)

holiday_names = getHolidayNames('holiday_names.txt')
print (holiday_names)
