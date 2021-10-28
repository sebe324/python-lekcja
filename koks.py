import random
print ("Hello World!")
talia_kart=[]
kolor_karty=["Wino","Żołądź","Dzwonek","Czerwo"]
nazwa_karty=["2","3","4","5","6","7","8","9","10","Jopek","Królowa","Król","As"]
hand1, hand2=[],[]
for j in range(4):     
    for i in range(13):
        talia_kart.append([nazwa_karty[i],kolor_karty[j]])
print(talia_kart)

hand1.random.sample(talia_kart, 5);

