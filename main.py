# Import Libraries
import numpy as np
import config
import units
import display
import audio
import pygame

from generate import generateRooms
from generate import moveRooms
from display import displayRooms
from display import startGraphics
from display import displayMST
from display import displayHalls
from room import Room
from path_generation import createMST
from path_generation import GraphNode

config.init()

# Ge desired size
#size = int(input('Enter desired size: '))
# Scale it to a viewable size
screen = startGraphics()

# Generate Rooms
print("Generating Rooms")
rooms = generateRooms()
#displayRooms(screen, rooms)

# Move Rooms
print("Moving Rooms")
rooms = moveRooms(rooms)
displayRooms(screen, rooms)

# Connect Rooms
print("Connect Rooms")
halls = createMST(rooms)

#displayMST(screen, halls)
	
displayHalls(screen, halls)


pygame.image.save(screen, "map.png")
display.setMap()
# Begin working on game logic (and game loop)	

import event

player = units.player(500, 500)

display.register(player)

def quit(e):
	global playing
	if e.type == pygame.QUIT:
		playing = False
	elif e.type == pygame.KEYUP:
		if ((e.key == pygame.K_F4) and
		   (e.mod and pygame.KMOD_ALT)):
			playing = False
	
	
	
	
event.register(player.handler)
event.register(quit)
event.register(audio.handler)

audio.init()
clock = pygame.time.Clock()
playing = True

while(playing):

	clock.tick(30)

	event.update()
	player.update()
	display.update()
	
pygame.display.quit()