import input_process_output

input_process_output.display_output()

input_process_output.echo_value("Python")
input_process_output.echo_value("C++")

input_process_output.say_hello("Python learners")

#create variable in the main.py file(program) but use it in functions
result = input_process_output.add_values(5, 5) #create a whole number variable
print(result)

result = 10.99
result = input_process_output.add_values(result, 1.50)
print(result)

result = "10.99"
result = input_process_output.add_values(result, "1.50")
print(result)
