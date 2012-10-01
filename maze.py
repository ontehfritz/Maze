#Author: Fritz (Fredrick Seitz) 
#Language Version: Python 
#Description:
#Creates and renders mazes to the console.

import dimension
import random

class Maze:
	OBSTICLE = -1
	START_LOC_VALUE = -2
	GOAL_LOC_VALUE = -3

	def __init__(self,x_size=0,y_size=0):
		self.x = x_size
		self.y = y_size
		self.startloc = dimension.Dimension2D(1,1)
		self.goalloc = dimension.Dimension2D(self.x-2,self.y-2)
		self.maze = []
		self.__fill()
   

	def getSizeX(self):
		"""
		Returns the width
		"""
		return self.x
    
	
	def getSizeY(self):
		"""
		Returns the Height
		"""
		return self.y

	
	def __fill(self):
		"""
		Internal method - Fill the field with zeros
		"""
		nums = []
		for _y in range(self.y):
			nums = []
			for _x in range(self.x):
				nums.append(0)

			self.maze.append(nums)
	
		
	def getValue(self,x_cor,y_cor):
		"""
		Gets the value at a specific coordinate
		"""	
		return self.maze[y_cor][x_cor]
		
	
	def setValue(self,x_cor,y_cor,value):
		"""
		Sets a value at specific coordinate
		"""
		self.maze[y_cor][x_cor] = value
	
	
	def setUpMaze(self):
		"""
		Generates a random maze
		"""
		ran = random.Random();
		ran.seed()
		for _y in range(self.y):
			self.maze[_y][0] = self.maze[_y][self.x-1] = self.OBSTICLE
		for _x in range(self.x):
			self.maze[0][_x] = self.maze[self.y-1][_x] = self.OBSTICLE
		
		_max = (self.x*self.y)/3
		for _r in range(_max):
			self.setValue(ran.randint(0,self.x-1),ran.randint(0,self.y-1),self.OBSTICLE)
			
		self.setValue(1,1,self.START_LOC_VALUE);
		self.setValue(self.x-2,self.y-2,self.GOAL_LOC_VALUE);
	
	
	def renderConsoleMaze(self):
		"""
		Prints the maze to the console
		"""
		for _y in range(self.y):
			for _x in range(self.x):
				if self.maze[_y][_x] == 0:
					print "O",
				elif self.maze[_y][_x] == -1:
					print "X",
				elif self.maze[_y][_x] == self.GOAL_LOC_VALUE:
					print "E",
				elif self.maze[_y][_x] == self.START_LOC_VALUE:
					print "S",
				else:
					print "#",
					
			print "\n"
			
