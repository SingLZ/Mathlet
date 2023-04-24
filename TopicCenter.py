from backend.classes_data.problem import Problem
from backend.classes_data.ProblemSet import ProblemSet
from dataclasses import dataclass

@dataclass
class TopicCenter():
    sets: dict
    current_set: ProblemSet = None

    def getSet(self):
        return self.sets

    def selectSet(self, set_name: str):
        self.current_set = self.sets[set_name]

    def calculateCompositeCompletion(self): # average
        sum = 0
        total = 0
        for problemSet in self.sets:
            sum += problemSet.current
            total += len(problemSet.getProblems())
        
        return sum/total
    
from backend.classes_data.FractionProblems import problems
main = TopicCenter(
    {
        'Fractions': ProblemSet(
            problems[0]
        )
    }
)

'''
main = TopicCenter(
    {
        'Topic': ProblemSet(
            Problem(...),
            Problem(...),
            ...
        ),
        'MoreTopics': ProblemSet(
            ...
        )
    }
)
'''