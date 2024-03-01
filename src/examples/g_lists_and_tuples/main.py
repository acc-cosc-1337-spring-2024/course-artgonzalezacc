#main program
import lists

nums = [9,1,0,2,8,5,7,4,3,6]

item = int(input("Enter number: "))

if item in nums:
    nums.remove(item)
    print("item removed")
else:
    print("Item not in list.")

for num in nums:
    print(num)