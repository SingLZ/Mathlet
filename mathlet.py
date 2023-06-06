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

from TopicCenter import main
from mathimg import make_img
from kivy.core.audio import SoundLoader
from timeit import default_timer
from random import randint

def getProgressBarId(name: str):
	return name.lower() + 'ProgressBar'

def getLabelId(name: str):
	return name.lower() + 'Label'

def loadInto(id, txt: str = '', fileName: str = 'output'):
	then = default_timer()
	make_img(txt, fileName)
	id.reload() # image refresh
	now = default_timer() - then
	if (now > 0.25):
		print("Image load bottleneck possible. Time: " + str(now))

# set window size to phone size 
Window.size = (400,600)

#Define different Screens
class LevelWindow(Screen):
	def play_button_sound(self):
		self.button_sound = SoundLoader.load('button.wav')
		self.button_sound.loop = False
		if self.ids.volume.source == "volume.png":
			self.button_sound.play()
		else:
			self.button_sound.stop()

class ProblemCards(Screen):
	strA = StringProperty("A")
	strB = StringProperty("B")
	strC = StringProperty("C")
	strD = StringProperty("D")
	question = StringProperty("Question")
	currentCorrectChoice = None # index
	currentWrongChoices = [] # indices

	feedbackMode = False
	
	def __init__(self, **kw):
		super().__init__(**kw)

	def randomize_correct_choice(self):
		self.currentCorrectChoice = randint(1, 4)

	def generate_wrong_steps(self):
		self.currentWrongChoices.clear()
		available_wrong_choices = [0, 1, 2, 3]
		del available_wrong_choices[self.currentCorrectChoice-1]
		while (len(available_wrong_choices) != 0):
			self.currentWrongChoices.append(available_wrong_choices.pop(randint(0, len(available_wrong_choices) - 1)))

	def loadWrongSteps(self):
		problem = main.getCurrentProblem()
		self.generate_wrong_steps()
		wrong_steps = problem.getCurrentWrongSteps()
		for stepIndex, choiceIndex in enumerate(self.currentWrongChoices):
			id = getattr(self.ids, f'answerChoice{choiceIndex+1}')
			print(f"stepIndex: {stepIndex}")
			loadInto(id, wrong_steps[stepIndex].step, f'choice{choiceIndex+1}')

	# def loadWrongSteps(self):
	# 	wrong_steps = main.getCurrentProblem().getCurrentWrongSteps()
	# 	if wrong_steps:
	# 		for i in range(2, 5): # [2, 5)
	# 			id = getattr(self.ids, f'answerChoice{i}')
	# 			loadInto(id, wrong_steps[i - 2].step, f'choice{i}')

	def loadProblem(self):
		problem = main.getCurrentProblem()
		self.ids.stepcounter.text = f'Step {problem.CurrentStep+1} of {len(problem.Steps)}'
		loadInto(self.ids.question, problem.getEquation(), 'output')
		self.randomize_correct_choice()
		loadInto(getattr(super().ids, f"answerChoice{self.currentCorrectChoice}"), problem.getCurrentStep().step, f'choice{self.currentCorrectChoice}')
		self.loadWrongSteps()

	def loadTopic(self, topicName: str, loadNew: bool = False):
		problemSet = main.selectSet(topicName) or main.getCurrentSet()
		if loadNew:
			problemSet.current = problemSet.high_score_index
		self.loadProblem()

	def correctAnswer(self, choiceNumber: int):
		if not main.current_set:
			return # sanity check
		problem = main.getCurrentProblem()
		choiceId = self.ids[f'answerChoice{choiceNumber}']
		if self.feedbackMode:
			try:
				problem.next()
				self.loadProblem()
			except IndexError: # finished
				problemSet = main.getCurrentSet()
				if problemSet.current == len(problemSet.problems) - 1:
					self.feedbackMode = True # block feedback buttons
					self.unload(True) # save
					loadInto(self.ids.question, "You have reached the end!", 'output')
					for i in range(1, 5): # erase all	[1, 5)
						id = getattr(self.ids, f'answerChoice{i}')
						loadInto(id, '', f'choice{i}')
					return
				else:
					problemSet.next()
				problem = problemSet.getCurrentProblem()
				self.loadProblem()
			loadInto(choiceId, problem.getCurrentStep().step, 'choice1')
			self.feedbackMode = False
			return
		self.ids.stepcounter.text = f'Step {problem.CurrentStep+1} of {len(problem.Steps)}'
		loadInto(self.ids.question, problem.strToCurrentStep(), 'output')
		loadInto(choiceId, problem.getCurrentStep().feedback, f'choice{choiceNumber}')
		self.feedbackMode = True 

	def wrongAnswer(self, choiceNumber: int):
		if not self.feedbackMode:
			loadInto(self.ids[f'answerChoice{choiceNumber}'], main.getCurrentProblem().getCurrentWrongSteps()[choiceNumber-2].feedback, f'choice{choiceNumber}')
	
	def answer(self, choiceNumber: int):
		if self.currentCorrectChoice == choiceNumber:
			self.correctAnswer(choiceNumber)
		else:
			self.wrongAnswer(choiceNumber)

	def on_clickedButtonA(self):
		# example use:
		self.answer(1)

	def on_clickedButtonB(self):
		self.answer(2)

	def on_clickedButtonC(self):
		self.answer(3)

	def on_clickedButtonD(self):
		self.answer(4)
		
	def load(self, class_type: str = None):
		self.topic = class_type
		self.feedbackMode = False
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
		self.feedbackMode = False

	def play_button_sound(self):
		self.button_sound = SoundLoader.load('button.wav')
		self.button_sound.loop = False
		if self.ids.volume.source == "volume.png":
			self.button_sound.play()
		else:
			self.button_sound.stop()

class Elementary(Screen):
	def update_progressBar(self, progress_bar_id, label_id, class_name: str = None):
		current = None
		if class_name:
			current = main.peekSet(class_name).get_score()
		else:
			# Grabs the current progress bar value
			current = self.ids[progress_bar_id].value
			# Increments value by 20%
			if current < 1:
				current += .20
		# Update the value of the progress bar
		self.ids[progress_bar_id].value = current
		# Update the Label
		self.ids[label_id].text = f'{int(current*100)}%'

	def play_button_sound(self):
		ProblemCards = App.get_running_app().root.get_screen("ProblemCards")
		self.button_sound = SoundLoader.load('button.wav')
		self.button_sound.loop = False
		if ProblemCards.ids.volume.source == "volume.png":
			self.button_sound.play()
		else:
			self.button_sound.stop()

	def on_kv_post(self, *args):
		self.load()
	
	def load(self):
		self.update_progressBar("pemdasProgressBar", "pemdasLabel", "Order of Operations")

class MiddleSchool(Screen):
	def update_progressBar(self, progress_bar_id, label_id, class_name: str = None):
		current = None
		if class_name:
			current = main.peekSet(class_name).get_score()
		else:
			# Grabs the current progress bar value
			current = self.ids[progress_bar_id].value
			# Increments value by 20%
			if current < 1:
				current += .20
		# Update the value of the progress bar
		self.ids[progress_bar_id].value = current
		# Update the Label
		self.ids[label_id].text = f'{int(current*100)}%'

	def play_button_sound(self):
		ProblemCards = App.get_running_app().root.get_screen("ProblemCards")
		self.button_sound = SoundLoader.load('button.wav')
		self.button_sound.loop = False
		if ProblemCards.ids.volume.source == "volume.png":
			self.button_sound.play()
		else:
			self.button_sound.stop()
	
	def on_kv_post(self, *args):
		self.load()
	
	def load(self):
		self.update_progressBar("fractionProgressBar", "fractionLabel", "Fractions")

class HighSchool(Screen):
	def update_progressBar(self, progress_bar_id, label_id, class_name: str = None):
		current = None
		if class_name:
			current = main.peekSet(class_name).get_score()
		else:
			# Grabs the current progress bar value
			current = self.ids[progress_bar_id].value
			# Increments value by 20%
			if current < 1:
				current += .20
		# Update the value of the progress bar
		self.ids[progress_bar_id].value = current
		# Update the Label
		self.ids[label_id].text = f'{int(current*100)}%'

	def play_button_sound(self):
		ProblemCards = App.get_running_app().root.get_screen("ProblemCards")
		self.button_sound = SoundLoader.load('button.wav')
		self.button_sound.loop = False
		if ProblemCards.ids.volume.source == "volume.png":
			self.button_sound.play()
		else:
			self.button_sound.stop()
	
	def on_kv_post(self, *args):
		self.load()
	
	def load(self):
		self.update_progressBar("quadraticProgressBar", "quadraticLabel", "Quadratics")

class College(Screen):
	def update_progressBar(self, progress_bar_id, label_id, class_name: str = None):
		current = None
		if class_name:
			current = main.peekSet(class_name).get_score()
		else:
			# Grabs the current progress bar value
			current = self.ids[progress_bar_id].value
			# Increments value by 20%
			if current < 1:
				current += .20
		# Update the value of the progress bar
		self.ids[progress_bar_id].value = current
		# Update the Label
		self.ids[label_id].text = f'{int(current*100)}%'

	def play_button_sound(self):
		ProblemCards = App.get_running_app().root.get_screen("ProblemCards")
		self.button_sound = SoundLoader.load('button.wav')
		self.button_sound.loop = False
		if ProblemCards.ids.volume.source == "volume.png":
			self.button_sound.play()
		else:
			self.button_sound.stop()

	def on_kv_post(self, *args):
		self.load()
	
	def load(self):
		self.update_progressBar("derivativesProgressBar", "derivativesLabel", "Derivatives")

class UserManual(Screen):
	def play_button_sound(self):
		ProblemCards = App.get_running_app().root.get_screen("ProblemCards")
		self.button_sound = SoundLoader.load('button.wav')
		self.button_sound.loop = False
		if ProblemCards.ids.volume.source == "volume.png":
			self.button_sound.play()
		else:
			self.button_sound.stop()

class HomeScreen(Screen):
	def play_button_sound(self):
		ProblemCards = App.get_running_app().root.get_screen("ProblemCards")
		self.button_sound = SoundLoader.load('button.wav')
		self.button_sound.loop = False
		if ProblemCards.ids.volume.source == "volume.png":
			self.button_sound.play()
		else:
			self.button_sound.stop()

class WindowManager(ScreenManager):
	pass

# for back button to return to previous screen
class RootWidget(ScreenManager):
	pass

kv = Builder.load_file('homeScreen.kv')
# Builder.load_file("ProblemCards.kv")

class LevelApp(App):
	# for back button in ProblemCards.kv to return to previous screen
	def __init__(self, **kwargs):
		super(LevelApp, self).__init__(**kwargs)
		self.previous_screen = "" 

	def build(self):
		Window.clearcolor = (255, 255, 255)
		return kv
	
	def toggleMusic(self):
		ProblemCards = App.get_running_app().root.get_screen("ProblemCards")
		ChooseLevel = App.get_running_app().root.get_screen("mathLevel")
		if ProblemCards.ids.volume.source == "volume.png" or ChooseLevel.ids.volume.source == "volume.png":
			ProblemCards.ids.volume.source = "mute.png"
			ChooseLevel.ids.volume.source = "mute.png"
		else:
			ProblemCards.ids.volume.source = "volume.png"
			ChooseLevel.ids.volume.source = "volume.png"

	def on_stop(self):
		main.save()
		# save with pickle here
	
if __name__ == '__main__':
	LevelApp().run()
