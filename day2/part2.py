def splitIntoChunks(number, n):
    stringifyNumber = str(number)
    
    if len(stringifyNumber) % n != 0:
        return None  # or raise an error
    
    chunkSize = len(stringifyNumber) // n
    chunks = [stringifyNumber[i:i + chunkSize] for i in range(0, len(stringifyNumber), chunkSize)]
    return chunks

def getDivisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def isNumberInvalid(number):
    print(f"Number: {number}")
    stringifyNumber = str(number)
        
    divisorsOfNumber = getDivisors(len(stringifyNumber))
    halfOfNumber = len(stringifyNumber) // 2
    isNumberInvalid = True
    
    for divisor in divisorsOfNumber:
        divisorChunks = splitIntoChunks(number, divisor)
        print(f"Chunks for divisor {divisorChunks}")
        
        firstChunk = divisorChunks[0]
        
        if all(chunk == firstChunk for chunk in divisorChunks):
            isNumberInvalid = True
            break

    return (stringifyNumber[:halfOfNumber] == stringifyNumber[halfOfNumber:]) or isNumberInvalid

fileReader = open("day2/input.txt", "r")
textLine = fileReader.read()
fileReader.close()

intervals = textLine.split(",")

sumOfInvalidNumbers = 0
listOfInvalidNumbers = []

for interval in intervals:
    intervalNumbers = interval.split("-")
    startOfInterval = int(intervalNumbers[0])
    endOfInterval = int(intervalNumbers[1])

    for number in range(startOfInterval, endOfInterval + 1):        
        if isNumberInvalid(number):
            print(f"{number} is invalid and is added to invalid numbers")
            listOfInvalidNumbers.append(number)
            sumOfInvalidNumbers += number
                
print(f"Sum of invalid numbers: {sumOfInvalidNumbers}")
print(f"List of invalid numbers {listOfInvalidNumbers}")