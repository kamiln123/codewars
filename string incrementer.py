#funkcja dodaje 1 na koniec stringa lub jeżeli posiada już liczbę na końcu zwiększa ją o 1
def increment_string(strng):
    x=-1
    y=[]
    z=''
    if strng=='':#jeżeli pusty string dodaj '1'
        return '1'
    elif strng[-1] in '0123456789':
        while True:#pętla wyszukująca liczb od końca
            if strng[x] in '0123456789':
                y.append(strng[x])
                x-=1
            else:
                break
        strng=strng[:-len(y)]#usunięcie starych liczb
        y.reverse()#ułożenie liczb w odpowiedniej kolejności
        for i in y:#połączenie listy w liczbę
            z+=i
        print(z)
        z=str(int(z)+1)#zwiększenie liczby o 1
        while True:#uzupełnienie liczby '0'
            if len(y)==len(z):
                break
            elif len(y)>len(z):
                z='0'+z
            elif len(y)<len(z):
                break
        return strng+ z
    elif strng[-1] not in '0123456789':#jeżeli na końcu stringa nie ma cyfry dodaje 1
        return strng+ '1'
    
    
        
            
            
    
