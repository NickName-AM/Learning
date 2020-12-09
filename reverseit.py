def reverseit(a):

    # Reverse function for float type
    def float_reverseit(a):
        str_converter = str(a)  #Convert float value into string
        reversed_str = str_converter[::-1]  #Reverse the string
        to_return = float(reversed_str)  #Convert string into float value
        return to_return

    # Reverse function for int type
    def int_reverseit(a):
        str_converter = str(a)  #Convert int value into string
        reversed_str = str_converter[::-1]   #Reverse the string
        to_return = int(reversed_str)   #Convert string into int value
        return to_return

    # Reverse function for string type
    def str_reverseit(a):
        to_return = a[::-1]  #Reverse the string
        return to_return

    if type(a) == float:
        return float_reverseit(a)
    elif type(a) == int:
        return int_reverseit(a)
    else:
        return str_reverseit(a)
