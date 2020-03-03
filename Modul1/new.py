from math import sqrt as sq
from random import randint
def cetakSiku(x):
    a=0
    while(a<=x):
        print (a*('*'))
        a=a+1
    
def gambarlahPersegiEmpat(x,y):
    a=0
    print (y*('@'))
    while(a<x-2):
        print ('@'+(y-2)*(' ')+'@')
        a=a+1
    print (y*('@'))

def jumlahHurufVokal(x):
    k=len(x)
    a=('AEIOUaeiou')
    b=0
    for c in x :
        if c in a :
            b=b+1
    d =[k,b]
    print(d)

def jumlahHurufKonsonan(x):
    k=len(x)
    a=('AEIOUaeiou')
    b=0
    for c in x :
        if c not in a :
            b=b+1
    d =[k,b]
    print(d)

def rerata(b):
    a=len(b)
    c=0
    d=0
    while (c<a) :
       d=d+b[c]
       c=c+1
    print (d/a)

def prime(x):
    x=int(x)
    assert x>=0
    sp = [2,3,5,7,11]
    nsp = [0,1,4,6,8,9,10]
    if x in sp:
        return True
    elif x in nsp:
        return False
    else :
        for i in range(2,int(sq(x))+1):
            if ((x%i)==0) :
                return False
            elif (i>=int(sq(x))):
                return True
            else :
                continue

def writeprime():
    f=[]
    for i in range (2,1000):
        x=True
        for a in range(2,i):
            if (i%a==0):
                x=False
        if (x==True):
            f.append(i)
    print(f)
def faktorPrima(x):
    x=int(x)
    assert x>=0
    fp=[]
    a=2
    while (a<=x):
        if (x%a==0):
            x=x/a
            fp.append(a)
        else :
            a=a+1
    print(fp)

def apakahTerkandung(a,b):
    a=a.lower()
    b=b.lower()
    if a in b :
        return True
    else :
        return False

def cetak():
    for i in range (1,100):
        if (i%3==0):
            if(i%5==0):
                print("Python UMS")
            else :
                print("Python")
        elif (i%5==0):
            print ("UMS")
        else :
            print (i)

def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if (D<0):
        print ("Determinannya negatif. Persamaan tidak mempunyai akar real")
    else :
        x1=(-b+sq(D))/(2*a)
        x2=(-b-sq(D))/(2*a)
        hasil=[x1,x2]
        print(hasil)

def apakahKabisat(x):
    if(x%4==0):
        if (x%100==0):
            if(x%400==0):
                return True
            else:
                return False
        else :
            return True
    else :
        return False
            
def tebakAngka():
    x=0
    a=randint(1,101)
    b=-100
    print ("Permainan Tebak Angka\nSaya Menyimpan sebuah Angka Bulat antara 1 sampai 100. Coba Tebak.")
    while (b!=a):
        x+=1
        b=input("Masukkan tebakkan ke-"+str(x)+" : ")
        b=int(b)
        if (b<a):
            print("Itu terlalu kecil")
        elif (b>a):
            print("Itu terlalu besar")
        if (b==a):
            print ("Ya anda benar")

def katakan(bilangan):
    angka=["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh",
           "Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = " "
    n = int(bilangan)
    if n>=0 and n<=11:
        Hasil = Hasil +angka[n]
    elif n<20:
        Hasil = katakan(n % 10) + " Belas"
    elif n<100:
        Hasil = katakan(n / 10) + " Puluh" + katakan(n%10)
    elif n<200:
        Hasil = " Seratus" + katakan(n-100)
    elif n<1000:
        Hasil = katakan(n/100) + " Ratus" + katakan(n%100)
    elif n<2000:
        Hasil = " Seribu" + katakan(n-1000)
    elif n<10000:
        Hasil = katakan(n/1000) + " Ribu" + katakan(n%1000)
    elif n<20000:
        Hasil = " Sepuluh Ribu" + katakan(n-10000)
    elif n<100000:
        Hasil = katakan(n/10000) + " Puluh" + katakan(n%10000)
    elif n<200000:
        Hasil = " Seratus Ribu" + katakan(n-100000)
    elif n<1000000:
        Hasil = katakan(n/100000) + " Ratus" + katakan(n%100000)
    elif n<2000000:
        Hasil = " Satu Juta" + katakan(n-1000000)
    elif n<10000000:
        Hasil = katakan(n/1000000) + " Juta" + katakan(n%1000000)
    elif n==10000000:
        Hasil = "Satu Milyar" + katakan(n%10000000)
    else:
        Hasil = "Angka Hanya Sampai Satu Milyar"
    return Hasil

def formatRupiah(bilangan):
    a = str (bilangan)
    if len(a) <= 3 :
         return "Rp " + a
    else :
         y = a[-3:]
         z = a[:-3]
         return formatRupiah(z) + "." + y
         print  ("Rp ") + formatRupiah(z) + "." +y


      
