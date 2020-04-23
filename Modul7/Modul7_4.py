import re
a=open('KEI.html','r', encoding='latin1')
b = a.read()
a.close()
x=r'([\w+]+)</a></td>'
y=r'>([\w+]+)</a></td>\n<td>([0-9.]+)</td>'
display = re.findall(x,b)
print("Nama Negara :")
print(display)
display = re.findall(x,b)
display = re.findall(y,b)
lc=[]
for i in display:
    lc.append((i[0], float(i[1])))
print("\n\nNama Negara beserta Innovation Indexnya :")
print(lc)
