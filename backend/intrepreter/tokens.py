from dataclasses import dataclass
from enum import Enum
import math

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
    FUNCTION = 9,
    WORD = 10,
    EQUALS = 11,
    VARIABLE = 12

class Function(Enum):
    sin = 1
    cos = 2
    tan = 3
    asin = 4
    acos = 5
    atan = 6
    sqrt = 7
    ln = 8

@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")