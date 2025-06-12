# Returns -1 if Substring does not exist, and index of the Substring if it exists.

def subst(st, sub): 
    y = st.find(sub)

    if (y == -1):
        print("NOT AVAILABLE")

    else:
        print("The Sub-String is available at : ", y + 1)
    return 0

def stcount(st, sub):
    return st.count(sub)
    

sd = input("Enter the string : ")
sbstring = input("Enter the substring : ")

ans = subst(sd, sbstring)
print("Count of Substring is: ", stcount(sd, sbstring))
