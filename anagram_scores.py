import sys
from collections import Counter
from absl import logging


def load_and_sort_dictionary_words(file):
    """Open a text file & turn contents into a sorted list of lowercase strings.
    
    Args:
        file (str): The file location of the dictionary.

    Returns:
        A list of sorted and lowercased dictionary words.

    Raises:
        IOError: An error occurred accessing the dictionary file.
    """
    
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().lower().split('\n')
            return sorted(loaded_txt)
    except IOError as e:
        logging.fatal('Unable to open file %s',file)
 

dict_file = load_and_sort_dictionary_words('dictionary.words')


class AnagramsInfo:
    """A class used to represent an information(word and point) of an anagram.

    Attributes:
        word (str): A word in list of anagrams made from the input letters.  
        point (int): A count of points of each of the words.

    """
    
    def __init__(anagram,word,point):
        """
        Args:
            word (str): A word in list of anagrams made from the input letters.  
            point (int): A count of points of each of the words.            
        """

        anagram.word = word
        anagram.point = point

        
def find_anagrams(input_letters, dictionary_word_list):
    """Read dictionary file & display all anagrams IN input_letters.

    Args:
        input_letters (str): An input from user.             
        word_list (list): A list of sorted and lowercased dictionary words.
  
    """
    
    input_letter_map = Counter(input_letters)
    anagrams_list = []
      
    for word in dictionary_word_list:
        test = ''
        dictionary_letter_map = Counter(word.lower())
        for letter in word:
            if dictionary_letter_map[letter] <= input_letter_map[letter]:
                test += letter
        if Counter(test) == dictionary_letter_map:
            anagrams_list.append(AnagramsInfo(word,0))
  
    point = 0
    THREE_POINT_LETTERS = frozenset(['j','k','x','z'])
    TWO_POINT_LETTERS = frozenset(['q','c','f','h','l','m','p','v','w','y'])
    
    for word in anagrams_list:
        for letter in word.word:            
            if letter in THREE_POINT_LETTERS:
                point += 3
            elif letter in TWO_POINT_LETTERS:    
                point += 2
            else:
                point += 1
        point = (point+1)**2
        word.point = point   
        point = 0
        
    top_point = 0
    top_word = ''
      
    for word in anagrams_list:
        if word.point > top_point:
            top_point = word.point
            top_word = word.word

    if top_word =='':
        print('Could not find any anagrams')
    else:
        print('highest scored anagram --> '+ top_word)
        print('highest score --> '+ str(top_point))


def main():

    print('enter "q" to quit')
    
    while True:
        ini_input_letters = input("Enter : ")
        input_letters = ini_input_letters.lower()  # convert to lower case

        if input_letters == "q":
            break

        find_anagrams(input_letters, dict_file)
    

if __name__ == '__main__':
    main()    
