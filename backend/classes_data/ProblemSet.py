from dataclasses import dataclass
from .problem import Problem

test = 2

class ProblemSet():
    problems: set
    current: int = 0

    def __init__(self, *args) -> None:
        if isinstance(args[0], set):
            if len(args) == 0:
                raise Exception('Problem set cannot be empty.')
            self.problems = args[0]
        else:
            self.problems = (args)
        self.current = 0

    def getProblems(self):
        return self.problems

    def getCurrentProblem(self): # may become deprecated
        return self.problems[self.current]

    def next(self): # may become deprecated
        if self.current == len(self.problems):
            return False
        self.current += 1
        return True
    
    def getCurrentProgress(self) -> float: # from 0 to 1 (float)
        return '%.02f' % self.current/len(self.problems)
    
    def cycle(self): # USE
        for index in range(0, len(self.problems)):
            self.current = index
            yield self.problems[index]