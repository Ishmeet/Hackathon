# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:42:29 2019

@author: Ishmeet
"""

from flask import Flask, jsonify, abort, request, make_response
import pickle

app = Flask(__name__, static_url_path = "")

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found2(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/assignee', methods = ['POST'])
def predict_assignee():
    print("request.json:",request.json)
    if not request.json or not 'Summary' in request.json:
        abort(400)

    # Loading the saved model pickle
    HackPickle = 'HackPickle.pkl'
    Hack_Pickle_model_pkl = open(HackPickle, 'rb')
    model = pickle.load(Hack_Pickle_model_pkl)
    vectorizer = pickle.load(open("vector.pickel", "rb"))
    print ("Loaded model :: ", model)
    print ("Loaded vectorizer :: ", vectorizer)
    
    
    print("Summary: ", request.json['Summary'])
    print ("Description: ", request.json['Description'])
    
    #Predict
    vector_test = vectorizer.transform([request.json['Description']])
    print ("Here")
    predicted_assignee = model.predict(vector_test)
    print ("predicted_assignee: ", predicted_assignee)
    assignee = {
        'assignee': ''.join(map(str,predicted_assignee))
    }
    #''.join(map(str,predicted_assignee))
    #return jsonify( { 'assignee': assignee } ), 200
    return jsonify( assignee ), 200

if __name__ == '__main__':
    app.run(host="169.38.77.105",debug=False)
