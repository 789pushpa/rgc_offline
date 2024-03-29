import pytz #timezone operations: convert datetime objects between different time zones,localize naive datetime objects, allowing you to work with time zone information from around the world.
import yaml #human-readable data serialization format commonly used for configuration files and data exchange between programming languages.
from PyQt5.QtWidgets import QMainWindow, QErrorMessage, QTabWidget, QLabel, QWidget, QDialog, QDialogButtonBox, \ #allows developers to create graphical user interfaces (GUIs) using the Qt APIs.
    QVBoxLayout

#from app.event import Config, Scan, RunningScan, Event, Baseline, HistPoint, History
from app.gui_history import HistTab #Where app is the root package and gui_history.py contains the HistTab class


class MainWindow(QMainWindow): #QMainWindow is a predefined class that provides a main application window. suggests that you are defining a class named MainWindow that inherits from the QMainWindow class.
    '''
    '''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_settings()


        self.tz = pytz.timezone('US/Eastern')

        self.left = 100
        self.top = 100
        self.title = 'Run Group C Offline Polarization'
        self.width = 1500
        self.height = 1200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Make tabs
        self.hist_tab = HistTab(self)
        self.tab_widget.addTab(self.hist_tab, "History")

    def load_settings(self):
        '''Load settings from YAML config file'''

        with open('config.yaml') as f:                           # Load settings from YAML files
           self.config_dict = yaml.load(f, Loader=yaml.FullLoader)
        self.settings = self.config_dict['settings']
        print(f"Loaded settings from config.yaml.")
