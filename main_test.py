from intrepreter.lexer import Lexer
from intrepreter.parser import Parser
from intrepreter.intrepreter import Interpreter

#import classes_data.problem # to be used later
#import classes_data.GradeLevel

import tkinter as tk
#

if __name__ == "__main__":
    tkinter_flag = False
    while True:
        test_input = input("enter > ").lower()
        if test_input == "exit" or test_input == "quit":
            exit()
        lexer = Lexer(test_input)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: 
            continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        text = f"tree: {tree}; computed result: {value}"
        if tkinter_flag:
            root = tk.Tk()
            label = tk.Label(root, text=text, font=("Arial", 72))
            label.pack()

            root.mainloop()
        else:
            print(text)