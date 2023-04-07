from .nodes import *
from .nodes import NumberNode as Number

class Interpreter:
	def __init__(self, optionalNode = None):
		if optionalNode:
			return self.visit(optionalNode)

	def visit(self, node):
		method_name = f'visit_{type(node).__name__}'
		method = getattr(self, method_name)
		return method(node)
		
	def visit_NumberNode(self, node):
		return Number(node.value)

	def visit_AddNode(self, node):
		return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

	def visit_SubtractNode(self, node):
		return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

	def visit_MultiplyNode(self, node):
		return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

	def visit_DivideNode(self, node):
		return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
	
	def visit_PlusNode(self, node):
		return Interpreter.visit_NumberNode(self, node.node)
	
	def visit_MinusNode(self, node): # double recursion forward technique
		current = node
		while True: # check next node to negate, if unavailable, check next node to be positive, if unavailable, repeat cycle
			current = current.node
			if isinstance(current, NumberNode):
				return Number(-current.value)
			else:
				current = current.node
				if isinstance(current, NumberNode):
					return Number(current.value)
		# note: recursion was tested to be up to 3x slower than this implementation
		# negative counter was up to 1.5x slower + boolean variable switching was 10% slower (approx.)