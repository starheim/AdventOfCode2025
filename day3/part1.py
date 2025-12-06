fileReader = open("day3/input.txt", "r")
textLine = fileReader.readlines()
fileReader.close()

for line in textLine:
    bank = line.strip()
    print(f"Bank: {line.strip()}")