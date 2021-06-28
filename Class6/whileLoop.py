
# i = 0
# while i < 10:
#     print(i)
#     i = i+1

# var = True
# i = 0
# while var:
#     name = input('Enter student name: ')
#     print(name)
#     if name == 'mehedi':
#         var = False

# studentNames = ['Mehedi','sifat','Mahadi','khairul','Israt','hasnat','Nahid','hasnat','hasnat']

# studentNames.remove('hasnat')
# studentNames.remove('hasnat')
# studentNames.remove('hasnat')
# print(studentNames)

# while 'hasnat' in studentNames:
#     studentNames.remove('hasnat')
# print(studentNames)

# studentNames = ['Mehedi','sifat','Mahadi','khairul','Israt','hasnat','Nahid',]
#
# # studentNames.append('karim')
# # studentNames.append('rahim')
# # studentNames.append('abc')
# # studentNames.append('bcd')
# # print(studentNames)
#
# decision = True
# while decision:
#     name = input('Enter sudent name:')
#     studentNames.append(name)
#     ans = input('Do you want to enroll another student? (Yes/No)').upper()
#     if ans == 'NO':
#         decision = False
#     elif ans == "YES":
#         continue
# print(studentNames)

studentNamesDict = { 'Mehedi': 24, 'sifat': 23,'Mahadi':23,'khairul':24,'Israt':21,'hasnat':22,'Nahid':20 }


decision = True
while decision:
    name = input('Enter student name:')
    age = int(input("Enter student's age: "))
    studentNamesDict[name] = age
    ans = input('Do you want to enroll another student? (Yes/No)').upper()
    if ans == 'NO':
        decision = False
    elif ans == "YES":
        continue
print(studentNamesDict)