import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from dataStructure import ds

"""
sorting examples

comparison sort
-bubble sort
-quick sort

selection sort
-selection sort

"""



"""
bubble sort

1. take first value, first step n = 0
2. compare with next value, if current value is bigger than next value then swap
3. repeat 1-2 step (list length - n - 1) times
4. n += 1
5. repeat 1-4 step (list length) times
"""

def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(l - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



"""
quick sort
Ref) https://ko.wikipedia.org/wiki/%ED%80%B5_%EC%A0%95%EB%A0%AC - pseudocode

1. set random pivot
2. divide list base on pivot value
3. repeat 1-2 step until list length become 1 using recursive
4. return list and concatenate
"""

"""
using more memory(make additional list)
"""

def _quick_sort(arr):
    less, greater = [], []
    if len(arr) <= 1:
        return arr
    pivot = arr.pop(len(arr)//2)
    for index in arr:
        if pivot < index:
            greater.append(index)
        else:
            less.append(index)
    return _quick_sort(less) + [pivot] + _quick_sort(greater)

"""
using only one list(need less memory)
1. set random pivot
2. divide base on pivot value in current range -> partition
3. recursive(pass right and left range)
4. repeat 1-3 step until arr no more need to divide
"""

def quick_sort(arr):
    def partition(arr, left, right, pivot_index):
        pivot = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        stored_index = left
        for i in range(left, right):
            if arr[i] <= pivot:
                arr[i], arr[stored_index] = arr[stored_index], arr[i]
                stored_index += 1
        arr[stored_index], arr[right] = arr[right], arr[stored_index]
        return stored_index

    def recursive_quick_sort(arr, left, right):
        if right > left:
            pivot = (left+right)//2
            pivot = partition(arr, left, right, pivot)
            recursive_quick_sort(arr, left, pivot-1)
            recursive_quick_sort(arr, pivot+1, right)
    
    recursive_quick_sort(arr, 0, len(arr)-1)

    return arr



"""
selection sort

1. find min value index in range( n ~ list length - 1), first try n = 0
2. swap(min value index, n)
3. repeat 1-2 step (list length) times
"""

def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        min = i
        for j in range(i+1, l):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr



"""
heap sort
"""

def heap_sort(arr):
    
    pass



def sort(method):
    origin_data = []
    while input_data := input():
        try:
            input_numbers = map(int, input_data.split())
            origin_data += input_numbers
            origin_data = method(origin_data)
            print(*origin_data)
        except Exception as e:
            print(e)

sort(selection_sort)