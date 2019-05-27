import sys
from collections import Counter
def load(file):
    """Open a text file & turn contents into a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)

dict_file = load('dictionary.words')

dict_file = sorted(dict_file)

class anagramsInfo:
    def __init__(anagram,word,point):
        anagram.word = word
        anagram.point = point

        
def find_anagrams(mixedletters, word_list):
    """Read name & dictionary file & display all anagrams IN mizedletters."""
    mixed_letter_map = Counter(mixedletters)
    anagrams = []
    
    
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= mixed_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            #anagrams.append(word)
            anagrams.append(anagramsInfo(word,0))
    #print(*anagrams, sep='\n')
    

    point = 0
    toppoint = 0
    for word in anagrams:
        
        for letter in word.word:
            
            if letter == 'j' or letter == 'k'or letter == 'x'or letter == 'z':
                word.point += 3
            elif letter == 'q' or letter == 'c'or letter == 'f' or letter == 'h' or letter == 'l' or letter == 'm' or letter == 'p' or letter == 'v' or letter == 'w' or letter == 'y':
                word.point += 2
            else:
                word.point += 1
            
            
       # if point > toppoint:
        #    toppoint = point
           
        point = 0
        
    
    topword = ''
    
    '''    
    for word in anagrams:
        print('word --> ' + word.word)
        print('point --> ' + str(word.point))
    '''        
    for word in anagrams:
        if word.point > toppoint:
            toppoint = word.point
            topword = word.word
            
    print('highest scored anagram --> '+ topword)
    print('highest score --> '+ str(toppoint))
        
    #print("Remaining letters = {}".format(name))
    #print("Number of remaining letters = {}".format(len(name)))
    #print("Number of remaining (real word)anagrams = {}".format(len(anagrams)))



def main():
    """Help user build anagram phrase from their name."""

    
    running = True
    print('enter "q" to quit')
    while running:
        
        ini_mixedletters = input("Enter : ")
        #  convert to lower case
        mixedletters = ini_mixedletters.lower()

        if mixedletters == "q":
            running = False
            sys.exit()

        find_anagrams(mixedletters, dict_file)
    

if __name__ == '__main__':
    main()    
