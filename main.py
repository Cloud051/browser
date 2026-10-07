from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aether browser")
        self.setGeometry(100, 100, 1024, 768)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search Google or type a URL...")
        self.search_input.returnPressed.connect(self.search_bar)
        
        layout = QVBoxLayout()
        layout.addWidget(self.search_input)
        layout.addWidget(self.browser)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.show()
    
    def search_bar(self):
        search_text = self.search_input.text().strip()
        if search_text:
            if search_text.startswith("http://") or search_text.startswith("https://") or ("." in search_text and " " not in search_text):
                if not search_text.startswith("http"):
                    search_text = "https://" + search_text
                self.browser.setUrl(QUrl(search_text))
            else:
                self.browser.setUrl(QUrl(f"https://www.google.com/search?q={search_text}"))

app = QApplication(sys.argv)
QApplication.setApplicationName("Aether browser")
window = MainWindow()
app.exec_()