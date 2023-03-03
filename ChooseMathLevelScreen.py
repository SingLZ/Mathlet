from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

#Define different Screens
class LevelWindow(Screen):
    pass

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
