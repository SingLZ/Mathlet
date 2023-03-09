from problem import Problem
from random import randint, choice
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass

@dataclass
class GradeLevel(ABC):
    @staticmethod
    @abstractmethod
    def problems() -> list:
        pass
    
    def pickRandomProblem(self, problemsList: list = None):
        getProblems = problemsList or self.problems()
        lenOfProblems = len(getProblems)
        if not getProblems or lenOfProblems == 0:
            raise IndexError("There are no problems to randomly index.")
        return getProblems[randint(0, lenOfProblems)]

def factors(x: int):
    results = []
    i = 1
    while i*i <= x: # up to sqrt(a); small optimization by not using sqrt
        if x%i == 0: # is divisible
            results.append(i)
            if x//i != i: # because a may be a square of some number, example: 4^2 = 16 = 4*4
                results.append(x//i)
        i += 1
    return results

# example:
class PreSchool(GradeLevel):
    def problems(): # used as an attribute but can be modified to liking
        return [
            
        ]
    
    def makeRandomProblem(self, maxMultiplier: int = None): # maxMultiplier must be <= maxInteger
        operator = choice(("+", "-", "*", "/")) # lazy implementation
        maxInteger = 10 # set to whatever you want >= 1
        a = randint(1, maxInteger)
        b = None
        if operator == "/" and maxInteger >= 2:
            b = a == 1 and 1 or choice(factors(a))
        elif maxMultiplier and operator == "*":
            b = randint(1, maxMultiplier)
        else:
            b = randint(1, maxInteger)
        if operator == "-" and b > a: # exclude negatives for preschoolers
            a, b = b, a # tuple unpack swap
        problem = f'{a} {operator} {b}'
        # have to convert result into int because it's by default in float form (1.0)
        return Problem(problem, [], PreSchool, int(eval(problem))) # eval for laziness, as the argument is not user-input anyways
    
    def getRandomizedProblems(self, length: int) -> Problem: # recyclable for integer arithmetic
        problems = [None]*length
        for index in range(0, length):
            def recurseGetProblem(problem = self.makeRandomProblem()):
                if problem in problems:
                    recurseGetProblem(self.makeRandomProblem())
                return problem
            problems[index] = recurseGetProblem()
        return problems

if __name__ == "__main__": # for testing
    while True:
        inp = input("run > ")
        if not inp or inp.isspace() or inp.lower() == "quit" or inp.lower() == "exit":
            exit()
        try:
            inp = int(inp)
            if inp > 500: # limit
                raise ValueError
        except ValueError:
            pass
        for problem in PreSchool().getRandomizedProblems(isinstance(inp, int) and inp or 3):
            print(problem.Equation, "=", problem.Answer)