from abc import ABC, abstractmethod


class Tag(ABC):
	@abstractmethod
	def get_children(self):
		pass

	@abstractmethod
	def get_attributes(self):
		pass

	@abstractmethod
	def get_name(self):
		pass

	@abstractmethod
	def print(self):
		pass

	def print(self, tag):
		print("<" + tag.name, end="")
		for key, value in tag.attributes.items():
			print(" " + key + "=\"" + value + "\" ", end="")
		if len(tag.children) == 0:
			print("/>")
		else:
			print(">")
			for child in tag.children:
				super(type(tag), self).print(child)
			print("</" + tag.name + ">")
