from flask import Flask, render_template, request, redirect, jsonify, url_for
import json
import os

app = Flask(__name__)

# Chemin du fichier JSON des utilisateurs
users_json_path = 'registration/users.json'

# Vérifie si le fichier JSON existe, sinon le crée avec une liste vide
if not os.path.exists(users_json_path):
    with open(users_json_path, 'w') as f:
        json.dump([], f)

# Route pour la page d'inscription
@app.route('/')
def index():
    return render_template('inscription_connection.html')
@app.route('/inscription')
def inscription():
    return render_template('inscription_connection.html')
# Route pour le traitement du formulaire d'inscription
@app.route('/register', methods=['POST'])
def register():
    # Récupère les données du formulaire
    nom = request.form['nom']
    email = request.form['email']
    mot_de_passe = request.form['mot_de_passe']
    sexe = request.form['sexe']  # Ajout de cette ligne pour récupérer le sexe

    # Charge les utilisateurs existants depuis le fichier JSON
    with open(users_json_path, 'r') as f:
        users = json.load(f)

    # Ajoute le nouvel utilisateur 
    new_user = {'nom': nom, 'email': email, 'mot_de_passe': mot_de_passe, 'sexe': sexe}
    users.append(new_user)

    # Enregistre les utilisateurs mis à jour dans le fichier JSON
    with open(users_json_path, 'w') as f:
        json.dump(users, f, indent=4)

    # Redirige vers la page réussie après l'inscription
    return redirect(url_for('inscription'))

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
    return render_template('inscription_connection.html', erreur='Adresse email ou mot de passe incorrect')

# Route pour la page réussie
@app.route('/reussi')
def reussi():
    return render_template('reussi.html')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
