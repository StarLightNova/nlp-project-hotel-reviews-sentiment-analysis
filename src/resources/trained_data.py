import pickle
import json
import requests

db = open('../../db.json')

data = json.load(db)

input_x_train = data['training'][-1]['input_x_train']

# Load trained model
model = pickle.load(open('pre_trained.sav', 'rb'))
# result  = model
sentiment = model.predict([input_x_train])

text_sent = {'text' : input_x_train, 'sentiment' : sentiment}

requests.post('http://localhost:3000/sentiments', data=text_sent)
