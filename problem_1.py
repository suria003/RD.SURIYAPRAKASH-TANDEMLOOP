# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
# Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
# Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Solutions:
  def __init__(self, a: float, b: float, type: str) -> None:
    self.a = a
    self.b = b
    self.type = type

    match type:

      case 'add':
        self.result = a+b

      case 'subtract':
        self.result = a-b

      case 'multiple':
        self.result = a*b

      case 'divide':
        self.result = a/b

      case _:
        self.result = f'Invalid type is "{type}"'


if __name__ == '__main__':
  a, b = float(input("A value : ")), float(input("B value : "))
  type = input("note: 'add', 'subtract', 'multiple', 'divide' only allowed.\ntype : ") # add, subtract, multiple, divide
  calculator = Solutions(a, b, type)
  print(calculator.result)