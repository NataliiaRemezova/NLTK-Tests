import numpy
import nltk

def main(): 
    example = 'I was on hold for 40 minutes, their customer support service is a nightmare'
    tokens = nltk.word_tokenize(example)
    print(tokens)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    entities.pprint()

if __name__ == "__main__":
    main()
