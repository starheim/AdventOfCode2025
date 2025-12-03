fileReader = open("day1/input.txt", "r")
lines = fileReader.readlines()
fileReader.close()

numberOfTimesPointedAtZero = 0
initialPosition = 50

for line in lines:
    
    line = line.strip()
    direction = line[0]
    number = int(line[1:])
    factorOfHundred = number // 100
    print("Number: %d" %number)
    print("Factor of hundred: %d" %factorOfHundred)
    rotation = number % 100
    
    if direction == "L":
        if(initialPosition - rotation < 0):
            initialPosition = initialPosition + 100 - rotation
            if factorOfHundred > 1:
                numberOfTimesPointedAtZero += factorOfHundred
            else:
                numberOfTimesPointedAtZero += 1
        else: initialPosition -= rotation
    
    else:
        if(initialPosition + rotation > 99):
            initialPosition = initialPosition - 100 + rotation
            if factorOfHundred > 1:
                numberOfTimesPointedAtZero += factorOfHundred
            else:
                numberOfTimesPointedAtZero += 1
        else: initialPosition += rotation
    
    if initialPosition == 0:
        numberOfTimesPointedAtZero += 1
        
    print("Current Position: %d" %initialPosition)

print("Number of times touching zero: %d" %numberOfTimesPointedAtZero)