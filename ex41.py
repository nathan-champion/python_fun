import random
from urllib.request import urlopen
import sys
import copy



def convert(snippet, phrase):
    # make a list A from a random sample of words in the WORDS from url up to the count of %%% in the string.
    # capitalize the first letter of the word
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    # look for every *** in the snippet from PHRASES and for each ***, get a random
    # sample from WORDS and store it in list B
    other_names = random.sample(WORDS, snippet.count("***"))
    # making some empty arrays
    results = []
    param_names = []

    # for every @@@ in your snippet from PHRASES, get a random number between 1 and 3.
    # get that many WORDS randomly, put them into a string separated with ', ', and
    # append that to the param_names.
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    # we're using snippet and phrase as a kind of 2 index "array" and for every 
    # part...
    for sentence in snippet, phrase:
        #we're making a copy of the string so we can replace words without affecting
        #snippet or phrase
        result = sentence[:]

        #we have one class_name for every %%% in the snippet
        #replace one %%% with one of those names.
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #we have one other name for every *** in snippet
        #replace one *** with one of those names
        for word in other_names:
            result = result.replace("***", word, 1)

        #we have the parameters string, replace every @@@ with the params list.  
        for word in param_names:
            result = result.replace("@@@", word, 1)

        #add the symbol-replaced string to the list of results.
        results.append(result)

    # return those results
    return results


WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":                                                      #snippet
      "Make a class named %%% that is-a %%%",                               #phrase
    "class %%%(object):\n\tdef __init__(self, ***)":                        #snippet
      "class %%% has-a __init__ that takes self and *** params",            #phrase
    "class %%%(object)\n\tdef ***(self, @@@)":                              #snippet
      "class %%% has-a function *** that takes self and @@@ params.",       #phrase
    "*** = %%%()":                                                          #snippet
      "Set *** to an instance of class %%%.",                               #phrase
    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@",
    "***.*** = '***'":                                                      #snippet
      "From *** get the *** attribute and set it to '***'."                 #phrase
}

# do they want to drill phrases first?
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website.
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

good = "good"
bad = copy

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)

            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER:  {answer}\n\n")
except EOFError:
    print("\nBye")
