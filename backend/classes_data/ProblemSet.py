from dataclasses import dataclass
from .problem import Problem

class ProblemSet():
    problems: set
    current: int = 0
    high_score_index: int = 0

    def __init__(self, *args) -> None:
        if len(args) == 0:
            raise Exception("Cannot run problem set with no arguments.")
        new_args = []
        for arg in args:
            if isinstance(arg, set) or isinstance(arg, list):
                new_args.extend(tuple(arg))
            elif isinstance(arg, tuple):
                new_args.extend(arg)
            else:
                new_args.append(arg)
        self.problems = tuple(new_args) # becomes immutable
        self.current = 0

    def reset(self):
        self.current = 0

    def getProblems(self):
        return self.problems

    def getCurrentProblem(self):
        return self.problems[self.current]

    def next(self):
        if self.current == len(self.problems) - 1: # is last
            print('failed, is last (ProblemSet.py)')
            return False
        self.current += 1
        return True
    
    def save_score(self, num: int = None): # for saving
        if not num:
            num = self.current
            if self.getCurrentProblem().isAtAnswer():
                num += 1
        if 0 <= num <= len(self.problems):
            self.high_score_index = num
        else:
            raise IndexError(f"num = {num}")
    
    def get_high_score(self):
        return self.high_score_index
    
    def get_score(self):
        return self.high_score_index/len(self.getProblems())

    def getCurrentProgress(self) -> str: # from 0 to 1 (float)
        return '%.02f' % self.current/len(self.problems)
    
    def cycle(self):
        for index in range(0, len(self.problems)):
            self.current = index
            yield self.problems[index]