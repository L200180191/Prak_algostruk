from LatOOP3 import Manusia 
class Mahasiswa(Manusia):
    listkuliah=[]
    def __init__(self):
        self.nama = str(input("Masukkan nama : "))
        self.NIM = str(input("Masukkan NIM : ")) 
        self.kotaTinggal= str(input("Masukkan Kota Tinggal : "))
        self.uangSaku= int(input("Masukkan jumlah uang saku : "))
    def __str__(self):
        a = self.nama +', NIM '+str(self.NIM)\
            +'. Tinggal di '+self.kotaTinggal\
            +'. Uang saku Rp '+str(self.uangSaku)\
            +' tiap bulannya'
        return a
    def ambilKuliah(self,a):
        self.listkuliah.append(a)
    def hapusKuliah(self,a):
        self.listkuliah.remove(a)
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
    
