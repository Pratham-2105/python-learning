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

def subst(st, sub):  # Returns (-1) if Substring does not exist, and index of the Substring if it exists.
    y = st.find(sub)

    if (y == -1):
        print("NOT AVAILABLE")

    else:
        print("The Sub-String is available at : ", y + 1)
    return 0

def stcount(st, sub):
    return st.count(sub)

def rep(string,st, rp):
    return string.replace(st, rp)

def split(string, char): # This creates a list.
    return string.split(char)

ch = 'Y'
while(ch == 'Y' or ch == 'y'):

    st = input("Enter the string: ")
    sub = input("Enter the substring: ")
    char = input("Enter the letter to replace: ")
    re = input("Enter char for replacing: ")
    spl = input("Enter the char for splitting: ")
    
    print("\nEnter 1 for UPPER")
    print("Enter 2 for LOWER")
    print("Enter 3 for SWAP")
    print("Enter 4 for TITLE")
    print("Enter 5 for CAPITALIZE")
    print("Enter 6 for index of SubString")
    print("Enter 7 for count of SubString")
    print("Enter 8 for replacing a letter")
    print("Enter 9 to split the string")

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
    elif (choice == 6):
        ans = subst(st, sub)
        print(ans)
    elif (choice == 7):
        ans = stcount(st, sub)
        print(ans)
    elif (choice == 8):
        ans = rep(st, char, re)
        print(ans)
    elif (choice == 9):
        ans = split(st, spl)
        print(ans)
    else:
        print("INVALID CHOICE")

    ch = input("\nContinue? Enter 'Y' for yes or 'N' for no : ")
