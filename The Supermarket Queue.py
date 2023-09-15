#funkcja oblicza ile czasu zajmie obsłużenie wszystkich klientów przez kasy samoobsługowe
#customers - czas potrzebny każdemu klientowi (kolejki nie można zmieniać)
#n - liczba kas
#np. queue_time([2,3,10], 2) -> 12

def queue_time(customers, n):
    if customers ==[]:#gdy brak kolejki zwraca zero
        return 0
    elif n ==1:#gdy liczba kas równa jeden zwraca sumę czasu klientów
        return sum(customers)
    elif n >len(customers):#gdy liczba kas większa od liczby klientów zwraca najdłuższy czas klienta
        return max(customers)
    else:
        x=[0]*n
        while True:
            x[x.index(min(x))]+=customers[0]
            customers=customers[1:]
            if customers==[]:
                return max(x)
