#Numero Menor y Mayor (09-06)
cantidadNumeros = int(input('\nDigite la cantidad de números: '))
numeros=[]
print('')
for i in range(cantidadNumeros):
    numeros.append(int(input('Digite el '+str(i+1)+'° número: ')))

numeroMayor = numeros[0]
numeroMenor = numeros[0]

for i in numeros:

    if(numeroMayor<i):
        numeroMayor=i

    if(numeroMenor>i):
        numeroMenor=i

print('\nEl número menor es:',numeroMenor,'\nEl número mayor es:',numeroMayor,'\n')
