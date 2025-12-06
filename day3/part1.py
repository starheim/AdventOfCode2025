import time

def findLargestJoltageForBank(bank):
    biggestJoltage = 0
    lengthOfBank = len(str(bank)) 
    
    for i in range(lengthOfBank):
        for n in range(i+1, lengthOfBank):
            currentJoltage = int(str(bank[i]) + str(bank[n]))
            if(currentJoltage > biggestJoltage):
                biggestJoltage = currentJoltage
    
    return biggestJoltage

fileReader = open("day3/input.txt", "r")
textLine = fileReader.readlines()
fileReader.close()

totalJoltage = 0

startTime = time.time()

for line in textLine:
    bank = line.strip()
    totalJoltage += findLargestJoltageForBank(bank)
    
endTime = time.time()   
    
print(f"Total output joltage: {totalJoltage} - calculation finished in {endTime - startTime:.4f} seconds.")
