import os

import history
from calculator import Calculator
from operationFactory import OprationFactory
from storge import history_storge
from validator import Validator


class main:
    validator = Validator()
    factory = OprationFactory()
    storage = history_storge.JsonStorage("./data/history.json")
    history_ = history.History(storage)
    calculator = Calculator(validator, factory, history_)
    while True:
        print("==============Calculator Program===============", end="\n")
        print("1)calculation Menu")
        print("2)History")
        print("0)Exit")
        choice = input("your choice(1/2/0):")
        os.system("cls")
        if choice == "1":
            while True:
                try:
                    operation = input("Enter Operation:(+,-,/,*) ")
                    num1 = input("Enter first number: ")
                    num2 = input("Enter second number: ")
                    result = calculator.calculate(num1, operation, num2)
                    print(f"{num1} {operation} {num2} : {result}")
                    os.system("pause")
                    os.system("cls")
                    break
                except ValueError as error:
                    print(error)
                    os.system("pause")
                    os.system("cls")
        elif choice == "2":
            while True:
                print("==============History Menu===============", end="\n")
                print("1)Show history")
                print("2)Clear history")
                print("0)Exit")
                choice = input("your choice(1/2/0):")
                match choice:
                    case "1":
                        history_.get_history()
                        os.system("pause")
                        os.system("cls")
                    case "2":
                        history_.delete()
                        print("history deleted")
                        os.system("pause")
                        os.system("cls")
                    case "0":
                        os.system("cls")
                        break
                    case "_":
                        print("Invalid input")
                        os.system("pause")
                        os.system("cls")
        elif choice == "0":
            break
        else:
            print("Invalid input")
            os.system("pause")
            os.system("cls")


if __name__ == "__main__":
    main()
