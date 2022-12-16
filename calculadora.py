def calculator():
  # Obtener los operandos del usuario
  num1 = float(input("Ingrese el primer número: "))
  num2 = float(input("Ingrese el segundo número: "))

  # Obtener la operación deseada del usuario
  operation = input("Ingrese la operación deseada (+, -, *, /): ")

  # Realizar la operación y mostrar el resultado
  if operation == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
  elif operation == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
  elif operation == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
  elif operation == "/":
    result = num1 / num2
    print(num1, "/", num2, "=", result)
  else:
    print("Operación inválida. Por favor, ingrese una operación válida.")

# Llamar a la función calculator
calculator()
