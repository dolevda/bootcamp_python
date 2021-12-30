from datetime import date


def calc_days(date1, date2):
    if date1 > date2:
        print(date1 - date2)
    else:
        print(date2 - date1)


calc_days(date(2021, 12, 2), date(2021, 12, 28))
