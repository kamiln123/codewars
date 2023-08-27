#funkcja zwraca listę elementów bez elementów o tej samej wartości obok siebie
#np. 'AAAABBBCCDAABBB' --> ['A', 'B', 'C', 'D', 'A', 'B']
def unique_in_order(sequence):
    if sequence =='' or sequence ==[] or sequence ==():
        return []
    x=[]
    x.append(sequence[0])
    for i in sequence:
        if i != x[-1]:
            x.append(i)
    return x
