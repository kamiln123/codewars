#funkcja liczy ile jest uśmiechniętych twarzy w arr
def count_smileys(arr):
    x=0
    for i in arr:
        if i[0]==':' or i[0]==';': #sprawdzenie czy twarz ma oczy 
            if len(i)==2 and i[1]=='D' or i[1]==')': #sprawdzenie czy twarz składa się z oczu i uśmiechniętych ust jeżeli tak dodaje do licznika
                x+=1
            elif len(i)==3 and i[1]=='-' or i[1]=='~':#sprawdzenie czy twarz składa się z oczu nosa i ust 
                if i[2]=='D' or i[2]==')':#jeżeli tak czy twarz jest uśmiechnięta
                    x+=1
    return x #zwrócenie liczby uśmiechniętych twarzy
            
