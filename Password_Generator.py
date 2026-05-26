name= input("Enter name on which you want to generate password: ")
length= int(input("Enter length of password: "))
l= list(name)
password = ""
import random
while length>0:
    random.shuffle(l)
    a= random.choice(l)
    password+= a
    length-=1
print("your password is: "+ password)