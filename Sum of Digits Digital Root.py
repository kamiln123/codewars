#jeżeli n jest liczbą przynajmniej dwucyfrową, funkcja zwraca sumę tych liczb do póki jej wynik nie jest jedną cyfrą

def digital_root(n):
    x=0
    while True:
        if n<10: #sprawdzenie czy n jest cyfrą jednocyfrową
            return n #zwrócenie liczby jeżeli jest jednocyfrowa
        elif n>=10: #jeżeli liczba jest przynajmniej dwucyfrowa
            for i in str(n): #cyfry w liczbie są sumowane
                x+=int(i)
            n=x
            x=0
            
    
