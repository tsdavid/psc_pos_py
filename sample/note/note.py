# LEARN QT From 15-minute-0app

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from MainWindow import *
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

print("DB Connection ")
Base = declarative_base()


class Note(Base):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True)
    text = Column(String(1000), nullable=False)
    x = Column(Integer, nullable=False, default=0)
    y = Column(Integer, nullable=False, default=0)


engine = create_engine('sqlite:///notes.db')

# Initialize the database if it is not already exit
# if not engine.dialect.has_table(engine, "note")
Base.metadata.create_all(engine)

# Create a Session to handle updates
print("Get DB Session")
Session = sessionmaker(bind=engine)
session = Session()

# HashMap contained Window Instance
_ACTIVE_NOTES = {}

def create_new_note():
    print("Create New Note")
    MainWindow()

class MainWindow(QMainWindow, Ui_MainWindow):

    print("Instantiate MainWindow")

    def __init__(self, *args, obj=None, **kwargs):
        print("run init method")

        # Initialize Super Class Ui_MainWindow
        super(MainWindow, self).__init__(*args, **kwargs)
        # Initialize Ui_MainWindow
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.show()

        # Load/Save note data, Store this notes db reference
        if obj:
            print(obj)
            self.obj = obj
            print("Load This obj")
            self.load()
        else:
            self.obj = Note()
            print("Save This obj")
            self.save()

        # UI, Close Btn => delete Window?
        self.closeButton.pressed.connect(self.delete_window)
        # UI, More Btn => New Window!.
        self.moreButton.pressed.connect(create_new_note)
        # UI, If Text Has been changed, save it.
        self.textEdit.textChanged.connect(self.save)
        # ~ connect => event generator.

        # Flags to store dragged-dropped



if __name__ == '__main__':

    print("Start note.py")

    app = QtWidgets.QApplication([])
    app.setApplicationName("Test Note")
    app.setStyle("Fusion")

    print("# Custom brown palette.")
    # Custom brown palette.
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(188, 170, 164))
    palette.setColor(QPalette.WindowText, QColor(121, 85, 72))
    palette.setColor(QPalette.ButtonText, QColor(121, 85, 72))
    palette.setColor(QPalette.Text, QColor(121, 85, 72))
    palette.setColor(QPalette.Base, QColor(188, 170, 164))
    palette.setColor(QPalette.AlternateBase, QColor(188, 170, 164))
    app.setPalette(palette)

    print("Check notes is exist")
    existing_notes = session.query(Note).all()

    if len(existing_notes) == 0:
        MainWindow()
    else:
        for note in existing_notes:
            MainWindow(obj=note)

