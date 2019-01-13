from Tag import Tag

class LeafTag(Tag):

	def __init__(self, name, attributes):
		self.name = name
		self.attributes = attributes

	def getChildren(self):
		return []

	def getName(self):
		return self.name

	def getAttributes(self):
		return self.attributes

	def print(self):
		print("<" + self.name + "/>")