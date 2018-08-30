from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MainScreen
import time
import sys


class Form(QDialog):
    """ Just a simple dialog with a couple of widgets
    """

    def __init__(self):

        super(Form, self).__init__()

        # Create and display the splash screen
        splash_pix = QPixmap('splash.jpg')

        splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        splash.setEnabled(False)
        # splash = QSplashScreen(splash_pix)
        # adding progress bar
        progressBar = QProgressBar(splash)
        progressBar.setMaximum(10)
        progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 10)

        # splash.setMask(splash_pix.mask())

        splash.show()
        # splash.showMessage("<h1><font color='blue'>Welcome To OLYSIS!</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)

        for i in range(1, 11):
            progressBar.setValue(i)
            t = time.time()
            while time.time() < t + 0.1:
                app.processEvents()

        # Simulate something that takes time
        time.sleep(2)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = Form()
    obj = MainScreen.MainScreen()
    obj.show()
    sys.exit(app.exec_())