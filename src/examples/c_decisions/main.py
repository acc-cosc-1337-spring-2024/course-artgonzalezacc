import decisions

num = int(input("Enter a number: "))

overtime = decisions.is_overtime(num)

print(overtime)

if(overtime):
    print("You earned overtime.")
else:
    print("No overtime.")

