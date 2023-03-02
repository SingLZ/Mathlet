from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty

#Define different Screens
class LevelWindow(Screen):
    pass

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

kv = Builder.load_file('new_window.kv')

class LevelApp(App):
    def build(self):
        Window.clearcolor = (255, 255, 255)
        return kv
    
if __name__ == '__main__':
    LevelApp().run()
