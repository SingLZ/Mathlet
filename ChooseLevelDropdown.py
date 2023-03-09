import kivy

from kivy.app import App

#import library
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

#for elementary
Builder.load_string("""
<ElementaryCustomDropDown>
    Button:
        text: "Perimeter and Shape"
        size_hint_y: None
        height: 44
        on_release: root.select("Perimeter and Shape")
    Button:
        text: "Rounding Whole Numbers"
        size_hint_y: None
        height: 44
        on_release: root.select("Rounding Whole Numbers")
    
""")

class ElementaryCustomDropDown(DropDown):
    pass

#middle school
Builder.load_string("""
<MiddleCustomDropDown>
    Button:
        text: "Fractions"
        size_hint_y: None
        height: 44
        on_release: root.select("Fractions")
    Button:
        text: "Probability"
        size_hint_y: None
        height: 44
        on_release: root.select("Probability")
    
""")

class MiddleCustomDropDown(DropDown):
    pass

#high school
Builder.load_string("""
<highCustomDropDown>
    Button:
        text: "Quadratic Equations"
        size_hint_y: None
        height: 44
        on_release: root.select("Quadratic Equations")
    Button:
        text: "Logarithms"
        size_hint_y: None
        height: 44
        on_release: root.select("Logarithms")
    
""")

class highCustomDropDown(DropDown):
    pass

#for college 
Builder.load_string("""
<collegeCustomDropDown>
    Button:
        text: "Derivative"
        size_hint_y: None
        height: 44
        on_release: root.select("Derivative")
    Button:
        text: "Integrals"
        size_hint_y: None
        height: 44
        on_release: root.select("Integrals")
    
""")

class collegeCustomDropDown(DropDown):
    pass

class DemoApp(App):
    def build(self):

        # one button for drop down
        box = FloatLayout()

        elementaryButton = Button(text = "Elementary", 
                                  size_hint=(0.9,0.15), 
                                  pos_hint={'center_x':0.5,'center_y':0.8})
        eleDropdown = ElementaryCustomDropDown()
        #open dropdown when you click elementary button
        elementaryButton.bind(on_release = eleDropdown.open)
    

        middleButton = Button(text = "Middle School", 
                                 size_hint=(0.9,0.15), 
                                  pos_hint={'center_x':0.5,'center_y':0.65})
        middleDropdown = MiddleCustomDropDown()
        #open dropdown when you click middleschool button
        middleButton.bind(on_release = middleDropdown.open)


        highButton = Button(text = "High School", 
                                 size_hint=(0.9,0.15), 
                                  pos_hint={'center_x':0.5,'center_y':0.50})
        highDropdown = highCustomDropDown()
        #open dropdown when you click high school button
        highButton.bind(on_release = highDropdown.open)


        collegeButton = Button(text = "College", 
                                 size_hint=(0.9,0.15), 
                                  pos_hint={'center_x':0.5,'center_y':0.35})
        collegeDropdown = collegeCustomDropDown()
        #open dropdown when you click college button
        collegeButton.bind(on_release = collegeDropdown.open)

        # creating a bottom navigation layout
        homeButton = Button(text = "Home",
                            size_hint = (0.25,0.2), 
                            pos_hint={"x":0.1, "y": 0.01})
        levelButton = Button(text = "Levels",
                            size_hint = (0.25,0.2), 
                            pos_hint={"x":0.35, "y": 0.01})
        progressButton = Button(text = "Progress",
                            size_hint = (0.25,0.2), 
                            pos_hint={"x":0.60, "y": 0.01})
        
        #create top label for Mathlet
        mathletLabel = Label(text ="Mathlet", font_size = '25sp', italic = True, size_hint= (0.9,0.1), pos_hint={'center_x':0.5, "y":0.9})

        
        box.add_widget(elementaryButton)
        box.add_widget(middleButton)
        box.add_widget(highButton)
        box.add_widget(collegeButton)
        box.add_widget(homeButton)
        box.add_widget(levelButton)
        box.add_widget(progressButton)
        box.add_widget(mathletLabel)
        return box

if __name__ =="__main__":
    DemoApp().run()