'''
Intelectual Property of Eirik Lid (C)

See README.md for instructions
'''

from random import shuffle


NUM_BASISGRUPPER = 22
NUM_PRAKSISGRUPPER = 4

f=open("Studentlist.txt",'r')

result = []

for student in f:
	if student != '\n':
		result.append(student.rstrip('\n'))

shuffle(result)

for i in range(len(result)):
	basisgruppe = 1+ i%NUM_BASISGRUPPER 
	result[i] = result[i] +"Plass: "+str(i)+ " Gruppe: "+ str(i%NUM_BASISGRUPPER)+'\n'
	print[result[i]]
	praksisgroup = basisgruppe%NUM_PRAKSISGRUPPER
	if(praksisgroup == 0):
		file = open("Praksisgroup1.txt",'a')
		file.write(result[i])
		file.close()
	
	elif(praksisgroup == 1):
		file = open("Praksisgroup2.txt",'a')
		file.write(result[i])
		file.close()
	
	elif(praksisgroup == 2):
		file = open("Praksisgroup3.txt",'a')
		file.write(result[i])
		file.close()
	
	elif(praksisgroup == 3):
		file = open("Praksisgroup4.txt",'a')
		file.write(result[i])
		file.close()

#print result

f.close()





