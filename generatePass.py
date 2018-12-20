#!/usr/bin/python3
import random
import sys
import random
import string
length=sys.argv[1]
#if leftOver <= 0:
#	print ("Usage:%s,%s",%ssys.argv[0],%ssys.argv[1])
#	exit 0
specialCharsList=["!","@","#","$","%","^","&","*","(",")","-","+","=","{","}","[","]","~","|"]
def randomPass(length):
	precentageList=[40,15,15,30]
	random.shuffle(precentageList)
	specialChars=(int(length)*precentageList[0])//100
	capLetters=(int(length)*precentageList[1])//100
	lowLetters=(int(length)*precentageList[2])//100
	numbers=(int(length)*precentageList[3])//100
	leftOver=int(length)-int(specialChars+capLetters+lowLetters+numbers)
	if leftOver>0:
		lowLetters=	lowLetters+leftOver
	newList=[]
	i=0
	while i < specialChars:
		char=random.choice(specialCharsList)
		newList.append(char)
		i+=1
	i=0
	while i < capLetters:
		char=random.choice(string.ascii_uppercase)
		newList.append(char)
		i+=1
	i=0
	while i < lowLetters:
		char=random.choice(string.ascii_lowercase)
		newList.append(char)
		i+=1
	i=0
	while i < numbers:
		char=random.randint(0,9)
		newList.append(char)
		i+=1
	newList2=[]
	random.shuffle(newList)
	print("PasswordGenerated:")
	for i in newList:
		print(i,end='')
	print ()
randomPass(length)
