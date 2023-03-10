import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from problemsData import ProblemsFeedback, steps01

problem01 = ProblemsFeedback("2+2*2/2+2", steps01)
problem02 = ProblemsFeedback("3+3*3/3+3", steps01)

class LetterButton:
    def __init__(self, letter):
        self.letter = letter
        self.strProp = problem01.steps["uno"][letter]["step"]

class ProblemCards(Screen):
    strA = LetterButton("A")
    strB = LetterButton("B")
    strC = LetterButton("C")
    strD = LetterButton("D")

    numStep = StringProperty("Step 1 of x:")
    question = StringProperty(problem01.problem)

    def changeSteps(self):
        print(self.ids.A)
        #letter = self.ids.strA.id
        #print(letter)
        # still need to display feedback one at a time 
        if problem01.steps["uno"]["A"]["correctness"]:
            self.ids.A.text = problem01.steps["dos"]["A"]["step"]
            self.ids.A.background_color = (127/255, 255/255, 0/255, 1)
            self.ids.B.text = problem01.steps["dos"]["B"]["step"]
            self.ids.C.text = problem01.steps["dos"]["C"]["step"]
            self.ids.D.text = problem01.steps["dos"]["D"]["step"]
            self.ids.question.text = problem02.problem
        else:
            self.ids.A.text = problem01.steps["uno"]["A"]["feedback"]
            self.ids.B.text = problem01.steps["uno"]["B"]["feedback"]
            self.ids.C.text = problem01.steps["uno"]["C"]["feedback"]
            self.ids.D.text = problem01.steps["uno"]["D"]["feedback"]


class WindowManager(ScreenManager):
    pass

twoTwo = Builder.load_file('TwoTwoProblemCards.kv')

class TwoTwoProblemCardsApp(App):
    def build(self):
        Window.clearcolor = (255, 255, 255)
        return twoTwo

if __name__ == '__main__':
    TwoTwoProblemCardsApp().run()