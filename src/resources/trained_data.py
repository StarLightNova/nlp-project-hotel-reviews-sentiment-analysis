import pickle
import json
import requests
from flask import Flask, render_template, g, jsonify, request, redirect, url_for, session, flash
from gensim import corpora
import os

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

@app.route("/get_trained_data", methods=['GET', 'POST'])
def get_trained_data():
	input_x_train = request.get_json()['text']
	model_file = request.get_json()['model']

	print(f"Trained model: {model_file}")
	# Load trained model
	model = pickle.load(open(model_file, 'rb'))
	# result  = model
	sentiment = model.predict([input_x_train])

	text_sent = {'text' : input_x_train, 'sentiment' : sentiment.tolist()[0]}

	return text_sent


port = os.getenv('PORT', '5006')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port),debug=True)
    #serve(app, url_scheme='http', threads=4, port=int(port))
