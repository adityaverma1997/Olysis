from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import NumericOp
import ComparisonOp
import GraphicOpChoose
import OtherOp
import Countries
import Graphs


class MainScreen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        pix = QPixmap("main.png")
        self.brush = QBrush(pix)
        self.mdi.setBackground(self.brush)

        self.setWindowTitle(" Welcome To OLYSIS ")
        self.setGeometry(200, 100, 1100, 700)
        mainMenu = self.menuBar()
        numeric = mainMenu.addMenu(" Numeric Operations ")
        graphic = mainMenu.addMenu(" Graphical Analysis ")
        compare = mainMenu.addMenu(" Comparison Analysis ")
        other = mainMenu.addMenu(" Other Analysis ")
        country = mainMenu.addMenu(" Countries Information ")
        exit = mainMenu.addMenu(" Exit ")



        ncountmed = QAction("View Countrywise Medals", self)
        ngendmed = QAction("View Genderwise Medals", self)
        nsportsmed = QAction("View Sportswise Medals", self)

        gcountmed = QMenu("Countrywise Medals Graph", self)
        ggendmed = QMenu("Genderwise Medals Graphs", self)
        gsportsmed = QMenu("Sportswise Medals Graphs", self)
        gtop10=QMenu("Top 10 of olympics",self)

        ccountmed = QMenu("Countrywise Medals Comparison", self)
        cgendmed = QMenu("Genderwise Medals Comparison", self)
        csportsmed = QMenu("Sportswise Medals Comparison", self)

        ocountmed=QAction("Multiple Countries Yearwise Analysis",self)
        osportsmed = QAction("Multiple Sports Yearwise Analysis",self)

        cntries = QAction("View Olympic Playing Countries", self)
        hostcntries = QAction("View Olympic Hosting Countries", self)
        cntrycode = QAction("View Country Codes", self)

        ext=QAction("Exit",self)



        subgcmSAct = QAction('Single Year Medals Graph', self)
        subgcmMAct = QAction('Year Wise Medals Graph', self)
        gcountmed.addAction(subgcmSAct)
        gcountmed.addAction(subgcmMAct)

        subggmSAct = QAction('Single Year Medals Graph', self)
        subggmMAct = QAction('Year Wise Medals Graph', self)
        ggendmed.addAction(subggmSAct)
        ggendmed.addAction(subggmMAct)

        subgsmSAct = QAction('Single Year Medals Graph', self)
        subgsmMAct = QAction('Year Wise Medals Graph', self)
        gsportsmed.addAction(subgsmSAct)
        gsportsmed.addAction(subgsmMAct)

        subgtmAct1=QAction('Top 10 medal winning countries',self)
        subgtmAct2 = QAction('Top 10 medal winning sportsperson', self)
        gtop10.addAction(subgtmAct1)
        gtop10.addAction(subgtmAct2)

        subccmSyAct = QAction('B/w Two Countries in a Single Year', self)
        subccmMyAct = QAction('Year VS Year of a country', self)
        subccmOAct = QAction('Overall Country VS Country', self)
        ccountmed.addAction(subccmSyAct)
        ccountmed.addAction(subccmMyAct)
        ccountmed.addAction(subccmOAct)

        subcgmSyAct = QAction('B/w Men VS Women in a Single Year', self)
        subcgmMyAct = QAction('Year VS Year of a gender', self)
        subcgmOAct = QAction('Overall Men VS Women', self)
        cgendmed.addAction(subcgmSyAct)
        cgendmed.addAction(subcgmMyAct)
        cgendmed.addAction(subcgmOAct)

        subcsmSyAct = QAction('B/w Two Sports in a Single Year', self)
        subcsmMyAct = QAction('Year VS Year of a Sport', self)
        subcsmOAct = QAction('Overall Sport VS Sport', self)
        csportsmed.addAction(subcsmSyAct)
        csportsmed.addAction(subcsmMyAct)
        csportsmed.addAction(subcsmOAct)



        ncountmed.setIcon(QIcon("view.png"))
        ngendmed.setIcon(QIcon("view.png"))
        nsportsmed.setIcon(QIcon("view.png"))

        gcountmed.setIcon(QIcon("graph.png"))
        subgcmSAct.setIcon(QIcon("graph.png"))
        subgcmMAct.setIcon(QIcon("graph.png"))

        ggendmed.setIcon(QIcon("graph.png"))
        subggmSAct.setIcon(QIcon("graph.png"))
        subggmMAct.setIcon(QIcon("graph.png"))

        gsportsmed.setIcon(QIcon("graph.png"))
        subgsmSAct.setIcon(QIcon("graph.png"))
        subgsmMAct.setIcon(QIcon("graph.png"))

        gtop10.setIcon(QIcon("graph.png"))
        subgtmAct1.setIcon(QIcon("graph.png"))
        subgtmAct2.setIcon(QIcon("graph.png"))

        ccountmed.setIcon(QIcon("compare.png"))
        subccmSyAct.setIcon(QIcon("compare.png"))
        subccmMyAct.setIcon(QIcon("compare.png"))
        subccmOAct.setIcon(QIcon("compare.png"))

        cgendmed.setIcon(QIcon("compare.png"))
        subcgmSyAct.setIcon(QIcon("compare.png"))
        subcgmMyAct.setIcon(QIcon("compare.png"))
        subcgmOAct.setIcon(QIcon("compare.png"))

        csportsmed.setIcon(QIcon("compare.png"))
        subcsmSyAct.setIcon(QIcon("compare.png"))
        subcsmMyAct.setIcon(QIcon("compare.png"))
        subcsmOAct.setIcon(QIcon("compare.png"))

        ocountmed.setIcon(QIcon("graph.png"))
        osportsmed.setIcon(QIcon("graph.png"))

        cntries.setIcon(QIcon("country.png"))
        hostcntries.setIcon(QIcon("country.png"))
        cntrycode.setIcon(QIcon("code.png"))

        ext.setIcon(QIcon("exit.png"))



        ncountmed.setShortcut("Ctrl+A")
        ngendmed.setShortcut("Ctrl+S")
        nsportsmed.setShortcut("Ctrl+D")

        subgcmSAct.setShortcut("Ctrl+F")
        subgcmMAct.setShortcut("Ctrl+G")
        subggmSAct.setShortcut("Ctrl+H")
        subggmMAct.setShortcut("Ctrl+J")
        subgsmSAct.setShortcut("Ctrl+K")
        subgsmMAct.setShortcut("Ctrl+L")
        subgtmAct1.setShortcut("Ctrl+M")
        subgtmAct2.setShortcut("Ctrl+N")

        subccmSyAct.setShortcut("Ctrl+O")
        subccmMyAct.setShortcut("Ctrl+P")
        subccmOAct.setShortcut("Ctrl+Q")
        subcgmSyAct.setShortcut("Ctrl+R")
        subcgmMyAct.setShortcut("Ctrl+S")
        subcgmOAct.setShortcut("Ctrl+T")
        subcsmSyAct.setShortcut("Ctrl+U")
        subcsmMyAct.setShortcut("Ctrl+V")
        subcsmOAct.setShortcut("Ctrl+W")

        ocountmed.setShortcut("Ctrl+Y")
        osportsmed.setShortcut("Ctrl+C")

        cntries.setShortcut("Ctrl+B")
        hostcntries.setShortcut("Ctrl+I")
        cntrycode.setShortcut("Ctrl+Z")

        ext.setShortcut("Ctrl+E")



        numeric.addAction(ncountmed)
        numeric.addAction(ngendmed)
        numeric.addAction(nsportsmed)

        graphic.addMenu(gcountmed)
        graphic.addMenu(ggendmed)
        graphic.addMenu(gsportsmed)
        graphic.addMenu(gtop10)

        compare.addMenu(ccountmed)
        compare.addMenu(cgendmed)
        compare.addMenu(csportsmed)

        other.addAction(ocountmed)
        other.addAction(osportsmed)

        country.addAction(cntries)
        country.addAction(hostcntries)
        country.addAction(cntrycode)

        exit.addAction(ext)



        ncountmed.triggered.connect(self.showCountMedals)
        ngendmed.triggered.connect(self.showGendMedals)
        nsportsmed.triggered.connect(self.showSportsMedals)

        subgcmSAct.triggered.connect(self.viewSCountMedalsGraph)
        subgcmMAct.triggered.connect(self.viewMCountMedalsGraph)
        subggmSAct.triggered.connect(self.viewSGendMedalsGraph)
        subggmMAct.triggered.connect(self.viewMGendMedalsGraph)
        subgsmSAct.triggered.connect(self.viewSSportsMedalsGraph)
        subgsmMAct.triggered.connect(self.viewMSportsMedalsGraph)
        subgtmAct1.triggered.connect(self.viewTopTenMedalCountries)
        subgtmAct2.triggered.connect(self.viewTopTenMedalists)

        subccmSyAct.triggered.connect(self.compareSCountMedals)
        subccmMyAct.triggered.connect(self.compareMCountMedals)
        subccmOAct.triggered.connect(self.compareOCountMedals)
        subcgmSyAct.triggered.connect(self.compareSGendMedals)
        subcgmMyAct.triggered.connect(self.compareMGendMedals)
        subcgmOAct.triggered.connect(self.compareOGendMedals)
        subcsmSyAct.triggered.connect(self.compareSSportsMedals)
        subcsmMyAct.triggered.connect(self.compareMSportsMedals)
        subcsmOAct.triggered.connect(self.compareOSportsMedals)

        ocountmed.triggered.connect(self.otherCountMedals)
        osportsmed.triggered.connect(self.otherSportsMedals)

        cntries.triggered.connect(self.viewCountries)
        hostcntries.triggered.connect(self.viewHostCountries)
        cntrycode.triggered.connect(self.viewCountryCode)

        exit.triggered.connect(self.exitWindow)


        self.setWindowIcon(QIcon("olyrings.png"))
        self.show()



    def showCountMedals(self):
        try:
            obj = NumericOp.NumericOp(num=1)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)


    def showGendMedals(self):
        try:
            obj = NumericOp.NumericOp(num=2)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)


    def showSportsMedals(self):
        try:
            obj = NumericOp.NumericOp(num=3)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)



    def viewSCountMedalsGraph(self):
        try:
            obj = GraphicOpChoose.TwoComboSection(num=1)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)

    def viewMCountMedalsGraph(self):
        try:
            obj = GraphicOpChoose.OneComboSection(num=1)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)


    def viewSGendMedalsGraph(self):
        try:
            obj = GraphicOpChoose.TwoComboSection(num=2)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)

    def viewMGendMedalsGraph(self):
        try:
            obj = GraphicOpChoose.OneComboSection(num=2)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)


    def viewSSportsMedalsGraph(self):
        try:
            obj = GraphicOpChoose.TwoComboSection(num=3)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)

    def viewMSportsMedalsGraph(self):
        try:
            obj = GraphicOpChoose.OneComboSection(num=3)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex:
            print(ex)


    def viewTopTenMedalCountries(self):
        try:
            Graphs.showTopTenMedalCountries(self)
        except BaseException as ex:
            print(ex)

    def viewTopTenMedalists(self):
        try:
            Graphs.showTopTenMedalists(self)
        except BaseException as ex:
            print(ex)



    def compareSCountMedals(self):
        try :
            obj = ComparisonOp.SingleYear(num=1)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex :
            print(ex)


    def compareMCountMedals(self):
        try :
            obj = ComparisonOp.MultipleYear(num=1)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex :
            print(ex)


    def compareOCountMedals(self):
        try :
            obj = ComparisonOp.Overall(num=1)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex :
            print(ex)


    def compareSGendMedals(self):
        try :
            obj = ComparisonOp.SingleYear(num=2)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex :
            print(ex)


    def compareMGendMedals(self):
        try :
            obj = ComparisonOp.MultipleYear(num=2)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex :
            print(ex)


    def compareOGendMedals(self):
        try :
            Graphs.cmpOGndrGraph(self)
        except BaseException as ex :
            print(ex)


    def compareSSportsMedals(self):
        try :
            obj = ComparisonOp.SingleYear(num=3)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex :
            print(ex)


    def compareMSportsMedals(self):
        try :
            obj = ComparisonOp.MultipleYear(num=3)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex :
            print(ex)


    def compareOSportsMedals(self):
        try :
            obj = ComparisonOp.Overall(num=3)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex :
            print(ex)


    def otherCountMedals(self):
        try :
            obj = OtherOp.OtherOp(num=1)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex :
            print(ex)

    def otherSportsMedals(self):
        try :
            obj = OtherOp.OtherOp(num=2)
            self.mdi.addSubWindow(obj)
            obj.show()
        except BaseException as ex :
            print(ex)


    def viewCountries(self):
        try :
            obj = Countries.ViewCountryTable()
            self.mdi.addSubWindow(obj)
            obj.show()

        except BaseException as ex :
            print(ex)


    def viewHostCountries(self):
        try :
            obj = Countries.ViewHostCountriesTable()
            self.mdi.addSubWindow(obj)
            obj.show()

        except BaseException as ex :
            print(ex)


    def viewCountryCode(self):
        try :
            obj = Countries.ViewCode()
            self.mdi.addSubWindow(obj)
            obj.show()

        except BaseException as ex :
            print(ex)


    def exitWindow(self):
        res=QMessageBox.question(self, 'Message from OLYSIS','Do you really want to close this application?', QMessageBox.Yes | QMessageBox.No)
        if res==QMessageBox.Yes:
            sys.exit(0)

'''
if __name__ == "__main__":

    app = QApplication(sys.argv)
    obj = MainScreen()
    obj.show()
    sys.exit(app.exec_())
'''