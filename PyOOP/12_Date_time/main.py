import datetime

def main():
    # we need to create a date object
    # the date() method allows us to create a date object of a given year, month and day
    date = datetime.date(year=2025, month=1, day=1)
    # to get today's date, we use the date.today() method
    today = datetime.date.today()
    print(date)
    print(today)

    # for time objects, we'll use the time method, passing hours, minutes and seconds
    time_ = datetime.time(hour=23, minute=59, second=59)
    print(time_)

    # to get the current time, we use the datetime.now method:
    now = datetime.datetime.now()

    # we can format the appearance of the time string:
    now = now.strftime("%H:%M:%S")
    print(now)

    # we can also format it to include the date:
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S %d/%m/%Y")
    print(now)

    # we can use < and > to confront datetime:
    target_date = datetime.datetime(year=2025, month=12, day=31, hour=23, minute=59, second=59)
    current_date = datetime.datetime.now()
    if target_date < current_date:
        print("Target date has already passed")
    else:
        print("Target date has not passed")

if __name__ == "__main__":
    main()