class Calculator():
    def __init__(self,validator,factory,history):
        self.validator = validator 
        self.factory = factory 
        self.history = history
    def calculate(self,a,operator,b):
        self.validator.validate_numbers(a,b)
        self.validator.validate_operator(operator)
        operation = self.factory.create(operator)
        result = operation.execute(a,b)
        expression = f"{a} {operator} {b}"
        self.history.add(expression,result)
        return result

        