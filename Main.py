from Design import*
from PyQt5.QtCore import QPropertyAnimation, QRect
import mysql.connector

class myWin(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.iu = Ui_MainWindow()
        self.iu.setupUi(self)
        self.iu.toolButton_31.clicked.connect(lambda:self.close())
        self.iu.pushButton_4.clicked.connect(self.oublier)
        self.iu.pushButton_8.clicked.connect(self.authentif)
        self.iu.toolButton_7.clicked.connect(self.interjoueur)
        self.iu.btnRetour.clicked.connect(self.retourjoueur)
        self.iu.toolButton_2.clicked.connect(self.interEntraineur)
        self.iu.btnRetour_2.clicked.connect(self.retourEntraineur)
        self.iu.toolButton_3.clicked.connect(self.interEquipe)
        self.iu.btnRetour_4.clicked.connect(self.retourEquipe)
        self.iu.toolButton_9.clicked.connect(self.interArbittre)
        self.iu.btnRetour_3.clicked.connect(self.retourArbittre)
        self.iu.toolButton_5.clicked.connect(self.interCompetition)
        self.iu.btnRetour_5.clicked.connect(self.retourCompetition)
        self.iu.toolButton_10.clicked.connect(self.interMatch)
        self.iu.btnRetour_7.clicked.connect(self.retourMatch)
        self.iu.toolButton_6.clicked.connect(self.interStat)
        self.iu.btnRetour_8.clicked.connect(self.retourStat)
        self.iu.toolButton_11.clicked.connect(self.interScore)
        self.iu.btnRetour_9.clicked.connect(self.retourScore)
        self.iu.btnConnect.clicked.connect(self.login)
        self.iu.btnAjout.clicked.connect(lambda:self.iu.AjoutJoueur.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.iu.btnAnnuleJoueur.clicked.connect(lambda:self.iu.AjoutJoueur.setGeometry(QtCore.QRect(0, 700, 1111, 611)))
        self.iu.btnModif.clicked.connect(lambda:self.iu.ModifJoueur.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.iu.btnAnnuleJoueur_2.clicked.connect(lambda:self.iu.ModifJoueur.setGeometry(QtCore.QRect(0, 700, 1111, 611)))
        self.iu.btnSupp.clicked.connect(lambda:self.iu.SupprimerJoueur.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.iu.btnSuppAnnuleJoueur.clicked.connect(lambda:self.iu.SupprimerJoueur.setGeometry(QtCore.QRect(0, 700, 1111, 611)))

        self.iu.btnAjoutEntre.clicked.connect(lambda:self.iu.AjoutEntrain.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.iu.btnAnnuleEntre.clicked.connect(lambda:self.iu.AjoutEntrain.setGeometry(QtCore.QRect(0, 700, 1111, 611)))
        self.iu.btnModifEntre.clicked.connect(lambda:self.iu.ModifEntrain.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.iu.btnModifAnnuleEntre.clicked.connect(lambda:self.iu.ModifEntrain.setGeometry(QtCore.QRect(0, 700, 1111, 611)))
        self.iu.btnSupp_2.clicked.connect(lambda:self.iu.SupprimerEntrain.setGeometry(QtCore.QRect(0, 0, 1111, 611)))
        self.iu.btnSuppAnnuleEntre.clicked.connect(lambda:self.iu.SupprimerEntrain.setGeometry(QtCore.QRect(0, 700, 1111, 611)))

    def acceuil(self):
        self.iu.animation = QPropertyAnimation(self.iu.Login, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(30, -650, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(30, 1100, 1041, 541))
        self.iu.anim.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.anim.start()

    def interjoueur(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Joueur, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(0, 0, 1101, 600))
        self.iu.anim.start()

    def retourjoueur(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Joueur, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(0, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.start()

    def interEntraineur(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Entreneur, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(0, 0, 1101, 600))
        self.iu.anim.start()
    def retourEntraineur(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Entreneur, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(0, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.start()

    def interArbittre(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Arbitre, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(0, 0, 1101, 600))
        self.iu.anim.start()
    def retourArbittre(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Arbitre, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(0, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.start()

    def interEquipe(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Equipe, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(0, 0, 1101, 600))
        self.iu.anim.start()
    def retourEquipe(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Equipe, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(0, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.start()

    def interCompetition(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Compition, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(0, 0, 1101, 600))
        self.iu.anim.start()

    def retourCompetition(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Compition, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(0, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.start()
    def interMatch(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Match, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(0, 0, 1101, 600))
        self.iu.anim.start()

    def retourMatch(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Match, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(0, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.start()

    def interStat(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Statistique, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(0, 0, 1101, 600))
        self.iu.anim.start()

    def retourStat(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Statistique, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(0, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.start()

    def interScore(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Sccore, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(0, 0, 1101, 600))
        self.iu.anim.start()

    def retourScore(self):
        self.iu.animation = QPropertyAnimation(self.iu.Acceuil, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(-1100, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.Sccore, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(0, 0, 1101, 600))
        self.iu.anim.setEndValue(QRect(1200, 0, 1101, 600))
        self.iu.anim.start()
    #---------------------------------------------------------
    def oublier(self):
        self.iu.animation = QPropertyAnimation(self.iu.Login, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(-1020, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.RecupMDP, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(1020, 30, 1041, 541))
        self.iu.anim.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.anim.start()


    def authentif(self):
        self.iu.animation = QPropertyAnimation(self.iu.Login, b"geometry")
        self.iu.animation.setDuration(300)
        self.iu.animation.setStartValue(QRect(-1020, 30, 1041, 541))
        self.iu.animation.setEndValue(QRect(30, 30, 1041, 541))
        self.iu.animation.start()
        self.iu.anim = QPropertyAnimation(self.iu.RecupMDP, b"geometry")
        self.iu.anim.setDuration(300)
        self.iu.anim.setStartValue(QRect(30, 30, 1041, 541))
        self.iu.anim.setEndValue(QRect(1020, 30, 1041, 541))

        self.iu.anim.start()
    def login(self):

        login = self.iu.login.text()
        password = self.iu.mdp.text()

        X = ("SELECT *  from admin where nomadmin = %s AND password= %s ")
        data = (login, password)
        myCursor.execute(X, data)
        result = myCursor.fetchall()

        if result:
            for i in result:
                self.acceuil()
                break

        else:
            print("error")
    def addPlayer(self):

        sql = "INSERT INTO  players (CIN, playerName , playerLastName ,) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        myCursor.execute(sql, val)

        mydb.commit()

        print(myCursor.rowcount, "record inserted.")



if __name__ == "__main__":
    import sys

    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="projectdb")
    myCursor = mydb.cursor(buffered=True)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myWin()
    MainWindow.show()
    sys.exit(app.exec_())
