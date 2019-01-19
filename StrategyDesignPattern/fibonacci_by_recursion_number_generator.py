from fibonacci_number_generator import FibonacciNumberGenerator


class FibonacciByRecursionNumberGenerator(FibonacciNumberGenerator):
    def generate(self, which):
        if which == 0:
            return 1
        elif which == 1:
            return 1
        else:
            return self.generate(which-1) + self.generate(which - 2)
