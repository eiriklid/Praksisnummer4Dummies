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

		group1 = []
		group2 = []
		group3 = []
		group4 = []

		for i,student in  enumerate(stud_list):
			student.assign_place(2,i+1)
			if(i < len(stud_list)/4):
				group1.append(student)
			elif(i < len(stud_list)/2):
				group2.append(student)
			elif(i < (3*len(stud_list))/4):
				group3.append(student)
			else:
				group4.append(student)
		
		group1.sort(key= lambda x: x.place[1], reverse = True)
		group2.sort(key= lambda x: x.place[1], reverse = True)
		group3.sort(key= lambda x: x.place[1], reverse = True)
		group4.sort(key= lambda x: x.place[1], reverse = True)
		
		lengths = [len(group1),len(group2),len(group3),len(group4)]

		for i in range(len(stud_list)):
			if(i < lengths[1]):
				group2[i].assign_place(3,i+1)
			elif(i < lengths[1]+lengths[2]):
				group3[i%lengths[2]].assign_place(3,i+1)
			elif(i < lengths[1]+lengths[2]+lengths[3]):
				group4[i%lengths[3]].assign_place(3,i+1)
			else:
				group1[i%lengths[0]].assign_place(3,i+1)
		
		group1.sort(key= lambda x: x.place[2], reverse = True)
		group2.sort(key= lambda x: x.place[2], reverse = True)
		group3.sort(key= lambda x: x.place[2], reverse = True)
		group4.sort(key= lambda x: x.place[2], reverse = True)
		

		for i in range(len(stud_list)):
			if(i < lengths[2]):
				group3[i].assign_place(4,i+1)
			elif(i < lengths[2]+lengths[3]):
				group4[i%lengths[3]].assign_place(4,i+1)
			elif(i < lengths[0]+lengths[2]+lengths[3]):
				group1[i%lengths[0]].assign_place(4,i+1)
			else:
				group2[i%lengths[1]].assign_place(4,i+1)
		
		group1.sort(key= lambda x: x.place[3], reverse = True)
		group2.sort(key= lambda x: x.place[3], reverse = True)
		group3.sort(key= lambda x: x.place[3], reverse = True)
		group4.sort(key= lambda x: x.place[3], reverse = True)
		
		for i in range(len(stud_list)):
			if(i < lengths[3]):
				group4[i].assign_place(5,i+1)
			elif(i < lengths[0]+lengths[3]):
				group1[i%lengths[0]].assign_place(5,i+1)
			elif(i < lengths[0]+lengths[1]+lengths[3]):
				group2[i%lengths[1]].assign_place(5,i+1)
			else:
				group3[i%lengths[2]].assign_place(5,i+1)

		for student in stud_list:
			pl = student.place
			
			print pl, pl[1]+pl[2]+pl[3]+pl[4]

assign_numbers("Praksisgroup1.json")
