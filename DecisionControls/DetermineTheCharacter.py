char=input("Enter a character: ")
if char.isalpha():
    print("The character is an alphabet.")
    # Check if the character is uppercase or lowercase      
    if char.isupper():
        print("The character is an uppercase letter.")
    else:
        print("The character is a lowercase letter.")
elif char.isdigit():
    print("The character is a digit.")  
elif char.isspace():
    print("The character is a whitespace character.")