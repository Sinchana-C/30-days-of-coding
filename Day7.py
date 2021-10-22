#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    ans=[]
    for i in range(n-1,-1,-1):
        ans.append(arr[i])
    st=" ".join(map(str,ans))
    print(st)
