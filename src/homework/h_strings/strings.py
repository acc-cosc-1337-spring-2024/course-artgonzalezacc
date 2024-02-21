#
def loop_string_w_while(str):
    index = 0
    size = len(str) #size of the string

    while(index < size):
        print(str[index])
        index += 1

def loop_string_w_for_range(str):

    size = len(str)
    for index in range(0, size):
        print(str[index])

def loop_string_w_for(str):

    for ch in str:
        ch = '9'
        print(ch)
    
    print(str)