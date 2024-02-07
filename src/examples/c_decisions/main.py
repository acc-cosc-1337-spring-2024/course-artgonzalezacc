import decisions

num = int(input("Enter a number: "))
result = decisions.is_even(num)

if(result == True):
    print("Even ", result)

result = decisions.is_odd(num)

if(result == True):
    print("Odd ", result)
