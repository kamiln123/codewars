#funkcja przesuwa wszystkie zera z listy na koniec
#np.[1, 0, 1, 2, 0, 1, 3] -> [1, 1, 2, 1, 3, 0, 0]
def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(0)
            lst.append(0)
    return lst
