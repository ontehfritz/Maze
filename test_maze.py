#Description:
#Unit tests for the maze generator and both solvers. Run from the repo root:
#python3 -m unittest -v

import collections
import contextlib
import copy
import io
import random
import unittest

import dimension
import maze
import searchengine

PATH_VALUE = 3
SEEDS = range(10)


def _reachable(m, passable):
	"""
	Flood fill from the start to the goal through cells whose value is in passable.
	Independent of searchengine, so the solvers are not checked against themselves.
	"""
	start = (m.startloc.x, m.startloc.y)
	goal = (m.goalloc.x, m.goalloc.y)
	seen = {start}
	todo = collections.deque([start])
	while todo:
		x, y = todo.popleft()
		if (x, y) == goal:
			return True
		for nx, ny in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
			if (nx, ny) in seen:
				continue
			if not (0 <= nx < m.getSizeX() and 0 <= ny < m.getSizeY()):
				continue
			if m.getValue(nx, ny) in passable:
				seen.add((nx, ny))
				todo.append((nx, ny))
	return False


def _solvable_maze(seed):
	"""
	Seeds random and regenerates 20x10 mazes until one has a path from S to E.
	SearchEngine only supports 20x10 mazes.
	"""
	random.seed(seed)
	for _ in range(100):
		m = maze.Maze(20, 10)
		m.setUpMaze()
		if _reachable(m, {0, maze.Maze.GOAL_LOC_VALUE}):
			return m
	raise AssertionError("no solvable maze in 100 tries for seed %d" % seed)


class SolverTest(unittest.TestCase):

	def assertPathFromStartToGoal(self, original, final):
		start = original.startloc
		goal = original.goalloc
		self.assertEqual(final.getValue(start.x, start.y), maze.Maze.START_LOC_VALUE)
		self.assertEqual(final.getValue(goal.x, goal.y), maze.Maze.GOAL_LOC_VALUE)
		self.assertTrue(_reachable(final, {PATH_VALUE, maze.Maze.GOAL_LOC_VALUE}),
			"solved path does not connect S to E")
		for y in range(original.getSizeY()):
			for x in range(original.getSizeX()):
				if final.getValue(x, y) == PATH_VALUE:
					self.assertEqual(original.getValue(x, y), 0,
						"path cell (%d,%d) was not open in the maze" % (x, y))

	def test_depth_first_finds_path(self):
		for seed in SEEDS:
			with self.subTest(seed=seed):
				m = _solvable_maze(seed)
				s = searchengine.SearchEngine(copy.deepcopy(m))
				self.assertTrue(s.depthFirstSearch(dimension.Dimension2D(1, 1), 1))
				self.assertPathFromStartToGoal(m, s.getSearchPath())

	def test_breadth_first_finds_path(self):
		for seed in SEEDS:
			with self.subTest(seed=seed):
				m = _solvable_maze(seed)
				s = searchengine.SearchEngine(copy.deepcopy(m))
				self.assertTrue(s.breadthFirstSearch())
				self.assertPathFromStartToGoal(m, s.getSearchPath())


class RenderTest(unittest.TestCase):

	def test_render_format(self):
		m = maze.Maze(6, 3)
		for x in range(6):
			m.setValue(x, 0, maze.Maze.OBSTICLE)
			m.setValue(x, 2, maze.Maze.OBSTICLE)
		m.setValue(0, 1, maze.Maze.OBSTICLE)
		m.setValue(1, 1, maze.Maze.START_LOC_VALUE)
		m.setValue(3, 1, PATH_VALUE)
		m.setValue(4, 1, maze.Maze.GOAL_LOC_VALUE)
		m.setValue(5, 1, maze.Maze.OBSTICLE)

		out = io.StringIO()
		with contextlib.redirect_stdout(out):
			m.renderConsoleMaze()

		self.assertEqual(out.getvalue(),
			"X X X X X X \n\n"
			"X S O # E X \n\n"
			"X X X X X X \n\n")


if __name__ == "__main__":
	unittest.main()
