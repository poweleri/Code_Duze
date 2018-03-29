# Import Libraries
import numpy as np
import config
import units
import display
import audio
import pygame

from generate import *
from display import *
from room import Room
from path_generation import *

# This function will do all of the necessary loading
def loading():
	# Create the config settings for the game
	config.init()

	# Scale it to a viewable size
	screen = startGraphics()

	# Generate Rooms
	print("Generating Rooms")
	rooms = generateRooms()

	# Move Rooms
	print("Moving Rooms")
	rooms = moveRooms(rooms)
	displayRooms(screen, rooms)

	# Connect Rooms
	print("Connect Rooms")
	halls = createMST(rooms)
	displayHalls(screen, halls)
	# Used to debug pathing
	#displayMST(screen, halls)

	# Display which room is first and last
	startEndRooms(screen, rooms)

	# Save the generated map to an editable image
	pygame.image.save(screen, "map.png")
	display.setMap("map.png")


# Load the Map 
loading()

# Begin game and game loop
import event

playing = True

def quit(e):
	global playing
	if e.type == pygame.QUIT:
		playing = False
	elif e.type == pygame.KEYUP:
		if ((e.key == pygame.K_F4) and
		   (e.mod and pygame.KMOD_ALT)):
			playing = False

player = units.player(500, 500)
display.register(player)

event.register(player.handler)
event.register(quit)
event.register(audio.handler)

audio.init()
clock = pygame.time.Clock()
while(playing):

	clock.tick(30)

	event.update()
	player.update()
	display.update()
	
pygame.display.quit()
