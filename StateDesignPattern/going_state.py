from robot_state import RobotState


class GoingState(RobotState):

	def __init__(self):
		print("I'm in GoingState")

	def stand(self):
		print("Changing state to StandingState")
		from standing_state import StandingState
		return StandingState()

	def go(self):
		print("I'm already going")
		return self

	def lie(self):
		print("Changing state to LyingState")
		from lying_state import LyingState
		return LyingState()

	def jump(self):
		print("Changing state to JumpingState")
		from jumping_state import JumpingState
		return JumpingState()
