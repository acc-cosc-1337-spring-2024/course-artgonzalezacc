import decisions

year = int(input("Enter a year: "))

generation = decisions.get_generation(year)

print(year, " is ", generation)
