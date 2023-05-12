from dataclasses import dataclass
from typing import Callable

@dataclass
class NumberNode:
	value: any

	def __repr__(self):
		return f"{self.value}"
	
	def __neg__(self):
		return NumberNode(-self.value)

@dataclass
class AddNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}+{self.node_b})"

@dataclass
class SubtractNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}-{self.node_b})"

@dataclass
class MultiplyNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}*{self.node_b})"

@dataclass
class DivideNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}/{self.node_b})"
	
@dataclass
class ExponentNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}^{self.node_b})"
	
@dataclass
class FunctionNode:
	node: any
	func: Callable

	def __repr__(self):
		return f'{str(self.func)}({self.node})'

@dataclass
class PlusNode:
	node: any

	def __repr__(self):
		return f"(+{self.node})"
	
@dataclass
class MinusNode:
	node: any

	def __repr__(self):
		return f"(-{self.node})"