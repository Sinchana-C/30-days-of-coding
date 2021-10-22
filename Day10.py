#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
res=0
max=0
while n>0:
    if n%2==1:
        res=res+1
        if res>max:
            max=res
    else:
        res=0
    n//=2
print(max)
