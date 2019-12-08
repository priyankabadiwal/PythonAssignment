#import library
#open file in read mode
inputFile =  open("input.txt","r")
#open file in write mode
outputFile =  open("output.txt","w") 


def readIntegers():
    #Step 1: Read file
    inputFileContent = inputFile.read()
    #Step 2: Split the single line using comma as separator
    separatedNumbers = inputFileContent.split(',')
    #Step 3: Add the numbers to a list Important: convert string to integer before adding
    mylist = []
    for n in separatedNumbers:
        mylist.append(int(n))
    print("My List: ")
    print(mylist)
    return mylist

def readUniqueContentFromList(integerFromFile):
    #Step 1: Create a list
    uniqueList = []
    #Step 2: For loop and find unique numbers
    for n in integerFromFile:
        if n not in uniqueList:
            uniqueList.append(n)
    print("Unique List:")
    print(uniqueList)
    return uniqueList

def listSum(uniqueValueFromList):
    #Step 1: Create a variable and initialize to 0
    sumOfNumbers = 0
    #Step 2: For Loop through uniqueList and sum the elements
    for n in uniqueValueFromList:
        sumOfNumbers = sumOfNumbers + n
    print("Sum of Numbers:")
    print(sumOfNumbers)
    return sumOfNumbers

def writeToFile(sumOfUniqueInteger):
    #Step 1: Write Output to file
    outputFile.write(str(sumOfUniqueInteger))


def releaseResources():
    #Step 1: Close both the files 
    inputFile.close()
    outputFile.close()
    
#Step 1: Call function to read integers
integersFromFile = readIntegers()
#Step 2: Call function to get unique values
uniqueIntegers = readUniqueContentFromList(integersFromFile)
#Step 3: Call function to sum unique integers
sumOfNumbers = listSum(uniqueIntegers)
#Step 4: Call function to write to file
writeToFile(sumOfNumbers)
#Step 5: Call function to close the file descriptors
releaseResources()


