#Author: Fritz (Fredrick Seitz) 
#Language Version: Python
#Description:
#contains the two search algorithms DepthFirstSearch and
#BreadthFirstSearch. 


import dimension
import maze
import copy
import queue


class SearchEngine:
	"""
	This class accepts a maze as an arguement, if one is not provided it creates a default maze.
	"""
	def __init__(self,newMaze = maze.Maze()):
		self.searchPath = []
		self.maze = newMaze
		self.finalMaze = copy.deepcopy(newMaze)
		self.maxDepth = 0
		self.startLoc = self.maze.startloc
		self.goalLoc = self.maze.goalloc
		self.searchPath = []
		
		for i in range(20*10):
			self.searchPath.append(dimension.Dimension2D())  
			
		self.searchPath[0] = dimension.Dimension2D(1,1)
		self.isSearching = True
		

	def equals(self,d1,d2):
		"""
		Check if two dimensions are equal
		"""
		return d1.equals(d2)
	
	def getPossibleMoves(self,loc):			
		"""
		This method gets all possible moves from a specified location, max moves can only be four
		"""
		dim = []
		x = loc.getX()
		y = loc.getY()
		
		if(self.maze.getValue(x,y + 1) == 0 or self.maze.getValue(x,y + 1) == maze.Maze.GOAL_LOC_VALUE):
			d = dimension.Dimension2D(x,y + 1)
			dim.append(d)
			
		if(self.maze.getValue(x,y - 1) == 0 or self.maze.getValue(x,y - 1) == maze.Maze.GOAL_LOC_VALUE):
			d = dimension.Dimension2D(x,y - 1)
			dim.append(d)
	
		if(self.maze.getValue(x + 1,y) == 0 or self.maze.getValue(x + 1,y) == maze.Maze.GOAL_LOC_VALUE):
			d = dimension.Dimension2D(x + 1,y)
			dim.append(d)
		
		if(self.maze.getValue(x - 1,y) == 0 or self.maze.getValue(x -1,y) == maze.Maze.GOAL_LOC_VALUE):
			d = dimension.Dimension2D(x-1,y)
			dim.append(d)
		
		return dim
		

	def depthFirstSearch(self,loc,depth):
		"""
		Recursive depth first algorithm
		"""
		
		if(self.isSearching == False): 
			return True
		
		self.maze.setValue(loc.x,loc.y,depth)
		moves = self.getPossibleMoves(loc)
		
		for move in moves:	
			self.searchPath[depth] = move

			if(self.equals(move,self.goalLoc)):
				self.isSearching = False
				self.maxDepth = depth 
				return True
			else:
				self.depthFirstSearch(move,depth+1)
				
				if(self.isSearching == False):
					return True
					
		return False
		
	
	def breadthFirstSearch(self):
		"""
		Track of all the visted nodes to avoid over searching. Also use a queue to help the predecessor 
		list obtain the shortest path.
		
		After each node has been visited and we have completed getting the predecessors. 
		We build our search path.
		"""	
		alreadyVisited = []
		predecessor = []
		dimqueue = queue.Queue()
		
		nones = []
		bools = []
		
		for y in range(self.maze.y):
			nones = []
			bools = []
			for x in range(self.maze.x):
				nones.append(None)
				bools.append(False)

			predecessor.append(nones)
			alreadyVisited.append(bools)
	
		alreadyVisited[self.startLoc.y][self.startLoc.x] = True
		dimqueue.push(self.startLoc)
		success = False
		
		while(dimqueue.isEmpty() == False):
		 
			dim = dimqueue.peek()
			
			if(dim == None):
				break
				
			moves = self.getPossibleMoves(dim)
			
			for move in moves:
				x = move.getX()
				y = move.getY()
				
				if(alreadyVisited[y][x] == False):
					alreadyVisited[y][x] = True
					predecessor[y][x] = dim
					dimqueue.push(move)
					if(self.equals(move,self.goalLoc)):
						success = True
						break
				
			dimqueue.pop() 
			
		maxDepth = 0
		if(success):
			self.searchPath[maxDepth] = self.goalLoc
			maxDepth = maxDepth + 1
			for i in range(20*10):
				self.searchPath[maxDepth] = predecessor[self.searchPath[maxDepth-1].getY()][self.searchPath[maxDepth-1].getX()]
				maxDepth = maxDepth + 1
				if(self.equals(self.searchPath[maxDepth-1],self.startLoc)):
					break
					
		self.maxDepth = maxDepth   
		if(maxDepth > 0):       		
			return True
		else:
			return False
		
	
	def getSearchPath(self):
		"""
		Applies the search path to the final output maze and returns this maze.
		"""
		for i in range(self.maxDepth):
			pathDimension = self.searchPath[i]
			
			if(pathDimension.x != 0 and pathDimension.y != 0):
				if(pathDimension.x == self.startLoc.x and pathDimension.y == self.startLoc.y):
					self.finalMaze.setValue(pathDimension.x,pathDimension.y,-2);
				elif(pathDimension.x == self.goalLoc.x and pathDimension.y == self.goalLoc.y):
					self.finalMaze.setValue(pathDimension.x,pathDimension.y,-3);
				else:
					self.finalMaze.setValue(pathDimension.x,pathDimension.y,3);
				
		return self.finalMaze
			

			
		
