import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(200,200,1500,1500)
    win.setWindowIcon(QtGui.QIcon('icon.png'))
    win.setToolTip('my tool tip')
    

    win.show()
    sys.exit(app.exec_())
window()