#Três números e colocá-los em ordem crescente.

nmr1 = int(input("Primeiro número: "))
nmr2 = int(input("Segundo número: "))
nmr3 = int(input("Terceiro número: "))

first = nmr1
if first > nmr2:
    first = nmr2
if first > nmr3:
    first = nmr3

second=third=0

if first == nmr1:
    if nmr2 < nmr3:
       second=nmr2
       third=nmr3
    else:
       second=nmr3
       third=nmr2
elif first == nmr2:
    if nmr1 < nmr3:
       second=nmr1
       third=nmr3
    else:
       second=nmr3
       third=nmr1
else:
    if nmr1 < nmr2:
       second=nmr1
       third=nmr2
    else:
       second=nmr2
       third=nmr1 
print(first,second,third)      
