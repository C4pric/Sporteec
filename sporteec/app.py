from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import json
import os

app = Flask(__name__)

# Configurer Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.hostinger.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'activation@sporteec.com'
app.config['MAIL_PASSWORD'] = 'Activation1!'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Obtenez le chemin absolu du répertoire du script Flask
script_directory = os.path.dirname(os.path.abspath(__file__))

# Chemin du fichier JSON des utilisateurs
users_json_path = os.path.join(script_directory, 'users.json')

# Vérifie si le fichier JSON existe, sinon le crée avec une liste vide
if not os.path.exists(users_json_path):
    with open(users_json_path, 'w') as f:
        json.dump([], f)

# Route pour la page d'inscription
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscription')
def inscription():
    return render_template('inscription.html')

# Route pour le traitement du formulaire d'inscription
@app.route('/register', methods=['POST'])
def register():
    # Récupère les données du formulaire
    nom = request.form['nom']
    email = request.form['email']
    mot_de_passe = request.form['mot_de_passe']
    sexe = request.form['sexe']  

    # Vérifie si tous les champs sont remplis
    if not (nom and email and mot_de_passe and sexe):
        return render_template('inscription.html', erreur='Tous les champs sont requis')

    # Continue avec le reste du traitement si tous les champs sont remplis

    # Vérifie si l'e-mail est déjà utilisé
    if email_exists(email):
        return render_template('inscription.html', erreur='Cet e-mail est déjà utilisé. Veuillez en choisir un autre.')

    # Continue avec le reste du traitement si l'e-mail n'est pas déjà utilisé

    # Envoyer un e-mail d'activation
    send_activation_email(nom, email, mot_de_passe, sexe)

    return render_template('message.html', message='Un e-mail d\'activation a été envoyé à votre adresse.')

# Route pour le traitement du formulaire de connexion
@app.route('/connexion', methods=['POST'])
def connexion():
    # Récupère les données du formulaire
    email = request.form['email']
    mot_de_passe = request.form['mot_de_passe']

    # Charge les utilisateurs existants depuis le fichier JSON
    with open(users_json_path, 'r') as f:
        try:
            users = json.load(f)
        except json.decoder.JSONDecodeError:
            users = []

    # Vérifie si l'adresse email existe dans la liste des utilisateurs
    for user in users:
        if user['email'] == email and user['mot_de_passe'] == mot_de_passe:
            # Vérifie si le mot de passe correspond
            if user['mot_de_passe'] == mot_de_passe:
                # Redirige vers la page réussie après la connexion
                return redirect(url_for('reussi'))

    # Si l'adresse email ou le mot de passe est incorrect
    return render_template('inscription.html', erreur='Adresse email ou mot de passe incorrect')

# Route pour la page réussie
@app.route('/reussi')
def reussi():
    return render_template('page-principale.html')

# Fonction pour envoyer un e-mail d'activation de compte
def send_activation_email(nom, email, mot_de_passe, sexe):
    try:
        activation_link = "http://127.0.0.1:5000/activate?email=" + email + "&nom=" + nom + "&mot_de_passe=" + mot_de_passe + "&sexe=" + sexe
        msg = Message('Activation de compte',
                      sender='activation@sporteec.com',
                      recipients=[email])
        msg.html = f"Cliquez sur le lien suivant pour activer votre compte : <a href='{activation_link}'>{activation_link}</a>"
        mail.send(msg)
    except Exception as e:
        print("Erreur lors de l'envoi de l'e-mail :", str(e))

@app.route('/deposer')
def deposer():
    return render_template('deposer.html')

# Ajoutez cette fonction pour enregistrer les utilisateurs dans le fichier JSON
def save_user(nom, email, mot_de_passe, sexe):
    # Charge les utilisateurs existants depuis le fichier JSON
    with open(users_json_path, 'r') as f:
        users = json.load(f)
    
    # Ajoute le nouvel utilisateur à la liste
    new_user = {'nom': nom, 'email': email, 'mot_de_passe': mot_de_passe, 'sexe': sexe}
    users.append(new_user)
    
    # Enregistre la liste mise à jour dans le fichier JSON
    with open(users_json_path, 'w') as f:
        json.dump(users, f, indent=4)  # Utilisez indent=4 pour une mise en forme lisible

# Ajoutez cette fonction pour vérifier si l'e-mail est déjà utilisé
def email_exists(email):
    # Charge les utilisateurs existants depuis le fichier JSON
    with open(users_json_path, 'r') as f:
        users = json.load(f)
    
    # Vérifie si l'e-mail existe déjà dans la liste des utilisateurs
    for user in users:
        if user['email'] == email:
            return True
    return False

# Route pour la page d'activation du compte
@app.route('/activate')
def activate_account():
    # Ici, vous pouvez activer le compte de l'utilisateur dans la base de données
    # Par exemple, vous pouvez marquer l'utilisateur comme activé

    # Récupère l'e-mail de l'utilisateur à partir du paramètre de la requête
    email = request.args.get('email')

    # Enregistre l'utilisateur seulement s'il a fourni un e-mail valide
    if email:
        # Obtenez d'autres informations de l'utilisateur à partir de la requête ou de la session
        nom = request.args.get('nom')
        mot_de_passe = request.args.get('mot_de_passe')
        sexe = request.args.get('sexe')

        # Enregistre l'utilisateur dans le fichier JSON
        save_user(nom, email, mot_de_passe, sexe)

        return render_template('account_activated.html')
    else:
        return "Erreur: Impossible de trouver l'e-mail de l'utilisateur."


if __name__ == '__main__':
    app.run(debug=True)


