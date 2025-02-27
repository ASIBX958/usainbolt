from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète'  # Important pour les sessions

# Exemple de données de produits (à remplacer par une base de données)
produits = [
    {'id': 1, 'nom': 'Photocopieuse Canon', 'description': ' Photocopieuse Canon ', 'prix': ("1 149 900"),'image': 'img/photocopieuse-canon-ir-2425i-complet-garantie-12-mois.jpg'},
    {'id': 2, 'nom': 'Nasco Congelateur Horizontal', 'description': 'Nasco Congelateur Horizontal', 'prix': ("239 900"),'image':"img/nasco-congelateur-horizontal-knas-400-hnas-400-gris-290-litres-garantie-12-mois-accueil.jpg"},
    {'id': 3, 'nom': 'HP Intel Core i5', 'description': 'HP Intel Core i5', 'prix': ('549 900'),'image':"img/hp-all-in-one-200-g4-215-intel-core-i5-10210u-4gb-ram-1tb-dd-garantie-12-mois-accueil.jpg"},
    {'id': 4, 'nom': 'Bill Counter Compteuse De Billets', 'description': 'Bill Counter Compteuse De Billets', 'prix':  ('499 000'),'image':"img/bill-counter-compteuse-de-billets-valorisatrice-avec-systeme-de-detection-de-faux-billets-garantie-12mois-accueil.jpg"},
    {'id': 5, 'nom': 'Hisense Barre De Son', 'description': 'Hisense Barre De Son', 'prix': ('169 900'),'image':"img/hisense-barre-de-son-340w-sans-fil-dolby-atmos-garantie-12-mois.jpg"},
    {'id': 6, 'nom': 'Canon Imprimante Multifonction', 'description': 'Canon Imprimante Multifonction', 'prix': ('269 900'),'image':"img/canon-imprimante-multifonction-laser-couleur-3-en-1-i-sensys-mf655cdw-garantie-06-mois-accueil.jpg"},
    {'id': 7, 'nom': 'Nasco Refrigerateur', 'description': 'Nasco Refrigerateur', 'prix': ('169 900'),'image':"img/hp-envy-14-2-en-1-tactile-amd-ryzen-7-16gb-ram-1tb-ssd-gris-garantie-06-mois.jpg"},
    {'id': 8, 'nom': 'HP Ecran Tactile', 'description': 'HP Ecran Tactile', 'prix': ('599 900'),'image':"img/nasco-refrigerateur-combine-309-litres-distributeur-deau-hnasd2-40wd-garantie-12-mois-accueil.jpg"},
    {'id': 9, 'nom': 'Midea Machine A Laver', 'description': 'Midea Machine A Laver', 'prix': ('249 900'),'image':"img/midea-machine-a-laver-8-kg-inverter-quatro-ouverture-frontale-garantie-12-mois.jpg"},
    {'id': 10, 'nom': 'Samsung Split', 'description': 'Samsung Split', 'prix': ('239 900'),'image':"img/samsung-split-15cv-digital-inverter-r410-garantie-12-mois-accueil.jpg"},
    {'id': 11, 'nom': ' Hisense Ultra HD', 'description': 'Hisense Ultra HD', 'prix': ('1 299 900'),'image':"img/hisense-50-tv-ultra-hd-4k-ecran-sans-bord-serie-a6kmodele-2024-wifi-bluetooth-assistant-vocal-garantie-12-mois-accueil.jpg"},
    {'id': 12, 'nom': ' HP Notebook Tactile Intel Core i3', 'description': 'HP Notebook Tactile Intel Core i3', 'prix': ('359 900'),'image':"img/hp-notebook-156-fhd-tactile-intel-core-i3-8go-ram-512-go-ssd-gris-garantie-06-mois(2).jpg"}


    
    # ... autres produits ...
]

@app.context_processor
def inject_now():
    return {'annee_actuelle': datetime.now().year}

@app.route('/')
def page1():
    return render_template('index.html', produits=produits)

# @app.route('/produit/<int:produit_id>')
# def produit_details(produit_id):
#     if 'utilisateur' not in session:
#         session['produit_selectionne'] = produit_id
#         return redirect(url_for('enregistrement'))
#     produit = next((p for p in produits if p['id'] == produit_id), None)
#     return render_template('details.html', produit=produit)

# @app.route('/enregistrement', methods=['GET', 'POST'])
# def enregistrement():
#     if request.method == 'POST':
#         session['utilisateur'] = request.form['nom']
#         session['email'] = request.form['email']
#         produit_id = session.pop('produit_selectionne', None)
#         print(f"Utilisateur: {session['utilisateur']}, Email: {session['email']}, Produit ID: {produit_id}") #Ajouter une instruction print
#         return redirect(url_for('produit_details', produit_id=produit_id))
#     return render_template('enregistrement.html')

@app.route('/produit/<int:produit_id>')
def produit_details(produit_id):
    if 'utilisateur' not in session:
        session['produit_selectionne'] = produit_id
        return redirect(url_for('enregistrement'))
    produit = next((p for p in produits if p['id'] == produit_id), None)
    return render_template('details.html', produit=produit)

@app.route('/enregistrement', methods=['GET', 'POST'])
def enregistrement():
    if request.method == 'POST':
        # Traiter l'enregistrement (stocker les données utilisateur et l'email)
        session['utilisateur'] = request.form['nom']
        session['email'] = request.form['email']
        produit_id = session.pop('produit_selectionne', None)
        return redirect(url_for('produit_details', produit_id=produit_id))
    return render_template('enregistrement.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')