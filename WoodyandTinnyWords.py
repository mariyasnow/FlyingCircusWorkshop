#################
# @file - WoodyandTinnyWords.py
# @author - Mariya Snow <mariya.snow@avg.com>
# @brief - Demo String Manipulation
# @usage
'''bash-3.2$ python WoodyandTinnyWords.py tin gorn antilope sausage
I just like the word. It gives me confidence ... It's got a sort of woody quality
WOODY  - GORN - SAUSAGE
TINY   - TIN
'''
#################
import sys

WOODY_WORDS  = ("GORN", "SAUSAGE", "BOUND", "VOLE", "RECIDIVIST", "CARIBOU")
TINY_WORDS = ["NEWSPAPER", "LITTERBIN", "TIN", "ANTELOPE", "SEEMLY", "PRODDING", "VACUUM", "LEAP", "LEAP"]

def main(argv):
   words_classified = classify_words(argv)
   print("I just like the word. It gives me confidence ... It's got a sort of woody quality ")
   print("WOODY {woody}\nTINY  {tiny}".format(**words_classified))

def cleanup_word(word):
   return word.strip().upper()

def classify_words(words):

   words_classified = {"woody": "",
                       "tiny" : ""}
   for naughty_word in words:
       word = cleanup_word(naughty_word)

       if word in WOODY_WORDS:
           words_classified["woody"] = "{} - {}".format(words_classified.get("woody", ""), word)

       elif word in TINY_WORDS:
           words_classified["tiny"] = "{1} - {0}".format(word, words_classified.get("tiny", ""))

       else:
           pass

   return words_classified

if __name__ == '__main__':
   main(sys.argv[1:])
