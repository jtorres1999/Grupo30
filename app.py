numero = input('Ey pasa el número: ')

cont = 0
for i in range(numero):
    if numero % i == 0:
        cont = cont + 1

if cont == 2:
    print('El numero: ', numero, ' es primo')
else:
    print('El numero: ', numero, ' NO es primo')