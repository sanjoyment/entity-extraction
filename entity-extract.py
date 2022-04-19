# -*- coding: utf-8 -*-
import os
import spacy
import json
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
try:
    nlp = spacy.load("en_core_web_trf")
except:
    os.system("python3 -m spacy download en_core_web_trf")
    nlp = spacy.load("en_core_web_trf")

app = Flask(__name__)
api = Api(app)

class server_ping_api(Resource):
    def get(self):
        return jsonify(result=True,message='Server responding perfectly')
api.add_resource(server_ping_api, '/server_ping')

class extraction_service(Resource):
    def post(self):
        # request_data = request.data

        # if 'text' not in request.json:
        #     return jsonify(result=False,message='Account ID is required.')
        # if len(request.json['text'])==0:
        #     return jsonify(result=False,message='Account ID is required.')
        # if 'data' not in request.json:
        #     return jsonify(result=False,message='Atleast a bunch of question and answer is required.')
        # if len(request.json['data'])==0:
        #     return jsonify(result=False,message='Atleast a bunch of question and answer is required.')
        #
        # if 'entity' in request.json and request.json['entity'] in ['name']:
        #     #source = '_' + request.json['source']           #for old db
        #     source = request.json['source']+'_'            #for new db
        doc = None
        person_name = dict()
        sentence = str(request.json['text'])
        entity = str(request.json['entity'])

        try:
            if sentence:
                if entity:
                    if entity == "name":
                        words = sentence.split(" ")
                        if len(words) > 1:
                            doc = nlp(sentence)
                            if doc.ents:
                                for ent in doc.ents:
                                    if ent.label_ == "PERSON":
                                        person_name.update({"name": ent.text})
                                        break
                            response = person_name
                        else:
                            response = sentence
                        status = True
                    else:
                        response = "Only name is supported for now!"
                        status = False
                else:
                    response = "Please add entity to proceed"
                    status = False
            else:
                response = "Please send text to be extracted"
                status = False
            return jsonify(status=200,response={"data": response, "status": status})
        except Exception as e:
                return jsonify(status=200,response={"data": str(e), "status": False})
api.add_resource(extraction_service, '/extract')

if __name__ == '__main__':
    # app.run('147.135.37.191',9978)
    app.run('0.0.0.0',8000)

