def isNumberValid(number):    
    stringifyNumber = str(number)
    
    halfOfNumber = len(stringifyNumber) // 2
    firstHalfOfNumber = int(stringifyNumber[:halfOfNumber])
    secondHalfOfNumber = int(stringifyNumber[halfOfNumber:])

    return firstHalfOfNumber == secondHalfOfNumber    

fileReader = open("day2/input.txt", "r")
textLine = fileReader.read()
fileReader.close()

intervals = textLine.split(",")

sumOfInvalidNumbers = 0

for interval in intervals:
    intervalNumbers = interval.split("-")
    startOfInterval = int(intervalNumbers[0])
    endOfInterval = int(intervalNumbers[1])

    for number in range(startOfInterval, endOfInterval + 1):        
        if len(str(number)) % 2 == 0:
            if isNumberValid(number):
                sumOfInvalidNumbers += number
                
print(f"Sum of invalid numbers: {sumOfInvalidNumbers}")