import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from typing import List, Dict


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def vectorizer_func(senetence_sequences: List[str], vectorizer = None, fit=False):
    # Vectorize the sentences
    if fit:
        vectorizer = TfidfVectorizer()
        sentence_vectors = vectorizer.fit_transform(senetence_sequences)

        return sentence_vectors, vectorizer 

    else:
        vectorizer = vectorizer
        sentence_vectors = vectorizer.transform(senetence_sequences)

    return sentence_vectors



# Function to preprocess text
def preprocess_text(text: str) -> str:
    # Convert text to lowercase
    lowercased_text = text.lower()
    
    # Remove punctuation from text
    punctuation_removed_text = re.sub(r'[^\w\s]', '', lowercased_text)
    
    # Remove special characters and numbers from text
    special_characters_removed_text = re.sub(r'[^a-zA-Z\s]', '', punctuation_removed_text)
    
    # Remove extra whitespace from text
    cleaned_text = re.sub(' +', ' ', special_characters_removed_text)
    
    return cleaned_text


# compare text with database
def get_similar_data(input_vec: List[float], database_vec: List[float]) -> Dict:
    # Calculate cosine similarity
    cosine_similarities = cosine_similarity(input_vec, database_vec).flatten()

    # Get the indices of the most similar sentences
    most_similar_indices = cosine_similarities.argsort()[:-6:-1]

    return most_similar_indices