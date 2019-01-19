from tag import Tag


class CompositeTag(Tag):

    def __init__(self, name, attributes, children):
        self.name = name
        self.attributes = attributes
        self.children = children

    def get_children(self):
        return self.children

    def get_name(self):
        return self.name

    def get_attributes(self):
        return self.attributes

    def print(self):
        super(CompositeTag, self).print(self)
