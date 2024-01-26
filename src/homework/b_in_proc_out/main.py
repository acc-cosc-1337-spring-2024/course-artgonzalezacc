#
import output

result = output.multiply_numbers(5, 5)
print(result)

value1 = input("Enter value 1: ") #get input from the user
value2 = input("Enter value 2: ")

result = output.multiply_numbers(int(value1), int(value2)) #convert to an int
print(result)
