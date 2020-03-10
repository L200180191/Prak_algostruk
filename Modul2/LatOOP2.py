class Pesan(object):
    def __init__(self,sebuahString):
        self.teks=sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumkar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai ',str(len(self.teks))," karaketer.")
    def perbarui(self,stringBaru):
        self.teks=stringBaru
    def apakahTerkandung(self,a):
        a.lower()
        if a in self.teks.lower() :
            return True
        else :
            return False
    def hitungKonsonan(self):
        a=('AEIOUaeiou')
        b=0
        for c in self.teks :
            if c not in a :
                b=b+1
        print(b)
    def hitungVokal(self):
        a=('AEIOUaeiou')
        b=0
        for c in self.teks :
            if c in a :
                b=b+1
        print(b)
