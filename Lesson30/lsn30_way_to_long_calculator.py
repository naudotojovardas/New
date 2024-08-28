# Create a Calculator program: it should contain an abstract class with methods (abstract and not), base class, geometry, and arithmetic calculator classes.
# Every subclass should have at least 5 methods to make some meaningful calculus operations.


from abc import ABC, abstractmethod
import math

class Calculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def sub(self, a, b):
        pass

    @abstractmethod
    def mul(self, a, b):
        pass

    @abstractmethod
    def div(self, a, b):
        pass

    @abstractmethod
    def pow(self, a, b):
        pass

    @abstractmethod
    def sin(self, a):
        pass

    @abstractmethod
    def cos(self, a):
        pass

class BaseCalculator(Calculator):
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def pow(self, a, b):
        return a ** b

    def sin(self, a):
        return math.sin(a)

    def cos(self, a):
        return math.cos(a)


class GeometryCalculator(Calculator):
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def pow(self, a, b):
        return a ** b

    def sin(self, a):
        return math.sin(a)

    def cos(self, a):
        return math.cos(a)
    

class ArithmeticCalculator(Calculator):
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def pow(self, a, b):
        return a ** b

    def sin(self, a):
        return math.sin(a)

    def cos(self, a):
        return math.cos(a)
    

base = BaseCalculator()
print(f'And the answer is:', base.add(5, 6))
print(f'And the answer is:', base.sub(5, 6))
print(f'And the answer is:', base.mul(5, 6))
print(f'And the answer is:', base.div(5, 6))
print(f'And the answer is:', base.pow(5, 6))
print(f'And the answer is:', base.sin(5))
print(f'And the answer is:', base.cos(5))

geometry = GeometryCalculator()
print(f'And the answer is:', geometry.add(5, 6))
print(f'And the answer is:', geometry.sub(5, 6))
print(f'And the answer is:', geometry.mul(5, 6))
print(f'And the answer is:', geometry.div(5, 6))
print(f'And the answer is:', geometry.pow(5, 6))
print(f'And the answer is:', geometry.sin(5))
print(f'And the answer is:', geometry.cos(5))

arithmetic = ArithmeticCalculator()
print(f'And the answer is:', arithmetic.add(5, 6))
print(f'And the answer is:', arithmetic.sub(5, 6))
print(f'And the answer is:', arithmetic.mul(5, 6))
print(f'And the answer is:', arithmetic.div(5, 6))
print(f'And the answer is:', arithmetic.pow(5, 6))
print(f'And the answer is:', arithmetic.sin(5))
print(f'And the answer is:', arithmetic.cos(5))


