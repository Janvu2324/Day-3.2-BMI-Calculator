# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight / (height ** 2)

BMI1=str(round(BMI))
print("You BMI is "+ BMI1 + ",")


if BMI < 18:
  print("you are underweight.")
elif BMI < 22:
  print("you have a normal weight.")
elif BMI < 28:
  print("you are slightly overweight.")
elif BMI < 33:
  print("you are obese.")
else:
  print("you are clinically obese.")




