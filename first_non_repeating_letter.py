#funkcja zwraca pierwszy znak, który nie powtórzył się w ciągu
#np. 'stress' --> 't'
def first_non_repeating_letter(s):
    x=[]
    y=s.lower()
    z=0
    if s=='':
        return ''
    for i in y:
        x.append(y.count(i))
        if y.count(str(i)) ==1:
            return s[z]
            break
        else:
            z+=1
    if 1 not in x:
            return ''
    
