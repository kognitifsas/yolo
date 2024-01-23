import os
import sqlite3

class GestionnaireBaseDeDonnees:
    def __init__(self, chemin_base_de_donnees='sqlite.db'):
        self.chemin_base_de_donnees = chemin_base_de_donnees
        self.connexion = None
        self.curseur = None

    def ouvrir_connexion(self):
        self.connexion = sqlite3.connect(self.chemin_base_de_donnees)
        self.curseur = self.connexion.cursor()
    def creer_table_state(self):
        self.curseur.execute('''
            CREATE TABLE IF NOT EXISTS state (
                id INTEGER PRIMARY KEY,
                active INTEGER DEFAULT 0
            )
        ''')
    def inserer_state(self, state=0):
        self.curseur.execute('INSERT INTO state (active) VALUES (?)', (state,))
    
    def update_state(self, state):
        self.curseur.execute('UPDATE state SET active = ? WHERE id = 1', (state,))
    def get_state(self):
        self.curseur.execute('SELECT active FROM state WHERE id = 1')
        return self.curseur.fetchone()[0]
    def fermer_connexion(self):
        if self.connexion:
            self.connexion.commit()
            self.connexion.close()

def init_db():
    chemin_personnalise = 'sqlite.db'
    gestionnaire_bd = GestionnaireBaseDeDonnees(chemin_base_de_donnees=chemin_personnalise)
    gestionnaire_bd.ouvrir_connexion()
    gestionnaire_bd.creer_table_state()
    gestionnaire_bd.update_state(0)
    gestionnaire_bd.fermer_connexion()



if __name__ == "__main__":
    init_db();