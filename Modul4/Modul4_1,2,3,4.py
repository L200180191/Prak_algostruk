from MhsTIF import *
c0=MhsTIF("Ika",10,"Sukoharjo",230000)
c1=MhsTIF("Budi",51,"Sragen",230000)
c2=MhsTIF("Ahmad",2,"Surakarta",250000)
c3=MhsTIF("Chandra",18,"Surakarta",235000)
c4=MhsTIF("Eka",4,"Boyolali",240000)
c5=MhsTIF("Fandi",31,"Salatiga",250000)
c6=MhsTIF("Deni",13,"Klaten",245000)
c7=MhsTIF("Galuh",5,"Wonogiri",245000)
c8=MhsTIF("Janto",23,"Klaten",245000)
c9=MhsTIF("Hasan",64,"Karanganyar",270000)
c10=MhsTIF("Khalid",29,"Purwodadi",265000)
Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
def cariKota(target):
    x=[]
    for i in Daftar :
        if i.kotaTinggal==target:
            x.append(Daftar.index(i))   
    print (x)
def cariusk():
    n = len(Daftar)
    x=[]
    terkecil=Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku == terkecil :
            x.append(i.nama)
            terkecil=i.uangSaku
        elif i.uangSaku < terkecil :
            x=[]
            terkecil=i.uangSaku
    print (x, ' adalah mahasiswa dengan uang saku terkecil dengan nominal ', terkecil)
def cariusk_2():
    n = len(Daftar)
    x=[]
    terkecil=Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku == terkecil :
            x.append(i)
            terkecil=i.uangSaku
        elif i.uangSaku < terkecil :
            x=[]
            x.append(i)
            terkecil=i.uangSaku
    for i in range(len(x)):
        print(x[i])
def cariusb():
    n = len(Daftar)
    terbesar=Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku > terbesar :
            nama = i.nama
            terbesar=i.uangSaku
    print (nama, ' adalah mahasiswa dengan uang saku terbesar dengan nominal ', terbesar)
def lebih():
    n = len(Daftar)
    x=[]
    terbesar=Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku > 250000 :
            x.append(i.nama)
    print ('mahasiswa dengan uang saku lebih dari 250 ribu rupiah adalah : ', x)

def kurang():
    n = len(Daftar)
    x=[]
    terbesar=Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku < 250000 :
            x.append(i)
    for i in range(len(x)):
        print(x[i])   
