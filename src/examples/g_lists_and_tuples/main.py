#main program
import lists

my_read_only_list = (1,2,3,4) #tuple

print(my_read_only_list)

print(my_read_only_list[2])

if 4 in my_read_only_list:
    print('4 exists')

index = my_read_only_list.index(2)

print(index)

print(len(my_read_only_list))