import sys, pickle, random, functions as fun



def makeChain(inputList, maxDepth):
	chain = {}
	for index in range(1, len(inputList)):
		for depth in range(1, maxDepth+1):
			if index >= depth:
				key = tuple(inputList[index-depth:index])
				if key in chain:
					chain[key] = chain[key] + inputList[index:index + 1]
				else:
					chain[key] = inputList[index:index + 1]
	return chain

def makeChainPlus(inputList, maxDepth):
	chain = {}
	for index in range(1, len(inputList)):
		for depth in range(1, maxDepth+1):
			if index >= depth:
				key = tuple(inputList[index-depth:index])
				if key in chain:
					if inputList[index] in chain[key]:
						chain[key][inputList[index]] += 1
					else:
						chain[key][inputList[index]] = 1
				else:
					chain[key] = {inputList[index]: 1}
	return chain

def formSentence(chain, maxLength, startingWord):
	key = [startingWord.lower()]
	looping = True
	while looping:
		if len(key) >= maxLength:
			looping = False
		for keyIndex in range(len(key)):
			if tuple(key[keyIndex:]) in chain:
				newKeyValue = random.choice(chain[tuple(key[keyIndex:])])
				key.append(newKeyValue)
				# print(newKeyValue, end=' ')
				break
			elif keyIndex == len(key)-1:
				looping = False


	return (' '.join(key) + '.').capitalize()

def saveChain(chain, fileName):
	saveFile = open(fileName, 'wb')
	pickle.dump(chain, saveFile)
	saveFile.close()

def loadChain(fileName):
	loadFile = open(fileName, 'rb')
	chain = pickle.load(loadFile)
	loadFile.close()
	return chain



def main():
	literatureFile = sys.argv[1]

	if literatureFile[len(literatureFile)-4:len(literatureFile)] == '.pkl':
		chain = loadChain(literatureFile)
		wordCount = int(sys.argv[2])
		startingWord = sys.argv[3]
		print(formSentence(chain, wordCount, startingWord))
	else:
		literature = fun.wordsFromString(open(literatureFile).read())
		maxDepth = int(sys.argv[2])
		chain = makeChain(literature, maxDepth)
		saveChain(chain, literatureFile[:-4]+str(maxDepth)+'.pkl')




if __name__ == '__main__':
	main()
