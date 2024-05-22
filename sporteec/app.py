from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
from flask_mail import Mail, Message
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Clé secrète pour la session

# Configurer Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.hostinger.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'activation@sporteec.com'
app.config['MAIL_PASSWORD'] = 'Activation1!'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Chemin du fichier JSON des annonces
annonces_json_path = "annonces.json"

# Vérifie si le fichier JSON des annonces existe, sinon le crée avec une liste vide
if not os.path.exists(annonces_json_path):
    with open(annonces_json_path, 'w') as f:
        json.dump([], f)

# Obtenez le chemin absolu du répertoire du script Flask
script_directory = os.path.dirname(os.path.abspath(__file__))

# Chemin du fichier JSON des utilisateurs
users_json_path = os.path.join(script_directory, 'users.json')

# Vérifie si le fichier JSON existe, sinon le crée avec une liste vide
if not os.path.exists(users_json_path):
    with open(users_json_path, 'w') as f:
        json.dump([], f)

# Route pour la page d'accueil
@app.route('/')
def index():
    check_remember_me()
    if 'email' in session:
        return redirect(url_for('reussi'))
    # Vérifier si le compte associé à 'remember_me' existe toujours dans la base de données
    if request.cookies.get('remember_me'):
        email = request.cookies.get('remember_me')
        with open(users_json_path, 'r') as f:
            try:
                users = json.load(f)
            except json.decoder.JSONDecodeError:
                users = []

        for user in users:
            if user['email'] == email:
                # Si le compte existe toujours, rediriger vers la page principale
                return redirect(url_for('reussi'))

        # Si le compte associé au cookie 'remember_me' n'existe plus, supprimer le cookie et rediriger vers index.html
        response = make_response(redirect(url_for('index')))
        response.delete_cookie('remember_me')
        flash('Votre compte a été supprimé.', 'info')
        return response

    return render_template('index.html')

@app.route('/inscription')
def inscription():
    inscription_erreur = session.pop('inscription_erreur', None)
    return render_template('inscription.html', inscription_erreur=inscription_erreur)

# Route pour le traitement du formulaire d'inscription
@app.route('/register', methods=['POST'])
def register():
    # Récupère les données du formulaire
    nom = request.form['nom']
    email = request.form['email']
    mot_de_passe = request.form['mot_de_passe']
    sexe = request.form['sexe']

    # Vérifier si tous les champs sont remplis
    if not (nom and email and mot_de_passe and sexe):
        flash('Tous les champs sont requis', 'error')
        session['inscription_erreur'] = 'Tous les champs sont requis'
        return redirect(url_for('inscription'))

    # Vérifier si l'e-mail est déjà utilisé
    if email_exists(email):
        flash('Cet e-mail est déjà utilisé. Veuillez en choisir un autre.', 'error')
        session['inscription_erreur'] = 'Cet e-mail est déjà utilisé. Veuillez en choisir un autre.'
        return redirect(url_for('inscription'))
    
    # Hasher le mot de passe
    mot_de_passe_hache = generate_password_hash(mot_de_passe)

    # Enregistrer l'utilisateur avec le mot de passe haché
    save_user(nom, email, mot_de_passe_hache, sexe)

    # Envoyer un e-mail d'activation
    send_activation_email(nom, email, mot_de_passe, sexe)

    flash('Un e-mail d\'activation a été envoyé à votre adresse.', 'info')
    return redirect(url_for('message'))  # Rediriger vers la nouvelle page message.html


# Route pour afficher la page de message après l'inscription
@app.route('/message')
def message():
    return render_template('message.html')

# Route pour le traitement du formulaire de connexion
@app.route('/connexion', methods=['POST'])
def connexion():
    # Récupère les données du formulaire
    email = request.form['email']
    mot_de_passe = request.form['mot_de_passe']
    remember_me = 'remember_me' in request.form

    # Charge les utilisateurs existants depuis le fichier JSON
    with open(users_json_path, 'r') as f:
        try:
            users = json.load(f)
        except json.decoder.JSONDecodeError:
            users = []

    # Vérifie si l'adresse email et le mot de passe sont corrects
    for user in users:
        if user['email'] == email and check_password_hash(user['mot_de_passe'], mot_de_passe):
            session['nom'] = user['nom']
            session['email'] = user['email']
            session['sexe'] = user['sexe']
            flash('Vous êtes connecté avec succès!', 'success')
            response = make_response(redirect(url_for('reussi')))
            if remember_me:
                response.set_cookie('remember_me', email, max_age=30*24*60*60)  # 30 jours
            return response

    flash('Adresse email ou mot de passe incorrect. Veuillez réessayer.', 'error')
    session['connexion_erreur'] = True
    return redirect(url_for('inscription'))

@app.route('/reussi')
def reussi():
    check_remember_me()
    if 'email' not in session:
        flash('Vous devez être connecté pour accéder à cette page.', 'error')
        return redirect(url_for('index'))

    # Vérifier si le compte associé à la session existe toujours dans la base de données
    with open(users_json_path, 'r') as f:
        try:
            users = json.load(f)
        except json.decoder.JSONDecodeError:
            users = []

    for user in users:
        if user['email'] == session.get('email'):
            # Si le compte existe toujours, charger les annonces et afficher la page principale
            with open(annonces_json_path, 'r') as f:
                annonces = json.load(f)
            return render_template('page-principale.html', annonces=annonces)

    # Si le compte n'existe plus, supprimer les informations de session et rediriger vers la page d'accueil
    session.clear()
    flash('Votre compte a été supprimé.', 'info')
    return redirect(url_for('index'))


@app.route('/deconnexion')
def deconnexion():
    session.clear()
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('remember_me')
    flash('Vous êtes déconnecté.', 'info')
    return response

def send_activation_email(nom, email, mot_de_passe, sexe):
    try:
        activation_link = url_for('activate_account', email=email, nom=nom, mot_de_passe=mot_de_passe, sexe=sexe, _external=True)
        msg = Message('Activation de compte',
                      sender='activation@sporteec.com',
                      recipients=[email])
        msg.html = f"Cliquez sur le lien suivant pour activer votre compte : <a href='{activation_link}'>{activation_link}</a>"
        mail.send(msg)
    except Exception as e:
        flash("Erreur lors de l'envoi de l'e-mail : " + str(e), 'error')

@app.route('/deposer')
def deposer():
    check_remember_me()
    if 'email' not in session:
        flash('Vous devez être connecté pour déposer une annonce.', 'error')
        return redirect(url_for('index'))
    return render_template('deposer.html')

def save_annonce(titre, description, date, heure, sport, niveau, lieu, email, nom_utilisateur):
    with open(annonces_json_path, 'r') as f:
        annonces = json.load(f)
    
    nouvelle_annonce = {
        'titre': titre,
        'description': description,
        'date': date,
        'heure': heure,
        'sport': sport,
        'niveau': niveau,
        'lieu': lieu,
        'email_utilisateur': email,
        'nom_utilisateur': nom_utilisateur
    }
    annonces.append(nouvelle_annonce)
    
    with open(annonces_json_path, 'w') as f:
        json.dump(annonces, f, indent=4)

@app.route('/creer_annonce', methods=['POST'])
def creer_annonce():
    titre = request.form['titre']
    description = request.form['description']
    date = request.form['date']
    heure = request.form['heure']
    sport = request.form['sport']
    niveau = request.form['niveau']
    lieu = request.form['lieu']
    nom_utilisateur = session.get('nom')

    if 'email' not in session:
        flash('Vous devez être connecté pour créer une annonce.', 'error')
        return redirect(url_for('index'))

    save_annonce(titre, description, date, heure, sport, niveau, lieu, session['email'], nom_utilisateur)

    flash('Annonce créée avec succès!', 'success')
    return redirect(url_for('reussi'))

def save_user(nom, email, mot_de_passe, sexe):
    with open(users_json_path, 'r') as f:
        users = json.load(f)
    
    # Hasher le mot de passe
    mot_de_passe_hache = generate_password_hash(mot_de_passe)
    
    new_user = {'nom': nom, 'email': email, 'mot_de_passe': mot_de_passe_hache, 'sexe': sexe}
    users.append(new_user)
    
    with open(users_json_path, 'w') as f:
        json.dump(users, f, indent=4)

# Fonction pour vérifier si un e-mail existe déjà dans le fichier JSON des utilisateurs
def email_exists(email):
    with open(users_json_path, 'r') as f:
        users = json.load(f)
    
    for user in users:
        if user['email'].lower() == email.lower():  # Comparaison insensible à la casse des emails
            return True
    return False

@app.route('/activate')
def activate_account():
    email = request.args.get('email')
    if email:
        nom = request.args.get('nom')
        mot_de_passe = request.args.get('mot_de_passe')
        sexe = request.args.get('sexe')

        save_user(nom, email, mot_de_passe, sexe)
        flash('Votre compte a été activé avec succès.', 'success')
        return render_template('account_activated.html')
    else:
        flash('Erreur: Impossible de trouver l\'e-mail de l\'utilisateur.', 'error')
        return redirect(url_for('index'))
    
def check_remember_me():
    if 'email' not in session and request.cookies.get('remember_me'):
        email = request.cookies.get('remember_me')
        with open(users_json_path, 'r') as f:
            try:
                users = json.load(f)
            except json.decoder.JSONDecodeError:
                users = []

        user_found = False
        for user in users:
            if user['email'] == email:
                session['nom'] = user['nom']
                session['email'] = user['email']
                session['sexe'] = user['sexe']
                user_found = True
                break

        if not user_found:
            # Supprimer le cookie 'remember_me' s'il n'y a pas de correspondance dans la base de données
            response = make_response(redirect(url_for('index')))
            response.delete_cookie('remember_me')
            flash('Votre compte a été supprimé.', 'info')
            return response


if __name__ == '__main__':
    app.run(debug=True)

