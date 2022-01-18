arr = [1,22,44,11,28]
arr.sort()
print(arr[len(arr)-1])
print(max(arr))

s = ["hajbhjsh", "jhghgh", "hvb"]
k = '_'.join(s)
print(k)
sp = "ahbxa jgh jhj sbxa"
print(sp.split())
print(s[0:2])

input_str = int(input())
arr = []
print("Enter the elements: ")
for i in range(input_str):
    element = int(input())
    arr.append(element)
    rev = arr[0]-arr[-1]
print(rev)
print("hello")