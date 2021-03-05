# Librairie(s) utilisée(s)
from flask import *
import sqlite3
from Bdd import *

def renvoie():
    '''
    Cette fonction renvoie les élements de la table sous forme de tuples
    '''
    # Ouverture de la connection à la base de donnée
    connexion = sqlite3.connect('weed.db')
    cursor = connexion.cursor()

    resultat = cursor.execute("""SELECT * FROM weed""")
    elements = resultat.fetchall()
    
    # Fermeture de la connection avec la base
    connexion.close()
    
    # Retourne la liste des éléménts
    return elements


def utiliser_table(table):
    '''
    Cette fonction va nous permettre d'enregistrer les commandes SQL
    '''
    
    # Ouverture de la connection à la base de donnée
    connexion = sqlite3.connect('weed.db')
    cursor = connexion.cursor()
    
    # Si elle se retrouve fausse, nous passons à une deuxième technique
    cursor.execute(""" INSERT INTO weed VALUES (?, ?, ?, ?, ?)""",
                   table);  
    
    connexion.commit()
    
    # Fermeture de la connection avec la base
    connexion.close()


# Création d'un objet application web Flask
app = Flask(__name__)

elements = renvoie()

@app.route("/")
def Formulaire():
    return render_template("formulaire.html")

@app.route("/site",methods=['POST'])
def bienvenue():
    nom_user = request.form["nom"]
    return render_template("index.html")

@app.route("/accueil")
def accueil():
    return render_template("accueil.html")

@app.route("/graines")
def graines():
    return render_template("graines.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/Bdd")
def tester_bdd():
    personnes = recuperer_personnes()

    return render_template("bdd.html",personnes=personnes)

# Pour generer la deuxieme page web dynamique
@app.route("/requete")


def requete():
    """ Affiche la requete """
    # On retourne le template
    return render_template("requete.html")

# Pour generer la troisième page web dynamique
@app.route("/base")

def base():
    """ Affiche la base """
    elements = renvoie()
    # On retourne le template
    return render_template("base.html", elements = elements)


    
@app.route("/requete", methods = ["POST"])
def requete2():
    ''' recupère les informations du client et les affecte des variable '''
    
    Id = request.form["id"]
    tarifs = request.form["tarifs"]
    varietes = request.form["varietes"]
    
    liste = [Id, tarifs, varietes]
    
    
    
    utiliser_table(liste)
    return base()
    
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 7000, debug=True)