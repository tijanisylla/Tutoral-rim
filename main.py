# Select an option
print("=============== Select option ===============")

print("1. ADD (+)")
print("2. SUBTRACT (-)")
print("3. MULTIPLY (x)")
print("4. DIVIDE (/)")


def calculatoor():
    operation  = input()
    
    if operation == str(1): # Opt 1
        num1 = input("Enter the first number : ")
        num2 = input("Enter the second number : ")
        print("The result is : " + str(int(num1) + int(num2))) # Contactinating 20 + 20 = 40 ? 2020
        
    elif operation == str(2): # Opt 2
         num1 = input("Enter the first number : ")
         num2 = input("Enter the second number : ")
         print("The result is : " +  str(int(num1) - int(num2)))
         
    elif operation == str(3): # Opt 3
         num1 = input("Enter the first number : ")
         num2 = input("Enter the second number : ")
         print("The result is : " + str(int(num1) * int(num2)))
         
    elif operation == str(4): # Opt 4
         num1 = input("Enter the first number : ")
         num2 = input("Enter the second number : ")
         print("The result is : " + str(int(num1) / int(num2)))
    else:
        print("Invalid Entry")

if __name__ == "__main__":
    calculatoor()
else:
    print("Its not equal to main")

        
        
        
        
    
    