'''
Intelectual Property of Eirik Lid (C)

See README.md for instructions
'''

from random import shuffle
import json
NUM_BASISGRUPPER = 22
NUM_PRAKSISGRUPPER = 4

class Student(object):
	
	
	def __init__(self, name,basisgruppe):
		self.place = [-1, -1, -1, -1, -1]
		self.name = name
		self.basisgruppe = basisgruppe

	def assign_place(self,praksis,position):
		if(praksis < 6 and praksis > 0 and position > 0) :
			self.place[praksis-1] = position

	def copy_placing(self,place):
		if len(place) == 5:
			self.place = place
	

def clear_praksisgroups():

	file = open("Praksisgroup1.json",'w')
	file.write('\n')
	file.close()

	file = open("Praksisgroup2.json",'w')
	file.write('\n')
	file.close()

	file = open("Praksisgroup3.json",'w')
	file.write('\n')
	file.close()

	file = open("Praksisgroup4.json",'w')
	file.write('\n')
	file.close()

def end_praksisgroups():
	file = open("Praksisgroup1.json",'a')
	file.write(']')
	file.close()

	file = open("Praksisgroup2.json",'a')
	file.write(']')
	file.close()

	file = open("Praksisgroup3.json",'a')
	file.write(']')
	file.close()

	file = open("Praksisgroup4.json",'a')
	file.write(']')
	file.close()

def dump_praksisgroup(praksisgroup, grouplist):
	if(praksisgroup == 1):
		file = open("Praksisgroup1.json",'wb')
	elif(praksisgroup == 2):
		file = open("Praksisgroup2.json",'wb')
	elif(praksisgroup == 3):
		file = open("Praksisgroup3.json",'wb')
	elif(praksisgroup == 4):
		file = open("Praksisgroup4.json",'wb')
	json.dump(grouplist,file)
	file.close()

def assignment_init():
	#clear_praksisgroups()
	with open("Studentlist.txt",'r') as f:

		result = []

		for student in f:
			if student != '\n':
				result.append(student.rstrip('\n'))

		shuffle(result)
		students = []
		group1 = []
		group2 = []
		group3 = []
		group4 = []

		for i in range(len(result)):
			basisgruppe = 1+ i%NUM_BASISGRUPPER 
			students.append( Student(result[i],basisgruppe))
			students[i].assign_place(1,i+1)
			#result[i] = result[i] +" Plass: "+str(i+1)+ " Gruppe: "+ str(basisgruppe)+'\n'
			#print[result[i]]
			praksisgroup = basisgruppe%NUM_PRAKSISGRUPPER
			if(praksisgroup == 1):
				group1.append(students[i].__dict__)
			
			elif(praksisgroup == 2):
				group2.append(students[i].__dict__)
				
			
			elif(praksisgroup == 3):
				group3.append(students[i].__dict__)
				
			elif(praksisgroup == 4):
				group4.append(students[i].__dict__)
				

		#print result
		dump_praksisgroup(1,group1)
		dump_praksisgroup(2,group2)
		dump_praksisgroup(3,group3)
		dump_praksisgroup(4,group4)

assignment_init()

import sys

def assign_numbers(praksisfile):
	with open(praksisfile,'r') as f:
		basisgrupper = {}
		stud_list = []
		students = json.load(f)
		for student in students:
			#print student[u'name'].encode(sys.stdout.encoding, errors='replace')
			new_student = Student(student[ u'name'],student[ u'basisgruppe'])
			
			new_student.copy_placing(student[u'place'])
			stud_list.append(new_student)

			#Hvis basisgupper skal kunne hentes ut
			if new_student.basisgruppe in basisgrupper:
				basisgrupper[new_student.basisgruppe].append(new_student)
			else:
				basisgrupper[new_student.basisgruppe] = [new_student]
			
		stud_list.sort(key= lambda x: x.place[0], reverse = True)

		for i,student in  enumerate(stud_list):
			student.assign_place(2,i+1)
			
assign_numbers("Praksisgroup1.json")
