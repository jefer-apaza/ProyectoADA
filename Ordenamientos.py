import random
import time
import matplotlib.pyplot as plt
import tkinter as tk

def partition(lista, start, end):
    pivot = lista[end]
    i = start - 1
    for j in range(start, end):
        if lista[j] < pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i+1], lista[end] = lista[end], lista[i+1]
    return i + 1

def quick_sort(lista, start=0, end=None):
    if end is None:
        end = len(lista) - 1
    if start < end:
        pivot_idx = partition(lista, start, end)
        quick_sort(lista, start, pivot_idx - 1)
        quick_sort(lista, pivot_idx + 1, end)
    return lista



def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def selection_sort(lista):

    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        current_value = lista[i]
        position = i
        while position > 0 and lista[position-1] > current_value:
            lista[position] = lista[position-1]
            position -= 1
        lista[position] = current_value
    return lista

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def shellsort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Lista inicial de 100 elementos
size = 100
random_list = [random.randint(0, 10000) for _ in range(size)]

# Listas para almacenar los tiempos de ejecución y el tamaño de las listas
merge_times = []
shell_times = []
quick_times = []
bubble_times = []
selection_times = []
insertion_times = []
log_n_times = []
sizes = [size]

# Ordenar la lista inicial con ambos algoritmos
start_time = time.time()
bubble_sort(random_list)
end_time = time.time()
bubble_time = end_time - start_time
bubble_times.append(bubble_time)

start_time = time.time()
quick_sort(random_list)
end_time = time.time()
quick_time = end_time - start_time
quick_times.append(quick_time)

start_time = time.time()
selection_sort(random_list)
end_time = time.time()
selection_time = end_time - start_time
selection_times.append(selection_time)

start_time = time.time()
insertion_sort(random_list)
end_time = time.time()
insertion_time = end_time - start_time
insertion_times.append(insertion_time)

start_time = time.time()
mergesort(random_list)
end_time = time.time()
merge_time = end_time - start_time
merge_times.append(merge_time)

start_time = time.time()
shellsort(random_list)
end_time = time.time()
shell_time = end_time - start_time
shell_times.append(shell_time)


# Ordenar la lista con ambos algoritmos para tamaños de 100 hasta 50000
while size <= 1000:
    size += 100
    random_list = [random.randint(0, 10000) for _ in range(size)]
    sizes.append(size)
    # Bubble Sort
    start_time = time.time()
    bubble_sort(random_list)
    end_time = time.time()
    bubble_time = end_time - start_time
    bubble_times.append(bubble_time)
    random_list = [random.randint(0, 10000) for _ in range(size)]
    
    # Quick Sort
    start_time = time.time()
    quick_sort(random_list)
    end_time = time.time()
    quick_time = end_time - start_time
    quick_times.append(quick_time)
    random_list = [random.randint(0, 10000) for _ in range(size)]

    # Selection Sort
    start_time = time.time()
    selection_sort(random_list)
    end_time = time.time()
    selection_time = end_time - start_time
    selection_times.append(selection_time)
    random_list = [random.randint(0, 10000) for _ in range(size)]

    # Insertion Sort
    start_time = time.time()
    insertion_sort(random_list)
    end_time = time.time()
    insertion_time = end_time - start_time
    insertion_times.append(insertion_time)
    random_list = [random.randint(0, 10000) for _ in range(size)]

    # Mergesort
    start_time = time.time()
    mergesort(random_list)
    end_time = time.time()
    merge_time = end_time - start_time
    merge_times.append(merge_time)
    random_list = [random.randint(0, 10000) for _ in range(size)]

    # Shellsort
    start_time = time.time()
    shellsort(random_list)
    end_time = time.time()
    shell_time = end_time - start_time
    shell_times.append(shell_time)
    random_list = [random.randint(0, 10000) for _ in range(size)]


    # Actualizar gráfico
    plt.plot(sizes, bubble_times, label='Bubblesort')
    plt.plot(sizes, merge_times, label='Mergesort')
    plt.plot(sizes, shell_times, label='Shellsort')
    plt.plot(sizes, quick_times, label='Quicksort')
    plt.plot(sizes, selection_times, label='Selectionsort')
    plt.plot(sizes, insertion_times, label='Insertionsort')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ejecución entre Mergesort y Shellsort')
    plt.legend()
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

