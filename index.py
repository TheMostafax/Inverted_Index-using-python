import numpy as np
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from tabulate import tabulate
nltk.download('punkt')
nltk.download('stopwords')
ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

doc1 = "The cat in the hat"
doc2 = "The cat sat on the mat"
doc3 = "The dog ate my homework"
doc4 = "I hate cats and dogs"

token1 = word_tokenize(doc1)
token2 = word_tokenize(doc2)
token3 = word_tokenize(doc3)
token4 = word_tokenize(doc4)

term=token1+token2+token3+token4

Stemmingone = []
Stemmingtwo = []
Stemmingthree = []
Stemmingfour = []
for x in token1:
    Stemmingone.append(ps.stem(x))
for y in token2:
    Stemmingtwo.append(ps.stem(y))
for z in token3:
    Stemmingthree.append(ps.stem(z))
for m in token4:
    Stemmingfour.append(ps.stem(m))

Remove_stopWordsone = []
Remove_stopWordstwo = []
Remove_stopWordsthree = []
Remove_stopWordsfour = []
for i in Stemmingone:
    if i not in stop_words:
        Remove_stopWordsone.append(i)
for i in Stemmingtwo:
    if i not in stop_words:
        Remove_stopWordstwo.append(i)
for i in Stemmingthree:
    if i not in stop_words:
        Remove_stopWordsthree.append(i)
for i in Stemmingfour:
    if i not in stop_words:
        Remove_stopWordsfour.append(i)


        
Stemming = []
for w in Remove_stopWords:
    Stemming.append(ps.stem(w))

    
    
LowerCaseone = []
LowerCasetwo = []
LowerCasethree = []
LowerCasefour = []
for i in Remove_stopWordsone :
    LowerCaseone.append(i.lower())
for i in Remove_stopWordstwo :
    LowerCasetwo.append(i.lower())
for i in Remove_stopWordsthree :
    LowerCasethree.append(i.lower())
for i in Remove_stopWordsfour :
    LowerCasefour.append(i.lower())

LowerCase = []
for i in term :
    LowerCase.append(i.lower())

Remove_stopWords = []
for i in LowerCase:
    if i not in stop_words:
        Remove_stopWords.append(i)


Stemming = []
for w in Remove_stopWords:
    Stemming.append(ps.stem(w))


Unique_elements= set(Stemming)
Unique_elements_sort = sorted(Unique_elements)


inverted_index = {}
count=0
for i, doc in enumerate(Unique_elements_sort):
    for term in doc.split():
        if term in inverted_index:
            inverted_index[term].add(i)
            
        else: inverted_index[term] = {i}
        



count = 0
save = []
frequency = []
posting_list = []
for x in inverted_index:
    count=0
    save.append(x)
    frequency.append(x)
    for  y in LowerCaseone:
        if x==y:
            count+=1
            save.append("Doc: (1)")
    for  z in LowerCasetwo:
        if x==z:
            count+=1
            save.append("Doc: (2)")
    for  m in LowerCasethree:
        if x==m:
            count+=1
            save.append("Doc: (3)")
        
    for  n in LowerCasefour:
        if x==n:
            count+=1
            save.append("Doc: (4)")
    frequency.append("Frecuency : " +str(count))

print("The Word : ....." + "The Frequency : ....")
print()
print()
for u in frequency:
    print(u)
    print("--")
print()
print("-----(Posting List)----")
print()
print("The Word : ....." + "The Doc ID : ....")
print()
for t in save:
    print(t)
    print("--")
#print(tabulate(save))

