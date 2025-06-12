def cap(a):
    return a.capitalize()

def low(a):
    return a.lower()

def up(a):
    return a.upper()

def ti(a):
    return a.title()

def sw(a):
    return a.swapcase()

ch = 'Y'
while(ch == 'Y'):
    st = input("Enter the string: ")
    print("\nEnter 1 for UPPER")
    print("Enter 2 for LOWER")
    print("Enter 3 for SWAP")
    print("Enter 4 for TITLE")
    print("Enter 5 for CAPITALIZE")
    choice = int(input("\nEnter your choice : "))
    print("String after choice is: \n")
    
    if (choice == 1):
        ans = up(st)
        print(ans)
    elif (choice == 2):
        ans = low(st)
        print(ans)
    elif (choice == 3):
        ans = sw(st)
        print(ans)
    elif (choice == 4):
        ans = ti(st)
        print(ans)
    elif (choice == 5):
        ans = cap(st)
        print(ans)
    else:
        print("INVALID CHOICE")

    ch = input("\nContinue? Enter 'Y' for yes or 'N' for no : ")
