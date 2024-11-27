from datetime import *
from calendar import *
from random import *
from math import *

# #Ulesanne 1
# paevadekogus=monthrange(2024,11)[1]
# print(paevadekogus)

# tana=date.today() #mimetus()-funksioon
# tanaf=date.today().strftime("%B %d?, %Y")

# print(f"Tere! Tana on {tanaf}")
# d=tana.day #nimetus - omadus
# m=tana.month
# y=tana.year
# print(d)
# print(m)
# print(y)

# detsP=monthrange(2024,12)[1] #31
# novP=monthrange(2024,11)[1] #30
# jaak=detsP+novP-d
# jaak2=novP-d
# print(f"Aasta loppuni on {jaak}")
# print(f"Kuu lopuni on {jaak2}")

#Ulesanne 2

# print("Какие есть варианты ответов для операции 3+8/(4 - 2)*4?")
# a = 3 + 8 / (4 - 2) * 4 
# a1 = 3 + 8 / 4 - 2 * 4 
# a2 = (3 + 8) / (4 - 2) * 4
# print(f"1. 3+8/(4-2)*4 = {a}")
# print(f"2. 3+8/4-2*4 = {a1}")
# print(f"3. (3+8)/(4-2)*4 = {a2}")

# #Ulesanne 3

# try:
# 	R=float(input("Sisesta R: "))
# 	Sk=pi*R**2
# 	Lk=2*pi*R
# 	Skv=(2*R)**2
# 	Lkv=2*R*4
# 	print(f"Ruudu pindald on {Sk}\nRingi umnbermoot on {Lk}\nRuudu pindala on {Lkv}\nRuudu umnbermoot on {Lkv}\n")
# except:
# 	print("On vaja number!")

# #2 variant
# R=round(random()*100) #0.0...1.0
# print(f"R={R}")
# Sk=pi*R**2
# Lk=2*pi*R
# Skv=(2*R)**2
# Lkv=2*R*4
# print(f"Ruudu pindald on {Sk}\nRingi umnbermoot on {Lk}\nRuudu pindala on {Lkv}\nRuudu umnbermoot on {Lkv}\n")

#Ulesanne 4
d=2.575 #mundi d sm
maa=6378 #maa radius km
maa*=100000 #radius sm
Lmaa=2*pi*maa
kogus=Lmaa/d
print(f"On vaja {kogus} mundi.\nMeil on valja {kogus*2} eur")

#Ulesanne 5

