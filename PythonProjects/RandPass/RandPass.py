import random
import string

#Asking user to present preffered length of password
print("New Password Creator")
length = int(input("Enter the preffered length for the password: "))

#Using string module to create a mix of password requirements
low = string.ascii_lowercase
up = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all_req = low + up + num + symbols #adding everything to requirements
temp = random.sample(all_req, length) #Using random module to select truly random 
password = "".join(temp)
print(password)
#The .join is to connect the random chars, that would otherwise be printed as an array

