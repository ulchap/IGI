def print_list(words):
    """Outputs the given list"""
    for word in words: print(word)
    
def instruction_msg():
    """"Describes program's functionality."""
    print("This program analyzes given string and outputs following data about it:\n"
          "1. Get the list of words that start with vowel.\n"
          "2. Get the words with double letters.\n"
          "3. Get sorted list of words.")
    
def print_result(result):
    print("Words with double letters and indexes:", result)