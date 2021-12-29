#  find Perfect Number using For loop
user_intput = int(input('What is your number? '))
sum = 0
for i in range(1,user_intput):
    if user_intput%i == 0:
        sum = sum + 1
if sum == user_intput:
    print("It's a Perfect Number!!")
else:
    print("It's not a Perfect Number")