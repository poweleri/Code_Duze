import numpy as np
import random
import config
from room import Room

def generateRooms(): # Create the needed number of Rooms
    area = 0
    rooms = []
    while(area < config.dunSize): # Stop generating when we reach the requested area
        room = Room()
        if (area == 0):
            room.firstRoom()
            rooms = [room]
        else:
            rooms.append(room)
        area  += (room.width * room.length)
        #room.roomInfo()
    return rooms

# This function will ensure the room spaced out
def moveRooms(rooms):

    # Must loop through every room except the first one.
    for i in range(1, len(rooms)):
        # Each room will push out a random amount of times. 0-5
        push = random.randrange(0,1)

        while(push > -1):
        # We also push out everytime there is an overlap detected
        # Checking for overlap we look at each room before the current room
            for z in range(i):
                overlap = rooms[i].shape.colliderect(rooms[z].shape)
                # if there is an overlap we need to push an extra time.
                if(overlap):
                    push += 1
                    break# Exit for loop
            
            rooms[i].pushOut()
            push -= 1

    return rooms
