#Prueba Técnica - Backend Developer - Datamart
#Aspirante: Santiago Esteawens Torres Zapata

#8. Dada una lista de números en orden ascendente y un número objetivo, 
# escribe una función recursiva que encuentre si el número objetivo está en la lista
# utilizando una búsqueda binaria.

from concurrent.futures import ThreadPoolExecutor

def binary_search(array, target):
    if len(array) == 0:
        return False
    else:
        middle = len(array) // 2

        if array[middle] == target:
            return True
        elif array[middle] < target:
            return binary_search(array[middle+1:], target)
        else:
            return binary_search(array[:middle], target)
    
array = [8,13,17,19,33,35,40,42,44,46,51,53,63,72,75,85,87,89,92,99]
target1 = 44
target2 = 41
print('Problema 8.')
print(f'Lista a evaluar: {array}')
print(f'Resultado evaluando el objetivo {target1} = {binary_search(array,target1)}')
print(f'Resultado evaluando el objetivo {target2} = {binary_search(array,target2)}')

# Implemente un algoritmo que reciba en la entrada dos listas de números enteros y haga un map de cada elemento 
# de la segunda lista con la función del problema 8 utilizando la primera lista como dominio de la búsqueda. 
# Teniendo en cuenta que el tamaño de la primera lista podría ser muy grande explique qué beneficios tiene utilizar 
# una búsqueda binaria en lugar de utilizar una búsqueda secuencial y cómo impacta la complejidad computacional de la solución.
# En circunstancias donde el segundo listado sea también grande es conveniente procesar las peticiones en paralelo; 
# en este escenario sería conveniente poder configurar una máxima cantidad de workers para que procesen de forma 
# paralela el segundo arreglo. Proponga una solución general a este problema utilizando Python3

def map_list_with_binary_search(array1, array2, max_workers=None):
    result = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(binary_search, array1, elem): elem for elem in array2}
        for future in futures.as_completed(futures):
            elem = futures[future]
            if future.result():
                result[elem] = True
            else:
                result[elem] = False
    return result

# En este código, map_list_with_binary_search es la función que realiza el mapeo. 
# Utiliza un ThreadPoolExecutor para procesar las búsquedas en paralelo, con un número máximo de workers 
# especificado por el parámetro opcional max_workers, lo que significa que la cantidad de workes 
# se determina automáticamente en función de la cantidad de procesadores disponibles en el sistema.

# La función utiliza la clase ThreadPoolExecutor para crear un conjunto de subprocesos de trabajo
# y envía una tarea de búsqueda binaria para cada elemento de la segunda lista array2 al conjunto.
# La función futures.as_completed se usa para esperar a que se completen las tareas, y los resultados 
# se recopilan y se usan para construir el diccionario de resultados.

# El uso del procesamiento paralelo mejora el rendimiento de la función, especialmente si la segunda lista
# array2 es grande. Esto se debe a que la función puede procesar múltiples elementos en array2 simultáneamente,
# lo que puede reducir el tiempo total necesario para construir el diccionario de resultados.


# La búsqueda binaria es una técnica eficiente para buscar un elemento en una lista ordenada.
# La complejidad temporal de la función modificada es O (n * log m), donde n es el 
# tamaño de la segunda lista array2 y m es el tamaño de la primera lista array1.
# Sin embargo, el factor constante en la complejidad del tiempo se reduce mediante el
# uso de procesamiento paralelo, ya que la función puede procesar múltiples elementos en array2 simultáneamente.
# Hay que tener en cuenta que el paralelismo tiene sus propios costos, como la sobrecarga de la 
# creación de threads y la sincronización. Por lo tanto, el número óptimo de workers dependerá de los detalles 
# específicos del hardware y del sistema operativo.

# La complejidad espacial de la función es O (n), ya que la función necesita construir un diccionario con n elementos 
# y el tamaño del diccionario es linealmente proporcional al tamaño de la segunda lista array2.
# Sin embargo, el espacio adicional que necesita la función es ligeramente mayor, ya que la función necesita realizar 
# un seguimiento de las tareas y sus resultados. El espacio adicional necesario es proporcional al número de tareas, 
# que es igual al tamaño de la segunda lista array2, por lo que la complejidad del espacio se puede considerar O(n).