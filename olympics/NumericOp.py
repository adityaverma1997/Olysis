from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
import NumericResults
import Graphs

class NumericOp(QDialog):
    def __init__(self,num,parent=None):
        super(NumericOp, self).__init__()
        self.num=str(num)
        self.parent = parent
        self.setGeometry(200, 100, 800, 500)
        grid = QGridLayout()

        newfont = QFont("Browallia New", 18, QFont.Bold)


        yearlbl = QLabel("Choose Any Year : ")
        yearlbl.setFont(newfont)

        self.btnshow_medals = QPushButton("Show Medals")
        self.btnshow_medals.setFont(newfont)

        dataoly = pd.read_csv("olympic_medalists.csv")

        if self.num=="1":
            self.setWindowTitle(" View Countrywise Medals ")
            cntrylbl = QLabel("Choose Any Country : ")
            cntrylbl.setFont(newfont)
            self.cmbcntry = QComboBox()
            data = pd.read_csv("Country medals count.csv")
            data["Country"] = data["Country"].astype('str')
            countries = data["Country"].sort_values()
            self.cmbcntry.addItem("Choose Any Country")
            self.cmbcntry.addItems(countries)
            self.cmbcntry.setFont(newfont)
            self.btnshow_medals.clicked.connect(self.cntrywise)
            grid.addWidget(cntrylbl, 0, 0)
            grid.addWidget(self.cmbcntry, 0, 1, 1, 2)
        elif self.num=="2":
            self.setWindowTitle(" View Genderwise Medals ")
            gnderlbl = QLabel("Choose Any Gender : ")
            gnderlbl.setFont(newfont)
            self.cmbgnder = QComboBox()
            values = ["Men", "Women"]
            self.cmbgnder.addItem("Choose Any Gender")
            self.cmbgnder.addItems(values)
            self.cmbgnder.setFont(newfont)
            self.btnshow_medals.clicked.connect(self.gnderwise)
            grid.addWidget(gnderlbl, 0, 0)
            grid.addWidget(self.cmbgnder, 0, 1, 1, 2)
        else:
            self.setWindowTitle(" View Sportswise Medals ")
            sprtslbl = QLabel("Choose Any Sports : ")
            sprtslbl.setFont(newfont)
            self.cmbsprts = QComboBox()
            dataoly["Sport"] = dataoly["Sport"].astype('str')
            sports = dataoly["Sport"].unique()
            self.cmbsprts.addItem("Choose Any Sport")
            self.cmbsprts.addItems(sports)
            self.cmbsprts.setFont(newfont)
            self.btnshow_medals.clicked.connect(self.sprtswise)
            grid.addWidget(sprtslbl, 0, 0)
            grid.addWidget(self.cmbsprts, 0, 1, 1, 2)


        self.cmbyear = QComboBox()
        self.cmbyear.addItem("Choose Any Year")

        dataoly["Edition"] = dataoly["Edition"].astype('str')
        years=dataoly["Edition"].unique()

        self.cmbyear.addItems(years)
        self.cmbyear.setFont(newfont)

        grid.addWidget(yearlbl, 2, 0, 1, 3)
        grid.addWidget(self.cmbyear, 2, 1, 1, 3)
        grid.addWidget(self.btnshow_medals, 3, 0, 1, 4)

        self.setLayout(grid)
        self.show()


    def cntrywise(self):
        country = self.cmbcntry.currentText()
        year = self.cmbyear.currentText()
        if country=="Choose Any Country" or year=="Choose Any Year":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.", QMessageBox.Ok)
        else:
            result=NumericResults.showSCntryMGraph(self,country,year)
            QMessageBox.information(self, 'Message from OLYSIS', result, QMessageBox.Ok)


    def gnderwise(self):
        gender = self.cmbgnder.currentText()
        year = self.cmbyear.currentText()
        if gender=="Choose Any Gender" or year=="Choose Any Year":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.", QMessageBox.Ok)
        else:
            result = NumericResults.showSGndrMGraph(self, gender, year)
            QMessageBox.information(self, 'Message from OLYSIS', result, QMessageBox.Ok)


    def sprtswise(self):
        sport = self.cmbsprts.currentText()
        year = self.cmbyear.currentText()
        if sport=="Choose Any Sport" or year=="Choose Any Year":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.", QMessageBox.Ok)
        else:
            result = NumericResults.showSSprtMGraph(self, sport, year)
            QMessageBox.information(self, 'Message from OLYSIS', result , QMessageBox.Ok)