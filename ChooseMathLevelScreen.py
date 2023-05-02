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
from TopicCenter import TopicCenter, main
from mathimg import make_img

def loadProblem(self, problem):
	self.ids.stepcounter.text = f'Step {problem.CurrentStep+1} of {len(problem.Steps)}'
	self.ids.question.source = make_img(problem.getEquation(), 'output')
	self.ids.question.reload()
	self.ids.answerChoice1.source = make_img(problem.getCurrentStep().step, 'choice1')
	self.ids.answerChoice1.reload()
	wrong_steps = problem.getCurrentWrongSteps()
	if wrong_steps:
		for i in range(0, 3):
			id = getattr(self.ids, 'answerChoice' + str(i + 2))
			id.source = make_img(wrong_steps[i].step, 'choice' + str(i + 2))
			id.reload()

def load(self, topicName: str = None, loadNew: bool = False):
	problemSet = main.selectSet(topicName) or main.getCurrentSet()
	if loadNew:
		problemSet.current = problemSet.high_score_index
	problem = problemSet.getCurrentProblem()
	loadProblem(self, problem)
	
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
		if not main.current_set:
			return # temporary sanity check
		problem = main.getCurrentProblem()
		if self.feedbackMode:
			try:
				problem.next()
				wrong_steps = problem.getCurrentWrongSteps()
				if wrong_steps:
					for i in range(0, 3):
						id = getattr(self.ids, 'answerChoice' + str(i + 2))
						id.source = make_img(wrong_steps[i].step, 'choice' + str(i + 2))
						id.reload()
			except IndexError: # finished
				problemSet = main.getCurrentSet()
				if problemSet.current == len(problemSet.problems) - 1:
					# done (put go back function call here)
					self.feedbackMode = True # block feedback buttons
					self.unload(True) # save
					self.ids.question.source = make_img("You have reached the end!", 'output')
					self.ids.question.reload()
					for i in range(0, 4): # erase all
						id = getattr(self.ids, 'answerChoice' + str(i + 1))
						id.source = make_img('', 'choice' + str(i + 1))
						id.reload()
					return
				else:
					problemSet.next()
				problem = problemSet.getCurrentProblem()
				loadProblem(self, problem)
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
			problem = main.getCurrentProblem()
			self.ids.answerChoice2.source = make_img(problem.getCurrentWrongSteps()[0].feedback, 'choice2')
			self.ids.answerChoice2.reload() # image refresh
	def on_clickedButtonC(self):
		if not self.feedbackMode:
			problem = main.getCurrentProblem()
			self.ids.answerChoice3.source = make_img(problem.getCurrentWrongSteps()[1].feedback, 'choice3')
			self.ids.answerChoice3.reload() # image refresh
	def on_clickedButtonD(self):
		if not self.feedbackMode:
			problem = main.getCurrentProblem()
			self.ids.answerChoice4.source = make_img(problem.getCurrentWrongSteps()[2].feedback, 'choice4')
			self.ids.answerChoice4.reload() # image refresh
	def load(self, class_type: str = None):
		load(self, class_type)
	def unload(self, save: bool = False):
		self.question = ''
		self.strA = ''
		self.strB = ''
		self.strC = ''
		self.strD = ''

		if save:
			main.save()
			main.current_set = None
	def reload(self, class_type: str):
		self.unload()
		self.load(class_type) # temporary

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
	
	def on_stop(self):
		main.save()
		# save with pickle here
	
if __name__ == '__main__':
	LevelApp().run()