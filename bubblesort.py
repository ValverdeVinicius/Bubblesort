def trocar(sequencia, indice):
    auxiliar = sequencia[indice]
    sequencia[indice] = sequencia[indice+1]
    sequencia[indice+1] = auxiliar

sequencia = [1, 13, 32, 64, 76, 23, 89, 45, 234, 5253, 439]
troca = 1

while troca:
    troca = 0
    i=0

    for i in range(len(sequencia)-1):
        if sequencia[i]>sequencia[i+1]:
                trocar(sequencia, i)
                troca = 1

print(sequencia)