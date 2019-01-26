from random_obstacle_factory import RandomObstacleFactory
from fire import Fire
from rat import Rat
from block import Block

factory = RandomObstacleFactory(Fire, Rat, Block)


for i in range(0, 20):
    obstacle = factory.create_obstacle()
    obstacle.show()
