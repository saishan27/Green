import wikipedia as wk

input = input("Q: ")

#wk.set_lang("fr") #change language if u want

print(wk.summary(input,sentences=2))