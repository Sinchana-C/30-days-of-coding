#!/bin/python3

import math
import os
import random
import re
import sys
def factorial(n):
    ans=1
    for i in range(n,0,-1):
        ans=ans*i
    return ans
print(factorial(int(input())))
