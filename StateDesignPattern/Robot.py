from StandingState import StandingState

class Robot:

	def __init__(self):
		self.state = StandingState()


	def on_stand(self):
		self.state = self.state.stand()

	def on_go(self):
		self.state = self.state.go()

	def on_lie(self):
		self.state = self.state.lie()

	def on_jump(self):
		self.state = self.state.jump()