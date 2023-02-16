from intrepreter.lexer import Lexer
from intrepreter.parser import Parser

if __name__ == "__main_test__":
    test_input = input("> ")
    lexer = Lexer(test_input)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    print(tree)