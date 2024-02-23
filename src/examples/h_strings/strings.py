def test_config():
    return True

def concat_string(str1, str2):
    return str1 + str2

def concat_string_w_plus_equal(str1, str2):
    str1 += str2 #str1 = str1 + str2
    return str1

def string_params(str):
    str = "Python"

def string_return_value(lang):
    lang = "Python"
    return lang

def get_length_of_string(str):
    return len(str)

def get_number_of_ch_in_string(str, ch):
    index = 0
    count = 0

    while index < len(str):
        if str[index] == ch:
            count += 1
        
        index += 1 

    return count

