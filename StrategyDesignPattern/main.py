from fibonacci_by_recursion_number_generator import FibonacciByRecursionNumberGenerator
from fibonacci_by_iterations_number_generator import FibonacciByIterationsNumberGenerator

generator = FibonacciByRecursionNumberGenerator()
result = generator.generate(7)
print(result)

generator = FibonacciByIterationsNumberGenerator()
result = generator.generate(7)
print(result)
