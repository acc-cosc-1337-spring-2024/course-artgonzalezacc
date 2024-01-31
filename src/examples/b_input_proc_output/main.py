import input_process_output

value = input("Enter value: ")
result = input_process_output.add_values(value, value) #treats the value variable as a string
print(result)


value = input("Enter value: ") #reads values from keyboard as string(alphanumeric)
result = input_process_output.add_values(int(value), int(value)) #convert alpha to int(whole number) or float(decimal number)
print(result)

value = input("Enter value: ") #reads values from keyboard as string(alphanumeric)
result = input_process_output.add_values(float(value), float(value)) #convert alpha to int(whole number) or float(decimal number)
print(result)

