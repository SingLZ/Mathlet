from tokens import Token, TokenType

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
				pass # skip
			elif self.current_char == '.' or self.current_char.isdigit():
				yield self.generate_number()
			elif self.current_char == '+':
				yield Token(TokenType.PLUS)
			elif self.current_char == '-':
				yield Token(TokenType.MINUS)
			elif self.current_char == '*':
				yield Token(TokenType.MULTIPLY)
			elif self.current_char == '/':
				yield Token(TokenType.DIVIDE)
			elif self.current_char == '(':
				yield Token(TokenType.LPAREN)
			elif self.current_char == ')':
				yield Token(TokenType.RPAREN)
			#elif self.current_char.isalpha():
				
			else:
				raise Exception(f"Illegal character '{self.current_char}'")
			self.advance()

	def generate_number(self):
		decimal_flag = False
		num_str = self.current_char
		self.advance()
		
		while self.current_char != None and (self.current_char == "." or self.current_char.isdigit()):
			if self.current_char == ".":
				if decimal_flag:
					raise Exception("Multiple decimal points in one number.")
				decimal_flag = True
				number_str += self.current_char
				self.advance()

		if number_str.startswith('.'):
			number_str = '0' + number_str
		if number_str.endswith('.'):
			number_str += '0'
		
		return Token(TokenType.NUMBER, float(number_str))