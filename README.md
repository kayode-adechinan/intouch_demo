# Demo integration intouch



## Comment ça marche

* L'utilisateur de l'api intouch initie une transaction (voir le fichier test_transaction.py)
* Intouch valide la transaction et appel la fonction de retour de l'utilisateur (voir api.py)
* toute la doc (voir FONCTIONNEMENT TOUCHPAYAPI.pdf)

## Comment reproduire ?

* cloner le dépôt

```bash
$ git clone git@github.com:kayode-adechinan/intouch_demo.git
```

* installer les dépendances

```bash
$ pip install -r requirements.txt
```

ou

```bash
$ pip install flask requests
```

## Comment lancer une transaction

* lancer le serveur dans un terminal

```bash
$ python api.py
```

* lancer ngrok pour un test en local

```bash
$ ngrok http 5000
```

* Remplacer l'url générer dans le fichier test_transaction.py

* lancer la transaction dans un autre terminal

```bash
$ python test_transaction.py
```

## Comment utiliser l'api

* Créer une commande
```bash
/orders/
```

* Spécifier un callback
```bash
/transactions/
```

## Mode de paiement

* PAIEMENTMARCHANDTIGO -> Tigo
* SNPAIEMENTMARCHAND_EMONEY -> Expresso 
* PAIEMENTMARCHANDOM -> Orange

## Exemple de jeu de données pour passer une commande

```bash
{
    "amount": 100,
    "callback":
        "https://1239d192.ngrok.io/transactions",  
    "recipientNumber": "781833456",
    "serviceCode": "PAIEMENTMARCHANDOM"  
}
```

## Retour de intouch

```bash
{
    "details": {
        "amount": 100.0,
        "dateTime": 1574436022464,
        "fees": 1.5,
        "idFromClient": "e993da62-384b-4ba5-ba8f-294d9e77b421",
        "idFromGU": "1574436022464",
        "recipientNumber": "781833456",
        "serviceCode": "PAIEMENTMARCHANDOM",
        "status": "INITIATED"
    }
}
```