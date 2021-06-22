#ordenar_números
cantidad = int(input('\nDigite la cantidad de números: '))
print('')
numeros = []
for i in range(cantidad):
    numeros.append(int(input('Digite el '+str(i+1)+'° número: ')))

numerosCopia = numeros.copy() # Copia de la lista para usar con los Descendentes    

ordenAscendente = []
ordenDescendente = []

#Ascendentes
for i in range(len(numeros)):
    numeroMenor = numeros[0]
    posicionNumMenor = 0    
    for e in range(len(numeros)):        
        if numeros[e]<numeroMenor:            
            numeroMenor=numeros[e]
            posicionNumMenor=e
    ordenAscendente.append(numeroMenor)
    numeros.pop(posicionNumMenor)

#Descendentes
for i in range(len(numerosCopia)):
    numeroMayor = numerosCopia[0]
    posicionNumMayor = 0    
    for e in range(len(numerosCopia)):        
        if numerosCopia[e]>numeroMayor:            
            numeroMayor=numerosCopia[e]
            posicionNumMayor=e
    ordenDescendente.append(numeroMayor)
    numerosCopia.pop(posicionNumMayor)

print('\nNúmeros en orden: ascendete - descendente:')
for i in range(len(ordenAscendente)):
    print(ordenAscendente[i],' - ',ordenDescendente[i])
print('')      