import re

#general functions

#get sentences
def get_sentences(text):
    sentences = re.split(r'[.!?]', text)
    return sentences

#kol sent
def count_sentences(text):
    sentences = re.findall(r'[A-Z][^.!?]*[.!?]', text)
    num_sentences = len(sentences)
    return num_sentences

#kol sent every type
def count_sentences_by_type(text, choice):
    narrative_sentences = len(re.findall(r'[A-Z][^.!?]*\.', text))
    interrogative_sentences = len(re.findall(r'[A-Z][^.!?]*\?', text))
    imperative_sentences = len(re.findall(r'[A-Z][^.!?]*!', text))
    if choice == 1:
        return narrative_sentences
    elif choice == 2:
        return interrogative_sentences
    elif choice == 3:
        return imperative_sentences
    else:
        return -1

#average length of sent
def average_length_sentence(text):
    sentences = get_sentences(text)
    num_sentences = count_sentences(text)
    avg_sentence_length = sum(len(sentence) for sentence in sentences) / num_sentences
    return avg_sentence_length

#average length of word
def average_length_word(text):
    words = re.findall(r'\b\w+\b', text)
    avg_word_length = sum(len(word) for word in words) / len(words)
    return avg_word_length

#count smileys
def count_smileys(text):
    smileys = re.findall(r'[;:]\-*[\(\[\)\]]+', text)
    return len(smileys)

#functions 17 variant

# Вывести все слова, включающие символы, лежащих в диапазоне от 'f' до 'y'
def words_in_range_f_to_y(text):
    pattern = r'\b[a-z]*[f-y][a-z]*\b'
    matches = re.findall(pattern, text)
    return matches

# Есть текст со списками цен. Извлечь из него цены в USD, RUR, EU.
def extract_prices(text):
    prices = re.findall(r'\b\d+\.\d+\s*(?:USD|RUB|EU)\b', text)
    return prices

# определить число слов, длина которых меньше 7 символов;
def short_words(text):
    short_words = re.findall(r'\b\w{1,6}\b', text)
    return len(short_words)

# найти самое короткое слово, заканчивающееся на букву 'a';
def shortest_a_word(text):
    pattern = r'\b[a-zA-Z]*a\b'
    matches = re.findall(pattern, text)
    shortest_word = min(matches, key=len) if matches else None
    return shortest_word

# вывести все слова в порядке убывания их длин
def sorted_len_words(text):
    words = re.findall(r'\b\w+\b', text)
    sorted_words = sorted(set(words), key=len, reverse=True)
    return sorted_words
