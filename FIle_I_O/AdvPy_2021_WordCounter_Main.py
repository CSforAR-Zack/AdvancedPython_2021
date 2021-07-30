from tkinter import Tk
from tkinter.filedialog import askopenfilename
from string import punctuation

def main():
    fileCreator()
    filename = fileSelector()

    fileContents = getFileContents(filename)
    
    text = fileContents.lower()
    
    for symbol in punctuation:
        text = text.replace(symbol, "")
    
    words = text.split()
    
    wordList = wordFreq(words)


    for index, item in enumerate(wordList):
        if index > 10:
            break
        print(item[0], item[1])

def wordFreq(words):
    wordSet = set(words)

    frequencies = {}
    for word in wordSet:
        f = words.count(word)
        frequencies[word] = f

    sortedFreq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    return sortedFreq

def getFileContents(filename):
    with open(filename, "r") as fObj:
        fileContents = fObj.read()

    return fileContents


def fileSelector():
    Tk().withdraw()
    filename = askopenfilename()
    return filename

def fileCreator():
    with open("sample.txt", "w") as fObj:
        for line in range(10):
            if line % 2 == 0:
                text = f"This is line {line + 1}.\n"
            else:
                text = f"This is line {line + 1}."
                text = f"{text} This is appended to this line.\n"
            fObj.write(text)


main()