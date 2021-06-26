#simple search
key = 100
lis = [1,2,3,4,5,7,4,5,5,6,7,5,5,8,9,7,6]
count = 0
for i in lis:
    count = count + 1
    if i == key:
        print(key, 'is found at index number ',lis.index(key))
        break
if count == len(lis):
    print(key, 'is not found')


