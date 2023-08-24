#funkcja usuwa z listy liczbę jeżeli powtórzy się x razy bez zmiany kolejności
#np. ([1,1,3,3,7,2,2,2,2], 3) odp. [1, 1, 3, 3, 7, 2, 2, 2]
def delete_nth(order,max_e):
    x=[]
    for i in order:
        if x.count(i)<max_e:
            x.append(i)
    return x
