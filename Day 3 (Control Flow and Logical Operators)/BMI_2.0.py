# This program calculates the BMI of a person and prints out a message based on the BMI.
# BMI = weight(kg) / height^2(m^2)


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI= float(weight) / float(height) ** 2

print("Your BMI is " + str(int(BMI)) + ".")

if BMI <= 18.5:
    print("You are underweight.")
if BMI >18.5:
    if BMI <= 25:
        print("You have normal weight.")
if BMI > 25:
    if BMI <= 30:
        print("You are slightly overwieght.")
if BMI > 30:
    if BMI <= 35:
        print("You are obese")
if BMI > 35:
    print("You are clinically obese.")

#what is the elif statement?
#the elif statement is short for else if
#the elif statement is used when you have more than 2 conditions
#