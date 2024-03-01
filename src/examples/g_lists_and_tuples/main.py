#main program
import lists

prods = ["V475", "F987", "Q143", "R688"]

item = input("Enter item number: ")

result = lists.find_item_in_list(item, prods)

if(result):
    print("Item found")
else:
    print("Item not in list")