num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: ")) 
if num1 > num2 and num1 > num3:
    print("The first number is the greatest.")      
elif num2 > num1 and num2 > num3:
    print("The second number is the greatest.")
elif num3 > num1 and num3 > num2:
    print("The third number is the greatest.")
elif num1 == num2 and num1 == num3:
    print("All three numbers are equal.")   
elif num1 == num2:
    print("The first and second numbers are equal and greater than the third number.")  
elif num1 == num3:
    print("The first and third numbers are equal and greater than the second number.")
elif num2 == num3:
    print("The second and third numbers are equal and greater than the first number.")
else:
    print("There is no single greatest number among the three.")