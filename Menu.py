from PyQt5 import QtWidgets
from Windowbuttom import Ui_Windowbuttom 
from frmEncriptar import Ui_frmEncriptar 

class Menu(QtWidgets.QMainWindow, Ui_Windowbuttom):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.show_frm_encriptar)

    def show_frm_encriptar(self): 
        self.frmEncriptar = QtWidgets.QMainWindow()
        self.ui_frmencriptar = Ui_frmEncriptar() 
        self.ui_frmencriptar.setupUi(self.frmEncriptar)
        self.frmEncriptar.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Menu()
    window.show()
    app.exec_()