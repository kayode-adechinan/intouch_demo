from flask import Flask
from flask import jsonify
from flask import request
import requests
from requests.auth import HTTPDigestAuth
import uuid
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import MongoClient
from flask_cors import CORS


client = MongoClient('mongodb', 27017)
db = client['api-database']

orders_collection = db['orders']
transactions_collection = db['transactions']



app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'health': 'ok'})


@app.route('/orders', methods=['GET', 'POST'])
def orders():

    """
        {
        "amount": 100,
        "recipientNumber": "781833456",
        "serviceCode": "PAIEMENTMARCHANDOM"  
        }
    """

    if request.method == 'GET':
        #return jsonify({'orders': orders_collection.count_documents({})})
        #records_fetched = collection.find({key: value})
	    return dumps(orders_collection.find())
        

    data = request.json
    data["idFromClient"] =  str(uuid.uuid4())
    data["callback"] =  "https://1239d192.ngrok.io/transactions"

    req = requests.put(
        'https://dev-api.gutouch.com/dist/api/touchpayapi/v1/CPZ0829/transaction?loginAgent=4456987&passwordAgent=0000',
        json=data,
        auth=HTTPDigestAuth('MTN', 'passer'))

    orders_collection.insert_one(data)

    return jsonify({'details': req.json()})


# cet url sera appelé par intouch une fois la transaction
# achevée
@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    # les données retournées par intouch seront du genre:
    # Libre à vous de les manipuler comme il vous semble
    '''
        {  
        "service_id":"String",
        "gu_transaction_id":"String",
        "status":"String",
        "partner_transaction_id":"String",
        "call_back_url":"String",
        "commission":"Double"
        }
    '''

    if request.method == 'GET':
        partner_transaction_id = request.args.get("partner_transaction_id")
        record_fetched = transactions_collection.find_one({"partner_transaction_id": partner_transaction_id})
        return dumps(record_fetched)

    data = request.json

    transactions_collection.insert_one(data)

    return jsonify({'data': dumps(request.json)})


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')