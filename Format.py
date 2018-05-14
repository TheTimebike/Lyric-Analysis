wordList = open('./Lyrics.txt', 'r').readlines()
newWord = []
for word in wordList:
    if word.lower().endswith('\n'):
        newWord.append(str(word)[:-2])
    else:
        newWord.append(str(word))
f = open('./NewLyrics.txt', 'w+')
joinedStr = ' '.join(newWord)
f.write(joinedStr.lower().replace('!', '').replace('(', '').replace(')', '').replace('.', '').replace(',', '').replace('\'', '').replace('\"', ''))
