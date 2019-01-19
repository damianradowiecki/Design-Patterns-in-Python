from Robot import Robot
from GoingState import GoingState
from StandingState import StandingState
from LyingState import LyingState

robot = Robot()

robot.on_stand()
robot.on_go()
robot.on_go()
robot.on_lie()
robot.on_jump()
robot.on_stand()
robot.on_jump()