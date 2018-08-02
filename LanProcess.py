from nltk.tokenize import  word_tokenize


def check_cmd(text):

    words = word_tokenize(text)
    return words


out = (check_cmd("hello this what is saidharshan, pleased to meet you"))
# def
for i in range(1,len(out)):
    if(i == "what"):
            # & i+1 == "is"):
        print("it knows")



