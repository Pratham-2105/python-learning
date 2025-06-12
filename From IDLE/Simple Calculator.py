a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
choice  = int(input("Enter 1 to add and 2 to subtract 3 to multiply and 4 to divide : "))

if(choice == 1):
    print("The sum of two numbers is : ", a + b)

elif(choice == 2):
    print("The differece of two numbers is : ", a - b)

elif(choice == 3):
    print("The product of two numbers is : ", a * b)

elif(choice == 4):
    print("The division of the two numbers is : ", a / b)

else:
    print("Invalid input")
    
