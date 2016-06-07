def max_contiguous_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        a = [int(x) for x in input().split()]
        
        sum_positive = sum([x if x > 0 else 0 for x in a])
        if sum_positive <= 0:
            sum_positive = max(a)
        # Max sum of contiguous subarray, Sum of positive elements
        print(max_contiguous_subarray(a), sum_positive)

if __name__ == '__main__':
    main()