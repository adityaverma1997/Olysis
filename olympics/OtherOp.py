from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
import NumericResults
import Graphs

class OtherOp(QDialog):
    def __init__(self,num,parent=None):
        super(OtherOp, self).__init__()
        self.num=str(num)
        self.parent = parent
        self.setGeometry(200, 100, 800, 500)
        grid = QGridLayout()
        result=""

        self.countries=list()
        self.sports = list()

        newfont = QFont("Browallia New", 18, QFont.Bold)

        medallbl = QLabel("Choose Medal : ")
        medallbl.setFont(newfont)
        self.cmbmdl = QComboBox()
        medal=["Choose Any Medal","Gold","Silver","Bronze","Total medals"]
        self.cmbmdl.addItems(medal)
        self.cmbmdl.setFont(newfont)

        self.btnadd = QPushButton("Add")
        self.btnadd.setFont(newfont)

        self.btnshow_medals = QPushButton("Show Medals")
        self.btnshow_medals.setFont(newfont)

        dataoly = pd.read_csv("olympic_medalists.csv")

        if self.num=="1":
            self.setWindowTitle(" View Multiple Countries Yearwise Medals ")
            result+="Please select any 4 countries from the combo box.\n"
            result+="Select any country and then click to add.\n"
            result+="Repeat this process 4 times to view comparison graph.\n"
            result+="(It is compulsory to select 4 countries only.)"
            cntrylbl = QLabel("Choose Any Country : ")
            cntrylbl.setFont(newfont)
            self.cmbcntry = QComboBox()
            data = pd.read_csv("Country medals count.csv")
            data["Country"] = data["Country"].astype('str')
            countries = data["Country"].sort_values()
            self.cmbcntry.addItem("Choose Any Country")
            self.cmbcntry.addItems(countries)
            self.cmbcntry.setFont(newfont)
            self.btnadd.clicked.connect(self.addCounts)
            self.btnshow_medals.setDisabled(True)
            self.btnshow_medals.clicked.connect(self.multiCount)
            grid.addWidget(cntrylbl, 2, 0)
            grid.addWidget(self.cmbcntry, 2, 1, 1, 2)
        else:
            self.setWindowTitle(" View Multiple Sports Yearwise Medals ")
            result += "Please select any 4 sports from the combo box.\n"
            result += "Select any sport and then click to add.\n"
            result += "Repeat this process 4 times to view comparison graph.\n"
            result += "(It is compulsory to select 4 sports only.)"
            sprtslbl = QLabel("Choose Any Sport : ")
            sprtslbl.setFont(newfont)
            self.cmbsprts = QComboBox()
            dataoly["Sport"] = dataoly["Sport"].astype('str')
            sports = dataoly["Sport"].unique()
            self.cmbsprts.addItem("Choose Any Sport")
            self.cmbsprts.addItems(sports)
            self.cmbsprts.setFont(newfont)
            self.btnadd.clicked.connect(self.addSports)
            self.btnshow_medals.setDisabled(True)
            self.btnshow_medals.clicked.connect(self.multiSport)
            grid.addWidget(sprtslbl, 2, 0)
            grid.addWidget(self.cmbsprts, 2, 1, 1, 2)

        grid.addWidget(medallbl, 0, 0, 1, 3)
        grid.addWidget(self.cmbmdl, 0, 1, 1, 3)
        grid.addWidget(self.btnadd, 3, 0, 1, 4)
        grid.addWidget(self.btnshow_medals, 4, 0, 1, 4)

        self.setLayout(grid)
        self.show()

        QMessageBox.information(self, 'Message from OLYSIS', result, QMessageBox.Ok)


    def addCounts(self):
        country = self.cmbcntry.currentText()
        self.medal=self.cmbmdl.currentText()
        if country == "Choose Any Country" or self.medal=="Choose Any Medal":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.",QMessageBox.Ok)
        else:
            if len(self.countries)<3:
                self.countries.append(country)
            else:
                self.countries.append(country)
                self.btnadd.setDisabled(True)
                self.btnshow_medals.setEnabled(True)



    def addSports(self):
        sport = self.cmbsprts.currentText()
        self.medal = self.cmbmdl.currentText()
        if sport == "Choose Any Sport" or self.medal=="Choose Any Medal":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.",
                                QMessageBox.Ok)
        else:
            if len(self.sports) < 3:
                self.sports.append(sport)
            else:
                self.sports.append(sport)
                self.btnadd.setDisabled(True)
                self.btnshow_medals.setEnabled(True)


    def multiCount(self):
        Graphs.otherCountGraph(self, self.countries,self.medal)

    def multiSport(self):
        Graphs.otherSportsGraph(self, self.sports,self.medal)