from backend.classes_data.problem import Problem
from backend.classes_data.ProblemSet import ProblemSet
from dataclasses import dataclass
import pickle

data_file_name = 'data.pickle'

@dataclass
class TopicCenter():
    def __init__(self, sets: dict):
        self.sets = sets
        self.current_set: ProblemSet = None
        self.topic_access_cache = []

    def getCurrentSet(self):
        return self.current_set

    def getSets(self) -> dict:
        return self.sets

    def selectSet(self, set_name: str) -> ProblemSet:
        self.current_set = self.sets[set_name]
        try:
            self.topic_access_cache.index(set_name)
        except ValueError:
            self.topic_access_cache.append(set_name)
        return self.current_set

    def cycleProblems(self):
        return self.current_set.cycle()
    
    def getCurrentProblem(self) -> Problem:
        return self.getCurrentSet().getCurrentProblem()
    
    def cache_scores(self): # overwrite data but not to file
        for set_name in self.topic_access_cache:
            if self.sets[set_name].get_score() != 0:
                print('NOT 0:', self.sets[set_name].get_score())
            elif self.sets[set_name].current != 0:
                print('but the current is not 0, its', self.sets[set_name].current)
            self.sets[set_name].save_score()
        print("Cached, progress is: " + self.calculateCompositeCompletion())

    def save(self): # true save
        print("Saved, progress is: " + self.calculateCompositeCompletion())
        #with open(data_file_name, "w") as file:
            #pickle.dump(self.sets, file)
        return self.sets

    def load(self):
        try:
            with open(data_file_name, "rb") as file:
                self.sets = pickle.load(file)
        except FileNotFoundError:
            pass

    def calculateCompositeCompletion(self) -> str: # average
        sum = 0
        total = 0
        for problemSet in self.getSets().values():
            sum += problemSet.get_score()
            total += len(problemSet.getProblems())
        
        return "%.02f" % (sum/total)
    
from backend.classes_data.FractionProblems import problems
main = TopicCenter(
    sets={
        'Fractions': ProblemSet(
            problems # add here
        )
    }
)

'''
main = TopicCenter(
    {
        'Topic': ProblemSet((
            Problem(...),
            Problem(...)),
            ...
        ),
        'MoreTopics': ProblemSet(
            (...)
        )
    }
)

encase arguments in problem sets with tupling (...)
'''

if __name__ == "__main__": # test routine
    main.selectSet('Fractions')
    for i in main.cycleProblems():
        print(i)