# Import Libraries
import numpy as np
from generate import generateRooms
from generate import moveRooms
from display import displayRooms
from display import startGraphics
from display import displayMST
from display import displayHalls
from room import Room
from path_generation import createMST
from path_generation import GraphNode

# Ge desired size
#size = int(input('Enter desired size: '))
# Scale it to a viewable size
size = 50000
screen = startGraphics()

# Generate Rooms
print("Generating Rooms")
rooms = generateRooms(size)
#displayRooms(screen, rooms)

# Move Rooms
print("Moving Rooms")
rooms = moveRooms(rooms)
displayRooms(screen, rooms)

# Connect Rooms
print("Connect Rooms")
halls = createMST(rooms)

displayMST(screen, halls)
	
displayHalls(screen, halls)
	
playing = True

while(playing):
    play = input("")
    if (play == 'q'):
        playing = False