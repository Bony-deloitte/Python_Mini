class FormulaError(Exception): pass


def inputvalue(user_input):

  input_list = user_input.split()
  if len(input_list) != 3:
    raise FormulaError('Input do not have three elements')
  a1, operator, b1 = input_list
  try:
    a1 = float(a1)
    b1 = float(b1)
  except ValueError:
    raise FormulaError('The first and third value in input must be numbers')
  return a1, operator, b1


def calculate(a1, operator, b1):

  if operator == '+':
    return a1 + b1
  if operator == '-':
    return a1 - b1
  if operator == '*':
    return a1 * b1
  if operator == '/':
    return a1 / b1
  raise FormulaError('{0} is not a valid operator'.format(operator))

while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  a1, operator, b1 = inputvalue(user_input)
  result = calculate(a1, operator, b1)
  print(result)