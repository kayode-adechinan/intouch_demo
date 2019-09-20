import requests
from requests.auth import HTTPDigestAuth
import uuid

# Les donnéées à envoyer à intouch sont définies par le
# dictionnaire ci-dessous.

data = {
    "idFromClient": str(uuid.uuid4()),  # identifiant unique de la transaction
    "additionnalInfos": {
        "recipientEmail": "pathé@hubsocial.org",  # email de l'acheteur
        "recipientFirstName": "Samba",  # prenom de l'acheteur
        "recipientLastName": "SECK",  # nom de l'acheteur
        "destinataire": "781833456"  # phone de l'acheteur
    },
    "amount": 100,
    "callback":
        "https://f6b5b4da.ngrok.io/callback",  # url callback à adapter (voir api.py)
    "recipientNumber": "781833456",
    #"serviceCode": "PAIEMENTMARCHANDTIGO"
    #"serviceCode": "SNPAIEMENTMARCHAND_EMONEY"
    "serviceCode": "PAIEMENTMARCHANDOM"  # moyen de paiement
}

req = requests.put(
    'https://dev-api.gutouch.com/dist/api/touchpayapi/v1/CPZ0829/transaction?loginAgent=4456987&passwordAgent=0000',
    json=data,
    auth=HTTPDigestAuth('MTN', 'passer'))

print(req.status_code)
print(req.json())

# La réponse du serveur contiendra des données du genre
'''

{  
   "idFromClient":"fcaa72b2-76f2-4cbb-acfe-41e303efe6f2",
   "idFromGU":"1568999465693",
   "amount":100.0,
   "fees":1.5,
   "serviceCode":"PAIEMENTMARCHANDOM",
   "recipientNumber":"781833456",
   "dateTime":1568999465693,
   "status":"INITIATED"
}

'''