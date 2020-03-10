from LatOOP3 import Manusia 
class Mahasiswa(Manusia):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM= NIM
        self.kotaTinggal=kota
        self.uangSaku=us
    def __str__(self):
        a = self.nama +', NIM '+str(self.NIM)\
            +'. Tinggal di '+self.kotaTinggal\
            +'. Uang saku Rp '+str(self.uangSaku)\
            +' tiap bulannya'
        return a
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def makan(self,a):
        print('Saya baru saja makan ',a,' sambil belajar.')
        self.keadaan='kenyang'
    def perbaruiKotaTinggal(self,a):
        self.kotaTinggal=a
    def tambahUangSaku(self,a):
        self.uangSaku+=a
    
