# Program Purpose: Task 4.
# Lab Work Number: 3
# Program Name: Lexical Analyzer
# Version: 1.0
# Developer: Pobortsava Ulyana

import lexicalAnalysis as analyzer
import output as out
import input as inp

given_str="So she was considering in her own mind, as well as she could," \
          " for the hot day made her feel very sleepy and stupid, whether the pleasure" \
          " of making a daisy-chain would be worth the trouble of getting up and picking the daisies," \
          " when suddenly a White Rabbit with pink eyes ran close by her."


words=analyzer.split_line(given_str)  #Split line into words.
out.instruction_msg()  #Print the program's functionality.
while True:
    choice = inp.input_int()  #Input function's number.

    if choice==1:
        print("The list of words that start with vowel: ")
        words1 =analyzer.starts_vowel(words)
        out.print_list(words1)
    elif choice==2:
        print("The words with double letters: ")
        words2=analyzer.find_words_with_double_letters(given_str)
        out.print_result(words2)
    elif choice==3:
        print("Words sorted in alphabet:")
        sorted_words=analyzer.get_sorted_words(words)
        out.print_list(sorted_words)
    if not inp.continue_or_exit():  #Ask user if he wants to finish the program or continue.  
        break