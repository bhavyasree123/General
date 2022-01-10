number = int(input("Enter your number: "))
if number>1:
    for i in range(2,number):
        if (number%2 == 0):
            print(number,"Not a prime number ")
            break
    else:
        print(number,"is a prime number")


else:
    print(number,"Please enter a positive number  ")
