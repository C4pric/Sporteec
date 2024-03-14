# Troph-e-NSI



Architecture : 

- base de donnes SQL

    - liste de comptes

    - liste de demande

- wepbpage

    - Account creation
        add a new entry to account database
        - une page Web
        - ajout d'un utilisateur à la base de donnee
        - 2ème page Web
        - permet de se connecter à un compte existant (ajoute des cookies afin que l'utilisateur reste connecté sur tout les pages.)

    - Gestion de compte
        allow to modify and delete account + request made by that account
        - une page de modificatione de compte
        - un moyen d'obtenir les informations sur un compte


    - Recuperation des match + creation de recherche
        post a request and look in the database for compatible request
        - une page Web de recherche
        Cette page ajoute une nouvelle ligne à la base de données
        et elle renvoie la liste des personnes disponibles

        - Prend en entrée des criteres : Sport, heure, lieux, niveau, compte (token)
        Sport, heure, lieux sont renseignés par l'utilisateur.
        Compte (token) est stocké dans les cookies
        Niveau est stocké dans la base de données des comptes, avec possibilité de récupérer les données grâce au token.

        - envoi les infos a la base de donnée : Sport, heure, lieux, niveau, compte (token)

        - renvoi une liste de match : chaque match contiens : Sport , heure , lieux , niveau, compte (token)
    - render matches

        render the list of compatible request

        - Prend en entrée une liste de compte/crénaux de sport et renvoie une page web pour sélectionner les crénaux que l'on veut : Sport, heure, lieux, niveau, compte (token)
        Cette liste est fournie par l'étape du dessus.

        - Renvoie une page Web qui contient tous les résultats
        Sur cette page, on peut choisir des crénaux et valider

    - Accept match
        Allow to select a request and accept it
        - Prend en entrée une liste de crénaux choisis. (de l'étape précedente)
        - Envoie une notification aux participants comme quoi une personne est intérressé et les mets en contact.


# Trophée NSI

Sporteec est une WebApp permettant de trouver des partenaires pour pratiquer vos sports favoris. Il suffit simplement de vous inscrire, sélectionner votre/vos sport(s) puis votre niveau dans ce sport et notre site vous trouvera automatiquement un ou plusieurs partenaires adaptés à vos critères. 


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


