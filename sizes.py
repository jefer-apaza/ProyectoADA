import random
import time
import matplotlib.pyplot as plt
import tkinter as tk
import math

#Quick sort
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
# heapsort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#bubble sort
def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

#Selection Sort
def selection_sort(lista):

    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

#insertion sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        current_value = lista[i]
        position = i
        while position > 0 and lista[position-1] > current_value:
            lista[position] = lista[position-1]
            position -= 1
        lista[position] = current_value
    return lista

#bucket sort
def bucket_sort(arr):
    n = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    bucket_size = 10

    # Crear cubetas vacías
    buckets = [[] for _ in range(bucket_size)]

    # Colocar los elementos en las cubetas
    for num in arr:
        index = int((num - min_val) // ((max_val - min_val) / (bucket_size - 1)))
        buckets[index].append(num)

    # Ordenar las cubetas usando Insertion Sort
    for bucket in buckets:
        insertion_sort(bucket)

    # Concatenar las cubetas ordenadas para obtener el resultado final
    k = 0
    for i in range(bucket_size):
        for num in buckets[i]:
            arr[k] = num
            k += 1

#merge sort
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

#counting sort
def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    count = [0] * range_val
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

#radix sort
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10

# Lista inicial de 100 elementos
size = 100
random_list = [random.randint(0, 10000) for _ in range(size)]

# Listas para almacenar los tiempos de ejecución y el tamaño de las listas
merge_times = []#4
quick_times = []#5
bubble_times = []#2
selection_times = [] #1
insertion_times = []#3
heap_times = []#6
counting_times = []#7
radix_times = []#8
bucket_times = []#9
log_n_times = []#10
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
heap_sort(random_list)
end_time = time.time()
heap_time = end_time - start_time
heap_times.append(heap_time)


start_time = time.time()
counting_sort(random_list)
end_time = time.time()
counting_time = end_time - start_time
counting_times.append(counting_time)

start_time = time.time()
radix_sort(random_list)
end_time = time.time()
radix_time = end_time - start_time
radix_times.append(radix_time)

start_time = time.time()
bucket_sort(random_list)
end_time = time.time()
bucket_time = end_time - start_time
bucket_times.append(bucket_time)


log_n_time = math.log(size) * 0.01  # Ajusta el factor 0.01 según sea necesario para escalas adecuadas en el gráfico
log_n_times.append(log_n_time)


# Ordenar la lista con ambos algoritmos para tamaños de 100 hasta 50000
while size <= 5000:
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

    # Heapsort
    start_time = time.time()
    heap_sort(random_list)
    end_time = time.time()
    heap_time = end_time - start_time
    heap_times.append(heap_time)
    random_list = [random.randint(0, 10000) for _ in range(size)]

    # Counting sort
    start_time = time.time()
    counting_sort(random_list)
    end_time = time.time()
    counting_time = end_time - start_time
    counting_times.append(counting_time)
    random_list = [random.randint(0, 10000) for _ in range(size)]

    # Radix sort
    start_time = time.time()
    radix_sort(random_list)
    end_time = time.time()
    radix_time = end_time - start_time
    radix_times.append(radix_time)
    random_list = [random.randint(0, 10000) for _ in range(size)]

    # Bucket sort
    start_time = time.time()
    bucket_sort(random_list)
    end_time = time.time()
    bucket_time = end_time - start_time
    bucket_times.append(bucket_time)
    random_list = [random.randint(0, 10000) for _ in range(size)]

    log_n_time = math.log(size) *0.01  # Ajusta el factor 0.01 según sea necesario para escalas adecuadas en el gráfico
    log_n_times.append(log_n_time)

    # Actualizar gráfico
    plt.plot(sizes, selection_times, label='Selectionsort')
    plt.plot(sizes, bubble_times, label='Bubblesort')
    plt.plot(sizes, insertion_times, label='Insertionsort')
    plt.plot(sizes, merge_times, label='Mergesort')
    plt.plot(sizes, quick_times, label='Quicksort')
    plt.plot(sizes, heap_times, label='Heapsort')
    plt.plot(sizes, counting_times, label='Countingsort')
    plt.plot(sizes, radix_times, label='Radixsort')
    plt.plot(sizes, bucket_times, label='Bucketsort')
    plt.plot(sizes, log_n_times, label='log(n)')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ejecución entre Mergesort y Shellsort')
    plt.legend()
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

