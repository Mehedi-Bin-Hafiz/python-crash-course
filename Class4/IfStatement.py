#
# age = 69
#
# if age >= 18 :
#     print("You are able to attend Election.")
# else:
#     print('You are not able to attend Election.')
#

biman_bangladesh = [12,11,11,9,7,19,24,25,12,13,67]


for age in biman_bangladesh:
    print('Your age: ',age, end=' :')
    if age <=10 and age >=0 :
        print('No need to buy ticket.')
    elif age > 10 and age<=20 :
        print('Traveller need to pay half of total cost.')
    elif age > 20 and age<=30 :
        print('Traveller need to pay total cost')
    else:
        print('No need to travel')
