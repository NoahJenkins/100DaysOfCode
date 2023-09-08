# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#BMI = weight(kg) / height^2(m^2)

BMI= float(weight) / float(height) ** 2

print("Your BMI is " + str(int(BMI)) + ".")

#Why did we use int(BMI) instead of str(BMI) or just BMI?
#Because we want to round the BMI to the nearest whole number.
#If we used str(BMI), it would have given us a decimal number.
#Why did BMI have to be a whole number?
#Because the output is supposed to be a whole number.

#BMI Calculator 2.0
