from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys

class ViewCode(QDialog):
    def __init__(self):
        super(ViewCode, self).__init__()
        self.setWindowTitle(" Know Your Country Code!!! ")
        grid = QGridLayout()
        self.setGeometry(200, 100, 800, 500)
        newfont = QFont("Browallia New", 18, QFont.Bold)

        lblcntry = QLabel("Choose Any Country : ")
        lblcntry.setFont(newfont)
        btnshow = QPushButton("Show Country Code")
        btnshow.setFont(newfont)

        data = pd.read_csv("Country medals count.csv")
        data["Country"] = data["Country"].astype('str')
        countries = data["Country"].sort_values()

        self.cmbcntry = QComboBox()
        self.cmbcntry.addItem("Choose Any Country")
        self.cmbcntry.addItems(countries)
        self.cmbcntry.setFont(newfont)

        btnshow.clicked.connect(self.getCode)
        grid.addWidget(lblcntry, 0, 0)
        grid.addWidget(self.cmbcntry, 0, 1, 1, 2)
        grid.addWidget(btnshow, 4, 0, 1, 4)

        self.setLayout(grid)
        self.show()


    def getCode(self):
        try :
            data = pd.read_csv("Olympic_codes.csv")
            country = self.cmbcntry.currentText()
            if country=="Choose Any Country":
                QMessageBox.warning(self,"Message from OLYSIS","Please select any Country to view Country Code.",QMessageBox.Ok)
            else:
                ioccode = data[data['Country'] == country]['Int Olympic Committee code'].item()
                isocode = data[data['Country'] == country]['ISO code'].item()
                result="Country code of " + country + " is : \n\n"
                result+="IOC code : " + ioccode + "\n"
                result+="ISO code : " + isocode
                QMessageBox.information(self, 'Message from OLYSIS', result, QMessageBox.Ok)

        except BaseException as ex :
            print(ex)


class ViewCountryTable(QWidget):
    def __init__(self):
        super(ViewCountryTable,self).__init__()
        self.title = 'List of Countries who participated in Olympics'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        data = pd.read_csv("Country medals count.csv")
        count=len(data)
        r=self.tableWidget.rowCount()
        self.tableWidget.setRowCount(count-1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["Country Names"])
        data["Country"] = data["Country"].astype('str')
        countries = data["Country"].sort_values().values
        for entryPos in range(r, len(data)-1):
            for fieldPos in range(1):
                item = QTableWidgetItem(countries[entryPos])
                self.tableWidget.setItem(entryPos, fieldPos, item)

        self.tableWidget.move(0, 0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())



class ViewHostCountriesTable(QWidget):
    def __init__(self):
        super(ViewHostCountriesTable,self).__init__()
        self.title = 'Olympic Hosting Countries'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        data = pd.read_csv("Hosting.csv")
        r=self.tableWidget.rowCount()
        self.tableWidget.setRowCount(19)
        self.tableWidget.setColumnCount(2)
        header = self.tableWidget.horizontalHeader()
        header.setStretchLastSection(True)
        self.tableWidget.setHorizontalHeaderLabels(["Country Names","Total Games Hosted"])
        data["Host Country"] = data["Host Country"].astype('str')
        countries = data["Host Country"].head(19).values
        hostno=data["Total games"].head(19).values
        hstno = [int(i) for i in hostno]
        hno = [str(i) for i in hstno]
        for entryPos in range(r, len(data)-8):
            for fieldPos in range(2):
                item = QTableWidgetItem(countries[entryPos])
                val = QTableWidgetItem(hno[entryPos])
                if fieldPos==0:
                    self.tableWidget.setItem(entryPos, fieldPos, item)
                elif fieldPos==1:
                    self.tableWidget.setItem(entryPos, fieldPos, val)

        self.tableWidget.move(0, 0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
