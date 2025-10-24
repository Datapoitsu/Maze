mazeArray = [
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
    1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,
    1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,
    1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,
    1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,
    1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,
    1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,
    1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,
    1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,
    1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,
    1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,
    1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,
    1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,
    1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,
    1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,
    1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,
    1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,
    1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,
    1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
]
width = 21
height = int(len(mazeArray) / width)

currentPos = 22 #Index
goalPos = 175
mazeArray[goalPos] = 2

def printBoard():
    global mazeArray
    for i in range(height):
        print(mazeArray[i*width:(i+1)*width])


def move(dir:int):   #0 = right, 1 up, 2 left, 3 down
    global currentPos
    match dir:
        case 0:
            if mazeArray[currentPos + 1] == 1:
                print("Cannon't go to right from pos " + str(currentPos))
            else:
                currentPos += 1
        case 1:
            if mazeArray[currentPos - width] == 1:
                print("Cannon't go to up from pos " + str(currentPos))
            else:
                currentPos -= width
        case 2:
            if mazeArray[currentPos - 1] == 1:
                print("Cannon't go to left from pos " + str(currentPos))
            else:
                currentPos -= 1
        case 3:
            if mazeArray[currentPos + width] == 1:
                print("Cannon't go to down from pos " + str(currentPos))
            else:
                currentPos += width
        case _:
            print("Incorrect direction")

def look(dir:int):   #0 = right, 1 up, 2 left, 3 down
    global currentPos
    match dir:
        case 0:
            return mazeArray[currentPos + 1]
        case 1:
            return mazeArray[currentPos - width]
        case 2:
            return mazeArray[currentPos - 1]
        case 3:
            return mazeArray[currentPos + width]
        case _:
            print("Incorrect direction")