from abc import ABC, abstractmethod


class RobotState(ABC):

	@abstractmethod
	def stand(self):
		pass

	@abstractmethod
	def go(self):
		pass

	@abstractmethod
	def lie(self):
		pass

	@abstractmethod
	def jump(self):
		pass
