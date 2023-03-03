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

twoTwo = Builder.load_file('TwoTwoProblemCards.kv')

class TwoTwoProblemCardsApp(App):
    def build(self):
        Window.clearcolor = (255, 255, 255)
        return twoTwo

if __name__ == '__main__':
    TwoTwoProblemCardsApp().run()