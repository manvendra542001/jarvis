from cv2 import inpaint


a=input()
dbl=a.findall("double",0,100)
trp=a.findall("triple",0,100)
dbl=dbl+6
trp=trp+6
print(dbl,trp)
new="-"
temp=list(a)
temp[dbl]=new
a="".join(temp)
print(a)
temp2=list(a)
temp2[trp]=new
a="".join(temp2)
print(a)