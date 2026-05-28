import random
computer= random.choice([-1,0,1])
youstr=input("Enter your choice : ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youstr]

print(f"you chose {reverseDict[you]} and the computer chose {reverseDict[computer]}")



if(computer==you):
    print("Its a draw")
else:
    if(computer==-1 and you==1):
        print("you won")
    elif(computer==-1 and you==0):
        print("you lost")
    elif(computer==1 and you==-1):
        print("you lost")
    elif(computer==1 and you==0):
        print("you won")
    elif(computer==0 and you==1):
        print("you lost")
    elif(computer==0 and you==-1):
        print("you won")
    else:
        print("something went wrong in the input")
