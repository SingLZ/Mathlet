import sys
import intrepreter.lexer as lexer
import intrepreter.parser as parser

Lexer = lexer.Lexer
Parser = parser.Parser

if __name__ == "__main_test__":
    test_input = input("enter > ")
    lexer = Lexer(test_input)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    print(tree)