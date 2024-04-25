#Prueba Técnica - Backend Developer - Datamart
#Aspirante: Santiago Esteawens Torres Zapata

#1. Escribe una función llamada merge_arrays que acepte dos arrays ordenados de enteros 
# como parámetros y devuelva un solo array ordenado que contenga todos los elementos de ambos.
def merge_arrays(array1, array2):
    merge_array = array1
    merge_array.extend(array2)
    merge_array.sort()
    return merge_array

array1 = [1,3,5,7,9]
array2 = [2,4,6,8,10]

print("Problema 1.")
print(f'Lista número 1 {array1}')
print(f'Lista número 2 {array2}')
print(f'Resultado: {merge_arrays(array1,array2)}')

#2. Escribe una función llamada find_median que acepte un array de enteros como parámetro 
# y devuelva la mediana del conjunto.
def find_median(array):
    array_sorted = sorted(array)
    index = len(array_sorted) // 2

    if len(array_sorted) % 2 != 0:
        return array_sorted[index]
    
    return (array_sorted[index -1] + array_sorted[index]) / 2

arrayPar = [130,110,230,222,154,181]
arrayImpar = [130,110,230,222,154,181,185]

print("Problema 2.")
print(f'Listas par a evaluar: {arrayPar}')
print(f'Listas impar a evaluar: {arrayImpar}')
print(f'Resultado lista par = {find_median(arrayPar)}')
print(f'Resultado lista impar = {find_median(arrayImpar)}')

#7. Escribe una función llamada remove_duplicates que acepte una lista como parámetro 
# y devuelva una nueva lista sin elementos duplicados.
def remove_duplicates(array):
    newArray = []

    for item in array:
        if item not in newArray:
            newArray.append(item)
    return newArray 

arrayduplicates = [43,32,33,56,56,33,23,19,19,20]
print('Problema 7.')
print(f'Lista con elementos duplicados: {arrayduplicates}')
print(f'Resultado: {remove_duplicates(arrayduplicates)}')
