# creation of the class;


""" model and weight are the properties/attributes of an object """
""" self is the current object to be created """
""" __init__ is a function that is also the constructor --> initializer """


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("{} is {} years old and is a {}". format(self.name, self.age, self.gender))

class Car:
    def __init__(self, model, weight):
        self.model = model
        self.weight = weight


class Greeting:
    message = "Hello, World!"

    def say_hello(self):
        print(self.message)

class Employee:
    def  __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_details(self):
        print("Employee name - {}\n" "Employee position - {}\n" "Employee Salary - {}".format(self.name, self.position, self.salary))

    # Instance function to give raise to employee;

    def give_raise(self, amount):
        self.salary += amount
        print("New Salary - {}".format(self.salary))

    # Instance function to change position of employee;

    def change_position(self, new_position):
        self.position = new_position
        print("New Position - {}".format(self.position))

# @classmethod

class Student:
    counter = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.counter += 1

    def msg(self):
        print("Hello "+ self.name + " you got", self.marks, "% marks")

    @classmethod
    def object_count(cls):
        return cls.counter

# staticmethod

class MathOperations:

    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def subtract_numbers(a , b):
        return a - b


# Constructor over-flow

class Constructor:
    def __init__(self):
        print("Constructor - 1")
    #def __init__(self):
        # print("Constructor - 2")

class BankAccount:
    totalAccounts = 0
    next_account_number = 1001

    def __init__(self, name, balance, account_type):
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

        self.name = name
        self.balance = balance
        self.account_type = account_type

        BankAccount.totalAccounts += 1

    def display_details(self):
        print(f"Account number : {self.account_number} || Name : {self.name} || Balance : ₹{self.balance} || Account type : {self.account_type}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Amount = ₹{amount}, New Balance = ₹{self.balance}")
        else:
            print("Deposit cannot be negative!!!")

        print(f"Deposited Amount = ₹{amount}, New Balance = ₹{self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            print(f"Remaining Amount = ₹{self.balance}")
        else:
            print("Not Sufficient Funds")

    @classmethod
    def get_total_accounts(cls):
        print(f"Total active accounts: {cls.totalAccounts}")

# object for the class;
'''
honda = Car('CRV', 1200)
mazda = Car('XL7', 1000)

print(honda.__dict__)
print(mazda.__dict__)

greet = Greeting()
greet.say_hello()

Person1 = Person("Pratham", 19, "Male")
Person1.show_details()

emp1 = Employee("Raghav", "Manager", 45000)
emp1.display_details()
emp1.change_position("AGM") # instance_function
print()
emp1.display_details()
print()
emp2 = Employee("Ritik", "Sr-Manager", 65000)
emp2.display_details()
emp2.give_raise(5000) # instance_function
print()
emp2.display_details()
print()

student_1=  Student("Ritik", 98)
print(student_1.object_count())
student_2 = Student("Raghav", 99)
print(Student.object_count())
print(student_2.object_count())
student_1.msg()
student_2.msg()


obj = MathOperations()
result_add = MathOperations.add_numbers(10, 5) # called by class
result_subtract = obj.subtract_numbers(10, 5)   # called by obj

print("Addition:", result_add)
print("Subtraction:", result_subtract)

'''


'''


# attributions for the object Car();

honda.model = 'CRV'
honda.weight = 1200

mazda.model = 'RX7'
mazda.weight = 900

# printing of the attributes;

print("For Honda: ", honda.model, honda.weight)
print("For Mazda: ", mazda.model, mazda.weight)
print(honda.__dict__)
print(mazda.__dict__)

'''