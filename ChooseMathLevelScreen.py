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

from TopicCenter import TopicCenter, main
from mathimg import make_img
from threading import Thread
	
def threadLoad(id, txt: str = '', fileName: str = 'output'):
	loadInto(id, txt, fileName) #Thread(target=loadInto, args=(id, txt, fileName)).start()

def loadInto(id, txt: str = '', fileName: str = 'output'):
	id.source = make_img(txt, fileName)
	id.reload() # image refresh

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

	def loadWrongSteps(self):
		wrong_steps = main.getCurrentProblem().getCurrentWrongSteps()
		if wrong_steps:
			for i in range(2, 5): # [2, 5)
				id = getattr(self.ids, f'answerChoice{i - 1}')
				threadLoad(id, wrong_steps[i - 2].step, f'choice{i - 1}')

	def loadProblem(self):
		problem = main.getCurrentProblem()
		self.ids.stepcounter.text = f'Step {problem.CurrentStep+1} of {len(problem.Steps)}'
		threadLoad(self.ids.question, problem.getEquation(), 'output')
		threadLoad(self.ids.answerChoice1, problem.getCurrentStep().step, 'choice1')
		self.loadWrongSteps()

	def loadTopic(self, topicName: str, loadNew: bool = False):
		problemSet = main.selectSet(topicName) or main.getCurrentSet()
		if loadNew:
			problemSet.current = problemSet.high_score_index
		#problem = problemSet.getCurrentProblem()
		self.loadProblem()

	def on_clickedButtonA(self):
		if not main.current_set:
			return # temporary sanity check
		problem = main.getCurrentProblem()
		if self.feedbackMode:
			try:
				problem.next()
				self.loadWrongSteps()
			except IndexError: # finished
				problemSet = main.getCurrentSet()
				if problemSet.current == len(problemSet.problems) - 1:
					# done (put go back function call here)
					self.feedbackMode = True # block feedback buttons
					self.unload(True) # save
					threadLoad(self.ids.question, "You have reached the end!", 'output')
					for i in range(1, 5): # erase all	[1, 5)
						id = getattr(self.ids, f'answerChoice{i}')
						threadLoad(id, '', f'choice{i}')
					return
				else:
					problemSet.next()
				problem = problemSet.getCurrentProblem()
				self.loadProblem()
			threadLoad(self.ids.answerChoice1, problem.getCurrentStep().step, 'choice1')
			self.feedbackMode = False
			return
		self.ids.stepcounter.text = f'Step {problem.CurrentStep+1} of {len(problem.Steps)}'
		threadLoad(self.ids.question, problem.strToCurrentStep(), 'output')
		threadLoad(self.ids.answerChoice1, problem.getCurrentStep().feedback, 'choice1')
		self.feedbackMode = True

	def on_clickedButtonB(self):
		if not self.feedbackMode:
			threadLoad(self.ids.answerChoice2, main.getCurrentProblem().getCurrentWrongSteps()[0].feedback, 'choice2')
	def on_clickedButtonC(self):
		if not self.feedbackMode:
			threadLoad(self.ids.answerChoice3, main.getCurrentProblem().getCurrentWrongSteps()[1].feedback, 'choice3')
	def on_clickedButtonD(self):
		if not self.feedbackMode:
			threadLoad(self.ids.answerChoice4, main.getCurrentProblem().getCurrentWrongSteps()[2].feedback, 'choice4')
	def load(self, class_type: str = None):
		self.topic = class_type
		self.loadTopic(class_type)
	def unload(self, save: bool = False):
		self.question = ''
		self.strA = ''
		self.strB = ''
		self.strC = ''
		self.strD = ''
		self.topic = None

		if save and main.getCurrentSet():
			main.cache_scores()
			main.getCurrentProblem().reset()
			main.current_set = None
	def reload(self, class_type: str):
		self.unload()
		self.loadTopic(class_type) # temporary

class Elementary(Screen):
	def update_progressBar(self, progress_bar_id, label_id):
		# Grabs the current progress bar value
		current = self.ids[progress_bar_id].value
		# Increments value by 20%
		if current < 1:
			current += .20
		# Update the value of the progress bar
		self.ids[progress_bar_id].value = current
		# Update the Label
		self.ids[label_id].text = f'{int(current*100)}%'

class MiddleSchool(Screen):
	def update_progressBar(self, progress_bar_id, label_id):
		# Grabs the current progress bar value
		current = self.ids[progress_bar_id].value
		# Increments value by 20%
		if current < 1:
			current += .20
		# Update the value of the progress bar
		self.ids[progress_bar_id].value = current
		# Update the Label
		self.ids[label_id].text = f'{int(current*100)}%'

class HighSchool(Screen):
	def update_progressBar(self, progress_bar_id, label_id):
		# Grabs the current progress bar value
		current = self.ids[progress_bar_id].value
		# Increments value by 20%
		if current < 1:
			current += .20
		# Update the value of the progress bar
		self.ids[progress_bar_id].value = current
		# Update the Label
		self.ids[label_id].text = f'{int(current*100)}%'

class College(Screen):
	def update_progressBar(self, progress_bar_id, label_id):
		# Grabs the current progress bar value
		current = self.ids[progress_bar_id].value
		# Increments value by 20%
		if current < 1:
			current += .20
		# Update the value of the progress bar
		self.ids[progress_bar_id].value = current
		# Update the Label
		self.ids[label_id].text = f'{int(current*100)}%'

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