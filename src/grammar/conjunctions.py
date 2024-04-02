# checks if conjunctions are used correctly, i.e. 'and' is used to join two words, not 'or'
# cannot have multiple 'and's in a sentence
import spacy
from spacy import displacy
import re

# temporary until our own model is trained
nlp = spacy.load('en_core_web_sm')
def duplicateAnds (sentences):

    numOfDuplicates = 0
    for sentence in sentences:
        tokenizedSentence = nlp(sentence)
        foundAnd = False; 
        for tokenizedWord in tokenizedSentence:
            if str(tokenizedWord) == "and":
                if foundAnd == False:
                    foundAnd = True
                elif foundAnd == True: 
                    numOfDuplicates += 1
    return numOfDuplicates

def main(sentences):
    
    res = duplicateAnds(sentences)
    if res>0:
        print ("Minor Style Error: Detected two or more \"and\" in the sentence")

    

sentences = ['I like Chelsea and Juventus and hate Tottenham and AC Milan',
              'I went to the Andes and Lake Titicaca',
              'And then I walked and then I slept']
main(sentences)


