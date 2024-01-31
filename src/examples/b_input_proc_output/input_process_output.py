#output comments variables input calculations output constants
def display_output():
    print('hello')

def test_config():
    return True

def echo_value(value):
    print(value)

def say_hello(name):
    #sequence of characters -- string 
    display_value = "Hello " + name #display_value will hold the value of Hello Python(if the value that the name variables holds is Python)
    print(display_value)

def add_values(num1, num2):
    result = num1 + num2 #doing calculations/ return the value to make the function testable

    return result

def floating_point_division(val1, val2):
    result = val1 / val2
    return result

def integer_division(val1, val2):
    result = val1 // val2
    return result

def operator_precedence_1(val1, val2, val3):
    result = val1 + val2 / val3
    return result

def operator_precedence_2(val1, val2, val3):
    result = (val1 + val2) / val3
    return result

