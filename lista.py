lista = [4, 0, 5, 0, 3, 0, 0, 5, 0, 7, 2, 0, 5]


for i in range(0, len(lista)):
   if lista[i] ==0:
        print (lista[i])
        for j in range(i+1, len(lista)):
            if lista[j] !=0:
                lista[i] = lista[j]
                lista[j] = 0
                break
print(lista)
