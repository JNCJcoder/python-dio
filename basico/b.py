conjunto = { 1, 2, 3, 4 }
conjunto.add(5)
conjunto.discard(5)

conjunto2 = { 5, 6, 7, 8 }
conjunto_uniao = conjunto.union(conjunto2)

print(conjunto_uniao)

conjunto_interseccao = conjunto.intersection(conjunto2)

print(conjunto_interseccao)