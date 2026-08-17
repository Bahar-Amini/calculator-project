from calculator import Calculator 
from validator import Validator 
from operationFactory import OprationFactory
from history import History
from storge import history_storge
class main():
    validator = Validator()
    factory = OprationFactory()
    storage = history_storge.JsonStorage("./data/history.json")
    history = History(storage)
    calculator = Calculator(validator,factory,history)
    result = calculator.calculate(15,"+",5)
    result = calculator.calculate(15,"+",5)
    storage.delete_history()
    print(result)

if __name__=="__main__":
    main()