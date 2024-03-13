# Troph-e-NSI



Architecture : 

- base de donnes sql

    - liste de comptes

    - liste de demande

- wepbpage

    - account creation
        add a new entry to account database
        - une page web
        - ajout d'un utilisatuer a la base de donnee
        - 2eme page web
        - permet de se connecter as un compte existant (ajoute des cookies afin qu'il reste connecter sur tout les pages.)

    - gestion de compte
        allow to modify and delete account + request made by that account
        - une page de modificatione de compte
        - un moyen d'obtenir les informations sur un compte


    - recuperqtion des match + creqtion de recherche
        post a request and look in the database for compatible request
        - une page web de recherche
        cette page ajoute une nouvelle ligne a la base de donnes
        et elle renvoie la liste de personnes disponible

        - prend en entree des criteres : Sport , heure , lieux , niveau , compte (token)

        - envoi les infos a la base de donne : Sport , heure , lieux , niveau , compte (token)

        - renvoi une liste de match : chaque match contiens : Sport , heure , lieux , niveau , compte (token)
    - render matches

        render the list of compatible request

        - prend en entree une liste de compte/crenaux de sport et renvoi une page web pour selectionner les crenaux que l'ont veut : Sport , heure , lieux , niveau , compte (token)

        - renvoi une page web qui contien tous les resultats
    - accept match
        allow to select a request and accept it
        - prend en entree une liste de crenaux choisis. 
        - envoie une notification aux participants comme quoi aan est interresse et les met en contact.


# Trophée NSI

Sporteec est une web app permettant de trouver des partenaires pour pratiquer vos sports favoris. Il suffit simplement de vous inscrire, sélectionner votre/vos sports puis votre niveau et notre site vous trouvera automatiquement un ou plusieurs aprtenaires adaptés à vos critères. 


# participant

Romain
Alexis
Maxime
MAD
Charles botteau
Hugo
Rayan
Thomas
Clement
Julien

mettez vos noms a cote de la partie de la web page sur laquelle vous voulez bosser essayer d'etre equilibré

+dites si vous etes OK avec l'architecture aue j'ai presente.
 et si vous avez des ameliorations a proposer


