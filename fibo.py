

#Creamos una funcion y la estructura necesaria para poder desarrollar la sucesión de Fibonacci
def fibonacci(n):
    
    if n == 0 or n == 1:
         return n
    else:
         return fibonacci(n -1) + fibonacci(n -2)

#Utilizamos un bucle para imprimir la sucesion con una longitud de 10 
for x in range(10):
    print(fibonacci(x))


#Creamos otra funcion para comprobar la quinta posicion 

#Definimos  una función para  calcularla posición concreta de una posición de la sucesión de Fibonacci en este caso el quinto posicion 
posicion = 5
ini = 0
fin = 1

for x in range(0,posicion):
    if x == 0:
        fin = 0
    elif x == 1:
        fin = 1
    sum = fin
    fin = fin + ini
    ini = fin - ini
print(f'\nEl quinto numero de la sucesión de   : {x+1:>4} -- Valor en la serie de Fibonacci es:  {sum:>10}  ')  


# Importaremos la librería de testeo de software, en este caso unittest


#Crearemos nuestra clase (del tipo unittest.TestCase)

#2.2 - Importaremos la librería de testeo de software, en este caso unittest. 

import unittest


class  TestFibo (unittest.TestCase):

    def test_series_10(self):
        print('\nTest Series 10')
        wanted_result = [1,1,2,3,5,8,13,21,34,55,89]
        test_result = fibonacci(10)
        self.assertEqual(wanted_result,test_result)


        if __name__ == '__main__':
           unittest.main()


