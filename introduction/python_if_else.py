#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    remainder = n % 2
    if remainder == 1:
        print("Weird")
    else:
        if n in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")