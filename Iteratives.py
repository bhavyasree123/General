rows = 9
for i in range(rows+1):
    for j in range(i):
        print(i,end='') #used to place a space after the displayed string instead of a newline
    print('')
'''output   1
            22
            333
            4444
            55555
            666666
            7777777
            88888888
            999999999'''



rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

'''Output   1
            1 2
            1 2 3
            1 2 3 4
            1 2 3 4 5'''