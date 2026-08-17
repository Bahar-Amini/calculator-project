class Validator():
    @staticmethod
    def validate_numbers(a,b):
        if not isinstance(a,int):
            raise ValueError("enter integer")
        if not isinstance(b,int):
            raise ValueError("enter integer")
    @staticmethod
    def validate_operator(operator):
        operate = ("/","*","+","-")
        if operator not in operate :
            raise ValueError("the operater must be (*,/,+,,-)")
        if not isinstance(operator,str):
            raise ValueError("the operator must be string")

