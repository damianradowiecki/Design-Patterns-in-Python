from abc import ABC


class Report(ABC):

    def generate(self):
        self.data = self.prepare_data()
        self.diagram = self.prepare_diagram()
        print("----REPORT----")
        print()
        print(self.data)
        print()
        print(self.diagram)
        print()
        print("---------------")

    def prepare_data(self):
        pass

    def prepare_diagram(self):
        pass
