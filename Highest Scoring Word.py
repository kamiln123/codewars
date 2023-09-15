#funkcja wyświetla słowo, które ma najwyższą lczbę punktów w stringu i występuje jako pierwsze w zdaniu
#punkty są przyznawane w zależności od miejsca w alfabecie a=1, b=2, c=3 itd.
#np. high('man i need a taxi up to ubud') -> 'taxi'

def high(x):
    x=x.split()
    y={}
    z=1
    for i in range(97, 123):#stworzenie alfabetu z ilością punktów
        y[chr(i)]=z
        z+=1

    a=0
    b=''
    for i in x:#znalezienie słowa z największą liczbą punktów
        z=0
        for j in i:
            z+=y[j]
        if z >a:
            a=z
            b=i
        elif z==a:
            continue
    return b
    
        
