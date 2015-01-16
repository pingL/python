# Introduction Program
# takes the user's name and uses it in conversation with a yes/no question

yourname=input("May I know your name?")
print("Hello ", yourname, "! I hope you are OK")
know=input("Do you want to know a bit about me? yes or no?")

if know=="yes":
    print("Hello, my name is Atharv, I like computers, playing Table tennis and Badminton and reading books. I have done a bit of python before and enjoy programming. I hope that we will have a good time together.")
elif know=="no":
     yourinfo=input("OK, tell me a bit about yourself!")
     print("Thats great")
else:
    print("Please start again and make sure you say either yes or no.")
