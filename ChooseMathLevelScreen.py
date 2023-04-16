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
from kivy.animation import Animation

###
from mathimg import make_img
from backend.classes_data.OrderOfOperationsProblem import problems

problem = problems[2] # Test from 0-2

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
	
	# Animates Card based on the correctness of Card
	def animateCard(self, widget, *args):
        # Animation when the step is incorrect
		animateWrong = Animation(
            background_color=(100/255, 42/255, 42/255, 1),
            duration=0.5
        )
		animateWrong += Animation(
            background_color=(25/255, 44/255, 132/255, 1)
        )

        # Animation when the step is correct
		animateCorrect = Animation(
            background_color=(183/255, 140/255, 56/255, 1),
            duration=0.5,
        )
		animateCorrect += Animation(
            background_color=(25/255, 44/255, 132/255, 1)
        )

		#animateCorrect.start(widget) or animateWrong.start(widget)

	def __init__(self, **kw):
		super().__init__(**kw)

	def on_clickedButtonA(self, widget, *args):
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
		
		animateCorrect = Animation(
            background_color=(183/255, 140/255, 56/255, 1),
            duration=0.5,
        )
		animateCorrect += Animation(
            background_color=(25/255, 44/255, 132/255, 1)
        )

		animateCorrect.start(widget)

	def on_clickedButtonB(self, widget, *args):
		animateWrong = Animation(
        	background_color=(100/255, 42/255, 42/255, 1),
        	duration=0.5
    	)
		animateWrong += Animation(
        	background_color=(25/255, 44/255, 132/255, 1)
    	)

		wrong_steps = problem.getCurrentWrongSteps()

		if not self.feedbackMode:
			self.ids.answerChoice2.source = make_img(wrong_steps[0].feedback, 'choice2')
			self.ids.answerChoice2.reload() # image refresh
			animateWrong.start(widget)

	def on_clickedButtonC(self, widget, *args):
		animateWrong = Animation(
            background_color=(100/255, 42/255, 42/255, 1),
        	duration=0.5
    	)
		animateWrong += Animation(
            background_color=(25/255, 44/255, 132/255, 1)
        )

		wrong_steps = problem.getCurrentWrongSteps()
		
		if not self.feedbackMode:
			self.ids.answerChoice3.source = make_img(wrong_steps[1].feedback, 'choice2')
			self.ids.answerChoice3.reload() # image refresh
			animateWrong.start(widget)

	def on_clickedButtonD(self, widget, *args):
		animateWrong = Animation(
            background_color=(100/255, 42/255, 42/255, 1),
        	duration=0.5
    	)
		animateWrong += Animation(
            background_color=(25/255, 44/255, 132/255, 1)
        )

		wrong_steps = problem.getCurrentWrongSteps()
		
		if not self.feedbackMode:
			self.ids.answerChoice4.source = make_img(wrong_steps[2].feedback, 'choice2')
			self.ids.answerChoice4.reload() # image refresh
			animateWrong.start(widget)

	def reload(self):
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