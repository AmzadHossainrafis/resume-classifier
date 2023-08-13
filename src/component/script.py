import pickle
import os 
import argparse
import sys
import re
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
sb = SnowballStemmer("english")
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from PyPDF2 import PdfReader

stopwords = stopwords.words('english')


def remove_breket(text):
    text = text.replace(']', '').replace('[', '').replace("'", "").replace('(', '').replace(')', '').replace('/', '')
    return text

def remove_numbers(text):
    text = re.sub(r'\d+', '', text)
    return text

def lower_case(text):
    return text.lower()

def remove_extra_spaces(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def remove_stopwords(text):
    text = [word for word in word_tokenize(text) if word not in stopwords]
    return " ".join(text)


def snowball_stemmer(text):
    return ' '.join([sb.stem(word) for word in word_tokenize(text)])






vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)


#parser path 
parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default='data', help='path to data')
model_path = os.path.join(os.getcwd(), 'finalized_model.sav')
model = pickle.load(open(model_path, 'rb'))
args = parser.parse_args()


list_of_files = os.listdir(args.path) 
Id=[]
prediction=[]
for file in list_of_files:
    if file.endswith('.pdf'):
        pdf_path = os.path.join(args.path, file)
        pdf = PdfReader(pdf_path)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        text = remove_breket(text)
        text = remove_numbers(text)
        text = lower_case(text)
        text = remove_extra_spaces(text)
        text = remove_stopwords(text)
        text = snowball_stemmer(text)
        text = [text]
        X =vectorizer.fit_transform(text)
        X = np.hstack((X.toarray(), np.zeros((X.shape[0], 1000-X.shape[1]))))
        pred = model.predict(X)
        Id.append(file)
        prediction.append(pred[0])
        #make dir if not exist 
        if not os.path.exists(os.path.join(args.path, pred[0])):
            os.makedirs(os.path.join(args.path, pred[0]))
        #move file to the dir
        os.rename(pdf_path, os.path.join(args.path, pred[0], file))

     
    else:
        print("File format is not supported")   
    


df = pd.DataFrame({'Id':Id, 'Category':prediction})
df.to_csv(os.path.join(args.path, 'categorized_resumes.csv'), index=False)






