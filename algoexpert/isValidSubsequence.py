def isValidSubsequence(array, sequence):
    seq_index = 0
    for item in array:
        if seq_index == len(sequence):
            break
        if item == sequence[seq_index]:
            seq_index += 1
    return seq_index == len(sequence)
