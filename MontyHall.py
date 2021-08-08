import random
from random import seed, randint
import numpy

def game(winningdoor, selectdoor, change=False):
    assert winningdoor <3
    assert winningdoor >= 0

    removeddoor =  next(i for i in range(3) if i != selectdoor and i != winningdoor)

    if change:
        selectdoor = next(i for i in range(3) if i != winningdoor and i != removeddoor)

    return selectdoor == winningdoor

if __name__  == "__main__":
    playerdoor = numpy.random.random_integers(0,2,(1000*1000*1,))

    
    winningdoors = [d for d in playerdoor if game(1, d)]
    print("Winning percentage without changing choice: ", len(winningdoors) / len(playerdoor))

    winningdoors = [d for d in playerdoor if game(1, d, change=True)]
    print("Winning percentage while changing choice: ", len(winningdoors) / len(playerdoor))