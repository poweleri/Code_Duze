import numpy as np
import random
from room import Room

def generateRooms(size): # Create the needed number of Rooms
    area = 0
    rooms = []
    while(area < size): # Stop generating when we reach the requested area
        room = Room()
        if (area == 0):
            rooms = [room]
        else:
            rooms.append(room)
        area  += (room.width * room.length)
        #room.roomInfo()
    return rooms

def moveRooms(rooms):# Move Rooms into correct positions
    for i in range(1, len(rooms)):
        for z in range(i): # Check all rooms before it
            #print(z)
            overlapping = rooms[i].shape.colliderect(rooms[z].shape)
            contains = rooms[i].shape.contains(rooms[z].shape)
            while (overlapping or contains):# If overlapping push it out.
                print("Overlap Detected " + str(i) + " " + str(z))
                rooms[i].pushOut()
                overlapping = rooms[i].shape.colliderect(rooms[z].shape)
                contains = rooms[i].shape.contains(rooms[z].shape)
                
        # Push out a random amount of times to create spacing.abs
        push = random.randrange(1,6)
        for w in range(push):
            rooms[i].pushOut()
			

      	for z in range(i): # Check all rooms before it
            #print(z)
            overlapping = rooms[i].shape.colliderect(rooms[z].shape)
            contains = rooms[i].shape.contains(rooms[z].shape)
            while (overlapping or contains):# If overlapping push it out.
                print("Overlap Detected " + str(i) + " " + str(z))
                rooms[i].pushOut()
                overlapping = rooms[i].shape.colliderect(rooms[z].shape)
                contains = rooms[i].shape.contains(rooms[z].shape)
    return rooms
