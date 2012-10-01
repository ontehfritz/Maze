#Author: Fritz (Fredrick Seitz) 
#Language Version: Python
#Description:
#A simple queue class. 

class Queue:
	def __init__(self):
		self.q = []
	
	def push(self,obj):
		self.q.append(obj)
	
	def pop(self):
		return self.q.pop(0)
		
	def peek(self):
		return self.q[0]
		
	def isEmpty(self):
		if(len(self.q) > 0):
			return False
		else:
			return True
			
	def size(self):
		return len(self.q)
	
