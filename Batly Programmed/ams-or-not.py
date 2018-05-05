try:
    x=int(input("enter a num"))
    if(x>50):
        print("enter less than 50")
    sum=0
    a=x
    while (a>0):
        dig=a%10
        sum+=dig**3
        a//=10
    if x==sum:
        print("yes")
    else:
        print("no")
except:
    print("Invalid input")
