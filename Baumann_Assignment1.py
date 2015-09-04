#Jennifer Baumann
#Due 9/4/15
#AI Assignment 1

#Github username: jeba1858

#Queue implementation
#Used python documentation found @ https://docs.python.org/2.7/library/queue.html?highlight=queue#module-Queue
import Queue

q = Queue.Queue
for i in range(10):
	q.put(i)

while not q.empty:
	print q.get

#Stack implementation
class stack():
	def __init__(self):
		self.items =[]
	def checkSize():
		return self.items == []
	def push(self, item):
		return self.items.append(i)
	def pop(self):
		return self.items.pop()
	def getElements(self):
		return self.items

#Binary Tree
class node():
	def __init__(self, value):
		 self.leftChild =None
		 self.rightChild = None
		 self.parent = None
		 self.integerKey = value
class BinaryTree(Node):
	def __init__(self, RValue):
		self.root = RValue
	def add(self,value, parentValue):
		self = lookup(parentValue)
		if self is none:
			print "Parent not found"
		if self.left is none:
			self.left = value
			self.left.parent = self
		elif self.right is none:
			self.right = value
			self.right.parent = self
		else:
			print "parent has two children, node not added"
	def lookup(self,value):
		if value is not self.integerKey:
			lookup(self.left)
			lookup(self.right)
		elif value is self.integerKey:
			return self
		else:
			return none
	def delete(self, value)
