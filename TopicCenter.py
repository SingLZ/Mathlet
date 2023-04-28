from backend.classes_data.problem import Problem
from backend.classes_data.ProblemSet import ProblemSet
from dataclasses import dataclass

@dataclass
class TopicCenter():
    sets: dict
    current_set: ProblemSet = None

    def getSets(self) -> dict:
        return self.sets

    def selectSet(self, set_name: str) -> ProblemSet:
        self.current_set = self.sets[set_name]
        return self.current_set

    def cycleProblems(self):
        return self.current_set.cycle()

    def calculateCompositeCompletion(self) -> float: # average
        sum = 0
        total = 0
        for problemSet in self.sets:
            sum += problemSet.current
            total += len(problemSet.getProblems())
        
        return sum/total
    
from backend.classes_data.FractionProblems import problems
main = TopicCenter(
    sets={
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

if __name__ == "__main__":
    main.selectSet('Fractions')
    for i in main.cycleProblems():
        print(i)