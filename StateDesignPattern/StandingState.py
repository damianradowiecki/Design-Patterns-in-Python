from RobotState import RobotState


class StandingState(RobotState):

	def __init__(self):
		print("I'm in StandingState")

	def stand(self):
		print("I'm already standing...")
		return self

	def go(self):
		print("Changing state to GoingState")
		from GoingState import GoingState
		return GoingState()

	def lie(self):
		print("Changing state to LyingState")
		from LyingState import LyingState
		return LyingState()

	def jump(self):
		print("Changing state to JumpingState")
		from JumpingState import JumpingState
		return JumpingState()

