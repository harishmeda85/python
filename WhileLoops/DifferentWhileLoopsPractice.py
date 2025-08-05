#First 10 even numbers

# i=2
# while(i<=20):
#     print(i)
#     i=i+2

# First 20 odd numbers

# i=1
# while(i<=40):
#     print(i)
#     i=i+2
# First 10 natural numbers

# i=1
# while(i<=10):
#     print(i)
#     i+=1
# First 10 whole numbers
# i=0
# while(i<=10):
#     print(i)
#     i+=1

start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))

# Ensure start is less than end
if start > end:
    start, end = end, start

print(f"Even numbers between {start} and {end} (exclusive):")

num = start + 1  # Start after the first number
while num < end:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1