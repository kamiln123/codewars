#funkcja porządkuje zdanie w zależności od tego jaką literę zawiera słowo
#np. "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
def order(sentence):
    x=1
    y=''
    if sentence=='':#jeżeli sentence jest pusty zwraca pusty string
        return ''
    sentence=sentence.split()
    while True:#układanie wyrazów w kolejności 
        for i in sentence:
            if str(x) in i:
                y+=i + ' '
                x+=1
        if x==len(sentence)+1:
            break
    return y[:len(y)-1]
