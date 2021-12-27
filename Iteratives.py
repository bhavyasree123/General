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

rows = 5
b = 0
for i in range(rows,0,-1):
    b += 1
    for j in range(1,i+1):
        print(b,end='')
    print('')
'''Output   11111
            2222
            333
            44
            5'''
    
rows = 5
b = 0
for i in range(rows,0,-1):
    b = +1
    for j in range(1,i+1):
        print(b,end='')
    print('')

'''Output   11111
            1111
            111
            11
            1'''

rows = 5
b = 0
for i in range(rows,0,-1):
    b = +5
    for j in range(1,i+1):
        print(b,end='')
    print('')
'''Output   55555
            5555
            555
            55
            5 '''

rows =  5
for i in range(0,rows+1):
    for j in range(0,i+1):
        print(j,end='')
    print('')

'''Output   0
            01
            012
            0123
            01234
            012345'''
rows = 5
for i in range(rows,0,-1):
    for j in range(0,i+1):
        print(j,end='')
    print('')
'''Output   012345
            012345
            01234
            0123
            012
            01  https://pynative.com/print-pattern-python-examples/'''

