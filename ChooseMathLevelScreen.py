from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty
# removes red dot when you left click
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

###
from mathimg import make_img
from backend.classes_data.FractionProblems import problems
problem = problems[0]

def loadProblem(self):
	self.ids.stepcounter.text = f'Step {problem.CurrentStep+1} of {len(problem.Steps)}'
	self.ids.question.source = make_img(problem.getEquation(), 'output')
	self.ids.question.reload()
	self.ids.answerChoice1.source = make_img(problem.getCurrentStep().step, 'choice1')
	self.ids.answerChoice1.reload()
	wrong_steps = problem.getCurrentWrongSteps()
	if wrong_steps:
		for i in range(0, 3):
			id = getattr(self.ids, 'answerChoice' + str(i + 2))
			id.source = make_img(wrong_steps[i], 'choice' + str(i + 2))
			id.reload()
###

# set window size to phone size 
Window.size = (400,600)

#Define different Screens
class LevelWindow(Screen):
	pass

class ProblemCards(Screen):
	strA = StringProperty("A")
	strB = StringProperty("B")
	strC = StringProperty("C")
	strD = StringProperty("D")
	question = StringProperty("Question")

	feedbackMode = False # added
	
	def __init__(self, **kw):
		super().__init__(**kw)

	def on_clickedButtonA(self):
		if self.feedbackMode:
			try:
				problem.next()
				wrong_steps = problem.getCurrentWrongSteps()
				if wrong_steps:
					for i in range(0, 3):
						id = getattr(self.ids, 'answerChoice' + str(i + 2))
						id.source = make_img(wrong_steps[i], 'choice' + str(i + 2))
						id.reload()
			except IndexError:
				problem.reset()
				loadProblem(self)
			self.ids.answerChoice1.source = make_img(problem.getCurrentStep().step, 'choice1')
			self.ids.answerChoice1.reload()
			self.feedbackMode = False
			return
		self.ids.stepcounter.text = f'Step {problem.CurrentStep+1} of {len(problem.Steps)}'
		self.ids.question.source = make_img(f'{problem.strToCurrentStep()}', 'output')
		self.ids.question.reload()
		self.ids.answerChoice1.source = make_img(problem.getCurrentStep().feedback, 'choice1')
		self.ids.answerChoice1.reload()
		self.feedbackMode = True

	def on_clickedButtonB(self):
		if not self.feedbackMode:
			self.ids.answerChoice2.source = make_img('', 'choice2')
			self.ids.answerChoice2.reload() # image refresh
			self.strB = "Wrong"
	def on_clickedButtonC(self):
		self.strC = "Wrong"
	def on_clickedButtonD(self):
		self.strD = "Wrong"
	def reload(self):
		self.question = ''
		self.strA = ''
		self.strB = ''
		self.strC = ''
		self.strD = ''

		problem.reset()
		loadProblem(self)

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

	def build(self):
		Window.clearcolor = (255, 255, 255)
		return kv
	
if __name__ == '__main__':
	LevelApp().run()