import time

def getNumberOfAdjacentPaperRolls(x, y, ):
    print(x)
    print(y)

with open("day4/input.txt") as f:
    warehouseInventory = [list(line.strip()) for line in f]

startTime = time.time()


accessibleRollsOfPaper = 0

for lineIndex, line in enumerate(warehouseInventory):
    for itemIndex, item in enumerate(line):
        if(item == "@"):
            print(f"Item: {item}")
            getNumberOfAdjacentPaperRolls(lineIndex, itemIndex)