from LatOOP3 import *
class SiswaSMA(Manusia):
    def __init__(self):
        self.nama = str(input("Masukkan nama : "))
        self.NIS = str(input("Masukkan NIS : ")) 
        self.uangSaku= int(input("Masukkan jumlah uang saku : "))
    def __str__(self):
        a = self.nama +', NIS '+str(self.NIS)\
            +'. Uang saku Rp '+str(self.uangSaku)\
            +' tiap bulannya'
        return a
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,a):
        print('Saya baru saja makan ',a,' di kantin sekolah.')
        self.keadaan='kenyang'
    def tambahUangSaku(self,a):
        self.uangSaku+=a
