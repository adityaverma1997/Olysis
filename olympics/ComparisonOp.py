from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
import Graphs

class SingleYear(QDialog):
    def __init__(self,num,parent=None):
        super(SingleYear, self).__init__()
        self.parent=parent
        self.num=str(num)
        self.setGeometry(200, 100, 800, 500)
        newfont = QFont("Browallia New", 18, QFont.Bold)
        grid = QGridLayout()

        dataoly = pd.read_csv("olympic_medalists.csv")

        yearlbl = QLabel("Choose Any Year : ")
        yearlbl.setFont(newfont)
        self.cmbyear = QComboBox()

        dataoly["Edition"] = dataoly["Edition"].astype('str')
        years=dataoly["Edition"].unique()

        self.cmbyear.addItem("Choose Any Year")
        self.cmbyear.addItems(years)
        self.cmbyear.setFont(newfont)


        btnshow = QPushButton("Compare Graph")
        btnshow.setFont(newfont)

        if self.num=="1":
            self.setWindowTitle(" Single Year Country VS Country Comparison Analysis Section!!! ")
            cntrylbl1 = QLabel("Choose Any Country : ")
            cntrylbl1.setFont(newfont)
            self.cmbcntry1 = QComboBox()
            cntrylbl2 = QLabel("Choose Another Country : ")
            cntrylbl2.setFont(newfont)
            self.cmbcntry2 = QComboBox()
            data = pd.read_csv("Country medals count.csv")
            data["Country"] = data["Country"].astype('str')
            countries = data["Country"].sort_values()
            self.cmbcntry1.addItem("Choose Any Country")
            self.cmbcntry1.addItems(countries)
            self.cmbcntry1.setFont(newfont)
            self.cmbcntry2.addItem("Choose Any Country")
            self.cmbcntry2.addItems(countries)
            self.cmbcntry2.setFont(newfont)
            btnshow.clicked.connect(self.sCountry)
            grid.addWidget(cntrylbl1, 0, 0)
            grid.addWidget(self.cmbcntry1, 0, 1, 1, 2)
            grid.addWidget(cntrylbl2, 2, 0)
            grid.addWidget(self.cmbcntry2, 2, 1, 1, 2)
            grid.addWidget(yearlbl, 4, 0, 1, 3)
            grid.addWidget(self.cmbyear, 4, 1, 1, 3)
            grid.addWidget(btnshow, 5, 0, 1, 4)

        elif self.num=="2":
            self.setWindowTitle(" Single Year Men VS Women Compaison Analysis Section!!! ")
            btnshow.clicked.connect(self.sGender)
            grid.addWidget(yearlbl, 0, 0, 1, 2)
            grid.addWidget(self.cmbyear, 0, 3, 1, 2)
            grid.addWidget(btnshow, 1, 0, 1, 4)
        else:
            self.setWindowTitle(" Single Year Sport VS Sport Comparison Analysis Section!!! ")
            sprtslbl1 = QLabel("Choose Any Sports : ")
            sprtslbl1.setFont(newfont)
            self.cmbsprts1 = QComboBox()
            sprtslbl2 = QLabel("Choose Another Sports : ")
            sprtslbl2.setFont(newfont)
            self.cmbsprts2 = QComboBox()
            dataoly["Sport"] = dataoly["Sport"].astype('str')
            sports = dataoly["Sport"].unique()
            self.cmbsprts1.addItem("Choose Any Sport")
            self.cmbsprts1.addItems(sports)
            self.cmbsprts1.setFont(newfont)
            self.cmbsprts2.addItem("Choose Any Sport")
            self.cmbsprts2.addItems(sports)
            self.cmbsprts2.setFont(newfont)
            btnshow.clicked.connect(self.sSports)
            grid.addWidget(sprtslbl1, 0, 0)
            grid.addWidget(self.cmbsprts1, 0, 1, 1, 2)
            grid.addWidget(sprtslbl2, 2, 0)
            grid.addWidget(self.cmbsprts2, 2, 1, 1, 2)
            grid.addWidget(yearlbl, 4, 0, 1, 3)
            grid.addWidget(self.cmbyear, 4, 1, 1, 3)
            grid.addWidget(btnshow, 5, 0, 1, 4)

        self.setLayout(grid)
        self.show()



    def sCountry(self):
        country1 = self.cmbcntry1.currentText()
        country2 = self.cmbcntry2.currentText()
        year = self.cmbyear.currentText()
        if country1=="Choose Any Country" or country2=="Choose Any Country" or year=="Choose Any Year":
            QMessageBox.warning(self,"Message from OLYSIS","Please select any values from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.cmpSCntryGraph(self,country1,country2,year)


    def sGender(self):
        year = self.cmbyear.currentText()
        if year=="Choose Any Year":
            QMessageBox.warning(self,"Message from OLYSIS","Please select any values from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.cmpSGndrGraph(self,year)


    def sSports(self):
        sport1 = self.cmbsprts1.currentText()
        sport2 = self.cmbsprts2.currentText()
        year = self.cmbyear.currentText()
        if sport1=="Choose Any Sport" or sport2=="Choose Any Sport" or year=="Choose Any Year":
            QMessageBox.warning(self,"Message from OLYSIS","Please select any values from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.cmpSSprtGraph(self,sport1,sport2,year)



class MultipleYear(QDialog):
    def __init__(self,num,parent=None):
        super(MultipleYear, self).__init__()
        self.parent=parent
        self.num=str(num)
        self.setGeometry(200, 100, 800, 500)
        newfont = QFont("Browallia New", 18, QFont.Bold)
        grid = QGridLayout()

        dataoly = pd.read_csv("olympic_medalists.csv")

        yearlbl1 = QLabel("Choose Any Year : ")
        yearlbl1.setFont(newfont)
        self.cmbyear1 = QComboBox()

        dataoly["Edition"] = dataoly["Edition"].astype('str')
        years=dataoly["Edition"].unique()

        self.cmbyear1.addItem("Choose Any Year")
        self.cmbyear1.addItems(years)
        self.cmbyear1.setFont(newfont)

        yearlbl2 = QLabel("Choose Another Year : ")
        yearlbl2.setFont(newfont)
        self.cmbyear2 = QComboBox()
        self.cmbyear2.addItem("Choose Another Year")
        self.cmbyear2.addItems(years)
        self.cmbyear2.setFont(newfont)

        btnshow = QPushButton("Compare Graph")
        btnshow.setFont(newfont)

        if self.num=="1":
            self.setWindowTitle(" Year VS Year Single Country Comparison Analysis Section!!! ")
            cntrylbl = QLabel("Choose Any Country : ")
            cntrylbl.setFont(newfont)
            self.cmbcntry = QComboBox()
            data = pd.read_csv("Country medals count.csv")
            data["Country"] = data["Country"].astype('str')
            countries = data["Country"].sort_values()
            self.cmbcntry.addItem("Choose Any Country")
            self.cmbcntry.addItems(countries)
            self.cmbcntry.setFont(newfont)
            btnshow.clicked.connect(self.mCountry)
            grid.addWidget(cntrylbl, 0, 0)
            grid.addWidget(self.cmbcntry, 0, 1, 1, 2)

        elif self.num=="2":
            self.setWindowTitle(" Year VS Year Genderwise Comparison Analysis Section!!! ")
            gnderlbl = QLabel("Choose Any Gender : ")
            gnderlbl.setFont(newfont)
            self.cmbgnder = QComboBox()
            values = ["Men", "Women"]
            self.cmbgnder.addItem("Choose Any Gender")
            self.cmbgnder.addItems(values)
            self.cmbgnder.setFont(newfont)
            btnshow.clicked.connect(self.mGender)
            grid.addWidget(gnderlbl, 0, 0)
            grid.addWidget(self.cmbgnder, 0, 1, 1, 2)
        else:
            self.setWindowTitle(" Year VS Year Sportswise Comparison Analysis Section!!! ")
            sprtslbl = QLabel("Choose Any Sports : ")
            sprtslbl.setFont(newfont)
            self.cmbsprts = QComboBox()
            dataoly["Sport"] = dataoly["Sport"].astype('str')
            sports = dataoly["Sport"].unique()
            self.cmbsprts.addItem("Choose Any Sport")
            self.cmbsprts.addItems(sports)
            self.cmbsprts.setFont(newfont)
            btnshow.clicked.connect(self.mSports)
            grid.addWidget(sprtslbl, 0, 0)
            grid.addWidget(self.cmbsprts, 0, 1, 1, 2)

        grid.addWidget(yearlbl1, 2, 0)
        grid.addWidget(self.cmbyear1, 2, 1, 1, 2)
        grid.addWidget(yearlbl2, 4, 0, 1, 3)
        grid.addWidget(self.cmbyear2, 4, 1, 1, 3)
        grid.addWidget(btnshow, 5, 0, 1, 4)

        self.setLayout(grid)
        self.show()



    def mCountry(self):
        country = self.cmbcntry.currentText()
        year1=self.cmbyear1.currentText()
        year2 = self.cmbyear2.currentText()
        if country=="Choose Any Country" or year1=="Choose Any Year" or year2=="Choose Another Year":
            QMessageBox.warning(self,"Message from OLYSIS","Please select any values from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.cmpMCntryGraph(self,country,year1,year2)


    def mGender(self):
        gender = self.cmbgnder.currentText()
        year1 = self.cmbyear1.currentText()
        year2 = self.cmbyear2.currentText()
        if gender == "Choose Any Gender" or year1 == "Choose Any Year" or year2 == "Choose Another Year":
            QMessageBox.warning(self,"Message from OLYSIS","Please select any values from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.cmpMGndrGraph(self,gender,year1,year2)


    def mSports(self):
        sport = self.cmbsprts.currentText()
        year1 = self.cmbyear1.currentText()
        year2 = self.cmbyear2.currentText()
        if sport=="Choose Any Sports" or year1=="Choose Any Year" or year2=="Choose Another Year":
            QMessageBox.warning(self,"Message from OLYSIS","Please select any values from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.cmpMSprtGraph(self,sport,year1,year2)



class Overall(QDialog):
    def __init__(self,num,parent=None):
        super(Overall, self).__init__()
        self.parent = parent
        self.num = str(num)
        self.setGeometry(200, 100, 800, 500)
        newfont = QFont("Browallia New", 18, QFont.Bold)
        grid = QGridLayout()

        btnshow = QPushButton("Compare Graph")
        btnshow.setFont(newfont)

        if self.num == "1":
            self.setWindowTitle(" Overall Country VS Country Comparison Analysis Section!!! ")
            cntrylbl1 = QLabel("Choose Any Country : ")
            cntrylbl1.setFont(newfont)
            self.cmbcntry1 = QComboBox()
            cntrylbl2 = QLabel("Choose Another Country : ")
            cntrylbl2.setFont(newfont)
            self.cmbcntry2 = QComboBox()
            data = pd.read_csv("Country medals count.csv")
            data["Country"] = data["Country"].astype('str')
            countries = data["Country"].sort_values()
            self.cmbcntry1.addItem("Choose Any Country")
            self.cmbcntry1.addItems(countries)
            self.cmbcntry1.setFont(newfont)
            self.cmbcntry2.addItem("Choose Any Country")
            self.cmbcntry2.addItems(countries)
            self.cmbcntry2.setFont(newfont)
            btnshow.clicked.connect(self.oCountry)
            grid.addWidget(cntrylbl1, 0, 0)
            grid.addWidget(self.cmbcntry1, 0, 1, 1, 2)
            grid.addWidget(cntrylbl2, 2, 0)
            grid.addWidget(self.cmbcntry2, 2, 1, 1, 2)
            grid.addWidget(btnshow, 3, 0, 1, 4)

        elif self.num == "3":
            self.setWindowTitle(" Overall Sport VS Sport Comparison Analysis Section!!! ")
            sprtslbl1 = QLabel("Choose Any Sports : ")
            sprtslbl1.setFont(newfont)
            self.cmbsprts1 = QComboBox()
            sprtslbl2 = QLabel("Choose Another Sports : ")
            sprtslbl2.setFont(newfont)
            self.cmbsprts2 = QComboBox()
            dataoly = pd.read_csv("olympic_medalists.csv")
            dataoly["Sport"] = dataoly["Sport"].astype('str')
            sports = dataoly["Sport"].unique()
            self.cmbsprts1.addItem("Choose Any Sport")
            self.cmbsprts1.addItems(sports)
            self.cmbsprts1.setFont(newfont)
            self.cmbsprts2.addItem("Choose Any Sport")
            self.cmbsprts2.addItems(sports)
            self.cmbsprts2.setFont(newfont)
            btnshow.clicked.connect(self.oSports)
            grid.addWidget(sprtslbl1, 0, 0)
            grid.addWidget(self.cmbsprts1, 0, 1, 1, 2)
            grid.addWidget(sprtslbl2, 2, 0)
            grid.addWidget(self.cmbsprts2, 2, 1, 1, 2)
            grid.addWidget(btnshow, 3, 0, 1, 4)

        self.setLayout(grid)
        self.show()

    def oCountry(self):
        country1 = self.cmbcntry1.currentText()
        country2 = self.cmbcntry2.currentText()
        if country1=="Choose Any Country" or country2=="Choose Any Country":
            QMessageBox.warning(self,"Message from OLYSIS","Please select any values from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.cmpOCntryGraph(self, country1, country2)


    def oSports(self):
        sport1 = self.cmbsprts1.currentText()
        sport2 = self.cmbsprts2.currentText()
        if sport1=="Choose Any Sport" or sport2=="Choose Any Sport":
            QMessageBox.warning(self,"Message from OLYSIS","Please select any values from combo boxes.",QMessageBox.Ok)
        else:
            Graphs.cmpOSprtGraph(self, sport1, sport2)
