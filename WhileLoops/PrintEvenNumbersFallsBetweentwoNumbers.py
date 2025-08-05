firstNumber=int(input("Enter the First number: "))
secondNumber=int(input("Enter the Second number: "))


i=0
if firstNumber>secondNumber:
    while(firstNumber>secondNumber):
        if(secondNumber%2==0):
            print(secondNumber)
        secondNumber+=1
else:
    while(firstNumber<secondNumber):
        if(firstNumber%2==0):
            print(firstNumber)
        firstNumber+=1
