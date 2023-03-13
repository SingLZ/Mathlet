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
from kivy.animation import Animation

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

    numStep = "Step 1 of 2:"
    question = problem01.problem

    # Animates Card A based on the correctness of Card A
    def animateCardA(self, widget, *args):
        # Animation when the step is incorrect
        animateWrong = Animation(
            background_color=(100/255, 42/255, 42/255, 1),
            duration=2
        )
        animateWrong += Animation(
            background_color=(25/255, 44/255, 132/255, 1)
        )

        # Animation when the step is correct
        animateCorrect = Animation(
            background_color=(183/255, 140/255, 56/255, 1),
            duration=2,
        )
        animateCorrect += Animation(
            background_color=(25/255, 44/255, 132/255, 1)
        )

        if problem01.steps["uno"]["A"]["correctness"]:
            animateCorrect.start(widget)
        else:
            animateWrong.start(widget)

    def animateCard(self, widget, *args):
        # Animation when the step is incorrect
        animateWrong = Animation(
            background_color=(100/255, 42/255, 42/255, 1),
            duration=2
        )
        animateWrong += Animation(
            background_color=(25/255, 44/255, 132/255, 1)
        )

        # Animation when the step is correct
        animateCorrect = Animation(
            background_color=(183/255, 140/255, 56/255, 1),
            duration=2
        )
        animateCorrect += Animation(
            background_color=(25/255, 44/255, 132/255, 1)
        )

        if problem01.steps["uno"]["B"]["correctness"]:
            animateCorrect.start(widget)
        else:
            animateWrong.start(widget)

    def changeStepsA(self): 
        if problem01.steps["uno"]["A"]["correctness"]:
            self.ids.A.text = problem01.steps["dos"]["A"]["step"]
            self.ids.B.text = problem01.steps["dos"]["B"]["step"]
            self.ids.C.text = problem01.steps["dos"]["C"]["step"]
            self.ids.D.text = problem01.steps["dos"]["D"]["step"]
            self.ids.question.text = problem02.problem
            self.ids.label.text = "Step 2 of 2:"
        else:
            self.ids.A.text = problem01.steps["uno"]["A"]["feedback"]

    def changeStepsB(self):
        if problem01.steps["uno"]["B"]["correctness"]:
            self.ids.A.text = problem01.steps["dos"]["A"]["step"]
            self.ids.B.text = problem01.steps["dos"]["B"]["step"]
            self.ids.C.text = problem01.steps["dos"]["C"]["step"]
            self.ids.D.text = problem01.steps["dos"]["D"]["step"]
            self.ids.question.text = problem02.problem
        else:
            self.ids.B.text = problem01.steps["uno"]["B"]["feedback"]
    
    def changeStepsC(self):
        if problem01.steps["uno"]["C"]["correctness"]:
            self.ids.A.text = problem01.steps["dos"]["A"]["step"]
            self.ids.B.text = problem01.steps["dos"]["B"]["step"]
            self.ids.C.text = problem01.steps["dos"]["C"]["step"]
            self.ids.D.text = problem01.steps["dos"]["D"]["step"]
            self.ids.question.text = problem02.problem
        else:
            self.ids.C.text = problem01.steps["uno"]["C"]["feedback"]
    
    def changeStepsD(self):
        if problem01.steps["uno"]["D"]["correctness"]:
            self.ids.A.text = problem01.steps["dos"]["A"]["step"]
            self.ids.B.text = problem01.steps["dos"]["B"]["step"]
            self.ids.C.text = problem01.steps["dos"]["C"]["step"]
            self.ids.D.text = problem01.steps["dos"]["D"]["step"]
            self.ids.question.text = problem02.problem
        else:
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