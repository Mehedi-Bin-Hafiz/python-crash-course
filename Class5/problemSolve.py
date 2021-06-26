primenum = { 1:0,3:2,4:3,5:4,6:5,7:6,2:1,8:7,9:8,10:9,11:10,}
print(primenum)

for key,value in primenum.items():
    count = 0
    if value == 1:
        print(key)
    else:
        for i in range(1,value+1):
            if (value % i == 0):
                count = count +1
        if count == 2:
            print(key)
        else:
            pass




