from backend.classes_data.problem import Problem
from backend.classes_data.ProblemSet import ProblemSet
import pickle

class TopicCenter():
    def __init__(self, sets: dict = None):
        self.sets = sets
        self.current_set: ProblemSet = None
        self.topic_access_cache = []

    def getCurrentSet(self):
        return self.current_set

    def getSets(self) -> dict:
        return self.sets
    
    def peekSet(self, set_name: str) -> dict:
        return self.sets[set_name]

    def selectSet(self, set_name: str) -> ProblemSet:
        if not self.sets[set_name]:
            raise Exception("Set name does not exist.")
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
    
    def save(self):
        with open('user_data.pickle', 'wb') as f:
            pickle.dump(self.sets, f)

    def cache_scores(self):
        for set_name in self.topic_access_cache:
            self.sets[set_name].save_score()
            self.sets[set_name].reset()
        return self.sets

    def load(self, sets: dict = None):
        try:
            with open('user_data.pickle', 'rb') as f:
                self.sets = pickle.load(f)
            return True
        except FileNotFoundError:
            return False
            
    def calculateCompositeCompletion(self) -> str: # kept for future statistics/analytics
        sum = 0
        total = 0
        for problemSet in self.getSets().values():
            sum += problemSet.get_score()
            total += len(problemSet.getProblems())
        
        return "%.02f" % (sum/total)
    
from backend.classes_data.DerivativeProblems import problems as DeriProblems
from backend.classes_data.QuadraticProblems import problems as QuadraticProblems
from backend.classes_data.OrderOfOperationsProblems import problems as OOOProblems
from backend.classes_data.FractionProblems import problems as FracProblems

main = TopicCenter()
if not main.load(): # to reload the entire save, remove the .pickle file   
    main.sets = {
        'Fractions': ProblemSet(
            FracProblems
        ),
        'Derivatives': ProblemSet(
            DeriProblems
        ),
        'Order of Operations': ProblemSet(
            OOOProblems
        ),
        'Quadratics' : ProblemSet(
            QuadraticProblems
        )
    }

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

encase arguments in problem sets with sets
'''

if __name__ == "__main__": # debug print
    main.selectSet('Fractions')
    for i in main.cycleProblems():
        print(i)