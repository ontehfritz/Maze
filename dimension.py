#Author: Fritz (Fredrick Seitz) 
#Language Version: Python
#Description:
#Two classes used to create coordinates in 2D or 3D space.

class Dimension2D:
	"""Default coordinate creation"""
	def __init__(self,x_cor=0,y_cor=0):
		self.x = x_cor
		self.y = y_cor
	
	def equals(self,other):
		"""
		Compares two coordinates
		"""
		if self.x != other.x:
			return False
		if(self.y != other.y):
			return False
			
		return True
		
	
	def getX(self):
		"""
		Get the x coordinate
		"""
		return self.x

	def getY(self):
		"""
		Get the Y coordinate
		"""
		return self.y
		
class Dimension3D:
	def __init__(self,x_cor=0,y_cor=0,z_cor=0):
		self.x = x_cor
		self.y = y_cor
		self.z = z_cor
	
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def getZ(self):
		return self.z
