
def main():
    #fileRead()
    #fileWrite()
    fileAppend()
    pass

def fileAppend():
    with open("sample.txt", "a") as fObj:
        fObj.write("This line is appended in.\n")

def fileWrite():
    with open("sampleWrite.txt", "w") as fObj:
        text = "Awsome Possum!\n"
        fObj.write(text)
        fObj.write("Second line!\n")
        fObj.write("\tThird line!\nFourth line!\n")
    

def fileRead():
    with open("sample.txt", "r") as fObj:
        # text = fObj.read() # Read in all file content
        # text = fObj.readline().strip()
        # text2 = fObj.readline().strip()
        textList = fObj.readlines()
    
        # print(type(text))
        # print(text)
        # print(text2)
        print(textList)
        for line in textList:
            if "Cows" in line:
                print(line.strip())

main()
