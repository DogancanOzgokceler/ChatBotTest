import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.load(open('intents.json').read())

words = picle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('chatbot model.model')

def clean_up_sentence(sentence):
  sentence_words = nltk.word.teokenize(sentence)
  sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
  return sentence_words
def bag_of_words(sentence):
  sentence_words = clean_up_sentence(sentence)
  bag = [0] * len(words)
  for w in sentence words:
    for i, word in enumerate(words):
      if word == w:
        bag[i] = 1
    return np.array(bag)

def pretict_class(sentence):
  bow = bag_of_words(sentence)
  res = model.predict(np.array([bow]))[0]
  ERROR_THERESHOLD = 0.25
  result = [[i,r]for i, r in enumerate(res) if r > ERROR_THERESHOLD]
  result.sort(key=lambda x: x[1], reverse=True)
  rerurn_list = []
  for r in results:
    return_list.append({'intent': classes[r[0]],'probability': str(r[1])})
  return return_list

def get_response(intents_list, intents_json):
  tag = intents_list[0]['intent']
  list_of_intents = intents_json['intents']
  for i in list_of_intents:
    if i['tag'] == tag:
      result = random.choice(i['responses'])
      break
  return result

print("All System READY")
print("This System Made By Doğancan Özgökçeler")

while True:
  message = input("")
  ints = pretict_class(message)
  res = get_response(int, intents)
  print(res)