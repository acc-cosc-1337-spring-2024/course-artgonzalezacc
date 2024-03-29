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

def display_number_for(num):
    for val in range(1, num+1) :#val is a target variable
        print(val)

def sum_of_squares_for(num):
    sum = 0

    for val in range(1, num + 1):
        sum = sum + val * val

    return sum

def loop_a_list():
    for num in [1,2,3,4,5]:
        print(num)

def loop_a_word_list():
    for word in ["C", "C++", "Java", "Python"]:
        print(word)

def sum_of_squares_user_controlled():
    keep_going = 'y'

    while keep_going == 'y' or keep_going == 'Y':
        val = int(input('Enter a number: '))
        result = sum_of_squares(val)

        print(result)

        keep_going = input('To continue, enter y or Y: ')

def for_num_range_w_step_value(num1, num2, step):

    for n in range(num1, num2+1, step):
        print(n)

def get_sum__for(num): # 3 ---> 1 + 2 + 3 = 6
    sum = 0

    for n in range(num): 
        sum += n + 1 #is the same as sum = sum + n + 1
    
    return sum

def while_validate_user_input():
    lot_number = -1

    while(lot_number != 0):
        lot_number = input("Enter number from 1-10 or 0 to exit: ")

        if(lot_number.isnumeric()):
            lot_number = int(lot_number) #lot_number is a valid number, convert it to int(while number )

            if(lot_number != 0):
            
                while(not(lot_number >= 1 and lot_number <= 10)):
                    lot_number = int(input("Number not in range, please enter number from 1-10 or 0 to exit: "))

                print("Valid number entered ", lot_number)

            else:
                print("Program will exit")
        
        else:
            print("Value is not a number, please try again.")


    print('Exiting...')

def nested_while_loop(row, col):

    i = 0

    while(i < row):
        print("i:", i , "outer loop - wait for inner loop")
        i += 1
        j = 0

        while(j < col):
            print("j:", j, "\t inner loop -maker outer loop wait")
            j += 1

def while_multiplication_table(row, col):
    r = 0

    while r < row:    
        c = 0

        while c < col:
            product = (r + 1) * (c + 1)
            print(str(product).rjust(3, " "), end=" ")
            c += 1
        
        r += 1

        print(" ")
