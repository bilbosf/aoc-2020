validos = 0

for i in range(1000):
    entrada = input()
    criterios = entrada[:entrada.index(':')]
    senha = entrada[entrada.index(':')+2:]

    caractere = criterios[-1]
    n1 = int(criterios[:criterios.index('-')])
    n2 = int(criterios[criterios.index('-')+1:len(criterios)-2])

    if (senha[n1-1]==caractere) != (senha[n2-1]==caractere):
        validos += 1

print("{} validos".format(validos))