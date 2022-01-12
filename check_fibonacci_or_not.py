n =  int(input("Enter your number : "))
c = 0
a = 0
b = 1
if n==0 or n==1:
    print("YES")
else:
    while c<n:
        c = a+b
        a =b
        b=c
    if c == n:
        print("YES")
    else:
        print("NO :<(")