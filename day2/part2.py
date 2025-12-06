import time

def splitIntoChunks(number, n):
    stringifyNumber = str(number)
    
    if len(stringifyNumber) % n != 0:
        return None
    
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
    stringifyNumber = str(number)
        
    divisorsOfNumber = getDivisors(len(stringifyNumber))
    isNumberInvalid = False
        
    for divisor in divisorsOfNumber:
        if(divisor != 1):
            divisorChunks = splitIntoChunks(number, divisor)
            areAllChunksTheSame = len(set(divisorChunks)) == 1
        
            if(areAllChunksTheSame):
                isNumberInvalid = True
                break

    return isNumberInvalid

fileReader = open("day2/input.txt", "r")
textLine = fileReader.read()
fileReader.close()

intervals = textLine.split(",")

sumOfInvalidNumbers = 0
listOfInvalidNumbers = []

print(f"Calculating...")
start = time.time()

for interval in intervals:
    intervalNumbers = interval.split("-")
    startOfInterval = int(intervalNumbers[0])
    endOfInterval = int(intervalNumbers[1])

    for number in range(startOfInterval, endOfInterval + 1):        
        if isNumberInvalid(number):
            listOfInvalidNumbers.append(number)
            sumOfInvalidNumbers += number
            
end = time.time()

print(f"Calculation finished in {end - start:.4f} seconds.")
                
print(f"Sum of invalid numbers: {sumOfInvalidNumbers}")