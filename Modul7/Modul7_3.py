import re
a=open('Indonesia.txt','r', encoding='latin1')
b = a.read()
a.close()
x=r'di \w+'
display = re.findall(x,b)
print(display)
