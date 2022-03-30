def longest_word(filename):
    with open(filename, 'r') as in_file:
        words = in_file.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]


print(longest_word('test.txt'))
