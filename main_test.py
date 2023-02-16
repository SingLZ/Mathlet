from intrepreter.lexer import Lexer
from intrepreter.parser import Parser
from intrepreter.intrepreter import Interpreter

if __name__ == "__main__":
    while True:
        test_input = input("enter > ")
        if test_input == "exit":
            exit()
        lexer = Lexer(test_input)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: 
            continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(tree, value)