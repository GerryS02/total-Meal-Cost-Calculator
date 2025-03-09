################################################################
# Project: Utilities
# File: Utilities.py
# Description: Contains various functions to facilitate editing and other
# functions
# Author: Penny Russell
# Version: 1.0
# Date: April 2022
###############################################################

def is_numeric(str_var):
    ################################################################
    # Function: is_numeric
    # Description: examine each character of a string.  determine if
    # a digit 0 - 9.  If all are valid, input is numeric
    # Parameters: str_var
    # Returns: boolean: True if numeric; False if not numeric
    # Version: 1.1
    #          modified to reject input if it is an empty string (line 39)
    # Author: Penny Russell
    ###############################################################
    return_val = True
    index_of_char = 0
    decimal_point_found = False
    if len(str_var) > 0:
        while (index_of_char < len(str_var)) and return_val is True:
            # print(str_var[index_of_char])
            if str_var[index_of_char] < '0' or str_var[index_of_char] > '9':
                if str_var[index_of_char] == '.':
                    if decimal_point_found is True:
                        return_val = False
                    else:
                        decimal_point_found = True
                else:
                    return_val = False
           #bump to next character
            index_of_char += 1
    else:
        print("cannot process empty string")
        return_val = False
        #if return_val is still true, it is numeric
    return return_val




