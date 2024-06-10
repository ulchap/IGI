def split_line(line):
    """Splits a line into words by spaces and delimeters."""
    separators = [',', '.']
    for separator in separators:
        line = ' '.join(line.split(separator))
    return line.split()

def starts_vowel(words):
    """Returns words that start with vowel."""
    vowels = 'aeuioAEUIO'
    return [word for word in words if word[0] in vowels]

def find_words_with_double_letters(input_string):
    """Returns words with double letters."""
    words = input_string.split()
    result = []
    number = 0
    for word in words:
        number += 1
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                result.append((number, word))
                break
    return result

def get_sorted_words(words):
    """Returns list of words sorted by alphabet."""
    buffer = []
    for word in words:
        buffer.append(word.lower())
    return sorted(buffer)
