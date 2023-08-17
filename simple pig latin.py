#funkcja przenosi pierwszą literę wyrazu na koniec i dodaje końcówkę -ay
def pig_it(text):
    z=text
    text=text.split()
    y=''
    x=[]
    a=0
    b=[]
    c=''
    for i in z:
        if ord(i.lower())>=97 and ord(i.lower())<=122:
            y+=i
    for i in text:
        if i in y:
            x.append(i[1:]+i[0]+'ay ')
        else:
            x.append(' ')
    for i in text:
        if len(i)==len(x[a]):
            b.append(text[a])
            a+=1
        elif len(i)!=x[a]:
            b.append(x[a])
            a+=1
    for i in b: c+=i
    if c[len(c)-1]==' ':
        return c[:len(c)-1]
    else:
        return c
