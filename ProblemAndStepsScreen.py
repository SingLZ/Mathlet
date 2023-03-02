import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty

class ProblemCards(Screen):
    strA = StringProperty("A")
    strB = StringProperty("B")
    strC = StringProperty("C")
    strD = StringProperty("D")
    question = StringProperty("Question")
    def on_button_click(self):
        self.strA = "Transition to Feedback Screen"
    def clicked(self):
        self.strB = "Transition to Feedback Screen A Super Duper Duper Long Answer"

class WindowManager(ScreenManager):
    pass

#oneFour = Builder.load_file('OneFourProblemCards.kv')
#twoTwo = Builder.load_file('TwoTwoProblemCards.kv')
fourOne = Builder.load_file('FourOneProblemCards.kv')
#kv = Builder.load_file('new_window.kv')

class TwoTwoProblemCardsApp(App):
    def build(self):
        Window.clearcolor = (255, 255, 255)
        return twoTwo
    
class OneFourProblemCardsApp(App):
    def build(self):
        Window.clearcolor = (255, 255, 255)
        return oneFour 
    
class FourOneProblemCardsApp(App):
    def build(self):
        Window.clearcolor = (255, 255, 255)
        return fourOne 

if __name__ == '__main__':
    FourOneProblemCardsApp().run()

'''
Note for testing:
    Change line 46 to 
    TwoTwoProblemCardsApp().run() or
    OneFourProblemCardsApp().run()
    and
    Comment out lines 25/26/27 depending on which
    file you want to check and uncomment the other
    line

    For example, if we want to see the Two/Two
    format, switch line 46 to TwoTwoProblemCardsApp().run()
    and comment out line 25 and 27 and uncomment line 26
'''