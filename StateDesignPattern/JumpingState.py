from RobotState import RobotState


class JumpingState(RobotState):

	def __init__(self):
		print("I'm in JumpingState")

	def stand(self):
		print("Changing state to StandingState")
		from StandingState import StandingState
		return StandingState()

	def go(self):
		print("Changing state to GoingState")
		from GoingState import GoingState
		return GoingState()

	def lie(self):
		print("Changing state to LyingState")
		from LyingState import LyingState
		return LyingState()

	def jump(self):
		print("I'm already in JumpingState")
		return self
