import random
from room import Room
import numpy as np
from path_generation import GraphNode
import pygame
import config

screen = None
renderables = []
assets = {}
background = None
point = [0,0]
flash = ("upFlash", "downFlash", "leftFlash", "rightFlash")
direction = 1

def update():
	global screen, renderables, background
	screen.fill((0,0,0))
	if background:
		screen.blit(background, point)
	
	screen.blit(load(flash[direction]), (0,0))
	
	for r in renderables:
		r.render(screen)
		
	pygame.display.flip()

def handler(event):
	global point, direction
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_UP:
			point[1] += config.dunMultiply
			direction = 0
		elif event.key == pygame.K_DOWN:
			point[1] -= config.dunMultiply
			direction = 1
		elif event.key == pygame.K_LEFT:
			point[0] += config.dunMultiply
			direction = 2
		elif event.key == pygame.K_RIGHT:
			point[0] -= config.dunMultiply
			direction = 3


def setMap(back = "map.png"):
	global background, point
	background = pygame.image.load('map.png')
	scale = 4
	background = pygame.transform.rotozoom(background, 0, scale)
	point = [(config.screenSize/2) - (scale * config.screenSize/2) - 16, (config.screenSize/2) - (scale * config.screenSize/2) - 16]


def register(renderable):
	global renderables
	if renderable not in renderables:
		renderables.append(renderable)
		
def loadFlash():
	global assets
	leftFlash = pygame.image.load("ellipse.png")
	assets["leftFlash"] = leftFlash
	assets["downFlash"] = pygame.transform.rotate(leftFlash, 90)
	assets["rightFlash"] = pygame.transform.rotate(leftFlash, 180)
	assets["upFlash"] = pygame.transform.rotate(leftFlash, 270)
	
		
def load(file):
	global assets
	if file in assets:
		return assets[file]
	else:
		image = pygame.image.load(file)
		assets[file] = image
		return image
		
def startGraphics():
    # Initialize graphics
 global screen
 pygame.display.init()
 screen = pygame.display.set_mode((config.screenSize, config.screenSize))
 return screen
	
def startEndRooms(screen, rooms): # Used to create the beginning and end points for the map
	red = (255,0,0)
	blue = (0,0,255)
	doorSize = config.dunMultiply * 2
	pygame.draw.rect(screen, red, (rooms[0].pos[0], rooms[0].pos[1], doorSize, doorSize), 0)
	pygame.draw.rect(screen, blue, (rooms[len(rooms) - 1].pos[0], rooms[len(rooms) - 1].pos[1], doorSize, doorSize), 0)


def displayRooms(screen, rooms): # Display rooms on the screen
    white=(255,255,255)
    for i in range(len(rooms)):
        pygame.draw.rect(screen, white, (rooms[i].pos[0], rooms[i].pos[1], rooms[i].width, rooms[i].length), 0)
        pygame.display.update()
		
def displayMST(screen, nodes):
	green = (0, 255, 0)
	for i in nodes:
		for j in i.edges:
			pygame.draw.line(screen, green, (i.room.pos + ((np.array([i.room.width, i.room.length])/2))), (j.pos + ((np.array([j.width, j.length])/2))))
			pygame.display.update()
			
def displayHalls(screen, nodes):
	white = (255,255,255)
	for i in nodes:
		for j in i.edges:
			above = False
			below = False
			right = False
			left = False
		
			if (i.room.shape.centerx < j.shape.left):
				right = True
			elif (i.room.shape.centerx > j.shape.right):
				left = True
				
			if (i.room.shape.centery > j.shape.bottom):
				above = True
			elif (i.room.shape.centery < j.shape.top):
				below = True
				
			if (right):
				if (above):
					pygame.draw.lines(screen, white, False, (i.room.shape.center, [j.shape.centerx, i.room.shape.centery], j.shape.center), config.dunMultiply + 2)
				elif (below):
					pygame.draw.lines(screen, white, False, (i.room.shape.center,[j.shape.centerx, i.room.shape.centery], j.shape.center), config.dunMultiply + 2)
				else:
					pygame.draw.line(screen, white, i.room.shape.center, (j.shape.left, i.room.shape.centery), config.dunMultiply + 2)
				
			elif (left):
				if (above):
					pygame.draw.lines(screen, white, False, (i.room.shape.center, [j.shape.centerx, i.room.shape.centery], j.shape.center), config.dunMultiply + 2)
				elif (below):
					pygame.draw.lines(screen, white, False, (i.room.shape.center, [j.shape.centerx, i.room.shape.centery], j.shape.center), config.dunMultiply + 2)
				else:
					pygame.draw.line(screen, white, i.room.shape.center, (j.shape.right , i.room.shape.centery), config.dunMultiply + 2)
					
			else:
				if (above):
					pygame.draw.line(screen, white, i.room.shape.center, (i.room.shape.centerx, j.shape.centery), config.dunMultiply + 2)
				else:
					pygame.draw.line(screen, white, i.room.shape.center, (i.room.shape.centerx, j.shape.centery), config.dunMultiply + 2)
					
			pygame.display.update()
