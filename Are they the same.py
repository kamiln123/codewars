#funkcja sprawdza czy tablica pierwsza zgadza się z tablicą drugą
#w jednej tablicy są liczby a w drugie te same liczby pomnożone przez siebie
#np.
#a = [121, 144, 19, 161, 19, 144, 19, 11]  
#b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
#b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

def comp(array1, array2):
    #jeżeli jedna z tabel pusta zwraca False
    if array1 == None or array2==None:
        return False
    x=[i*i for i in array1]
    x.sort()
    array2.sort()
    if x==array2:
        return True
    else:
        return False
