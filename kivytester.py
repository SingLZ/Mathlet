import kivy
kivy.require('2.1.0')
  
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.properties import StringProperty

class GridLayoutEx(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    strA = StringProperty("A")
    strB = StringProperty("B")
    def on_button_click(self):
        self.ids.equation.text = "ppfewaov"
        self.strA = "Feedback Here!"
    def clicked(self):
        self.strB = "Another feedback"

class BoxLayoutEx(BoxLayout):
    pass

#class MainWidget(Widget):
#   pass

class MyApp(App):
    pass
    
if __name__ == '__main__':
    MyApp().run()