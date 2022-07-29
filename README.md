# Labo 

- [X] Créer la base du projet
- [X] Users (Profil) + Authentification (David)
- [ ] Comments + Rating (Amaury)
- [x] Services (Claire)
- [ ] Prestations (Etienne)
- [ ] Page de blog (David)
- [x] Messages privés (Claire)
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