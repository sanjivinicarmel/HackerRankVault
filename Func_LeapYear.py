def is_leap(year):
    if(1900<year<100000):
        return (year%4==0) and (year %100!=0 or year %400==0)
    else:
        return False 