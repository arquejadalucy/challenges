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

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def quick_sort_reverse(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i >= pivot]  # Alterado para i >= pivot
        greater = [i for i in array[1:] if i < pivot]  # Alterado para i < pivot
        return quick_sort_reverse(less) + [pivot] + quick_sort_reverse(greater)


def quick_sort_list(lista: list[list]):
    if len(lista) < 2:
        return lista
    else:
        pivot = lista[0]
        less = [item for item in lista[1:] if item[0] <= pivot[0]]
        greater = [item for item in lista[1:] if item[0] > pivot[0]]
        return quick_sort_list(less) + [pivot] + quick_sort_list(greater)


def quick_sort_list_reverse_by_freq(lista: list[list]):
    if len(lista) < 2:
        return lista
    else:
        pivot = lista[0]
        less = [item for item in lista[1:] if item[1] >= pivot[1]]
        greater = [item for item in lista[1:] if item[1] < pivot[1]]
        return quick_sort_list_reverse_by_freq(less) + [pivot] + quick_sort_list_reverse_by_freq(greater)


def groupSortTest(arr):
    # Write your code here
    result = {}
    for n in set(arr):
        count = arr.count(n)

    result.update({n: arr.count(n)})

    result = quick_sort_list_reverse_by_freq(result)
    result = quick_sort_list(result)

    return result


def groupSort(arr):
    # Write your code here
    freq_map = {}
    for n in set(arr):
        freq_map.update({n: arr.count(n)})

    sorted_arr = sorted(freq_map, key=lambda x: (-freq_map[x], x))
    return sorted_arr
