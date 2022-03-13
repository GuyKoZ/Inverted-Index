# H.W 1 - Guy Kozliner (316612662) || Kobi Hazout (205874233)
import nltk
import collections

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import snowball
from snowballstemmer import stemmer
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stwords = set(stopwords.words('english'))
stemmer = snowball.SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()


class InvIndex:

    def __init__(self):
        self.inv = {}

    def new_index(self, cor):
        global lemmatized_words
        punc = [',', '!', ';', '(', ')', '[', ']', '}', '{', '@', '#', '$', '%', '^', '&', '*', '.', '-', '--']
        counter = {}
        cor_words = []
        index_num = 0
        last_added = 0

        for n in cor:
            w_token = word_tokenize(n)
            cor_words += w_token
            # Set data to lower case and remove regular expressions and stopwords
            lower_cor = [x.lower() for x in cor_words if x not in punc and x not in stwords]
            # stem and lemmatization
            stem = [stemmer.stem(word)
                             for word in lower_cor]
            lemmatized_words = [lemmatizer.lemmatize(w) for w in stem]
            new_added = len(lemmatized_words)
            # count frequency for each word
            new_words = lemmatized_words[last_added:new_added]
            counter[index_num] = collections.Counter(
                new_words)
            index_num += 1

            last_added = new_added
        # remove duplicates
        final_words = set(lemmatized_words)
        val_list = []
        # adding index after checking appearances
        for words in final_words:
            for documents in counter:
                if words in counter[documents]:
                    freq = [documents + 1, counter[documents][words]]
                    val_list.append(freq)
            self.inv[words] = val_list
            val_list = []  # clean val_list

        print('The number of keys in the files is : ')
        print(len(self.inv.keys()))

    def search_index(self, query):
        punc = [',', '!', ';', '(', ')', '[', ']', '}', '{', '@', '#', '$', '%', '^', '&', '*', '.', '-', '--']
        matched_documents = []
        for word in word_tokenize(query):
            word_lower = word.lower()
            if word_lower not in stwords and word_lower not in punc:
                word_stem = stemmer.stem(word_lower)
                lemm_word = lemmatizer.lemmatize(word_stem)
                matches = self.inv.get(lemm_word)
                if matches:
                    doc_matches = []
                    # clean appearances from results
                    for list in matches:
                        doc_matches.append(list[0])
                    matched_documents.append(doc_matches)
        last_combination = matched_documents[0]
        for x in range(len(matched_documents)):
            last_combination = [
                val_list for val_list in last_combination if val_list in matched_documents[x]]

        return last_combination