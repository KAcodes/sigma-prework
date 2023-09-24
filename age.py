from datetime import datetime


def date_calculator(given_date):
    date = datetime.strptime(given_date, "%Y-%m-%d")
    now = datetime.now()
    days = (now - date).days
    ans = int(days/365)
    return ans
