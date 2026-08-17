from abc import ABC,abstractmethod
class Operation(ABC):
    @abstractmethod
    def execute(self,a,b):
        pass

class Addition(Operation):
    def execute(self,a,b):
        return a + b

class Division(Operation):
    def execute(self,a,b):
        if a ==0:
            return ValueError
        return a / b

class Mulltiplication(Operation):
    def execute(self,a,b):
        return a * b

class Subtraction(Operation):
    def execute(self,a,b):
        return a - b

