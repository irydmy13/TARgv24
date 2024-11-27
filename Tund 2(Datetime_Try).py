from datetime import *
from re import M

#Ulesanne 1
tana=date.today() #mimetus()-funksioon
tanaf=date.today().strftime("%B %d?, %Y")

print(f"Tere! Tana on {tanaf}")
d=tana.day
m=tana.month
y=tana.year
print(d)
print(m)
print(y)
