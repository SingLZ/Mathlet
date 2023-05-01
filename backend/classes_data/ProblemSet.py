from dataclasses import dataclass
from .problem import Problem

class ProblemSet():
    problems: set
    current: int = 0
    high_score_index: int = 0

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

    def getCurrentProblem(self):
        return self.problems[self.current]

    def next(self):
        if self.current == len(self.problems):
            return False
        self.current += 1
        return True
    
    def save_score(self, num: int = None): # for saving
        if not num:
            num = self.current 
        if 0 <= num <= len(self.problems):
            self.high_score_index = num
        raise IndexError
    
    def getCurrentProgress(self) -> str: # from 0 to 1 (float)
        return '%.02f' % self.current/len(self.problems)
    
    def cycle(self):
        for index in range(0, len(self.problems)):
            self.current = index
            yield self.problems[index]