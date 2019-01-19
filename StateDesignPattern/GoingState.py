from RobotState import RobotState

class GoingState(RobotState):

	def __init__(self):
		print("I'm in GoingState")
	def stand(self):
		print("Changing state to StandingState")
		from StandingState import StandingState
		return StandingState()

	def go(self):
		print("I'm already going")
		return self

	def lie(self):
		print("Changing state to LyingState")
		from LyingState import LyingState
		return LyingState()

	def jump(self):
		print("Changing state to JumpingState")
		from JumpingState import JumpingState
		return JumpingState()