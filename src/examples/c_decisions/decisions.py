def test_config():
    return True

def get_and_result(bool1, bool2):
    result = bool1 and bool2
    return result

def get_or_result(bool1, bool2):
    result = bool1 or bool2
    return result

def get_not_result(bool1):
    result = not bool1
    return result

def is_even(num):
    remainder = num % 2 # the remainder of 4/2 = 0   
    return remainder == 0 # 0 == 0

def is_odd(num):
    remainder = num % 2 # 3 / 2 remainder is 1
    return remainder == 1 #returns True or False --> it's a boolean expression

def is_vowel(letter):
    result = letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'

    return result

def is_overtime(hours):
    return hours > 40