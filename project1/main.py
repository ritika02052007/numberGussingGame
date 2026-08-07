import random as rd
computer = rd.randint(1,101)
i = 1
while i <=10 :
    user = int(input("enter the number"))
    if (computer<user):
        if(i<10):
            print("Guess the lower number")
    elif(computer>user):
        if(i<10):
            print("guess the higher number")
    elif(computer == user):
        print("Congratulation ","You Won the Game","in",i,"attempt")
    
    i = i+1

if(i>10):
    print("Please Try Again ","you are out of attempt")

