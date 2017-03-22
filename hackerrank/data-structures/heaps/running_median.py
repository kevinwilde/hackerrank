## Given an input stream of  integers, you must perform the following task for each  integer:
##
## 1. Add the  integer to a running list of integers.
## 2. Find the median of the updated list (i.e., for the first element through the  element).
## 3. Print the list's updated median on a new line. 

import heapq

class MaxHeap(object):
    def __init__(self):
        self._h = []

    def __len__(self):
        return len(self._h)

    def push(self, o):
        heapq.heappush(self._h, -1*o)

    def pop(self):
        return -1*heapq.heappop(self._h)

    def peek(self):
        if self._h:
            return -1*self._h[0]
        return None

    def empty(self):
        return len(self._h) == 0

class MinHeap(object):
    def __init__(self):
        self._h = []

    def __len__(self):
        return len(self._h)

    def push(self, o):
        heapq.heappush(self._h, o)

    def pop(self):
        return heapq.heappop(self._h)

    def peek(self):
        if self._h:
            return self._h[0]
        return None

    def empty(self):
        return len(self._h) == 0

def main():
    smaller = MaxHeap()
    bigger = MinHeap()

    for _ in range(int(input())):
        a = int(input())
        if smaller.empty() or a < smaller.peek():
            smaller.push(a)
        else:
            bigger.push(a)

        # Maintain balance
        while len(smaller) - len(bigger) not in [0, 1]:
            if len(smaller) > len(bigger):
                bigger.push(smaller.pop())
            else:
                smaller.push(bigger.pop())

        # Odd number of elements
        # Median is max of smaller
        if len(smaller) - len(bigger) == 1:
            print(float(smaller.peek()))

        # Even number of elements
        # Median is mean of max of smaller and min of bigger
        else:
            print((smaller.peek() + bigger.peek()) / 2)

if __name__ == '__main__':
    main()
