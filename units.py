import pygame
import display

class unit(object):
	def __init__ (self, x, y):
		self.x = x
		self.y = y
		self.frame = 1.0
		
class player (unit):
	def __init__(self, x, y):
		super (player, self).__init__(x, y)
		self.spritesheet = display.load("human_base.png")
		self.mapping = {
			"up"   : createTupleList(0) ,
			"right": createTupleList(18),
			"down" : createTupleList(36),
			"left" : createTupleList(54)
		}
		self.facing = "down"
		self.speed = 0.5
		self.moving = False
		
	def update(self):
		if self.moving:
			self.frame = (self.frame + self.speed) % 4
		
	def render(self, surface):
		surface.blit(self.spritesheet, 
			         (500, 500, 16, 16),
					 self.mapping[self.facing][int(self.frame)])
	
	def handler(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				# self.y -= 1
				# if self.y < 0:
					# self.y = 0
				self.facing = "up"
			elif event.key == pygame.K_DOWN:
				# self.y += 1
				# if self.y > (999 - 16):
					# self.y = 999 - 16
				self.facing = "down"
			elif event.key == pygame.K_LEFT:
				# self.x -= 1
				# if self.x < 0:
					# self.x = 0
				self.facing = "left"
			elif event.key == pygame.K_RIGHT:
				# self.x += 1
				# if self.x > (999 - 16):
					# self.x = 999 - 16
				self.facing = "right"
			self.moving = True
			
		elif event.type == pygame.KEYUP:
			self.moving = False
			self.frame = 1
					
def createTupleList(num):
	list = []
	for i in range(3):
		list.append((16 * i, num , 16, 18))
	list.append((16, num, 16, 18))
	return list