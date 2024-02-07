import decisions

num = int(input("Enter a number: "))
result = decisions.is_even(num)

if(result == True):
    print("Even ", result)
else:
    print("Number is not Even")

result = decisions.is_odd(num)

if(result == True):
    print("Odd ", result)
else:
    print("Number is not Odd")
