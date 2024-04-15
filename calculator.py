######### Basic Calculator ##########
def add(a,b):
    answer=a+b
    print(str(a) + "+" +str(b)+"="+str(answer))
def sub(a,b):
    answer=a-b
    print(str(a) + "-" + str(b) + "="+ str(answer))
def divide(a,b):
    answer=a/b
    print(str(a)+ "/" + str(b)+"="+str(answer))
def mul(a,b):
    answer=a*b
    print(str(a)+ "*" + str(b)+"="+str(answer))
while True:
    print("A.addition")
    print("B.Subtraction")
    print("C.Division")
    print("D.Multiplication")
    print("E.Exit")
    choice=input("Enter your choice: ")
    if choice=="a" or choice=="A":
        print("Addition")
        a=int(input("Enter 1st no: "))
        b=int(input("Enter 2nd no: "))
        add(a,b)
    elif choice=="b" or choice=="B":
        print("Subtraction")
        a=int(input("Enter 1st no: "))
        b=int(input("Enter 2nd no: "))
        sub(a,b)  
    elif choice=="c" or choice=="C":
        print("Division")
        a=int(input("Enter 1st no: "))
        b=int(input("Enter 2nd no: "))
        divide(a,b)
    elif choice=="d" or choice=="D":
        print("Multiplication")
        a=int(input("Enter 1st no: "))
        b=int(input("Enter 2nd no: "))
        mul(a,b)
    elif choice=="e" or choice=="E":
        print("Program ended ")
        quit()
        

    
     

    


