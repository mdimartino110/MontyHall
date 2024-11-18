import random

def montyHall(iterations, doors, willSwitch):
    i = 0
    winCount = 0
    for i in range(0,iterations):
        winningDoor = random.randint(1,doors)
        doorChoice = random.randint(1,doors)
        if doorChoice == winningDoor:
            win = True
        else:
            win = False

        if willSwitch:
            win = not win
        
        if win:
            winCount += 1

    return("Simulated Winning Chance: "+str(winCount / iterations * 100)+"%")

def main():
    print(montyHall(10000, 3, True))

main()
