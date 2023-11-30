from PySide6.QtWidgets import QMainWindow, QApplication
from hand_sound_squad_ui import Ui_MainWindow
class HAND_SOUND_SQUAD(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(HAND_SOUND_SQUAD, self). __init__(parent)
        self.setupUi(self)    

if __name__ == '__main__':
    app = QApplication()
    window = HAND_SOUND_SQUAD()
    window.show()
    app.exec()