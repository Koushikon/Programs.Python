def display(numbers):
    print(numbers)


def validate_sequence(array, sequence):
    '''
    Time Complexity = O(n)
    Space Complexity = O(1)
    '''
    # arrIdx = 0
    seqIdx = 0
    for idx in array:
        if seqIdx == len(sequence):
            return True
        if idx == sequence[seqIdx]:
            seqIdx += 1
    return seqIdx == len(sequence)

# Validate Sub-sequence Program
# With For loop implementation


arr = [5, 1, 22, 25, 6, -1, 8, 11, 15, 16]
seq = [1, 6, -1, 10]
display(arr)
display(seq)

result = validate_sequence(arr, seq)

if (result):
    print('The second array is the sub-sequence of the first array of elements')
else:
    print('The second array is not the sub-sequence of the first array of elements')
