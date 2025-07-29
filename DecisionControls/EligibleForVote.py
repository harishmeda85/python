Age= int(input("Enter your age: "))
# If statement to check if the age is eligible for voting   
if Age >= 18:
  print("You are eligible to vote.")
elif (Age < 18):
    yearsToEligible=18-Age
    print("You are not eligible to vote.", "You need", yearsToEligible, "more years to be eligible.")