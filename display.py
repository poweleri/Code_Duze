import random
import numpy as np
from room import Room
from path_generation import GraphNode
import pygame
import config

screen = None
renderables = []
assets = {}
background = None
point = [0,0]

def update():
	global screen, renderables, background
	screen.fill((0,0,0))
	if background:
		screen.blit(background, point)
	
	for r in renderables:
		r.render(screen)
		
	pygame.display.flip()

def handler(event):
	global point
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_UP:
			point[1] += 1
		elif event.key == pygame.K_DOWN:
			point[1] -= 1
		elif event.key == pygame.K_LEFT:
			point[0] += 1
		elif event.key == pygame.K_RIGHT:
			point[0] -= 1



def setMap(back = "map.png"):
	global background, point
	background = pygame.image.load('map.png')
	# background = pygame.transform.rotozoom(background, 0, 2.5)
	# point = [background.get_rect().center[0], background.get_rect().center[1]]

def register(renderable):
	global renderables
	if renderable not in renderables:
		renderables.append(renderable)
		
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
					pygame.draw.lines(screen, white, False, (i.room.shape.midright, [j.shape.centerx, i.room.shape.centery], j.shape.midbottom), 3)
				elif (below):
					pygame.draw.lines(screen, white, False, (i.room.shape.midright,[j.shape.centerx, i.room.shape.centery], j.shape.midtop), 3)
				else:
					pygame.draw.line(screen, white, i.room.shape.midright, (j.shape.left, i.room.shape.centery), 3)
				
			elif (left):
				if (above):
					pygame.draw.lines(screen, white, False, (i.room.shape.midleft, [j.shape.centerx, i.room.shape.centery], j.shape.midbottom), 3)
				elif (below):
					pygame.draw.lines(screen, white, False, (i.room.shape.midleft, [j.shape.centerx, i.room.shape.centery], j.shape.midtop), 3)
				else:
					pygame.draw.line(screen, white, i.room.shape.midleft, (j.shape.right, i.room.shape.centery), 3)
					
			else:
				if (above):
					pygame.draw.line(screen, white, i.room.shape.midtop, (i.room.shape.centerx, j.shape.bottom), 3)
				else:
					pygame.draw.line(screen, white, i.room.shape.midbottom, (i.room.shape.centerx, j.shape.top), 3)
			# extraRight = False
			# extraLeft = False
		
			# if (i.room.shape.centerx < j.shape.left):
				# print("Neighbor is to the right")
				# pygame.draw.rect(screen, white, (i.room.shape.midright, (j.shape.left - i.room.shape.right, 10)))
				# extraRight = True
				# # points.append([i.room.pos[0] + i.room.width, y])
				# # points.append([i.room.pos[0] + i.room.width, y + 20])
				# # points.append([i.room.pos[0] + j.width, y])
				# # points.append([i.room.pos[0] + j.width, y + 20])
				
			# elif (i.room.shape.centerx > j.shape.right):
				# print("Neighbor is to the left")
				# pygame.draw.rect(screen, white, (j.shape.midright, (i.room.shape.left - j.shape.right, 10)))
				# extraLeft = True
				# # pygame.draw.rect(screen, white, (j.pos[0] + (j.width / 2.0), y, j.pos[0] + (j.width / 2.0) - i.room.width, 10))
			# else:
				# print("Neighbor matches on x-axis")
				
				
			# if (i.room.shape.centery < j.shape.bottom):
				# print("Neighbor is below")
				# if (extraRight):
					# pygame.draw.rect(screen, white, (j.shape.left, i.room.shape.centery, (j.shape.centerx - j.shape.left), 10))
					# pygame.draw.rect(screen, white, (j.shape.midbottom, (10, i.room.shape.centerx - j.shape.bottom)))
				# elif (extraLeft):
					# pygame.draw.rect(screen, white, (j.shape.centery, i.room.shape.centery, (j.shape.right - j.shape.centerx), 10))
					# pygame.draw.rect(screen, white, (j.shape.midbottom, (10, i.room.shape.centerx - j.shape.bottom)))
				# else:
					# pygame.draw.rect(screen, white, (j.shape.midbottom, (10, i.room.shape.top - j.shape.bottom)))
					
			# elif (i.room.shape.centery > j.shape.top):
				# print("Neighbor is above")
				# if (extraRight):
					# pygame.draw.rect(screen, white, (j.shape.left, i.room.shape.centery, (j.shape.centerx - j.shape.left), 10))
					# pygame.draw.rect(screen, white, (j.shape.midtop, (10, j.shape.top - i.room.shape.centerx)))
				# elif (extraLeft):
					# pygame.draw.rect(screen, white, (j.shape.centery, i.room.shape.centery, (j.shape.right - j.shape.centerx), 10))
					# pygame.draw.rect(screen, white, (j.shape.midtop, (10, j.shape.top - i.room.shape.centerx)))
				# else:
					# pygame.draw.rect(screen, white, (j.shape.midtop, (10, j.shape.top - i.room.shape.bottom)))
			# # if (y > j.pos[1]):
				# # 
			# # elif (y < j.pos[1] + j.length):
				# # print("Neighbor is above")
			# # else:
				# # print("Neighbor matches on y-axis")
				
			pygame.display.update()
