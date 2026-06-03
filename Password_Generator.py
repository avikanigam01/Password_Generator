name= input("Enter name on which you want to generate password: ")
try:
    length= int(input("Enter length of password: "))
    import random
    slen= len(name)
    if length < len(name):
        print("Password length should be at least: ", len(name))
    else:
        l= list(name)
        password = ""
        symbols = "!@#$%"
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
except ValueError:
    print("Input should be a number")
