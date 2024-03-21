# Troph-e-NSI



Architecture : 

- base de donnes SQL

    - liste de comptes

    - liste de demandes
 
    - liste des anonces

- wepbpage

    - Account creation
        add a new entry to account database
        - une page Web
        - ajout d'un utilisateur à la base de donnee (page utilisateur avec les informations disponibles)
        - 2ème page Web
        - permet de se connecter à un compte existant (ajouter des cookies afin que l'utilisateur reste connecté sur tout les pages.)

    - Gestion de compte
        allow to modify and delete account + request made by that account
        - une page de modification de compte
        - un moyen d'obtenir les informations sur un compte : la page web user_profile, qui permet de récolter les informations sur l'utilisateur, la moyenne des notes que les         autres utilisateurs lui ont mis et ses sports pratiquer et ses niveaux dans ceux-ci.
        - un moyenne des avis des gens quand à la personne dans chaque sport


    - Recuperation des match + creation de recherche
        post a request and look in the database for compatible request
        - une page Web de recherche
        Cette page ajoute une nouvelle ligne à la base de données
        et elle renvoie la liste des personnes disponibles

        - Prend en entrée des criteres : Sport, heure, lieux, niveau, compte (token) et Notations (moyenne des notes attribuées par les précédents partenaires)
        Sport, heure, lieux sont renseignés par l'utilisateur.
        Compte (token) est stocké dans les cookies, tandis que la base donnée sql renvoit les notations des autres utilisateurs quand à au posteur de l'anonce dans ce sport;
        Niveau est stocké dans la base de données des comptes, avec possibilité de récupérer les données grâce au token, il a été définit lui même au préalable par                     l'utilisateurs.

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
        - Prend en entrée une liste de crénaux choisis. (définis lors de l'étape précedente : un lieu, un jour, un niveau et un sport)
        - Envoie une notification aux participants comme quoi une personne est intérressé et les informent qu'ils peuvent entrer en contact;

# Trophée NSI

Sporteec est une WebApp permettant de trouver des partenaires pour pratiquer vos sports favoris. Il suffit simplement de vous inscrire, sélectionner votre/vos sport(s) puis votre niveau dans ce sport et notre site vous trouvera automatiquement un ou plusieurs partenaires adaptés à vos critères. Vous pouvez également poster des anonces, afin de trouver un partenaire pour pratiquer un sport, l'anonce contient votre niveau, le sport concerné, le lieu et l'heure, ainsi qu'une courte description de vos attentes pour cette rencontre sportive.

# Statut de projet

déjà finies :
- répartitions des tâches, rôles et équipes de travails
- définition du style graphique du site (aspect global) et du logo
- définition des différentes fonctionnalité du site
- définition de l'architecture du site

en cours :
- architecture du site et aspects global
- formatage de la base de donnée
- différente page et fonctionnalités du site

à faire :
- système d'avis et notations d'un utilisateurs dans un sport

# participant

Romain
Alexis
Maxime
Marc-Antoine
Charles Botteau
Hugo
Rayan
Thomas
Clement
Julien
Julie

mettez vos noms a cote de la partie de la web page sur laquelle vous voulez bosser essayer d'etre equilibré

+dites si vous etes OK avec l'architecture aue j'ai presente.
 et si vous avez des ameliorations a proposer


