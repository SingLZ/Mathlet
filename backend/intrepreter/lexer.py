from .tokens import Token, TokenType, Function
import math

class Lexer():
	def __init__(self, text: str):
		self.text = iter(text)
		self.advance()
		#self.current_char = None
	
	def advance(self):
		try:
			self.current_char = next(self.text)
		except StopIteration:
			self.current_char = None
		return self.current_char
		
	def generate_tokens(self):
		while self.current_char != None:
			if self.current_char.isspace():
				self.advance()
			elif self.current_char == '.' or self.current_char.isdigit():
				yield self.generate_number()
			elif self.current_char == '+':
				self.advance()
				yield Token(TokenType.PLUS)
			elif self.current_char == '-':
				self.advance()
				yield Token(TokenType.MINUS)
			elif self.current_char == '*':
				self.advance()
				yield Token(TokenType.MULTIPLY)
			elif self.current_char == '/':
				self.advance()
				yield Token(TokenType.DIVIDE)
			elif self.current_char == '^':
				self.advance()
				yield Token(TokenType.EXPONENT)
			elif self.current_char == '(':
				self.advance()
				yield Token(TokenType.LPAREN)
			elif self.current_char == ')':
				self.advance()
				yield Token(TokenType.RPAREN)
			elif self.current_char == '=':
				self.advance()
				yield Token(TokenType.EQUALS)
			elif self.current_char.isalpha():
				yield self.generate_word()
			else:
				raise Exception(f"Illegal character '{self.current_char}'")

	def generate_number(self):
		decimal_flag = False
		num_str = self.current_char
		self.advance()
		
		while self.current_char != None and (self.current_char == "." or self.current_char.isdigit()):
			if self.current_char == ".":
				if decimal_flag:
					break
				decimal_flag = True
			num_str += self.current_char
			self.advance()

		if num_str.startswith('.'):
			num_str = '0' + num_str
		if num_str.endswith('.'):
			num_str += '0'
		
		return Token(TokenType.NUMBER, float(num_str))
	
	def generate_word(self):
		word = self.current_char
		self.advance()

		while self.current_char != None and (self.current_char == '.' or self.current_char.isalpha()):
			word += self.current_char
			self.advance()

		if len(word) == 1:
			if word == 'e':
				return Token(TokenType.NUMBER, math.e)
			return Token(TokenType.VARIABLE, word)
		
		if word == 'pi':
			return Token(TokenType.NUMBER, math.pi)
		elif getattr(Function, word):
			return Token(TokenType.FUNCTION, getattr(math, word)) # placeholder for now, not meant to only use math
		
		return Token(TokenType.WORD, word)