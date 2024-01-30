from math import *
from random import *
  #1
n = int(input("Sisestage majade arv (1 kuni 9): "))
# Maja ülemise osa joonistamine
for i in range(n):
    print("  ~~~~~ ", end=" ")
print()  #Üleminek uuele liinile

#Katuse joonistamine
for i in range(n):
    print("  /_____\ ", end=" ")
print()  #Üleminek uuele liinile

#Seina joonistamine aknaga
for i in range(n):
    print("  | []  | ", end=" ")
print()  #Üleminek uuele liinile

#Maja aluse joonistamine
for i in range(n):
    print("  ----- ", end=" ")
print()  #Üleminek uuele liinile





   #2
N = 0  #elanike arv

P = 0  #asustustihedus

for i in range(1, 13):
    n=float(input(f"Sisestage elanike arv {i}-m piirkond  (tuhandetes inimestes): "))
    p=float(input(f"Sisestage rahvastiku tihedus {i}-m piirkond tuhat inimest/km2): "))
    N+=n
    P+=p 
    S=N/P

print(f"Piirkonna territooriumi üldpindala: {S:.2f} km2")


   

   #3
# Loome juhuslike hinnangute loendi 25 õpilase jaoks
hinded=(randint(1,25) for i in range(25))

# Initsialiseerime muutujad miinimum- ja maksimumhinde jaoks
min_hinne = float("inf")  # lõpmatus, et kindlasti asendada
max_hinne = float("-inf")  # negatiivne lõpmatus

# Liigume läbi iga hinde loendis
for hinne in hinded:
    # Võrdleme praegust hinnangut miinimum- ja maksimumhinnetega
    if hinne<min_hinne:
        min_hinne=hinne
    if hinne>max_hinne:
        max_hinne=hinne

# Väljastame tulemused
print(f"Õpilaste hinded: {hinded}")
print(f"Miinimumhinne: {min_hinne}")
print(f"Maksimumhinne: {max_hinne}")




  #4





  #5





