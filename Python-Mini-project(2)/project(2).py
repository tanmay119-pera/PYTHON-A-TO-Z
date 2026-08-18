'''                                        RANDOM PASSWORD GENERATOR                                              '''

import random 
import string 

pass_len = 12
charValues = string.ascii_letters+string.digits+string.punctuation


'''list comprehension [function for i in range(n)]
res = [random.choice(charValues)for i in range (pass_len)]
print(res)'''

password = ""
for i in range(pass_len):
    password += (random.choice(charValues))

print("your random password is: ")