
dup = ['one','two','three','four','five','one','two']
for i in dup:
    print(i)
if i == i:
    print('It has duplicate elements ',i)
dup.remove(i)
print(dup)

#OR 
li = [1,8,9,0,-7,-7,8,5,1]
res = []
for r in li:
    if r not in res:
        res.append(r)
print(res)