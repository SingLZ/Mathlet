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
        pass

    def generate_number(self):
        decimal_flag = False
        num_str = self.current_char
        self.advance()
        
        while self.current_char != None and (self.current_char == "." or self.current_char.isdigit()):
            if self.current_char == ".":
                decimal_flag = True
                number_str += self.current_char
			    self.advance()