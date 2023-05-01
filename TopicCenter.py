from backend.classes_data.problem import Problem
from backend.classes_data.ProblemSet import ProblemSet
from dataclasses import dataclass

@dataclass
class TopicCenter():
    def __init__(self, sets: dict):
        self.sets = sets
        self.current_set: ProblemSet = None
        self.topic_access_cache = {}

    def getCurrentSet(self):
        return self.current_set

    def getSets(self) -> dict:
        return self.sets

    def selectSet(self, set_name: str) -> ProblemSet:
        self.current_set = self.sets[set_name]
        self.topic_access_cache[set_name] = True
        return self.current_set

    def cycleProblems(self):
        return self.current_set.cycle()
    
    def getCurrentProblem(self):
        return self.getCurrentSet().getCurrentProblem()
    
    def saveAndGet(self):
        for set in self.topic_access_cache:
            set.save_score()
        print("Saved, progress is: " + self.calculateCompositeCompletion())
        return self.sets

    def load(self, sets: dict):
        self.sets = sets

    def calculateCompositeCompletion(self) -> str: # average
        sum = 0
        total = 0
        for problemSet in self.sets:
            sum += problemSet.current
            total += len(problemSet.getProblems())
        
        return "%.02f" % sum/total
    
from backend.classes_data.FractionProblems import problems
main = TopicCenter(
    sets={
        'Fractions': ProblemSet(
            problems[0] # add here
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