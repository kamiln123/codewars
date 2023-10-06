#funkcja zwraca stringi, z a1, które występują w a2
#np.
#a1 = ["arp", "live", "strong"]
#a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#returns ["arp", "live", "strong"]

def in_array(array1, array2):
    r=[]
    for i in array1:
        for j in array2:
            if i in j and i not in r:
                r.append(i)
                r.sort()
    return r
