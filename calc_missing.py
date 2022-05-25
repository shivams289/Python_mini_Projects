#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#
import numpy as np
from scipy import interpolate as si
def calcMissing(readings):
    # Write your code here
    N = len(readings)
    data , price, target = [] ,  [] ,  []
    for i in range(N) :
        sharma = readings[i]
        val = sharma.split(" ")[1].split("\t")[1]
        if "Missing" in val:
            target.append(i+1)
        else:
            data.append(i+1)
            price.append(float(val))
    price = np.array(price)
    inter = si.UnivariateSpline(data, price, s=1)
    
    for a in target:
        print(inter(a))
if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)
