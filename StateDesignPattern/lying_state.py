from robot_state import RobotState


class LyingState(RobotState):

	def __init__(self):
		print("I'm in LyingState")

	def stand(self):
		print("Changing state to StandingState")
		from standing_state import StandingState
		return StandingState()

	def go(self):
		print("Changing state to GoingState")
		from goind_state import GoingState
		return GoingState()

	def lie(self):
		print("I'm already lying")
		return self

	def jump(self):
		print("Cannot jump from lying position...")
		return self
