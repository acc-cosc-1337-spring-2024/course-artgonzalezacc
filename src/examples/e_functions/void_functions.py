#
def say_hello(name): #name - is a parameter (variable)
    val = "C++"
    print("Hello " + name + " " + val)

def hello_world():
    val = "Hello World" #local function variables
    print(val)

val2 = 5 #global variables

def use_global_variable():
    print(val2)

def use_global_variable_1():
    print(val2)

def try_change_global_variable():
    val2 = 10
    print("Local: ", val2)

def change_global_variable():
    global val2 #tell python we want to use the val2 global variable
    val2 = 10
    print(val2)

def use_global_variable_w_param(val2):
    val2 = 10
    print("Local: ", val2)