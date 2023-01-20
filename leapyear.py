def leapyear(year):  
    if year%4 == 0 and year%100 != 0:
        return ("It's leap year")
    elif year%400 == 0 and year%100 == 0:
        return ("It's leap year")
    else:
        return("It's not leap year")

print(leapyear(1600))