def isNumberInvalid(number):    
    stringifyNumber = str(number)
    halfOfNumber = len(stringifyNumber) // 2

    return stringifyNumber[:halfOfNumber] == stringifyNumber[halfOfNumber:]

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
            if isNumberInvalid(number):
                sumOfInvalidNumbers += number
                
print(f"Sum of invalid numbers: {sumOfInvalidNumbers}")