class TimeDesk():
    def __init__(self, second):
        self.second = second


def seconds_to_dhms(time):
    seconds_to_minute = 60
    seconds_to_hour = 60 * seconds_to_minute
    seconds_to_day = 24 * seconds_to_hour
    days = time // seconds_to_day
    time %= seconds_to_day
    hours = time // seconds_to_hour
    time %= seconds_to_hour
    minutes = time // seconds_to_minute
    time %= seconds_to_minute
    seconds = time
    print("%d days, %d hours, %d minutes, %d seconds" % (days, hours, minutes, seconds))


time = int(input("Enter the number of seconds: "))
seconds_to_dhms(time)