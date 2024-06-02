from art import logo


#Functions for mathematic operation
def add(n1, n2):
  return n1 + n2


def sub(n1, n2):
  return n1 - n2


def mul(n1, n2):
  return n1 * n2


def div(n1, n2):
  return n1 / n2


def squ(n1, n2):
  return n1**n2


operations = {"+": add, '-': sub, '*': mul, '/': div, '^': squ}


#main function to calculate numbers
def calculator():
  num1 = float(input("Enter First number : "))
  for key in operations:
    print(key)
  CalculateAgain = True

  while CalculateAgain:
    operation_Symbol = input("Enter a Symbol from above line : ")
    num2 = float(input("Enter next number : "))
    function = operations[
        operation_Symbol]  #function = operation['+'] -----> function = add
    total = round(function(num1, num2),2)  #total = add(num1,num2)
    print(f"{num1} {operation_Symbol} {num2} = {total}")
    num1 = total

    again = input(
        f"type 'y' to continue with {total}. type 'n' to new calculation. type 'e' for exit :"
    )
    if again == 'e':
      CalculateAgain = False
    elif again == 'n':
      calculator()


print(logo)
calculator()
