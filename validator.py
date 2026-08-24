class Validator():
    @staticmethod
    def validate_numbers(a,b):
        try:
            return float(a),float(b)
        except:
            raise ValueError("please enter a valid integer.")
    @staticmethod
    def validate_operator(operator):
        operate = ("/","*","+","-")
        if operator not in operate :
            raise ValueError("the operater must be (*,/,+,,-)")
        if not isinstance(operator,str):
            raise ValueError("the operator must be string")
    

        

