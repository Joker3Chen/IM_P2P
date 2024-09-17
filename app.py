import sys

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QWidget, QToolTip, QMessageBox, QMainWindow, QMenuBar, QFileDialog, \
    QVBoxLayout, QPushButton
from PySide2.QtGui import QIcon, QFont


class MyWeight(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        my_button = QPushButton("sasasd")
        layout.addWidget(my_button)

        self.setLayout(layout)

        my_button.clicked.connect(self.my_button_clicked)

    @Slot()
    def my_button_clicked(self):
        print("you clicked")

class StockMainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.InitUI()

    def InitUI(self):
        self.center()
        self.resize(800, 600)
        self.setWindowTitle('Stock Pro')
        self.setWindowIcon(QIcon('resources/icons/cow.jpg'))
        self.setToolTip("waring!")
        QToolTip.setFont(QFont('Arial', 10))

        menu_control = self.menuBar().addMenu('File')
        project_chose_menu = menu_control.addAction("Project")
        project_chose_menu.triggered.connect(self.project_chose)

        # my_weight = MyWeight()
        # self.setCentralWidget(my_weight)


        self.statusBar().showMessage('程序已就绪...')
        self.show()

    def project_chose(self):
        folder_selected  = QFileDialog.getExistingDirectory(self, 'Select Folder')
        print(folder_selected)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "quit now?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = self.app.screens()[0]
        screen_size = screen.size()
        size = self.geometry()
        self.move((screen_size.width() - size.width()) // 2, (screen_size.height() - size.height()) // 2)

if __name__ == '__main__':
    stock_main_app = QApplication(sys.argv)
    stock_main_window = StockMainWindow(stock_main_app)
    stock_main_window.show()
    sys.exit(stock_main_app.exec_())
