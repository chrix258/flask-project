import sqlite3
def recuperer_personnes():
    connexion = sqlite3.connect("Bdd/puces_data.db")
    curseur = connexion.cursor()
    requete_sql = """SELECT * FROM t_puces WHERE id = 1;"""
    resultat = curseur.execute(requete_sql)
    personnes = resultat.fetchall()
    connexion.close()
    return personnes
print(recuperer_personnes())
