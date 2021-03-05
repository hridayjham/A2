## @file SeqServicesLibrary.py
#  @author Hriday Jham
#  @brief Library module that provides functions for working with sequences
#  @details This library assumes that all functions will be provided with arguments of the expected types
#  @date 03/04/2021

#returning the maximum asbolute value
def max_val(s):
    if len(s) == 0:
        raise ValueError("Invalid Length of input")
    else :
        maximum = -1
        for i in range(len(s)):
            if abs(s[i]) > abs(maximum):
                maximum = s[i]
        return abs(maximum)
   
#returning the occurences of t in the Sequence s     
def count(t, s):
    if len(s) == 0:
        raise ValueError("Invalid Length of input")
    else :
        counter = 0
        for i in range (len(s)):
            if s[i] == t:
                counter += 1
        return counter

#Returns a customized Sequence
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
        
#Returns the maximum absolute value after applying f to the sequence
def new_max_val(s, f):
    if len(s) == 0:
        raise ValueError("Invalid Length of input")
    else :
        new_list = []
        for x in s:
            if f(x) == True:
                new_list.append(x)                
        return max_val(new_list)