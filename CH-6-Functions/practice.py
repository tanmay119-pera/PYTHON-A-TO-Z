# wap to print thr length of a list (list is the parameter)

cities = ["delhi","noida","gurgaon","pune","mumbai","chennai"]
heroes = ["thor","iron man","hulk","tanmay"]
def print_len(list):
    print(list)
    return(list)

print_len(cities)
print_len(heroes) 

'''===================================================================================================================================================='''

# waf to print the elements of a list in a single line. (list is the parameter)

cities = ["delhi","noida","gurgaon","pune","mumbai","chennai"]
heroes = ["thor","iron man","hulk","tanmay"]

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(heroes)
print_list(cities)

'''=========================================================================================================================================='''

# waf to find the factorial of n (n is the parameter)
n = 5

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
      fact *= i
    print(fact)

cal_fact(6)
cal_fact(7)

'''=============================================================================================================='''

# waf to convert usd to inr 

def converter(usd_value):
    inr_val = usd_value * 96
    print(usd_value,"USD=",inr_val,"INR")

converter(73)
converter(4567)
