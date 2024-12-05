text = ""
with open("text word counter/text.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()
for i in range(len(words)):
    words[i] = words[i].strip(".,!-?*\'\"()")
    words[i] = words[i].lower()

allWords = {}

for words in words:
    if words[:4] in allWords:
        allWords[words[:4]] += 1
    else:
        allWords[words[:4]] = 1

callWords = {}

for one in allWords:
    if len(one) > 3:
        callWords[one] =  allWords[one]

alotOfWord = ["", "", "", "", ""]
wordCount = [0, 0, 0, 0, 0]

for one in callWords:
    if allWords[one] > wordCount[4]:
        alotOfWord[4] = one
        wordCount[4] = allWords[one]
        if wordCount[4] > wordCount[3]:
            temp = alotOfWord[3]
            alotOfWord[3] = alotOfWord[4]
            alotOfWord[4] = temp
            temp = wordCount[3]
            wordCount[3] = wordCount[4]
            wordCount[4] = temp
            if wordCount[3] > wordCount[2]:
                temp = alotOfWord[2]
                alotOfWord[2] = alotOfWord[3]
                alotOfWord[3] = temp
                temp = wordCount[2]
                wordCount[2] = wordCount[3]
                wordCount[3] = temp
                if wordCount[2] > wordCount[1]:
                    temp = alotOfWord[1]
                    alotOfWord[1] = alotOfWord[2]
                    alotOfWord[2] = temp
                    temp = wordCount[1]
                    wordCount[1] = wordCount[2]
                    wordCount[2] = temp
                    if wordCount[1] > wordCount[0]:
                        temp = alotOfWord[0]
                        alotOfWord[0] = alotOfWord[1]
                        alotOfWord[1] = temp
                        temp = wordCount[0]
                        wordCount[0] = wordCount[1]
                        wordCount[1] = temp
                    
        


print(alotOfWord)
print(wordCount)