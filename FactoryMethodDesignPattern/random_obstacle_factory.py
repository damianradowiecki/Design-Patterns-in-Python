from obstacle_factory import ObstacleFactory
from random import randint

class RandomObstacleFactory(ObstacleFactory):

    def __init__(self, *classes):
        self.classes = classes

    def create_obstacle(self):
        random_number = randint(0, len(self.classes)-1)
        return self.classes[random_number]()
