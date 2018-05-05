try:
    limit_n = int(input("enter limit:")) #50
    a_start = int(input("enter starting num:"))#25
    diff = int(input("enter common diff:"))#25
    sum = (limit_n / 2) * ((2 * a_start) + (limit_n - 1) * diff)
    print(sum)
except:
    print("Invalid entry")
