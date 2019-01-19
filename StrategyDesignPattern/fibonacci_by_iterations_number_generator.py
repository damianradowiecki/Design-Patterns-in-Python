from fibonacci_number_generator import FibonacciNumberGenerator

class FibonacciByIterationsNumberGenerator(FibonacciNumberGenerator):
    def generate(self, which):
        if which == 0 or which == 1:
            return 1
        else:
            a = 0
            b = 1
            result = 0
            for i in range(0, which):
                result = a + b
                a = b
                b = result
            return result
