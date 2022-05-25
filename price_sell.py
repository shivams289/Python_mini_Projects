#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'valuation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER reqArea
#  2. LONG_INTEGER_ARRAY area
#  3. LONG_INTEGER_ARRAY price
#
import statistics as s
from collections import defaultdict
import numpy as np
def remove_outliers(area, price):
    val = dict()
    res = []
    for i, j in enumerate(area):
        if j not in val.keys():
            val[j] = [i]
        else:
            val[j].append(i)
            
    for k, v in val.items():
        if len(v) == 1:
            res.append(v[0])
            
        else:
            p = list(map(lambda x:price[x], v))
            mean_ = sum(p)/len(p)
            std_ = s.pstdev(p)
            for i in v:
                if abs(price[i] - mean_) <= 3*std_:
                    res.append(i)
                    
    return res
                
            


    
def interpolate(x1, y1, x2, y2, x):
    ans = y1 + (y2 - y1)/(x2-x1) *(x-x1)
    return ans 
                
         

def valuation(reqArea, area, price):
    # Write your code here
    dt = defaultdict(list) 
    ap = zip(area, price)
    
    for a in ap:
        dt[a[0]].append(a[1]) 
    res = [] 
    
    for a in dt :
        lt = dt[a] 
        if len(lt) == 1:
            res.append((a, dt[a][0])) 
        else:
            for i in range(len(lt)):
                c = []
                for j in range(len(lt)):
                    if i!=j:
                        c.append(lt[j]) 
                mean_ = np.mean(c)
                std = np.std(c) 
                if abs(lt[i] - mean_) <= 3*std:
                    res.append((a, lt[i])) 
    if res == []:
        return 1000 
    if len(res) ==1 :
        return res[0][1] 
    lt2 = [] 
    for a in res:
        if a[0] == reqArea:
            lt2.append(a[1]) 
    if lt2 != []:
        return sum(lt2)/len(lt2) 
    dt3 = defaultdict(list)
    
    for a in res:
        dt3[a[0]].append(a[1])
    res2 = [] 
    for a in dt3:
        mean_ = sum(dt3[a])/len(dt3[a])
        res2.append((a , mean_))
    res2.sort() 
    
    if reqArea < res2[0][0]:
        x1, y1 , x2 , y2 , x = res2[0][0], res2[0][1] , res2[1][0], res2[1][1], reqArea
        return interpolate(x1, y1 , x2 , y2 , x)
    if reqArea > res2[-1][0]:
        x1, y1 , x2 , y2 , x = res2[-2][0], res2[-2][1] , res2[-1][0], res2[-1][1], reqArea
        return interpolate(x1, y1 , x2 , y2 , x)
       
    i = 0 
    while i < len(res2):
        if res2[i][0] < reqArea :
            i+=1 
        else:
            break 
    x1, y1 , x2 , y2 , x = res2[i-1][0], res2[i-1][1] , res2[i][0], res2[i][1], reqArea 
        
    return interpolate(x1, y1 , x2 , y2 , x)
    
    
        
    
                
        
    
    
            
            
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    reqArea = int(input().strip())

    area_count = int(input().strip())

    area = []

    for _ in range(area_count):
        area_item = int(input().strip())
        area.append(area_item)

    price_count = int(input().strip())

    price = []

    for _ in range(price_count):
        price_item = int(input().strip())
        price.append(price_item)

    result = int(round(valuation(reqArea, area, price), 0))
    if result < 10**3 :
        result = 10**3 
    if result > 10**6:
        result = 10**6
    fptr.write(str(result) + '\n')

    fptr.close()
