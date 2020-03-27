from LatOOP4 import Mahasiswa
class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Python is cool")

m1=MhsTIF("Budi",131,"Sleman",300000)
m2=MhsTIF("Ahmad",213,"Jambi",2000000)
m3=MhsTIF("Erik",125,"Jakarta",1750000)
m4=MhsTIF("Zainuddin",141,"Depok",1000000)
m5=MhsTIF("Andre",172,"Tangerang",800000)
m6=MhsTIF("Putri",192,"Klaten",300000)
m7=MhsTIF("Fatimah",181,"Depok",900000)
m8=MhsTIF("Nurul",113,"Karanganyar",200000)
m9=MhsTIF("Jason",138,"Jakarta",1500000)
m10=MhsTIF("Bagoes",159,"Semarang",500000)

def arrange(x):
    for i in range (len(x)-1, 0, -1):
        for a in range (i):
            if x[a] > x[a+1]:
                c = x[a]
                x[a] = x[a+1]
                x[a+1] = c
    print(x)

    
def arrange_TO(f,g):
    x=f+g
    for i in range (len(x)-1, 0, -1):
        for a in range (i):
            if x[a] > x[a+1]:
                c = x[a]
                x[a] = x[a+1]
                x[a+1] = c
    print(x)
