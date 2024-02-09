def test_config():
    return True

def display_numbers(num):

    cnt = 0

    while cnt <= num: #boolean expression
        cnt = cnt + 1 #a statement that makes the boolean expression false
        print(cnt + 1, cnt, cnt <= num, num)

# sum_of_squares(3)  1 *1 + 2*2 + 3*3 = 14
def sum_of_squares(num): #boolean expression
    sum = 0
    i = 0

    while i <= num:#boolean expression
        sum = sum + i * i
        i = i + 1 #a statement that eventually makes the boolean expression false

    return sum

def prompt_user():
    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':
        keep_going = input('Loop again, type y or Y? ')
        

