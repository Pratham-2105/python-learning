# per >= 90 : A, 90 > per >= 80 : B, per >= 70 : C

a = int(input("Enter the marks of first subject : "))
b = int(input("Enter the marks of second subject : "))
c = int(input("Enter the marks of third subject : "))

total = a + b + c
totalout = print("The total marks of the subjects are : ", total)

percentage = (total / 300) * 100
print("Your percentage is : ", percentage)

if(percentage >= 90):
    print("Grade : A")

elif(90 > percentage >= 80):
    print("Grade : B")

elif(80 > percentage >= 70):
    print("Grade : C")

else:
    print("Invalid")
