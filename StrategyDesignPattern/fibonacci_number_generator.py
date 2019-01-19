from abc import ABC, abstractmethod


class FibonacciNumberGenerator(ABC):
    @abstractmethod
    def generate(self, which):
        pass
