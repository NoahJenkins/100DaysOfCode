#This is how you work out whether if a particular year is a leap year.
#on every year that is evenly divisible by 4 
#**except** every year that is evenly divisible by 100 
#**unless** the year is also evenly divisible by 400
#e.g. The year 2000:
#2000 ÷ 4 = 500 (Leap)
#2000 ÷ 100 = 20 (Not Leap)
#2000 ÷ 400 = 5 (Leap!)
#So the year 2000 is a leap year.
#But the year 2100 is not a leap year because:
#2100 ÷ 4 = 525 (Leap)
#2100 ÷ 100 = 21 (Not Leap)
#2100 ÷ 400 = 5.25 (Not Leap)

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("A leap year.")
        else:
            print("Not a leap year.")
    else:
        print("A leap year.")
else:
    print("Not a leap year.")
