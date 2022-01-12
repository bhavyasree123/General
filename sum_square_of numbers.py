N = int(input("Enter your sequence : "))
sum_of_numbers = 0
for i in range(1,N+1):
    sum_of_numbers += (i*i)
    print(sum_of_numbers)
print("Sum and squares of numbers : " , sum_of_numbers)