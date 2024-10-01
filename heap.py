import random
import time
import numpy as np
import matplotlib.pyplot as plt
import unittest

############
# II. Heap #
############


# class TestHeapify(unittest.TestCase):
#     def test_insert_into_empty_heap(self):
#         # Caso 1: Insertar en un heap vacío
#         heap = []
#         heap_insert(heap, 5)
#         self.assertEqual(heap, [5])  # El heap solo debe contener el valor insertado

#     def test_insert_single_element(self):
#         # Caso 2: Insertar un valor en un heap con un solo elemento
#         heap = [10]
#         heap_insert(heap, 5)
#         self.assertEqual(heap, [5, 10])  # El nuevo valor debe ser la raíz (min-heap)

#     def test_insert_larger_element(self):
#         # Caso 3: Insertar un valor mayor que la raíz
#         heap = [1, 3, 6]
#         heap_insert(heap, 10)
#         self.assertEqual(heap, [1, 3, 6, 10])  # El nuevo valor debe ir al final

#     def test_insert_smaller_element(self):
#         # Caso 4: Insertar un valor menor que la raíz
#         heap = [3, 5, 7, 10, 12]
#         heap_insert(heap, 2)
#         self.assertEqual(heap, [2, 3, 7, 10, 12, 5])  # El nuevo valor debe ser la nueva raíz

#     def test_insert_duplicate_element(self):
#         # Caso 5: Insertar un valor duplicado
#         heap = [2, 3, 6, 7, 9]
#         heap_insert(heap, 3)
#         self.assertEqual(heap, [2, 3, 3, 7, 9, 6])  # Los valores duplicados deben respetar la propiedad del heap

#     def test_insert_multiple_elements(self):
#         # Caso 6: Insertar múltiples elementos de forma secuencial
#         heap = [1]
#         heap_insert(heap, 4)
#         heap_insert(heap, 2)
#         heap_insert(heap, 6)
#         heap_insert(heap, 0)

#         # Verificar que el heap mantenga su estructura
#         self.assertEqual(heap, [0, 1, 2, 6, 4])
    
    # def test_extract_from_non_empty_heap(self):
    #     # Caso 1: Estrai da un heap non vuoto
    #     heap = [1, 3, 5, 7, 9]
    #     extracted_value, modified_heap = pq_extract(heap)
    #     self.assertEqual(extracted_value, 1)  # Il valore estratto deve essere il minimo
    #     self.assertEqual(modified_heap, [3, 7, 5, 9])  # L'heap deve essere riordinato

    # def test_extract_empty_heap(self):
    #     # Caso 2: Tentare di estrarre da un heap vuoto
    #     heap = []
    #     with self.assertRaises(IndexError):  # Deve sollevare un'eccezione
    #         pq_extract(heap)

    # def test_extract_after_multiple_inserts(self):
    #     # Caso 3: Estrarre dopo aver inserito più elementi
    #     heap = []
    #     pq_insert(heap, 5)
    #     pq_insert(heap, 3)
    #     pq_insert(heap, 8)
    #     pq_insert(heap, 1)

    #     extracted_value, modified_heap = pq_extract(heap)
    #     self.assertEqual(extracted_value, 1)  # Il valore estratto deve essere il minimo
    #     self.assertEqual(modified_heap, [3, 5, 8])  # L'heap deve essere riordinato correttamente

    # def test_extract_until_empty(self):
    #     # Caso 4: Estrarre fino a svuotare l'heap
    #     heap = [2, 3, 4, 5]
    #     extracted_values = []
    #     while heap:
    #         value, heap = pq_extract(heap)
    #         extracted_values.append(value)
        
    #     self.assertEqual(extracted_values, [2, 3, 4, 5])  # I valori estratti devono essere ordinati
    #     self.assertEqual(heap, [])  # L'heap deve essere vuoto alla fine


#II.A.1 OK
def heap_heapify(h,i):
    if i >= len(h):
        return h
    small=h[i]
    indx=i
    izq=(2*i)+1 #Indx Hijo Izquierdo
    der=(2*i)+2 #Indx Hijo Derecho
    if izq < len(h) and h[izq]<small:
        small=h[izq]
        indx=izq
    if der < len(h) and h[der]<small:
        small=h[der]
        indx=der
    if indx == i:
        return h
    h[i],h[indx]=h[indx],h[i]
    heap_heapify(h,indx)
    return h

#II.A.2
def heap_insert(h, key):
    h += [key]
    k=len(h)-1
    while k > 0:
        p=int((k-1)/2)
        if h[k] > h[p]:
            return h
        h[k], h[p] = h[p], h[k]
        k=p

#II.A.3 OK
def heap_extract(h):
    u=h[0]
    h[0]=h[-1]
    h=h[:-1]
    h =heap_heapify(h, 0)
    return h,u 

#II.A.3 OK
def heap_create(h):
    for k in range(len(h)-1,-1,-1):
        heap_heapify(h,k)
    return h

# if __name__ == "__main__":
#     unittest.main()

#II.B.1
def pq_ini():
    return []

#II.B.2
def pq_insert(h, key):
    heap_insert(h, key)
    return h

def pq_extract(h):
    (h,e)=heap_extract(h)
    return e,h


#Nlist= numValores de la lista, NRep=numero de veces que se repite LA MISMA LISTA, #NStat=num de veces con la lista del mismo tamaño (pero no la misma lista)
#print(time_measure(itr_bs,dataprep_bs,lista,1000,100))

