name= input("Enter name on which you want to generate password: ")
length= int(input("Enter length of password: "))
import string
slen= len(name)
if length < len(name):
    print("Password length should be at least: ", len(name))
else:
    l= list(name)
    password = ""
    symbols = "!@#$%"
    import random
    while slen>0:
        random.shuffle(l)
        a= random.choice(l)
        password+= a
        slen-=1
    while len(password)<length:
        chars = "0123456789@#$%^&*"
        s= random.choice(chars)
        password += s
    print("your password is: "+ password)
