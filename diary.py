#!/bin/bash python
"""
created by m1ghtfr3e
"""
import datetime

class Diary:
	

	def readDiary(self):
		
		d = open('MyDiary.txt', 'r')
		for line in d:
			print(line.strip())
		d.close()

	def writeDiary(self):

		date = datetime.datetime.now()
		
		entry = input("You can tell me now:  ")
		
		with open('MyDiary.txt', 'a') as md:
			md.write("\n--------------------------\n")
			md.write("\n Entry made on:  ")
			md.write(str(date))
			md.write("\n")
			md.write(entry)
			md.write("\n")
		return



if __name__ == '__main__':

	print("""
		Welcome to this diary program
			Hope you like it :)
""")
	
	diary = Diary()

	option = input("Do you want to read me or write something? (r/w):  ")
	if option == 'r':
		diary.readDiary()
	if option == 'w':
		diary.writeDiary()

	


