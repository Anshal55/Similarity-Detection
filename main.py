import pandas as pd
import numpy as np
import json
from flask import escape
import functions_framework
from solutions.text_cleaning import preprocess_text, vectorizer_func, get_similar_data

@functions_framework.http
def find_similar(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'query' in request_json:
        query = request_json['query']
    elif request_args and 'query' in request_args:
        query = request_args['query']
    else:
        query = ''

    if query == "":
        return "Please enter a query."

    # laod the database and pre-process
    dataframe = pd.read_csv("fashion_data.csv")
    dataframe = dataframe.drop_duplicates(subset='text')
    database_sequences = dataframe["text"].map(preprocess_text)

    sentence_vectors, vectorizer = vectorizer_func(database_sequences.values.tolist(), fit=True)

    # input_text = str(input("Enter a search query: "))
    input_vector = vectorizer_func([preprocess_text(query)], vectorizer=vectorizer)

    data_out = dataframe[["link", "image_url"]]

    # Calculate cosine similarity
    matching_indices = get_similar_data(input_vector, sentence_vectors)

    out_results = data_out.iloc[matching_indices].to_dict(orient="records")
    
    # Convert the list to JSON string
    json_data = json.dumps(out_results, indent=4)

    return json_data

def test() -> None:
    # laod the database and pre-process
    dataframe = pd.read_csv("fashion_data.csv")
    dataframe = dataframe.drop_duplicates(subset='text')
    database_sequences = dataframe["text"].map(preprocess_text)

    
    sentence_vectors, vectorizer = vectorizer_func(database_sequences.values.tolist(), fit=True)

    input_text = str(input("Enter a search query: "))
    input_vector = vectorizer_func([preprocess_text(input_text)], vectorizer=vectorizer)

    data_out = dataframe[["link", "image_url"]]

    # Calculate cosine similarity
    matching_indices = get_similar_data(input_vector, sentence_vectors)

    out_results = data_out.iloc[matching_indices].to_dict(orient="records")
    # Convert the list to JSON string
    json_data = json.dumps(out_results, indent=4)
    print(json_data)


if __name__ == "__main__":
    test()