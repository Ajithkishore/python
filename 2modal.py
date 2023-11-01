def is_leap_year(year):
    if(year%4==0 and year%100!=0)or(year%400==0):
        return True
    else:
        return False
def fin_anniversary(year):
    if is_leap_year(year):
        print(year,"is a leap year.next anniversary:",year+4)
    else:
        print(year,"is not aleap year.next anniversary:",year-1)
anniversary_year=int(input("enter the anniversary year:"))
fin_anniversary(anniversary_year)
