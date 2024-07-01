#!/bin/python3

import math
import os
import random
import re
import sys
#https://www.chegg.com/homework-help/questions-and-answers/amazon-uses-smaif-roomba-thaped-robots-called-deives-deimer-lacket-sacks-products-tyuman-w-q118531187

#
# Complete the 'numIdleDrives' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER_ARRAY y
#

def numIdleDrives(x, y):
    # Write your code here
    rows = len(x)
    cols = len(y)
    idle_robots = 0

    for r in range(rows):
        xr = x[r]
        yr = y[r]
        has_robot_above = False
        has_robot_below = False
        has_robot_left = False
        has_robot_right = False

        for c in range(cols):
            if r != c:
                xc = x[c]
                yc = y[c]
                if xc == xr and yc == yr + 1:
                    has_robot_above = True
                if xc == xr and yc == yr - 1:
                    has_robot_below = True
                if xc == xr - 1 and yc == yr:
                    has_robot_left = True
                if xc == xr + 1 and yc == yr:
                    has_robot_right = True
            if has_robot_above and has_robot_right \
                    and has_robot_below and has_robot_left:
                idle_robots += 1
    return idle_robots


if __name__ == '__main__':

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    y_count = int(input().strip())

    y = []

    for _ in range(y_count):
        y_item = int(input().strip())
        y.append(y_item)
    breakpoint()
    result = numIdleDrives(x, y)
