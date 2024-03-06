def test_config():
    return True

def display_list():
    even_numbers = [2,4,6,8,10]
    print(even_numbers[2])

def display_list_while(list1):
    index = 0
    size = len(list1)

    print("Loops\tIndex\tSize\tindex < size\tlist1[index]")

    while(index < size):
        print(str(index+1) + "\t" + str(index)  + "\t" + str(size) + "\t" + str(index < size) + "\t" + str(list1[index]))
        index += 1 #same as index = index + 1
    
def display_list_for_range(list1):

    for index in range(0, len(list1)):
        print(list1[index])

def display_list_for(list1):

    for list_item in list1:
        print(list_item)

def list_parameter(list1):
    list1[0] = 0

def list_parameter_return(list1):
    list1[0] = 0
    return list1

def find_item_in_list(item, list1):
    result = item in list1
    return result

def copy_lists():
    list1 = [1,2,3,4]
    print(list1)

    list2 = list1
    list2[0] = -1

    print(list1)
    print(list2)

def copy_lists_manually():
    list1 = [1,2,3,4]
    list2 = []

    print(list1)

    for num in list1:
        list2.append(num)

    list2[0] = -1
    print(list1)
    print(list2)

def two_dimensional_list():
    students = [['Joe', 'Kim'],['Sam', 'Sue'],['Kelly', 'Chris']]
    print(students[0])
    print(students[1])
    print(students[2])

    print('Select one name')

    print(students[1][1])
    print(students[2][0])

    print('use loop to display')

    for i in range(0, len(students)):
        for j in range(0, len(students[i])):
            print(students[i][j])