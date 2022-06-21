

import enum


def solv(st):
    temp = st.split()
    t1 = 0
    t2 = 0
    for i,c in enumerate(temp):
        if i<3:
            t1+= int(temp[0])
        else:
            t2+= int(temp[0])
    
    return "YES" if t1==t2 else "NO"










t = int(input()) 
for _ in range(t):
    print(solv(input()))