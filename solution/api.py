

import pymongo
import pandas
import json
import re
import os
from flask import Flask
import more_itertools
from flask_cors import CORS, cross_origin
from flask.json import JSONEncoder
from bson.objectid import ObjectId
from flask import jsonify
from flask import Flask, request, make_response
from itertools import chain
from collections import Counter
from solution_start import *
import requests


cwd = os.getcwd()
cwd_need = cwd.split("solution")[0]


transaction_path = cwd_need + 'input_data/starter/transactions'
customer_path = cwd_need + 'input_data/starter/customers.csv'
product_path = cwd_need + 'input_data/starter/products.csv'



x = customer_product_data(transaction_path,customer_path,product_path)




client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client["customer_product_data"]  # Database Name
col = db["customer_data"]    # Collection Name


app = Flask(__name__)


@app.route('/hc', methods=['GET'])
@cross_origin(supports_credentials=True)
def hc():
    try:
        resp = jsonify({"success": True, 'message': 'Hello World!'})
        return resp
    except Exception as e:
        print(e)
        resp = {"success": False,  'message': 'Some error occurred!'}
        return resp



@app.route('/customer_id',methods=['POST'])
@cross_origin(supports_credentials=True)

def fetchdata():
    try:
        _json=request.json
        customer_id=_json['customer_id']
        # print(customer_id)
        query = { "customer_id" : { "$eq" : customer_id } }
        data = db.customer_data.find(query)


        file_info = []
        for i in data:
            # print(i)
            file_info.append({"product_id":i.get("product_id")})

        # print(file_info)

        total_purches = len(file_info)

        obj_value = []
        for i in file_info:
            obj_value.append(list(i.values())[0])


        counts = dict(Counter(obj_value))
        duplicates = {key:value for key, value in counts.items()}
        # print(duplicates)

        lst = []
        for i in duplicates:
            # print(i)
            product_category = x.product_category_by_product_id(i)
            lst.append({"product_id":i,"product_category":product_category,"number_of_purches":str(duplicates[i])})

        result = [{"customer_id":customer_id,"loyalty_score":str(x.loyalty_score_by_customer_id(customer_id)), "total_purches":str(total_purches),"purches_details":lst}]
        print(result)

        resp=jsonify({"success":True,"response":result})
        return resp
        
    except Exception as e:
        print("Exception:",e)
        resp=jsonify({"success":False,"message":"Invalid username or password"})
        return resp



if __name__ == '__main__':
	app.run(debug=True)
