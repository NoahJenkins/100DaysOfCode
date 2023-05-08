#This will be a more streamlined version of BMI 2.0
#This will use the elif statement.


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI= float(weight) / float(height) ** 2

print("Your BMI is " + str(int(BMI)) + ".")

if BMI < 18.5:
    print("You are underweight.")
elif BMI < 25:
    print("You have normal weight.")
elif BMI < 30:
    print("You are slightly overwieght.")
elif BMI < 35:
    print("You are obese")

else:
    print("You are clinically obese.")

#