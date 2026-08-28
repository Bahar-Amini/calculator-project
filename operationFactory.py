from operation import *


class OprationFactory:
    def create(self, operator):
        operations = {
            "+": Addition,
            "/": Division,
            "*": Mulltiplication,
            "-": Subtraction,
        }
        return operations[operator]()
