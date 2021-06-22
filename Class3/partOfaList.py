studentNames = ['Mehedi','sifat','Mahadi','khairul','Israt','hasnat','Nahid']

print(studentNames[:3])
print(studentNames[4:7])

############Copy list############

copyList = studentNames[:]
studentNames.remove('Mehedi')
print(studentNames)
print(copyList)

