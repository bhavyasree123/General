user_input = float(input("Enter your number : "))
sum = 0
temp = user_input
while temp>0:
    digit = temp%10
    sum  += digit**3
    temp //=10
if user_input == sum:
    print(sum,"is an Armstrong number")
else:
    print(user_input,"is not an Armstrong number")


