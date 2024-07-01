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
import heapq
from collections import Counter


def groupSort(arr):
    # Write your code here
    # Count the frequency of each value in the array
    freq_map = Counter(arr)

    # Initialize an empty heap
    heap = []

    # Push frequency-key pairs onto the heap
    for key, freq in freq_map.items():
        heapq.heappush(heap, (-freq, key))  # Using negative frequency for max heap

    # Construct the output list of lists
    sorted_value_freq_lists = []
    while heap:
        freq, key = heapq.heappop(heap)
        sorted_value_freq_lists.append([key, -freq])  # Restoring frequency to positive value

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
