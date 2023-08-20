#funkcja tworzy hasztag z napisu
def generate_hashtag(s):
    if s=='':#string nie może być pusty
        return False
    s=s.split()
    a=''
    for i in s:
        a+=i.capitalize()#dodanie do pustego stringa każdego słowa osobno, które zaczyna musi zaczynać się od dużej litery
    if len('#'+ a)>140:#hasztag nie może być dłuższy niż 140 znaków
        return False
    else:
        return '#'+a
