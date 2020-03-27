from time import time as detak
from random import shuffle as kocok

def BubbleSort(a):
    x = len(a)
    for i in range (x-1):
        for c in range (x-i-1):
            if a[c] > a[c+i]:
                swap (a, c, c+1)

def SelectionSort(a):
    x = len(a)
    for i in range (x-1):
        S_Index = FindS(a, i, x)
        if S_Index != i :
            swap (a, i, S_Index)

def InsertionSort(a):
    x = len(a)
    for i in range (1, x):
        n = a[i]
        d = i
        while d > 0 and n < a[d-1]:
            a[d] = a[d-1]
            d = d-1
        a[d] = n

def swap (a, b, c):
    d = a[b]
    a[b] = a[c]
    a[c] = d

def FindS(a, startpt, stoppt):
    smallest = startpt
    for x in range (startpt+1, stoppt):
        if a[x] < a[smallest]:
            smallest = x
    return smallest

k = []
for x in range (1, 6001):
    k.append(x)

kocok(k)

u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak(); BubbleSort(u_bub); ak = detak(); print("Bubble : %g detik" %(ak-aw));
aw = detak(); SelectionSort(u_sel); ak = detak(); print("Selection : %g detik" %(ak-aw));
aw = detak(); InsertionSort(u_ins); ak = detak(); print("Insertion : %g detik" %(ak-aw))
