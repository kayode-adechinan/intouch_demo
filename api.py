from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

# cet url sera appelé par intouch une fois la transaction
# achevée


@app.route('/callback', methods=['POST'])
def callback():
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
    return jsonify({'data': request.json}), 201


if __name__ == '__main__':
    app.run(debug=True)