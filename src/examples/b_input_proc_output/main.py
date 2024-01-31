import input_process_output

val1 = int(input("Enter value 1: "))
val2 = int(input("Enter value 2: "))
val3 = int(input("Enter value 3: "))

result = input_process_output.operator_precedence_1(val1, val2, val3)

print(result)

result = input_process_output.operator_precedence_2(val1, val2, val3)

print(result)
