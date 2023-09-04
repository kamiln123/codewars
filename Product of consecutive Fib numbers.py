#funkcja mnoży ze sobą następujące po sobie liczby fibonaciego, jeżeli wynikiem ich pomnożenia jest liczba w prod, wtedy zwraca te liczby oraz True
#lub False, jeżeli nie da się znaleźć pasujących liczb
#np.
#productFib(714)
                # should return (21, 34, true), 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

#productFib(800)
                # should return (34, 55, false), 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
def productFib(prod):
    fib=0
    x=[0]
    y=0
    while True:
        if fib==0:
            fib+=1
            x.append(fib)
        elif fib>0:
            fib=x[0]+x[1]
            x=[x[1]]
            x.append(fib)
            y=x[0]*x[1]
            if prod==0:
                return [0, 1, True]
            if y==prod:
                return [x[0], x[1], True]
            elif y>prod:
                return [x[0], x[1], False]
