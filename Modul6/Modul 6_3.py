from time import time as detak
from random import shuffle as kocok
import time
k = [i for i in range(1,6001)]
kocok(k)

def bubbleSort(X) :
    n = len(X)
    for i in range(n):
        for j in range(0, n-i-1):
            if X[j] > X[j+1] :
                X[j], X[j+1] = X[j+1], X[j]

def selectionSort(X) :
    for i in range(len(X)): 
        min_idk = i 
        for j in range(i+1, len(X)): 
            if X[min_idk] > X[j]: 
                min_idk = j         
        X[i], X[min_idk] = X[min_idk], X[i]

def insertSort(X) :
    n = len (X)
    for i in range (1, n) :
        nilai = X[i]
        abc = i-1
        while abc >= 0 and nilai < X[abc-1] :
            X[abc] = X[abc+1]
            abc -=1
        X[abc+1] = nilai

    
def mergeSort(X): 
    if len(X) >1: 
        mid = len(X)//2 
        L = X[:mid] 
        R = X[mid:] 
        mergeSort(L) 
        mergeSort(R) 
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                X[k] = L[i] 
                i+=1
            else: 
                X[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            X[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            X[k] = R[j] 
            j+=1
            k+=1
def partition(X,low,high): 
    i = ( low-1 )        
    pivot = X[high]    
    for j in range(low , high): 
        if   X[j] <= pivot: 
            i = i+1 
            X[i],X[j] = X[j],X[i] 
    X[i+1],X[high] = X[high],X[i+1] 
    return ( i+1 ) 
  
def quickSort(X,low,high): 
    if low < high: 
        pi = partition(X,low,high) 
        quickSort(X, low, pi-1) 
        quickSort(X, pi+1, high)

u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
u_mer = k[:]
u_qck = k[:]

aw = detak () ; bubbleSort (u_bub) ; ak = detak() ; print('bubble : % g detik' % (ak - aw)) ;
aw = detak () ; selectionSort (u_sel) ; ak = detak() ; print('selection : % g detik' % (ak - aw)) ;
aw = detak () ; insertSort (u_ins) ; ak = detak() ; print('insert : % g detik' % (ak - aw)) ;
aw = detak () ; mergeSort (u_mer) ; ak = detak() ; print('merge : % g detik' % (ak - aw)) ;
aw = detak () ; quickSort (u_qck, 0, len(u_qck)-1) ; ak = detak() ; print('quick : % g detik' % (ak - aw)) ;
