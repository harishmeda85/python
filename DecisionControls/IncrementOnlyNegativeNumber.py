x=int(input("Enter a number: "))
# If statement to check if a number is negative
if (x<0):
    print("The number is negative.")
    x = x + 1
    print("The incremented number is:", x)
elif x == 0:    
    print("The number is zero.")    
else:
    print("The number is not negative") 
    