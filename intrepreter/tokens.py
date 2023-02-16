from dataclasses import dataclass
from enum import Enum

class Operator(Enum):
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    EXPONENT = "^"
    MOD = "%"

class TokenType(Enum):
    NUMBER = 0,
    PLUS = 1,
    MINUS = 2,
    MULTIPLY = 3,
    DIVIDE = 4,
    LPAREN = 5,
    RPAREN = 6,
    EXPONENT = 7,
    MOD = 8,


@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")