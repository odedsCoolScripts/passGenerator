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
	if int(length)>4:
		specialChars=(int(length)*precentageList[0])//100
		capLetters=(int(length)*precentageList[1])//100
		lowLetters=(int(length)*precentageList[2])//100
		numbers=(int(length)*precentageList[3])//100
		leftOver=int(length)-int(specialChars+capLetters+lowLetters+numbers)
		if leftOver>0:
			lowLetters=	lowLetters+leftOver
		charTypesList=[specialChars,capLetters,lowLetters,numbers]
		i=0
		while i < len(charTypesList):
			if charTypesList[i]==0:
				charTypesList[i]=1
				n=0
				while n < len(charTypesList):
					if charTypesList[n] > 1:
						charTypesList[n] -= 1
						n=len(charTypesList)
					n+=1
			i+=1
	else:
		charTypesList=[1,1,1,1]
	newList=[]
	i=0
	while i < charTypesList[0]:
		char=random.choice(specialCharsList)
		newList.append(char)
		i+=1
	i=0
	while i < charTypesList[1]:
		char=random.choice(string.ascii_uppercase)
		newList.append(char)
		i+=1
	i=0
	while i < charTypesList[2]:
		char=random.choice(string.ascii_lowercase)
		newList.append(char)
		i+=1
	i=0
	while i < charTypesList[3]:
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
