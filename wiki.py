import wikipedia as wk

def wiki(Q):
    input = Q

    #wk.set_lang("fr") #change language if u want

    return(wk.summary(input,sentences=2))

print(wiki("trump"))