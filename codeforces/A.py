

import enum


def solv(inp):
    temp = []
    if inp==1:
        return 0
    temp = [int(c) for c in input().split()]
    m,i = min(temp), temp.index(min(temp))
    for j in range(len(temp)):
        temp[j] = temp[j]-m
    return sum(temp)


t = int(input()) 
for _ in range(t):
    print(solv(int(input())))