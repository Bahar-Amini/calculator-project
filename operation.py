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
        try:
            return a/b
        except :
            raise ZeroDivisionError("Division By zero error")
            
class Mulltiplication(Operation):
    def execute(self,a,b):
        return a * b

class Subtraction(Operation):
    def execute(self,a,b):
        return a - b

