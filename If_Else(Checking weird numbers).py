import math
import os
import random
import re
import sys

n=int(input("Enter and number between 1 to 100 ").strip())

if n<1 or n>100:
    print("Invalid Range")
else:
    if n%2!=0:
        print("Weird")
    elif n%2==0 and 2<n<5:
        print("Not Weird")
    elif n%2==0 and 6<n<=20:
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")
