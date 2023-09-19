#funkcja tworzy permutacje znaków
#np. 'abc' -> ['abc','acb','bac','bca','cab','cba']

def permutations(s):
    if len(s) ==1:
        return [s]
    else:
        x=s[0]
        y=[]
        z=[]
        for i in permutations(s[1:]):
            for j in range(len(i)+1):
                z=(i[:j]+x+i[j:])
                if z not in y:
                    y.append(z)
    return y
