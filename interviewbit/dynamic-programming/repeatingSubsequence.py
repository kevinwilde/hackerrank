# Given a string, find if there is any sub-sequence of length at least 2 that repeats itself.


def anytwo(A):
    subs = []
    for i in range(len(A)):
        for j in range(i):
            sub = A[j]+A[i]
            for t in subs:
                if t[0] == sub and t[1] != j and t[2] != i:
                    return True
            subs.append((sub,j,i))
    return False

### Tests
assert anytwo('abab')
assert not anytwo('abba')
assert anytwo('aaa')
assert anytwo('abcac')
assert not anytwo('abcde')
assert not anytwo('abcdcba')
