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

urut =[m1.NIM, m2.NIM, m3.NIM, m4.NIM, m5.NIM,
       m6.NIM, m7.NIM,m8.NIM, m9.NIM, m10.NIM]

def mergeSort(nlist):
    print("Membelah ", nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Menggabungkan ",nlist)
nlist = urut
print("Hasil MergeSort")
mergeSort(nlist)
print(nlist)

def quickSort(data_list):
   quickSortHlp(data_list,0,len(data_list)-1)

def quickSortHlp(data_list,first,last):
   if first < last:

       splitpoint = partition(data_list,first,last)

       quickSortHlp(data_list,first,splitpoint-1)
       quickSortHlp(data_list,splitpoint+1,last)


def partition(data_list,first,last):
   pivotvalue = data_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while data_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = data_list[leftmark]
           data_list[leftmark] = data_list[rightmark]
           data_list[rightmark] = temp

   temp = data_list[first]
   data_list[first] = data_list[rightmark]
   data_list[rightmark] = temp

   return rightmark

data_list = urut
quickSort(data_list)
print("\n"+"Hasil QuickSort")
print(data_list)









