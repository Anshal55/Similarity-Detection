import requests

def throw_exception_if_not_string(query):
  """
  Throw an exception if the query is not a string.

  Args:
    query: The query to check.

  Raises:
    TypeError: If the query is not a string.
  """

  if not isinstance(query, str):
    raise TypeError("Query must be a string.")

URL = "https://us-central1-mercortask.cloudfunctions.net/find_similar"

query = str(input("Enter search query: "))

try:
  throw_exception_if_not_string(query)
except TypeError as e:
  print(e)

req_2 = requests.post(URL, json={"query": query})
print(req_2.text)