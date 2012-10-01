#Author: Fritz (Fredrick Seitz) 
#Language Version: Python 
#Description:
#Runs the maze demos. Expand your console window so you can see both 
#maze solutions.

import maze
import searchengine
import dimension
import queue
import copy

solvable = False
m = maze.Maze(20,10)
m.setUpMaze()

m2 = copy.deepcopy(m)

#only show solvable mazes, scrap the junk mazes generated.
while(solvable != True):
	m = maze.Maze(20,10)
	m.setUpMaze()

	m2 = copy.deepcopy(m)

	s = searchengine.SearchEngine(m)
	loc = dimension.Dimension2D(1,1)
	
	solvable = s.depthFirstSearch(loc,1)
	

print "Depth First Search"
s.getSearchPath().renderConsoleMaze()

print ""
print "Breadth First Search"

s = searchengine.SearchEngine(m2)
s.breadthFirstSearch()
s.getSearchPath().renderConsoleMaze()

