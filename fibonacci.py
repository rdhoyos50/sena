# n-esimo numero termin de la sucesion fibonacci
 
def Fibonacci(n):
    if n<= 0:
        print("termino incorrecto")
    # El primer número de Fibonacci es 0
    elif n == 1:
        return 0
    # El segundo numero de Fibonacci es 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# imprime
 
print(Fibonacci(11))

 
