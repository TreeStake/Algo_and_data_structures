def biggest_sequence(sequence):
    max_counter = 0
    counter = 0
    n = 1
    for i in range(1, len(sequence) - 1):
        if sequence[i - 1] < sequence[i] and sequence[i] > sequence[i + 1]:
            counter = 3
            while (i - (n + 1)) >= 0 and sequence[i - n] > sequence[i - (n + 1)]:
                counter += 1
                n += 1
            else:
                n = 1
            while (i + (n + 1)) < len(sequence) and sequence[i + n] > sequence[i + (n + 1)]:
                counter += 1
                n += 1
            else:
                n = 1
        if counter > max_counter:
            max_counter = counter

    print(max_counter)

    return max_counter
