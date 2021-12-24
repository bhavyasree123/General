#lists into string

items = ['Hi!' , 'How', 'are','you?']
x=''.join(items)
print(x)
#(OR) by using function
def combine():
    i = ['o','k']
    j=''.join(i)
    print(j)
combine()
#OR
def list(list1):
    str = ''
    print(str.join(list1))
list1= ['I','am','XYZ']
list(list1)

#taking input from user

user_input = input("enter ")
splitting_user_input=user_input.split()
print(splitting_user_input)
input_join = ''.join(splitting_user_input)
print(input_join)