def test_config():
    return True

def create_dictionary():
    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'}
    print(prog_langs['C++'])
    print(prog_langs['C#'])
    #print(prog_langs['c++'])--generates a KeyError; c++ key doesn't exist in the dictionary

def find_key_in_dictionary_with_in(key, prog_langs):
    
    if key in prog_langs:
        print(prog_langs[key])
    else:
        print(key, "key not in dictionary")

def find_key_dictionary_with_not_in(key, prog_langs):
    
    if key not in prog_langs:
        print(key, "key not in dictionary")
    else:
        print(prog_langs[key])

def add_key_pair_to_dictionary(key, value, prog_langs):
    prog_langs[key] = value
        



