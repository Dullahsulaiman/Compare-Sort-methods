
"""
Abdallah Sulauman
Austin Welter
Srisaipranay Bande

Project 2

"""
import time
import sys
from numpy import random
from random import randint

def bubbleSort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)


def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


end = " "


def printList(list):
    for i in range(len(list)):
        print(list[i], end == " ")
    print()


x = 0
while (x != 12):

    arr = random.randint(100000, size=(1000))
    arr1 = random.randint(100000, size=(10000))
    arr2 = random.randint(100000, size=(50000))

    mergeSort(arr)
    mergeSort(arr1)
    mergeSort(arr2)

    sor = arr
    sor1 = arr1
    sor2 = arr2

    res = sor[::-1]
    res1 = sor1[::-1]
    res2 = sor2[::-1]

    arr = random.randint(100000, size=(1000))
    arr1 = random.randint(100000, size=(10000))
    arr2 = random.randint(100000, size=(50000))
    #t0 = time.time()
    if (x == 0):
        # Average Case
        print("Merge average case")
        t0 = time.time()
        mergeSort(arr)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        mergeSort(arr1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        mergeSort(arr2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
        # Best Case
    elif (x == 1):
        print("Merge best case")
        t0 = time.time()
        mergeSort(sor)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        mergeSort(sor1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        mergeSort(sor2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
        # Worst Case
    elif (x == 2):
        print("Merge worst case")
        t0 = time.time()
        mergeSort(res)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        mergeSort(res1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        mergeSort(res2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
        name = "mergeSort"
    elif (x == 3):
        # Average Case
        print("Bubble average case")
        t0 = time.time()
        bubbleSort(arr)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        bubbleSort(arr1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        bubbleSort(arr2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
        # Best Case
    elif (x == 4):
        print("Bubble best case")
        t0 = time.time()
        bubbleSort(sor)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        bubbleSort(sor1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        bubbleSort(sor2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
        
        # Worst Case
    elif (x == 5):
        print("Bubble worst case")
        t0 = time.time()
        bubbleSort(res)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        bubbleSort(res1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        bubbleSort(res2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
        name = "BubbleSort"
    elif (x == 6):
        print("Quick average case")
        t0 = time.time()
        quickSort(arr)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        quickSort(arr1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        quickSort(arr2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
    elif (x == 7):
        print("Quick best case")
        t0 = time.time()
        quickSort(res)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        quickSort(res1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        quickSort(res2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
    elif (x == 8):
        print("Quick worst case")
        t0 = time.time()
        quickSort(sor)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        quickSort(sor1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        quickSort(sor2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
        name = "QuickSort"
    elif (x == 9):
        # Average Case
        print("Insertion average case")
        t0 = time.time()
        insertionSort(arr)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        insertionSort(arr1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        insertionSort(arr2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
        # Best Case
    elif (x == 10):
        print("Insertion best case")
        t0 = time.time()
        insertionSort(sor)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        insertionSort(sor1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        insertionSort(sor2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
        # Worst Case
    elif (x == 11):
        print("Insertion worst case")
        t0 = time.time()
        insertionSort(res)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("1000 elements = ", total)
        t0 = time.time()
        insertionSort(res1)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("10000 elements = ", total)
        t0 = time.time()
        insertionSort(res2)
        t1 = time.time()
        total = str(round(t1 - t0, 3))
        print("50000 elements = ", total)
        name = "InsertionSort"
    #t1 = time.time()
    x = x + 1
    # printList(arr)
    """total = str(round(t1 - t0, 3))
    with open('output.txt', 'a') as f:
        f.write(total + " " + name + " \n")
    print(total)
    """