# Labo 

- [X] Créer la base du projet
- [ ] Users (Profil) + Authentification (David)
- [ ] Comments + Rating (Amaury)
- [ ] Services (Claire)
  - [x] Liste des services
    - [x] Ajouter la recherche de services selon plusieurs paramètres
  - [x] Form du service
    - [ ] Gérer les erreurs du form
  - [x] Détail d'un service
    - [x] Permettre à un utilisateur de proposer le même service
  - [ ] Gérer les actions en fonction de l'authentification
  - [x] Check qu'on a injecté les services partout où c'est possible
- [ ] Prestations (Etienne)

model view controller service dto mapper


Install steps: 
1. Setup venv
`python -m venv ./venv` et `source venv/bin/activate`
2. Installer les requirements
`pip install -r requirements.txt`
3. Upgrade la db
`./sqlAlchemy.sh -u`
4. Run le serveur
`python runserver.py`

Rappel:
- snake_case
- Suivre le schema
- Pour migrer la db : `./sqlAlchemy.sh -m yyyymmdd_hhmm_functionality` et ensuite l'upgrade avec `./sqlAlchemy.sh -u`