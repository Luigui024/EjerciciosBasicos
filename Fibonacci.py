#fibonacci
cantidad_n = int(input('\n--- Fibonacci ---\n\nDigite la cantidad de números: '))

numero_a , numero_b = 0 , 1

if cantidad_n==1:
    print('\nEl primer número de la secuencia es: 0\n')
    cantidad_n=0
else:    
    numeros = ''
    cantidad=str(cantidad_n)
    while (cantidad_n-1)>=0:
            numeros+=str(numero_a)+' '
            numero_a += numero_b
            numero_a,numero_b = numero_b,numero_a
            cantidad_n-=1

    print('\nLos',cantidad,'primeros números son:',numeros,'\n')