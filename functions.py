import re



def wordsFromString(inputString):
	returnString = ''
	for char in inputString:
		if char.isspace():
			returnString += ' '
		elif char.isalpha():
			returnString += char
	return returnString.lower().split()


def stripNonAlphaNumerics(inputString):
	return re.compile('[\W_]+', re.UNICODE).sub('', inputString)