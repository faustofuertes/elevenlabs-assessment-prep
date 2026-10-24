a = {10,20,30,40,50}

#agregar UN SOLO valor de manera desordenaba obivo (lo agrega solo sino esta ya ahi, pq no acepta duplicaods)
a.add(60)
print(a)

# agregar MULTIPLES valores ITERABLES (pueden ser cualqueir tipo de dato ITERABLE sino rompe)
# a.update(1,2,3,4,5) -> MAL! VALORES NO ITERABLES
a.update([1,2,3,4],[6,7,9])
print(a)

# eliminar un valor de un sets
# solo puede borrar valores q existen sino tira error
a.remove(10)
print(a)

# igual que remove pero si el valor no existe no tira error 
a.discart(100)
print(a)

# borra el ultimo elemento, al ser una lista desordenada borra un elemento random
a.pop()

a = {30,40,50,60}