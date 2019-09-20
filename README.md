# Demo integration intouch



## Comment ça marche

* L'utilisateur de l'api intouch initie une transaction (voir le fichier test_transaction.py)
* Intouch valide la transaction et appel la fonction de retour de l'utilisateur (voir api.py)
* toute la doc (voir FONCTIONNEMENT TOUCHPAYAPI.pdf)

## Comment reproduire ?

* cloner le dépôt

```bash
$ git clone 
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

```bash
$ python test_transaction.py
```

