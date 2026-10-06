num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

max = num1
if num1 > num2 and num1 > num3:
    max = num1
elif num2 > num1 & num2 > num3:
    max = num2
else:
    max = num3
print(max)
