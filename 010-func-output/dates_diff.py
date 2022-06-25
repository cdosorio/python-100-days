from datetime import date
import datetime

def diff_dates(date1, date2):
    return abs(date2-date1).days

def main():
    d1 = date.today() #date(2013,1,1)
    d2 = date(2021,8,29)
    result1 = diff_dates(d2, d1)
    print (f"{result1} days between")
    print ("Happy programmer's day!")

main()