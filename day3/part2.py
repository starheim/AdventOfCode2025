import time

lengthOfBank = None
totalJoltage = 0
MAX_BATTERIES = 12

def findLargestJoltageForBank(bank, listOfJoltages, biggestJoltage):
    print(f"Bank: {bank}")
    print(f"List of joltages: {listOfJoltages}")
    print(f"Length og listOfJoltages: {len(listOfJoltages)}")
    if(len(listOfJoltages) < MAX_BATTERIES):
        for i in range(0, len(bank)):
            print(f"Bank[0] = {bank[0]}")
            listOfJoltages.append(bank[0])
            findLargestJoltageForBank(bank[i + 1:], listOfJoltages + bank[i-1], biggestJoltage) 
    
    else:
        currentJoltage = sum(listOfJoltages)
        if(currentJoltage > biggestJoltage):
            biggestJoltage = currentJoltage
        return


fileReader = open("day3/input.txt", "r")
textLine = fileReader.readlines()
fileReader.close()

startTime = time.time()

for line in textLine:
    biggestJoltage = 0
    bank = line.strip()
    if(lengthOfBank == None):
        len(str(bank))
    findLargestJoltageForBank([int(ch) for ch in bank], [], biggestJoltage)
    totalJoltage += biggestJoltage
    
endTime = time.time()   
    
print(f"Total output joltage: {totalJoltage} - calculation finished in {endTime - startTime:.4f} seconds.")