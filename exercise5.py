
def getdate():
    import datetime
    return datetime.datetime.now()

def Take(k):
    if(k==1):
        c=int(input("Enter 1  for Exercise and Enter 2 for food" ))
        if (c==1):
            value =input("Enter Here\n")
            with open("harry-Exercise.txt","a") as f:
                f.write(str([str(getdate())])+":"+value+"\n")
            print( " Successfully written")
        elif(c==2):
            value=input("Enter Here\n")
            with open("harry-food.txt","a") as f:
                f.write(str([str(getdate())])+":"+value+"\n")
            print("Succesfully Written")
    elif(k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("Enter here\n")
            with open("rohan-exercise.txt", "a") as f:
                f.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("Enter here\n")
            with open("rohan-food.txt", "a") as f:
                f.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("Enter here\n")
            with open("hammad-exercise.txt", "a") as f:
                f.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as f:
                f.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("harry-exercise.txt") as f:
                for i in f:
                    print(i, end="")
        elif (c == 2):
            with open("harry-food.txt") as f:
                for i in f:
                    print(i, end="")
        elif (k == 2):
            c = int(input("enter 1 for excersise and 2 for food"))
            if (c == 1):
                with open("rohan-exercise.txt") as f:
                    for i in f:
                        print(i, end="")
            elif (c == 2):
                with open("rohan-food.txt") as f:
                    for i in f:
                        print(i, end="")
        elif (k == 3):
            c = int(input("enter 1 for excersise and 2 for food"))
            if (c == 1):
                with open("hammad-exercise.txt") as f:
                    for i in f:
                        print(i, end="")
            elif (c == 2):
                with open("hammad-food.txt") as f:
                    for i in f:
                        print(i, end="")
        else:
            print("plz enter valid input (harry,rohan,hammad)")

print("HEALTH MANAGEMENT SYSYTEM")
a = int(input("press 1 for lock the value and 2 for retrieve "))
if a==1:
    b= int(input("Press 1 for HARRY,2 for ROHAN, 3 for HAMMAD"))
    Take(b)
else:
    b=int(input("Press 1 for HARRY,2 for ROHAN, 3 for HAMMAD"))
    retrieve(b)