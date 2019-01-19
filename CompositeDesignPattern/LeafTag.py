from Tag import Tag

class LeafTag(Tag):

	def __init__(self, name, attributes):
		self.name = name
		self.attributes = attributes
		self.children = {}

	def get_children(self):
		return []

	def get_name(self):
		return self.name

	def get_attributes(self):
		return self.attributes

	def print(self):
		print("<" + self.name + "/>")
