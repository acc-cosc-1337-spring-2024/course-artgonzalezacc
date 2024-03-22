#main program
import dictionaries

prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}

key = input("Enter key: ")

dictionaries.find_key_dictionary_with_not_in(key, prog_langs)