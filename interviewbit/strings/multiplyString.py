# Given two positive integers as strings, return their product as a string

def multiply(A, B):
    outputs = []
    for (idx,j) in enumerate(B[::-1]):
        output = '0'*idx
        carry = 0
        for i in A[::-1]:
            output = str((int(j) * int(i) + carry) % 10) + output
            carry = (int(j) * int(i) + carry) / 10
        if carry:
            output = str(carry) + output
        outputs.append(output)
    return str(sum(map(int,outputs)))

### Tests
assert multiply('5', '3') == '15'
assert multiply('25', '4') == '100'
assert multiply('25', '40') == '1000'
assert multiply('117', '34') == '3978'
