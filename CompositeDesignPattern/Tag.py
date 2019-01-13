from abc import ABC, abstractmethod

class Tag(ABC):
	@abstractmethod
	def getChildren(self):
		pass

	@abstractmethod
	def getAttributes(self):
		pass

	@abstractmethod
	def getName(self):
		pass

	@abstractmethod
	def print(self):
		pass