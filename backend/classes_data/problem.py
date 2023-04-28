from dataclasses import dataclass

@dataclass
class Step():
    step: str
    result: str = None
    wrong_steps: set = None # (Step, Step, Step)
    feedback: str = ''

    def __repr__(self) -> str:
        return self.result

@dataclass
class Problem():
    Equation: str
    Steps: list | set

    CurrentStep = 0 # index for Steps

    def getCurrentStep(self) -> Step:
        return self.Steps[self.CurrentStep]
    
    def getCurrentWrongSteps(self) -> set:
        return self.getCurrentStep().wrong_steps
    
    def isAtAnswer(self):
        return self.CurrentStep == len(self.Steps)-1

    def strToCurrentStep(self):
        eq = self.getEquation()
        for step in range(0, self.CurrentStep + 1):
            eq += f'\n{self.Steps[step].result}'
        return eq

    def getEquation(self):
        return self.Equation
    
    def getAnswer(self):
        return self.Steps[len(self.Steps)-1].step

    def next(self):
        self.CurrentStep += 1
        return self.getCurrentStep()

    def reset(self):
        self.CurrentStep = 0
        return self.Equation

    def __iter__(self):
        self.CurrentStep -= 1
        while self.CurrentStep < len(self.Steps)-1:
            yield self.next()

    def __repr__(self) -> str:
        str = self.getEquation()
        for step in self:
            str += f'\n{step.result}'
        return str
    
# example implementation
'''
Problem(Equation='f(x)',
        Steps=Step(result='result', step='add 2 to both sides', feedback='GOOD JOB', 
            wrong_steps = (Step(step='+ 1 billion', feedback='you suck'), Step(...), Step(...))
            )
)
you don't need the Equation= or Steps=, you can just write it in order
'''