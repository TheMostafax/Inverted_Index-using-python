{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "f4c75dc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to C:\\Users\\Mostafa\n",
      "[nltk_data]     Hassan\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n",
      "[nltk_data] Downloading package stopwords to C:\\Users\\Mostafa\n",
      "[nltk_data]     Hassan\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n",
      "Unable to create process using 'C:\\Users\\Mostafa Hassan\\anaconda3\\python.exe \"C:\\Users\\Mostafa Hassan\\anaconda3\\Scripts\\pip-script.py\" install tabulate'\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import nltk\n",
    "from nltk.tokenize import word_tokenize,sent_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.stem import PorterStemmer\n",
    "from tabulate import tabulate\n",
    "nltk.download('punkt')\n",
    "nltk.download('stopwords')\n",
    "ps = PorterStemmer()\n",
    "stop_words = set(stopwords.words(\"english\"))\n",
    "!pip install tabulate"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c19d83d4",
   "metadata": {},
   "source": [
    "# Stop Words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "e4687e29",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'did', 's', 'wasn', 'o', 'and', 'so', 'few', \"wouldn't\", 'between', 'against', 'doesn', 've', 'itself', 'who', \"haven't\", 'wouldn', 'again', 'm', \"that'll\", 'here', 'been', 'they', 'themselves', 'but', 'yourself', \"mustn't\", 'it', 'from', \"shouldn't\", 'out', 'if', 'them', 'hadn', 'its', 'ourselves', 'was', 'after', 'won', 'were', 'down', 'yours', 'll', \"wasn't\", 'herself', 'those', 'does', 'we', 'own', \"mightn't\", 'you', 'how', 'hers', 'him', \"aren't\", \"don't\", 'this', 'y', 'no', 'aren', 'off', 'being', 'than', 'having', 'theirs', 'any', 'mightn', \"hasn't\", 'that', 'all', 'mustn', 'through', 'below', 'some', 'only', 'is', 'haven', 'most', 'the', 'where', 'each', 'your', \"it's\", 'such', 'not', 'doing', 'about', \"isn't\", 'isn', 'while', 'why', 'which', 'nor', 'her', \"couldn't\", \"you'll\", \"you're\", \"she's\", 'before', 'ain', 'should', \"you've\", 'now', 'other', 'weren', 'she', 'are', 'ma', 'further', 'just', 'same', 'on', 'very', 'until', 'more', 'ours', 'with', 're', 'my', 'a', 'there', 'shouldn', 'an', 'has', 'then', 'for', 'had', 'over', 'during', 'up', 't', 'at', 'because', \"won't\", 'couldn', 'too', 'have', \"needn't\", 'himself', \"should've\", 'didn', \"weren't\", 'to', 'i', 'whom', 'needn', 'be', 'in', 'both', 'by', 'above', 'am', 'don', 'into', 'as', 'do', 'when', 'or', 'his', 'myself', 'our', 'under', 'me', 'once', 'of', 'will', 'what', \"you'd\", 'hasn', 'can', \"shan't\", 'd', 'he', \"didn't\", \"doesn't\", 'yourselves', 'these', 'their', 'shan', \"hadn't\"}\n"
     ]
    }
   ],
   "source": [
    "print(stop_words)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4fa5d9ea",
   "metadata": {},
   "source": [
    "# Input Documents"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "3ab7a82b",
   "metadata": {},
   "outputs": [],
   "source": [
    "doc1 = \"The cat in the hat\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "f6f2eb24",
   "metadata": {},
   "outputs": [],
   "source": [
    "doc2 = \"The cat sat on the mat\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "225a1bb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "doc3 = \"The dog ate my homework\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "9dddd075",
   "metadata": {},
   "outputs": [],
   "source": [
    "doc4 = \"I hate cats and dogs\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f9474c02",
   "metadata": {},
   "source": [
    "# Tokenization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "1a07e637",
   "metadata": {},
   "outputs": [],
   "source": [
    "token1 = word_tokenize(doc1)\n",
    "token2 = word_tokenize(doc2)\n",
    "token3 = word_tokenize(doc3)\n",
    "token4 = word_tokenize(doc4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "816844ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['The', 'cat', 'in', 'the', 'hat']"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "token1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "e06e6cee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['The', 'cat', 'sat', 'on', 'the', 'mat']"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "token2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "c46cc4cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['The', 'dog', 'ate', 'my', 'homework']"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "token3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "0629f775",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['I', 'hate', 'cats', 'and', 'dogs']"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "token4"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58adf2e0",
   "metadata": {},
   "source": [
    "# All Term of the Documents"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "b279861d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['The',\n",
       " 'cat',\n",
       " 'in',\n",
       " 'the',\n",
       " 'hat',\n",
       " 'The',\n",
       " 'cat',\n",
       " 'sat',\n",
       " 'on',\n",
       " 'the',\n",
       " 'mat',\n",
       " 'The',\n",
       " 'dog',\n",
       " 'ate',\n",
       " 'my',\n",
       " 'homework',\n",
       " 'I',\n",
       " 'hate',\n",
       " 'cats',\n",
       " 'and',\n",
       " 'dogs']"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "term=token1+token2+token3+token4\n",
    "term"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65576485",
   "metadata": {},
   "source": [
    "# Stemming of each document"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "fac69567",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['the', 'cat', 'in', 'the', 'hat']\n",
      "['the', 'cat', 'sat', 'on', 'the', 'mat']\n",
      "['the', 'dog', 'ate', 'my', 'homework']\n",
      "['i', 'hate', 'cat', 'and', 'dog']\n"
     ]
    }
   ],
   "source": [
    "Stemmingone = []\n",
    "Stemmingtwo = []\n",
    "Stemmingthree = []\n",
    "Stemmingfour = []\n",
    "for x in token1:\n",
    "    Stemmingone.append(ps.stem(x))\n",
    "for y in token2:\n",
    "    Stemmingtwo.append(ps.stem(y))\n",
    "for z in token3:\n",
    "    Stemmingthree.append(ps.stem(z))\n",
    "for m in token4:\n",
    "    Stemmingfour.append(ps.stem(m))\n",
    "\n",
    "print(Stemmingone)\n",
    "print(Stemmingtwo)\n",
    "print(Stemmingthree)\n",
    "print(Stemmingfour)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "706584a0",
   "metadata": {},
   "source": [
    "# Remove Stop Words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "24ed059a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['cat', 'hat']\n",
      "['cat', 'sat', 'mat']\n",
      "['dog', 'ate', 'homework']\n",
      "['hate', 'cat', 'dog']\n"
     ]
    }
   ],
   "source": [
    "Remove_stopWordsone = []\n",
    "Remove_stopWordstwo = []\n",
    "Remove_stopWordsthree = []\n",
    "Remove_stopWordsfour = []\n",
    "for i in Stemmingone:\n",
    "    if i not in stop_words:\n",
    "        Remove_stopWordsone.append(i)\n",
    "for i in Stemmingtwo:\n",
    "    if i not in stop_words:\n",
    "        Remove_stopWordstwo.append(i)\n",
    "for i in Stemmingthree:\n",
    "    if i not in stop_words:\n",
    "        Remove_stopWordsthree.append(i)\n",
    "for i in Stemmingfour:\n",
    "    if i not in stop_words:\n",
    "        Remove_stopWordsfour.append(i)\n",
    "print(Remove_stopWordsone)\n",
    "print(Remove_stopWordstwo)\n",
    "print(Remove_stopWordsthree)\n",
    "print(Remove_stopWordsfour)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a4a59a8e",
   "metadata": {},
   "source": [
    "# LowerCase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "2ec145b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['cat', 'hat']\n",
      "['cat', 'sat', 'mat']\n",
      "['dog', 'ate', 'homework']\n",
      "['hate', 'cat', 'dog']\n"
     ]
    }
   ],
   "source": [
    "LowerCaseone = []\n",
    "LowerCasetwo = []\n",
    "LowerCasethree = []\n",
    "LowerCasefour = []\n",
    "for i in Remove_stopWordsone :\n",
    "    LowerCaseone.append(i.lower())\n",
    "for i in Remove_stopWordstwo :\n",
    "    LowerCasetwo.append(i.lower())\n",
    "for i in Remove_stopWordsthree :\n",
    "    LowerCasethree.append(i.lower())\n",
    "for i in Remove_stopWordsfour :\n",
    "    LowerCasefour.append(i.lower())\n",
    "\n",
    "print(LowerCaseone)\n",
    "print(LowerCasetwo)\n",
    "print(LowerCasethree)\n",
    "print(LowerCasefour)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "a5ffb801",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['the', 'cat', 'in', 'the', 'hat', 'the', 'cat', 'sat', 'on', 'the', 'mat', 'the', 'dog', 'ate', 'my', 'homework', 'i', 'hate', 'cats', 'and', 'dogs']\n"
     ]
    }
   ],
   "source": [
    "LowerCase = []\n",
    "for i in term :\n",
    "    LowerCase.append(i.lower())\n",
    "\n",
    "print(LowerCase)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "3a50fec7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['cat', 'hat', 'cat', 'sat', 'mat', 'dog', 'ate', 'homework', 'hate', 'cats', 'dogs']\n"
     ]
    }
   ],
   "source": [
    "Remove_stopWords = []\n",
    "for i in LowerCase:\n",
    "    if i not in stop_words:\n",
    "        Remove_stopWords.append(i)\n",
    "\n",
    "print(Remove_stopWords)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17710203",
   "metadata": {},
   "source": [
    "# Stemming the whole term"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "9d3f13e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['cat',\n",
       " 'hat',\n",
       " 'cat',\n",
       " 'sat',\n",
       " 'mat',\n",
       " 'dog',\n",
       " 'ate',\n",
       " 'homework',\n",
       " 'hate',\n",
       " 'cat',\n",
       " 'dog']"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Stemming = []\n",
    "for w in Remove_stopWords:\n",
    "    Stemming.append(ps.stem(w))\n",
    "Stemming"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b19dd333",
   "metadata": {},
   "source": [
    "# Sorted Unique elements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "10ca740e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'mat', 'homework', 'hat', 'ate', 'sat', 'dog', 'hate', 'cat'}\n",
      "Sorted Unique elements : ['ate', 'cat', 'dog', 'hat', 'hate', 'homework', 'mat', 'sat']\n"
     ]
    }
   ],
   "source": [
    "Unique_elements= set(Stemming)\n",
    "Unique_elements_sort = sorted(Unique_elements)\n",
    "print(Unique_elements)\n",
    "print(\"Sorted Unique elements : \" + str(Unique_elements_sort))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9665486",
   "metadata": {},
   "source": [
    "# Index of final list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "23946119",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'ate': {0}, 'cat': {1}, 'dog': {2}, 'hat': {3}, 'hate': {4}, 'homework': {5}, 'mat': {6}, 'sat': {7}}\n"
     ]
    }
   ],
   "source": [
    "inverted_index = {}\n",
    "count=0\n",
    "for i, doc in enumerate(Unique_elements_sort):\n",
    "    for term in doc.split():\n",
    "        if term in inverted_index:\n",
    "            inverted_index[term].add(i)\n",
    "            \n",
    "        else: inverted_index[term] = {i}\n",
    "        \n",
    "\n",
    "\n",
    "print(inverted_index)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e6be516",
   "metadata": {},
   "source": [
    "# Final Result of Documents (Posting List and frequency)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "4e0b0edb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Word : .....The Frequency : ....\n",
      "\n",
      "\n",
      "ate\n",
      "--\n",
      "Frecuency : 1\n",
      "--\n",
      "cat\n",
      "--\n",
      "Frecuency : 3\n",
      "--\n",
      "dog\n",
      "--\n",
      "Frecuency : 2\n",
      "--\n",
      "hat\n",
      "--\n",
      "Frecuency : 1\n",
      "--\n",
      "hate\n",
      "--\n",
      "Frecuency : 1\n",
      "--\n",
      "homework\n",
      "--\n",
      "Frecuency : 1\n",
      "--\n",
      "mat\n",
      "--\n",
      "Frecuency : 1\n",
      "--\n",
      "sat\n",
      "--\n",
      "Frecuency : 1\n",
      "--\n",
      "\n",
      "-----(Posting List)----\n",
      "\n",
      "The Word : .....The Doc ID : ....\n",
      "\n",
      "ate\n",
      "--\n",
      "Doc: (3)\n",
      "--\n",
      "cat\n",
      "--\n",
      "Doc: (1)\n",
      "--\n",
      "Doc: (2)\n",
      "--\n",
      "Doc: (4)\n",
      "--\n",
      "dog\n",
      "--\n",
      "Doc: (3)\n",
      "--\n",
      "Doc: (4)\n",
      "--\n",
      "hat\n",
      "--\n",
      "Doc: (1)\n",
      "--\n",
      "hate\n",
      "--\n",
      "Doc: (4)\n",
      "--\n",
      "homework\n",
      "--\n",
      "Doc: (3)\n",
      "--\n",
      "mat\n",
      "--\n",
      "Doc: (2)\n",
      "--\n",
      "sat\n",
      "--\n",
      "Doc: (2)\n",
      "--\n"
     ]
    }
   ],
   "source": [
    "count = 0\n",
    "save = []\n",
    "frequency = []\n",
    "posting_list = []\n",
    "for x in inverted_index:\n",
    "    count=0\n",
    "    save.append(x)\n",
    "    frequency.append(x)\n",
    "    for  y in LowerCaseone:\n",
    "        if x==y:\n",
    "            count+=1\n",
    "            save.append(\"Doc: (1)\")\n",
    "    for  z in LowerCasetwo:\n",
    "        if x==z:\n",
    "            count+=1\n",
    "            save.append(\"Doc: (2)\")\n",
    "    for  m in LowerCasethree:\n",
    "        if x==m:\n",
    "            count+=1\n",
    "            save.append(\"Doc: (3)\")\n",
    "        \n",
    "    for  n in LowerCasefour:\n",
    "        if x==n:\n",
    "            count+=1\n",
    "            save.append(\"Doc: (4)\")\n",
    "    frequency.append(\"Frecuency : \" +str(count))\n",
    "\n",
    "print(\"The Word : .....\" + \"The Frequency : ....\")\n",
    "print()\n",
    "print()\n",
    "for u in frequency:\n",
    "    print(u)\n",
    "    print(\"--\")\n",
    "print()\n",
    "print(\"-----(Posting List)----\")\n",
    "print()\n",
    "print(\"The Word : .....\" + \"The Doc ID : ....\")\n",
    "print()\n",
    "for t in save:\n",
    "    print(t)\n",
    "    print(\"--\")\n",
    "#print(tabulate(save))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b32f7968",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a4e2a23",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c66f86f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
