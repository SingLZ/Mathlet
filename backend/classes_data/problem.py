from dataclasses import dataclass

@dataclass
class Problem():
    Equation: str
    Steps: list | set
    CurrentStep = 0 # index for Steps

    def getCurrentStep(self):
        return self.Steps[self.CurrentStep]

    def getNextStep(self):
        CurrentStepData = self.getCurrentStep()
        self.CurrentStep += 1
        return CurrentStepData
    
    def isAnswer(self):
        return self.CurrentStep == len(self.Steps)-1

    def getAnswer(self):
        return self.Steps[-1]
    
    def reset(self):
        self.CurrentStep = 0

    def __iter__(self):
        self.CurrentStep -= 1
        while self.CurrentStep < len(self.Steps):
            yield self.getNextStep()

    def __repr__(self):
        string = self.Equation
        for step in self.Steps:
            string += "\n" + step
        return string