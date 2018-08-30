from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
import Graphs

class TwoComboSection(QDialog):
    def __init__(self,num,parent=None):
        super(TwoComboSection, self).__init__()
        self.parent=parent
        self.num=str(num)
        self.setGeometry(200, 100, 800, 500)
        newfont = QFont("Browallia New", 18, QFont.Bold)
        grid = QGridLayout()


        yearlbl = QLabel("Choose Any Year : ")
        yearlbl.setFont(newfont)
        medallbl = QLabel("Choose Medal : ")
        medallbl.setFont(newfont)

        btnshow = QPushButton("Show Graph")
        btnshow.setFont(newfont)

        dataoly = pd.read_csv("olympic_medalists.csv")

        if self.num=="1":
            self.setWindowTitle(" Country's Single Year Graphical Analysis Section!!! ")
            cntrylbl = QLabel("Choose Any Country : ")
            cntrylbl.setFont(newfont)
            self.cmbcntry = QComboBox()
            data = pd.read_csv("Country medals count.csv")
            data["Country"] = data["Country"].astype('str')
            countries = data["Country"].sort_values()
            self.cmbcntry.addItem("Choose Any Country")
            self.cmbcntry.addItems(countries)
            self.cmbcntry.setFont(newfont)
            btnshow.clicked.connect(self.sCntrywise)
            grid.addWidget(cntrylbl, 0, 0)
            grid.addWidget(self.cmbcntry, 0, 1, 1, 2)

        elif self.num=="2":
            self.setWindowTitle(" Gender's Single Year Graphical Analysis Section!!! ")
            gnderlbl = QLabel("Choose Any Gender : ")
            gnderlbl.setFont(newfont)
            self.cmbgnder = QComboBox()
            values = ["Men", "Women"]
            self.cmbgnder.addItem("Choose Any Gender")
            self.cmbgnder.addItems(values)
            self.cmbgnder.setFont(newfont)
            btnshow.clicked.connect(self.sGnderwise)
            grid.addWidget(gnderlbl, 0, 0)
            grid.addWidget(self.cmbgnder, 0, 1, 1, 2)
        else:
            self.setWindowTitle(" Sport's Single Year Graphical Analysis Section!!! ")
            sprtslbl = QLabel("Choose Any Sports : ")
            sprtslbl.setFont(newfont)
            self.cmbsprts = QComboBox()
            dataoly["Sport"] = dataoly["Sport"].astype('str')
            sports = dataoly["Sport"].unique()
            self.cmbsprts.addItem("Choose Any Sport")
            self.cmbsprts.addItems(sports)
            self.cmbsprts.setFont(newfont)
            btnshow.clicked.connect(self.sSprtswise)
            grid.addWidget(sprtslbl, 0, 0)
            grid.addWidget(self.cmbsprts, 0, 1, 1, 2)


        self.cmbyear = QComboBox()
        self.cmbmdl = QComboBox()
        self.cmbyear.addItem("Choose Any Year")

        dataoly["Edition"] = dataoly["Edition"].astype('str')
        years=dataoly["Edition"].unique()

        medal=["Choose Any Medal","Gold","Silver","Bronze","Total medals"]

        self.cmbyear.addItems(years)
        self.cmbmdl.addItems(medal)
        self.cmbyear.setFont(newfont)
        self.cmbmdl.setFont(newfont)

        grid.addWidget(yearlbl, 2, 0, 1, 3)
        grid.addWidget(self.cmbyear, 2, 1, 1, 3)
        grid.addWidget(medallbl, 4, 0, 1, 3)
        grid.addWidget(self.cmbmdl, 4, 1, 1, 3)
        grid.addWidget(btnshow, 5, 0, 1, 4)

        self.setLayout(grid)
        self.show()



    def sCntrywise(self):
        country = self.cmbcntry.currentText()
        year = self.cmbyear.currentText()
        medal=self.cmbmdl.currentText()
        if country=="Choose Any Country" or year=="Choose Any Year" or medal=="Choose Any Medal":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.showSCntryMGraph(self,country,year,medal)


    def sGnderwise(self):
        gender = self.cmbgnder.currentText()
        year = self.cmbyear.currentText()
        medal = self.cmbmdl.currentText()
        if gender=="Choose Any Gender" or year=="Choose Any Year" or medal=="Choose Any Medal":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.showSGndrMGraph(self,gender,year,medal)


    def sSprtswise(self):
        sport = self.cmbsprts.currentText()
        year = self.cmbyear.currentText()
        medal = self.cmbmdl.currentText()
        if sport=="Choose Any Sport" or year=="Choose Any Year" or medal=="Choose Any Medal":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.showSSprtMGraph(self,sport,year,medal)


class OneComboSection(QDialog):
    def __init__(self,num,parent=None):
        super(OneComboSection, self).__init__()
        self.parent = parent
        self.num = str(num)
        self.setGeometry(200, 100, 800, 500)
        newfont = QFont("Browallia New", 18, QFont.Bold)
        grid = QGridLayout()

        medallbl = QLabel("Choose Medal : ")
        medallbl.setFont(newfont)

        btnshow = QPushButton("Show Graph")
        btnshow.setFont(newfont)

        if self.num == "1":
            self.setWindowTitle(" Country's Yearwise Graphical Analysis Section!!! ")
            cntrylbl = QLabel("Choose Any Country : ")
            cntrylbl.setFont(newfont)
            self.cmbcntry = QComboBox()
            data = pd.read_csv("Country medals count.csv")
            data["Country"] = data["Country"].astype('str')
            countries = data["Country"].sort_values()
            self.cmbcntry.addItem("Choose Any Country")
            self.cmbcntry.addItems(countries)
            self.cmbcntry.setFont(newfont)
            btnshow.clicked.connect(self.mCntrywise)
            grid.addWidget(cntrylbl, 0, 0)
            grid.addWidget(self.cmbcntry, 0, 1, 1, 2)
        elif self.num == "2":
            self.setWindowTitle(" Gender's Yearwise Graphical Analysis Section!!! ")
            gnderlbl = QLabel("Choose Any Gender : ")
            gnderlbl.setFont(newfont)
            self.cmbgnder = QComboBox()
            values = ["Men", "Women"]
            self.cmbgnder.addItem("Choose Any Gender")
            self.cmbgnder.addItems(values)
            self.cmbgnder.setFont(newfont)
            btnshow.clicked.connect(self.mGnderwise)
            grid.addWidget(gnderlbl, 0, 0)
            grid.addWidget(self.cmbgnder, 0, 1, 1, 2)
        else:
            self.setWindowTitle(" Sport's Yearwise Graphical Analysis Section!!! ")
            sprtslbl = QLabel("Choose Any Sports : ")
            sprtslbl.setFont(newfont)
            self.cmbsprts = QComboBox()
            dataoly = pd.read_csv("olympic_medalists.csv")
            dataoly["Sport"] = dataoly["Sport"].astype('str')
            sports = dataoly["Sport"].unique()
            self.cmbsprts.addItem("Choose Any Sport")
            self.cmbsprts.addItems(sports)
            self.cmbsprts.setFont(newfont)
            btnshow.clicked.connect(self.mSprtswise)
            grid.addWidget(sprtslbl, 0, 0)
            grid.addWidget(self.cmbsprts, 0, 1, 1, 2)

        self.cmbmdl = QComboBox()

        medal = ["Choose Any Medal", "Gold", "Silver", "Bronze", "Total medals"]

        self.cmbmdl.addItems(medal)
        self.cmbmdl.setFont(newfont)

        grid.addWidget(medallbl, 2, 0, 1, 3)
        grid.addWidget(self.cmbmdl, 2, 1, 1, 3)
        grid.addWidget(btnshow, 3, 0, 1, 4)

        self.setLayout(grid)
        self.show()


    def mCntrywise(self):
        country = self.cmbcntry.currentText()
        medal=self.cmbmdl.currentText()
        if country=="Choose Any Country" or medal=="Choose Any Medal":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.showMCntryMGraph(self,country,medal)


    def mGnderwise(self):
        gender = self.cmbgnder.currentText()
        medal = self.cmbmdl.currentText()
        if gender=="Choose Any Gender" or medal=="Choose Any Medal":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.showMGndrMGraph(self,gender,medal)


    def mSprtswise(self):
        sport = self.cmbsprts.currentText()
        medal = self.cmbmdl.currentText()
        if sport=="Choose Any Sport" or medal=="Choose Any Medal":
            QMessageBox.warning(self, 'Message from OLYSIS', "Please select any value from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.showMSprtMGraph(self,sport,medal)

