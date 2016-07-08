from copy import deepcopy

NUM_SWAPS = 0
    
def partition(a, start, end):
    global NUM_SWAPS
    pivot = a[end]
    p = start
    for i in range(start, end):
        if a[i] < pivot:
            tmp = a[i]
            a[i] = a[p]
            a[p] = tmp
            p += 1
            NUM_SWAPS += 1
    if p < end:
        a[end] = a[p]
        a[p] = pivot
    NUM_SWAPS += 1
    return p

def quicksort_helper(a, start, end):
    if start < end:
        p = partition(a, start, end)
        quicksort_helper(a, start, p-1)
        quicksort_helper(a, p+1, end)

def quicksort(a):
    quicksort_helper(a, 0, len(a)-1)
    
def insertionsort(ar):
    num_shifts = 0
    for i in range(len(ar)):
        value = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > value:
            ar[j + 1] = ar[j]
            num_shifts += 1
            j -= 1
        ar[j + 1] = value
    return num_shifts

def main():
    n = int(input())
    ar = [int(x) for x in input().split()]
    quicksort(deepcopy(ar))
    num_shifts = insertionsort(ar)
    print(num_shifts - NUM_SWAPS)

if __name__ == '__main__':
    main()