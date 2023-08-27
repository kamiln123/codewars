#Funckja zwraca True albo False w zależności czy suma cyfr w liczbie podniesiona do kwadratu długości liczby będzie tą cyfrą
#np. 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 True
#1652 = 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938 False
def narcissistic(value):
    x=0
    for i in str(value):
        x+=int(i)**len(str(value))
    if x==value:
        return True
    else:
        return False
