import random
import datetime

between_delta = 5
start_date = datetime.datetime(2023, 6, 1)
end_date = datetime.datetime(2023, 12, 31)


def random_dates(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    current_addon_date = 0
    while current_addon_date < days_between_dates:
        current_addon_date += random.randrange(between_delta) + 1
        random_date = start_date + datetime.timedelta(days=current_addon_date)
        random_time = random_date.replace(hour=random.randint(10, 23), minute=random.randint(0, 59), second=random.randint(0, 59))
        random_str = random_time.strftime("%a %b %d %H:%M:%S %Y")
        print(f"{random_str}")


random_dates(start_date, end_date)