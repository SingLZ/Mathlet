<<<<<<< HEAD
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
=======
import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty
# removes red dot when you left click
>>>>>>> 8da0a82e3fb59051023a199e0b68edfd9e0bc66e
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

#Define different Screens
class LevelWindow(Screen):
    pass

<<<<<<< HEAD
=======
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

>>>>>>> 8da0a82e3fb59051023a199e0b68edfd9e0bc66e
class Elementary(Screen):
    pass

class MiddleSchool(Screen):
    pass

class HighSchool(Screen):
    pass

class College(Screen):
    pass

class WindowManager(ScreenManager):
    pass

<<<<<<< HEAD
kv = Builder.load_file('new_window.kv')

class LevelApp(App):
=======
# for back button to return to previous screen
class RootWidget(ScreenManager):
    pass

kv = Builder.load_file('new_window.kv')
# Builder.load_file("ProblemCards.kv")

class LevelApp(App):
    # for back button in ProblemCards.kv to return to previous screen
    def __init__(self, **kwargs):
        super(LevelApp, self).__init__(**kwargs)
        self.previous_screen = "" 

>>>>>>> 8da0a82e3fb59051023a199e0b68edfd9e0bc66e
    def build(self):
        Window.clearcolor = (255, 255, 255)
        return kv
    
if __name__ == '__main__':
    LevelApp().run()
