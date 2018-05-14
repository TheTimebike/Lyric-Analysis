import pylab, sys, os
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
saidList, totalList = [], []
dualWord, dualNum = [], []
limit = False
bannedLetters = [',', '.', '\"', '\'']
while True:
    userInput = input('What file would you like to analyse? ')
    if os.path.isfile('./{0}.txt'.format(userInput)):
        break
    else:
        print('Unexpected Input')


while True:
    userInput3 = input('Would you like to use a preset? Y/N (Recommended No)')
    if userInput3.lower() == 'y':
        limit = True
        break
    elif userInput3.lower() == 'n':
        limit = False
        break
    else:
        print('Unexpected Input')

if limit:
    while True:
        userInput2 = input('What preset would you like to use? ')
        if os.path.isfile('./{0}.txt'.format(userInput2)):
            vowelList = str(open('./{0}.txt'.format(userInput2), 'r').readlines()[0]).split(' ')
            print(vowelList)
            break
        else:
            print('Unexpected Input')

while True:
    userInput4 = input('Split the log file? Y/N (Recommended Yes) ')
    if userInput4.lower() == 'y':
        wordList2 = ''.join(open('./{0}.txt'.format(userInput), 'r').readlines()).lower().split(' ')
        break
    elif userInput4.lower() == 'n':
        wordList2 = ''.join(open('./{0}.txt'.format(userInput), 'r').readlines()).lower()
        break
    else:
        print('Unexpected Input')

wordList = []
for word in wordList2:
    for letter in bannedLetters:
        if letter in word:
            wordList.append(word.replace(letter, ''))
        elif letter == word:
            pass    
        else:
            wordList.append(word)

def makeChart(xArg1, yArg1):
    
    objects = yArg1
    y_pos = np.arange(len(objects))
    performance = xArg1
    
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.title('Word Frequency')
    pylab.savefig('EmoteGraph.png')
    plt.gcf().clear()

def makePieChart(xArg1, yArg1):
    labels = yArg1
    sizes = xArg1

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    pylab.savefig('PieChart.png')
    plt.gcf().clear()

for word in wordList:
    if word in saidList:
        index = saidList.index(word) + 1
        saidList[index] += 1
    else:
        saidList.append(word)
        saidList.append(1)


if not limit:
    f = open('./DataDump.txt', 'w+')
    for x in range(len(saidList)):
        if (x % 2 == 0):
            f.write(str(saidList[x]) + ' has a point total of ' + str(saidList[x + 1]) + '\n')
            totalList.append(saidList[x + 1])
            dualWord.append(saidList[x])
            dualNum.append(saidList[x + 1])
    f.close()
if limit:
    f = open('./DataDump.txt', 'w+')    
    for x in range(len(saidList)):
        if (x % 2 == 0):
            if saidList[x] in vowelList:
                f.write(str(saidList[x]) + ' has a point total of ' + str(saidList[x + 1]) + '\n')
                totalList.append(saidList[x + 1])
                dualWord.append(saidList[x])
                dualNum.append(saidList[x + 1])
    f.close()

if len(dualWord) > 10:
    rangeLimit = 10
else:
    rangeLimit = len(dualWord)

highestThree, highestThreeName, emoteArray, copyOfEmoteList, thingyArray = [], [], [], list(dualWord), list(dualNum)
for thisThis in range(rangeLimit):
    numberX = thingyArray.index(max(thingyArray))
    if copyOfEmoteList[numberX] != ' ' or copyOfEmoteList[numberX] != '':
        highestThreeName.append(copyOfEmoteList[numberX])
        highestThree.append(thingyArray[numberX])
    del thingyArray[numberX]
    del copyOfEmoteList[numberX]
makePieChart(xArg1 = highestThree, yArg1 = highestThreeName)
makeChart(xArg1 = highestThree, yArg1 = highestThreeName)

input('Press enter to leave')
