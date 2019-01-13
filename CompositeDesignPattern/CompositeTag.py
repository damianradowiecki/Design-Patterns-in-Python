from Tag import Tag

class CompositeTag(Tag):
	
	def __init__(self, name, attributes, children):
		self.name = name
		self.attributes = attributes
		self.children = children

	def getChildren(self):
		return self.children

	def getName(self):
		return self.name

	def getAttributes(self):
		return self.attributes

	def print(self):
		print("<" + self.name + ">")
		for child in self.children:
			print("\t", end="")
			child.print()
		print("</" + self.name + ">")
