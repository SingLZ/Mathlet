from dataclasses import dataclass

@dataclass
class Step():
    result: str
    step: str
    wrong_steps: set # (str, str, str)
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