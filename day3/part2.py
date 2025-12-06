import time

biggestJoltage = 0
lengthOfBank = None
biggestJoltage = 0

def findLargestJoltageForBank(bank, remainingCalls):
    for i in range(lengthOfBank):

fileReader = open("day3/input.txt", "r")
textLine = fileReader.readlines()
fileReader.close()

totalJoltage = 0

startTime = time.time()

for line in textLine:
    bank = line.strip()
    if(lengthOfBank == None):
        len(str(bank))
    totalJoltage += findLargestJoltageForBank(bank, lengthOfBank)
    
endTime = time.time()   
    
print(f"Total output joltage: {totalJoltage} - calculation finished in {endTime - startTime:.4f} seconds.")
