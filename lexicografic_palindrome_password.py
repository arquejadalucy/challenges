#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findEncryptedPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING password as parameter.
#

def findEncryptedPassword(password):
    char_counts = sorted((char, password.count(char)) for char in set(password))
    palindrome = ''
    middle_char = ''
    for char, count in char_counts:
        if count % 2 == 1:
            if middle_char == '':
                middle_char = char
            else:
                return "No palindrome possible"
        palindrome += char * (count // 2)
    return palindrome + middle_char + palindrome[::-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    password = input()

    result = findEncryptedPassword(password)

    fptr.write(result + '\n')

    fptr.close()
