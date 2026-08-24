class Calculator():
    def __init__(self,validator,factory,history):
        self.validator = validator 
        self.factory = factory 
        self.history = history
    def calculate(self,a,operator,b):
        num1,num2 = self.validator.validate_numbers(a,b)
        self.validator.validate_operator(operator)
        operation = self.factory.create(operator)
        result = operation.execute(num1,num2)
        expression = f"{num1} {operator} {num2}"
        self.history.add(expression,result)
        return result

        