import text_analyzer
import zipfile

# Открываем исходный файл
with open("D:/lab4_igi/task2/input.txt", 'r') as file:
    text = file.read()

with open("D:/lab4_igi/task2/prices.txt", 'r') as file:
    prices_text = file.read()    

num_sentences = text_analyzer.count_sentences(text)
narrative_sentences = text_analyzer.count_sentences_by_type(text, 1)
interrogative_sentences = text_analyzer.count_sentences_by_type(text, 2)
imperative_sentences = text_analyzer.count_sentences_by_type(text, 3)
avg_sentence_length = text_analyzer.average_length_sentence(text)
avg_word_length = text_analyzer.average_length_word(text)
short_words = text_analyzer.short_words(text)
shortest_a_word = text_analyzer.shortest_a_word(text)
sorted_words = text_analyzer.sorted_len_words(text)
prices = text_analyzer.extract_prices(prices_text)
smileys = text_analyzer.count_smileys(text)

# Сохранение результатов в файл
with open('results.txt', 'w') as result_file:
    result_file.write(f"Number of sentences: {num_sentences}\n")
    result_file.write(f"Narrative sentences: {narrative_sentences}\n")
    result_file.write(f"Interrogative sentences: {interrogative_sentences}\n")
    result_file.write(f"Imperative sentences: {imperative_sentences}\n")
    result_file.write(f"Average sentence length: {avg_sentence_length}\n")
    result_file.write(f"Average word length: {avg_word_length}\n")
    result_file.write(f"Number of words with less than 7 characters: {short_words}\n")
    result_file.write(f"Shortest word ending with 'a': {shortest_a_word}\n")
    result_file.write(f"Count smileys: {smileys}\n")
    result_file.write("Words in descending order of length:\n")
    for word in sorted_words:
        result_file.write(f"{word}\n")
    result_file.write("Extracted prices:\n")
    for price in prices:
        result_file.write(f"{price}\n")

# Архивация файла с результатами
with zipfile.ZipFile('results.zip', 'w') as zipf:
    zipf.write('results.txt')
    try:
        hello_file = zipf.getinfo("results.txt")
        print("File's size: ")
        print(hello_file.file_size)
        print("Archive's info: ")
        print(zipf.infolist())
        for item in zipf.namelist():
            print("Archive's items: ")
            print(item)
    except KeyError:
        print("Указанный файл отсутствует")

