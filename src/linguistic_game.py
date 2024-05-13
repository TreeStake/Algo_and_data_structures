def search_chain(filename):
    words_list = read_from_file(filename)

    words_list.sort(key=len)
    chain_lengths = {}

    for word in words_list:
        chain_lengths[word] = 1

        for i in range(len(word)):
            next_word = word[:i] + word[i + 1:]
            if next_word in chain_lengths:
                chain_lengths[word] = max(chain_lengths[word], chain_lengths[next_word] + 1)

    max_chain = max(chain_lengths.values())
    write_to_file(max_chain)
    return max_chain


def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        n = int(file.readline().strip())
        words_list = [file.readline().strip() for _ in range(n)]
    return words_list


def write_to_file(max_chain):
    with open('output.txt', "w", encoding="utf-8") as file:
        file.write(str(max_chain))
