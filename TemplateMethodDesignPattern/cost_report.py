from report import Report


class CostReport(Report):

    def prepare_data(self):
        return "COSTS"

    def prepare_diagram(self):
        return "DIAGRAM"
