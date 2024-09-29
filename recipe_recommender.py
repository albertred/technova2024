import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from ast import literal_eval

print("hi")

#  converts ing_list to a lowercase string with punctuation, extra spaces, and stopwords removed 
def ing_list_cleaner(ing_list):
    
    # convert all ingredients to lowercase
    ing_list = ing_list.lower()
    # remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    ing_list = ing_list.translate(translator)

    # remove stopwords and any extra spaces, new lines, or tabs within the individual strings
    
    #nltk.download("stopwords")
    stopwords_ = [] #set(stopwords.words("english"))
    ing_list = " ".join(w for w in ing_list.split() if w not in stopwords_)

    return ing_list

# finds tf idf of user's ingredients
def clean_user_ingredients(u_list):
    return ing_list_cleaner(" ".join(u_list))
    
def get_recommendations(given_ingredients, vectorizer):
    clean_list = clean_user_ingredients(given_ingredients)
    vectorized_user = vectorizer_model.transform([clean_list])
    cos_sim_scores = cosine_similarity(vectorized_user, df["Vectorized_Ingredients"].tolist())[0]
    df["Similarity_Score"] = cos_sim_scores
    top_matches = df.nlargest(12, "Similarity_Score")
    return (top_matches)

def gen_rec(given_ingredients):
    return get_recommendations(given_ingredients, vectorizer_model)

df = pd.read_pickle("recipe_ingredients_list.pkl")
vectorizer_model = pickle.load(open("vectorizer_model", "rb"))

# e.g.
#print(gen_rec(["brown bread", "bananas", "peanut butter", "milk", "strawberries", "soda", "cherries"]))
