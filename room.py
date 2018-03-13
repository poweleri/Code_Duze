import random
import pygame
import numpy as np

class Room:
    def __init__(self):#Create a new room
        # Each room when created has a random size between 2 and 10
        self.length = random.randrange(2,11) * 20
        self.width = random.randrange(2,11) * 20
        # The starting positions are 0 and 0
        self.pos = np.array([500,500])
        self.shape = pygame.Rect(self.pos, (self.width, self.length))

    def pushOut(self):#Push the room outwards from center
        r = random.randrange(1,3)
        move = 0
        if (r == 1): # Push horizontal
            if (self.shape.x < 500):
                move = -1
            elif (self.shape.x > 500):
                move = 1
            elif(self.shape.x == 500):
                z = random.randrange(1,3)
                if (z == 1): # Go negative
                    move = -1
                elif(z==2): # Go positive
                    move = 1
            move *= 20
            self.pos[0] += move
            self.shape = self.shape.move([move, 0])
        elif (r == 2): # push vertical
            if (self.shape.y < 500):
                move = -1
            elif (self.shape.y > 500):
                move = 1
            elif(self.shape.y == 500):
                z = random.randrange(1,3)
                if (z == 1): # Go negative
                    move = -1
                elif(z==2): # Go positive
                    move = 1
            move *= 20
            self.pos[1] += move
            self.shape = self.shape.move([0, move])

    def roomInfo(self):# Output all attributes of the room. Used for Debugging
        print("---Room Info---")
        print("Length " + str(self.length))
        print("Width " + str(self.width))
        print("Position " + str(self.pos))
        print("")

    