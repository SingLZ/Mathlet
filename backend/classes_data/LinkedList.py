class Node():
	# constructor
	def __init__(self, data, next = None):
		self.__data = data
		self.__next = next
	
	# getters
	def getData(self):
		return self.__data
	
	def getNext(self):
		return self.__next
	
	# setters
	def setData(self, d):
		self.__data = d

	def setNext(self, n):
		self.__next = n

	# for print
	def __str__(self):
		return str(self.getData())

class LinkedList():
	# constructor
	def __init__(self, *args):
		if args:
			current = self.__head
			for arg in args:
				if not isinstance(arg, Node):
					arg = Node(arg)
				if not current:
					self.__head = current
				else:
					current.next = arg
					current = arg
			self.__length = len(args)
		else:
			self.__head = None
			self.__length = 0
	
	# getter, check if head is None >> list is empty
	def isEmpty(self):
		return self.__head == None
	
	# setter, node to end of list
	def append(self, data):
		newNode = Node(data)
		if self.isEmpty(): # is empty: set head first
			self.__head = newNode
		else: # not empty, check for nodes after head without a next
			current = self.__head
			while current.getNext() != None:
				current = current.getNext()
			current.setNext(newNode)
		self.__length += 1
			
	# setter, remove node from linked list
	def remove(self, data):
		current = self.__head
		previous = None
		found = False
		
		# search item and mark as found, self.search is not used because "previous" needs to be accounted for
		while not found and current != None:
			if current.getData() == data:
				found = True
			else:
				previous = current
				current = current.getNext()
		
		if not found:  # case 1: empty list, case 2: not found in existing list
			return False # unsuccessful
		elif previous == None:
			self.__head = current.getNext()
		else:
			previous.setNext(current.getNext())
		self.__length -= 1
		return True # successful
	
	def search(self, data): # doesn't account for "previous", only that the node w/ the data exists, and to give it
		current = self.__head
		while current != None:
			current_data = current.getData()
			if current_data == data:
				return current_data
			current = current.getNext()
		return None
	
	def __getitem__(self, index): # add support for indexing
		if index < 0 or index > len(self) - 1:
			raise IndexError
		
		current = self.__head
		for i in range(index):
			current = current.getNext()
		return current.getData()
	
	# print(linkedList)
	def __str__(self):    
		mystr = ''
		current = self.__head
		
		while current != None:
			mystr += str(current)
			current = current.getNext()
		return mystr
	
	# length override, naive length implementation
	def __len__(self):    
		return self.__length