#! /user/bin/python3

# file: planina.py

# date: 23 jan 20232

import sys 

def main(): 
    line = sys.stdin.readline()
    line.strip()
    n = int(line)

    s = 2
    for i in range(n):
        s = s + (s-1)
    
    print(s *s)

if __name__ == "__main__":
    main()