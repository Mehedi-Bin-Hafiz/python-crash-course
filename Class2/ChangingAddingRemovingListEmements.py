
studentNames = ['Mehodi','sifat','Mahadi','khairul','Israt','hasnat','Nahid']


#Changing
studentNames[0] = 'Mehedi' #assigning
print(studentNames)

#adding using append method
studentNames.append('Karim')
print(studentNames)

# inserting elements in the list by index
studentNames.insert(1,'Rahim')
print(studentNames)

#deleting list elements
del studentNames[-1]
print(studentNames)