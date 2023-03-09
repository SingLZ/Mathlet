from abc import ABC, abstractmethod
#from GradeLevel import GradeLevel, PreSchool
from dataclasses import dataclass

@dataclass
class Problem(ABC):
    Equation: str
    Steps: list | set
    GradeLevel: any
    Answer: float | str # includes inf/-inf
    CurrentStep = 0 # index in Steps

    def getCurrentStep(self):
        return self.Steps[self.CurrentStep]

    def advanceAndGet(self):
        CurrentStepData = self.getCurrentStep()
        self.CurrentStep += 1
        return CurrentStepData
    
    def isLastStep(self):
        return self.CurrentStep == len(self.Steps)-1
    
    def __repr__(self):
        string = self.Equation
        for step in self.Steps:
            string += "\n" + step
        string += "\n" + self.Answer
        return string

import random
def randomize():
    firstTerm = str(random.randint(1, 10)) # coefficient
    secondTerm = str(random.randint(1, 10)) # constant
    result = (6 - float(secondTerm)) / float(firstTerm)
    randomizedProblem = Problem(firstTerm + "x + " + secondTerm + " = 6", ['- ' + secondTerm, '/ ' + firstTerm], 'PreSchool', 'x = ' + str(result))
    return randomizedProblem

def manufactureArithmeticProblem():
    problem = Problem("2x + 3 = 7", [("-3", "2x + 3 - 3 = 7 - 3", "2x = 7 - 3", "2x = 4"), ("/2", "x = 4/2")], 'PreSchool', "x = 2")
    return problem

print(randomize())

# sample problem
if __name__ == "__main__":
    problem = manufactureArithmeticProblem()
    while not problem.isDone():
        print(problem.Equation)
        if input("type anything to go to next step > ").lower() == "quit":
            exit()
        step = problem.advanceAndGet()
        for i in range(1, len(step)):
            print(step[i])
    print(f"The solution is: {problem.Answer}")