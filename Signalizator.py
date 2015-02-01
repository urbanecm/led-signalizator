#!/usr/bin/env python

#############################DEFINE VARIABLES################################

numbersUserText = {0 : "", 1 : "", 2 : "", 3 : ""}
numbersSystemText = {0 : "Ok", 1 : "Undefined", 2 : "Q", 3 : "Error"}
textSystemNumbers = {"Ok" : 0, "Undefined" : 1, "Q" : 2, "Error" : 3}
textUserNumbers = {"" : 0, "" : 1, "" : 2, "" : 3}
numbersMethod = {0 : lambda: signalizeOk(), 1 : lambda: signalizeUndefined(), 2 : lambda: signalizeQ(), 3 : lambda: signalizeError()}

##############################USER FRIENDLY FUNCTIONS#########################

def signalize(sig):
	type = checkType(sig)
	if type == None:
		raise ValueError
	elif type == "n":
		for key in numbersMethod:
			if key == sig:
				method = numbersMethod[key]
				method()
	else:
		number = textToNumber(sig)
		if number == None:
			raise ValueError
		else:
			signalize(number)

##############################BASIC FUNCTIONS##################################

def signalizeError():
	print "Error"
def signalizeOk():
	print "Ok"
def signalizeQ():
	print "Q"
def signalizeUndefined():
	print "Undefined"

#############################TRANSLATOR FUNCTIONS#############################

def numberToSystemText(number):
	if number in numbersSystemText:
		return numbersSystemText[number]
def numberToUserText(number):
	if number in numbersUserText:
		return numbersUserText[number]
def SystemTextToNumber(SystemText):
	if SystemText in textSystemNumbers:
		return textSystemNumbers[SystemText]
def UserTextToNumber(UserText):
	pass
def textToNumber(text):
	if isSystem(text) == True:
		return SystemTextToNumber(text)
	elif isUser(text) == True:
		return UserTextToNumber(text)
	else:
		return None

##########################HELP FUNCTION######################################

def checkType(o):
	if isNumber(o):
		return "n"
	elif isSystem(o):
		return "s"
	elif isUser(o):
		return "u"
	else:
		return None
def isSystem(s):
	if s in textSystemNumbers:
		return True
	elif s in textUserNumbers:
		return False
	else:
		return None
def isUser(s):
	if s in textUserNumbers:
		return True
	elif s in textUserNumbers:
		return False
	else:
		return None
def isNumber(o):
	if o in numbersSystemText:
		return True
	else:
		return False
