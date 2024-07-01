#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    k = k % len(alphabet)
    k_first_letters = alphabet[:k]
    new_alphabet = alphabet.replace(k_first_letters, "") + k_first_letters

    letters_map = {}
    for i in range(len(alphabet)):
        letters_map.update({
            alphabet[i]: new_alphabet[i],
            alphabet[i].upper(): new_alphabet[i].upper()
        })

    encripted_s = ""
    for i in range(len(s)):
        char = s[i]
        if char in letters_map.keys():
            encripted_s += letters_map[char]
        else:
            encripted_s += char

    return encripted_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
