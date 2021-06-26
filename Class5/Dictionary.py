#
# studentName = {}
#
# studentName['Mehedi'] = 24
# studentName['Mahadi'] = 25
#
# print(studentName)

studentNames = { 'Mehedi': 24, 'sifat': 23,'Mahadi':23,'khairul':24,'Israt':21,'hasnat':22,'Nahid':20 }
# print(studentNames.items())
# for key, age in studentNames.items():
#     print(key+"'s age is: ", age)
# for name, age in studentNames.items():
#     if age > 23:
#         print(name, 'will get gold.')
#     else:
#         print(name, 'will get silver.')
# del studentNames['Nahid']
#
# print(studentNames)
# for key in studentNames.keys():
#     print(key)
#
# for value in studentNames.values():
#     print(value)

studentNames2 = { 'Rahim': 24, 'Karim': 23,'Salam':23,'Borkot':24,'Rofic':21,'Sofic':22, }

allStudent=[studentNames,studentNames2]
# print(allStudent)

# for i in allStudent:
#     print(i)
#     for key in i.keys():
#         print(key)

# sifat's ans
# for k,i in allStudent[0].items():
#     print(k,i)

studentNames3 = { 'Rahim': 24, 'Karim': 23,'Salam':23,'Borkot':24,'Rofic':21,'Sofic':[22,23,24,25] }

print(studentNames3['Sofic'])

for age in studentNames3['Sofic']:
    print(age)

studentNames4 = { 'Rahim': 24, 'Karim': 23,'Salam':23,'Borkot':24,'Rofic':21,'Sofic':{'ab':34,'bc':50}}

for name, age in studentNames4['Sofic'].items():
    print(name, age)

