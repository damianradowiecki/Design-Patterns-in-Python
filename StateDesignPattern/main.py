from robot import Robot
from going_state import GoingState
from standing_state import StandingState
from lying_state import LyingState

robot = Robot()

robot.on_stand()
robot.on_go()
robot.on_go()
robot.on_lie()
robot.on_jump()
robot.on_stand()
robot.on_jump()