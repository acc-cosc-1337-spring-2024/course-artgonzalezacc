#main program
import dictionaries

prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
print(prog_langs)

key = input("Enter key: ")
value = input("Enter value: ")

dictionaries.add_key_pair_to_dictionary(key, value, prog_langs)

print(prog_langs)