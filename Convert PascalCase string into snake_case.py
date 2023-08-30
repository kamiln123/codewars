#funkcja zamienia string na string oddzielający słowa _
#np."TestController"  -->  "test_controller"
def to_underscore(string):
    if type(string) ==int:#jeżeli string jest typu int wtedy zamienia się w string
        return str(string)
    string=string[0].lower() +string[1:]
    x=''
    for i in string:
        if i in '0123456789':#cyfra w stringu jest traktowana jako mała litera
            x +=i
            continue
        if i ==i.upper():
            x +='_'
        x +=i.lower()
    return x
    
