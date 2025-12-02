fileReader = open("day1/input.txt", "r")
lines = fileReader.readlines()
fileReader.close()

numberOfTimesPointedAtZero = 0
initialPosition = 50

for line in lines:
    
    line = line.strip()
    direction = line[0]
    rotation = int(line[1:]) % 100
    
    if direction == "L":
        if(initialPosition - rotation < 0):
            initialPosition = initialPosition + 100 - rotation
        else: initialPosition -= rotation
    
    else:
        if(initialPosition + rotation > 99):
            initialPosition = initialPosition - 100 + rotation
        else: initialPosition += rotation
    
    if initialPosition == 0:
        numberOfTimesPointedAtZero+=1

print("Number of times pointed as zero: %d" %numberOfTimesPointedAtZero)