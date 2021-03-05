## @file SeqServicesLibrary.py
#  @author Your name
#  @brief Library module that provides functions for working with sequences
#  @details This library assumes that all functions will be provided with arguments of the expected types
#  @date 03/04/2021


def max_val(s):
    if len(s) == 0:
        raise ValueError("Invalid Length of input")
    else :
        maximum = 0
        for i in range(len(s)):
            if abs(s[i]) > abs(maximum):
                maximum = s[i]
        return abs(maximum)
        
def count(t, s):
    if len(s) == 0:
        raise ValueError("Invalid Length of input")
    else :
        counter = 0
        for i in range (len(s)):
            if s[i] == t:
                counter += 1
        return counter

def spices(s):
    if len(s) == 0:
        raise ValueError("Invalid Length of input")
    else :
        output = []
        for i in s:
            if i <= 0:
                output.append("nutmeg")
            else:
                output.append("ginger")                
        return output
        
def new_max_val(s, f):
    if len(s) == 0:
        raise ValueError("Invalid Length of input")
    else :
        new_list = []
        for x in s:
            if f(x) == True:
                new_list.append(x)                
        return max_val(new_list)