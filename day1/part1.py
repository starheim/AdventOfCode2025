fileReader = open("day1/input.txt", "r")
lines = fileReader.readlines()
fileReader.close()

numberOfTimesPointedAtZero = 0
initialPosition = 50

for line in lines:
    
    line = line.strip()  # Remove newline characters
    direction = line[0]
    rotation = int(line[1:]) % 100
    
    if direction == "L":
        print("Turn left")
        initialPosition = (initialPosition - rotation) % 100
    
    else:
        print("Turn right")
        initialPosition = (initialPosition + rotation) % 100
    
    if initialPosition == 0:
        numberOfTimesPointedAtZero+=1

    print("Current Position: %d" %initialPosition)

print("Number of times pointed as zero: %d" %numberOfTimesPointedAtZero)