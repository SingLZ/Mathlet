from dataclasses import dataclass

@dataclass
class Problem():
    Steps: list | set
    StepsData: list
    FalseSteps: list
    # FalseSteps needs to look like this:
    # [(wrongStep1, wrongStep2, wrongStep3), (...), ...]

    CurrentStep = 0 # index for Steps

    def getCurrentStep(self):
        return self.Steps[self.CurrentStep]

    def next(self):
        self.CurrentStep += 1
        return self.getCurrentStep()
    
    def getEquation(self):
        return self.Steps[0]

    def isAtAnswer(self):
        return self.CurrentStep == len(self.Steps)-1

    def isAtEquation(self):
        return self.CurrentStep == 0

    def getAnswer(self):
        return self.Steps[-1]
    
    def getCurrentFalseSteps(self):
        if not(self.isAtEquation() or self.isAtAnswer()): # if not equation nor answer
            return self.FalseSteps[self.CurrentStep]
        return None

    def getCurrentStepData(self):
        if not(self.isAtEquation() or self.isAtAnswer()): # if not equation nor answer
            return self.StepsData[self.CurrentStep]
        return None
    
    def reset(self):
        self.CurrentStep = 0

    def strToCurrentStep(self):
        string = self.getEquation()
        for step_index in range(1, self.CurrentStep+1):
            string += f'\n{self.Steps[step_index]}'
        return string

    def __iter__(self):
        self.CurrentStep -= 1
        while self.CurrentStep < len(self.Steps):
            yield self.next()

    def __repr__(self):
        string = ''
        for step in self.Steps:
            string += "\n" + step
        return string