#funkcja zwraca cyfrę, która występuje nieparzystą liczbę razy
#np. [0,1,0,1,0] -> [0]

def find_it(seq):
    for i in seq:
        if seq.count(i)%2 ==1:
            return i
