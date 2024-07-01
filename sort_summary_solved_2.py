#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'groupSort' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from collections import Counter


def groupSort(arr):
    # Conta a frequência de cada valor no array
    freq_map = Counter(arr)

    # Ordena as chaves do dicionário com base nas frequências e nos valores
    sorted_keys = sorted(freq_map.keys(), key=lambda x: (-freq_map[x], x))

    # Cria a lista de listas contendo cada valor e sua frequência, ordenada
    sorted_value_freq_lists = [[key, freq_map[key]] for key in sorted_keys]

    return sorted_value_freq_lists


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = groupSort(arr)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
