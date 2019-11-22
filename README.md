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