import random
import time
	
class CantMove (Exception):
	def __init__(self, reason):
		self.reason = reason
	def __repr__(self):
		return "unable to find a move: {}".format(self.__reason)
		
		
class Nim :
	def __init__( self, startstate ) :
		self. state = startstate
		
	def __repr__( self ) :
		repr = ""
		i = 0
		while i < len(self.state):
			repr = repr + "{} :".format(i+1)
			num = self.state[i]
			i = i + 1
			while num > 0:
				repr = repr + " 1"
				num = num - 1 
			repr = repr + "\n"
			
		return repr
		
	def sum(self) :
		res = 0
		for num in self.state:
			res = res + num
			
		return res
		
	def nimber(self):
		res = 0
		for num in self.state:
			res = res ^ num
			
		return res
		
	def lastmorethantwo(self):
		count = 0
		for num in self.state:
			if num > 1:
				count = count + 1
		if count == 1:
			return True
		else:
			return False
	
	def askRow(self):
		row = input("Select a row: ")
		if self.isInt(row):
			row = int(row) - 1
			if row >= 0 and row < len(self.state):
				if self.state[row]>0:
					return row
				else:
					print("Row is empty\n")
					return self.askRow()
			else:
				print("Row does not exist\n")
				return self.askRow()
		else:
			print("Row index is expected to be a number\n")
			return self.askRow()
			
	def askLeave(self, row):
		leave = input("Select a number of sticks to leave: ")
		if self.isInt(leave):
			leave = int(leave)
			if leave >= 0 and leave < self.state[row]:
				return leave
			else:
				if leave == self.state[row]:
					print("removing sticks is obligatory\n")
					return self.askLeave(row)
				if leave < 0:
					print ("cannot remove more sticks than that is present\n")
					return self.askLeave(row)
					
				if leave > self.state[row]:
					print ("adding sticks to a row is illegal move\n")
					return self.askLeave(row)
		else:
			print("number of sticks to leave is expected to be a number\n")
			return self.askLeave(row)
		
	def removeSticks(self, row, leave):
		self.state[row] = leave
		
	def isInt(self, s):
		try:
			int(s)
			return True
		except ValueError:
			return False
	
	def randommove(self) :
		if self.sum() <= 0:
			raise CantMove("no sticks left")
		row = random.randrange(0, len(self.state))
		while (self.state[row] <= 0):
			row = random.randrange(0, len(self.state))
		leave = random.randrange(0, self.state[row])
		self.removeSticks(row, leave)
		
	def removelastmorethantwo (self):
		row = -1
		i = 0
		nonempty = len(self.state)
		for num in self.state:
			if num == 0:
				nonempty = nonempty - 1
			if num > 1:
				if row == -1:
					row = i
				else:
					raise CantMove("more than one row has more than one stick")
					
			i = i + 1
				
		if nonempty%2==0:
			self.removeSticks(row, 0)
		else:
			self.removeSticks(row, 1)
			
	def usermove (self):
		row = self.askRow()
		leave = self.askLeave(row)
		self.removeSticks(row, leave)
		
	def makenimberzero(self):
		nmb = self.nimber()
		while (True):
			r = random.randrange(0, len(self.state))
			if self.state[r] > 0:
				if self.state[r] ^ nmb < self.state[r]:
					self.state[r] = self.state[r] ^ nmb
					break
				
	def optimalmove(self):
		nmb = self.nimber()
		if self.lastmorethantwo():
			self.removelastmorethantwo()
		elif nmb != 0:
			self.makenimberzero()
		else:
			self.randommove()
			
def play( ) :
	st = Nim( [ 1, 2, 3, 4, 5, 6 ] )
	turn = 'user'
	while st. sum( ) > 1 :

		if turn == 'user' :
			print( "\n" )
			print( st )
			print( "hello, user, please make a move" )
			st. usermove( )
			turn = 'computer'
		else :
			print( "\n" )
			print( st )
			print( "now i will make a move\n" )
			print( "thinking" )
			for r in range( 15 ) :
				print( ".", end = "", flush = True )
				time. sleep( 0.1 )
			print( "\n" )
			st. optimalmove( )
			turn = 'user'
		print( "\n" )
	if turn == 'user' :
		print( "you lost\n" )
	else :
		print( "you won\n" )
			
				


	


	
		