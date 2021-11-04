import random
print ("Hello World!")
talia_kart=[]
kolor_karty=["Wino","Żołądź","Dzwonek","Czerwo"]
kolor_kartyID=[0,1,2,3]
nazwa_karty=["2","3","4","5","6","7","8","9","10","Jopek","Królowa","Król","As"]
nazwa_kartyID=[]
for i in range(13):
    nazwa_kartyID.append(i)
liczba_graczy=4
liczba_kart=5
gracze=[]
for j in range(4):     
    for i in range(13):
        talia_kart.append([nazwa_kartyID[i],kolor_kartyID[j]])
print(len(talia_kart))
random.shuffle(talia_kart)
for g in range (liczba_graczy):
    gracze.append([])
for k in range(liczba_kart):
    for g in range(liczba_graczy):
       gracze[g].append(talia_kart.pop(0))
print("\n", gracze[0])
print("\n", gracze[1])
print("\n", gracze[2])
print("\n", gracze[3])
print(len(talia_kart))
def compare_cards(c1,c2):
    # najpierw sprawdza czy wartość karty jest większa
    # potem sprawdza kolor
    if(c1[0]>c2[0]):
        return True
    elif(c1[0]<c2[0]):
        return False
    elif(c1[0]==c2[0]):
        if(c1[1]>c2[1]):
            return True
        elif(c1[1]<c2[1]):
            return False
print(compare_cards(gracze[1][1], gracze[3][1]))
