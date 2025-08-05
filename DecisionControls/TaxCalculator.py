# if income is less than 200000, nill tax
# if income is between 200001 and 500000, tax is 10% of income
# if income is between 500001 and 1500000, tax is 15% of income
# if income is BEWEEN 1500001 and 2500000, tax is 20% of income
# if income is above 2500001, tax is 30% of income

income=int(input("Enter your income: "))

def calculate_tax(income):
    taxable_income = income-200000  # Exclude the first 200000 from tax calculation
    if taxable_income <= 0:
        return 0
    elif income <= 200000:
        return 0
    elif 200001 <= taxable_income <= 500000:
        return taxable_income * 0.10
    elif 500001 <= taxable_income <= 1500000:
        return taxable_income * 0.15
    elif 1500001 <= taxable_income <= 2500000:
        return taxable_income * 0.20
    else:  # income > 2500000
        return taxable_income * 0.30    
    
tax = calculate_tax(income)
print(f"The tax on an income of {income} is: {tax}")    