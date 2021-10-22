#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    m=int(10)
    for i in range(1,m+1):
        print(n,"x",i,"=",n*i)
