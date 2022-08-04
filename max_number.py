# find the maximum value of three number:

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
num3 = int(input("What is the third number? "))

if (num1 > num2) and (num1 > num3):
    maximum = num1
elif (num2 > num1) and (num2 > num3):
    maximum = num2
else:
    maximum = num3

print("The maximum number is", maximum)