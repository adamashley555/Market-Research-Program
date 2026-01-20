import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QLineEdit
from PySide6.QtCore import Qt
import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Market Model")

        # Define container for all objects
        mainContainer = QWidget()
        self.setCentralWidget(mainContainer)

        # Create Layout
        mainLayout = QGridLayout(mainContainer)

        # Create Info Menu
        infoMenuContainer = QWidget()
        infoMenuLayout = QGridLayout(infoMenuContainer)
        mainLayout.addWidget(infoMenuContainer, 0, 0)

        # Info Menu Elements
        self.tickerPrompt = QLabel("Enter Ticker: ")
        infoMenuLayout.addWidget(self.tickerPrompt, 0, 0)
        
        self.searchBox = QLineEdit()
        self.searchBox.returnPressed.connect(lambda: self.tickerSearch(self.searchBox.text()))
        infoMenuLayout.addWidget(self.searchBox, 0, 1)

        self.EPSLabel = QLabel("Earnings Per Share (EPS): ")
        infoMenuLayout.addWidget(self.EPSLabel, 1, 0)

        # Create Graph
        self.dataPlot = plt.figure()
        mainLayout.setColumnStretch(1, 4)
        mainLayout.addWidget(self.dataPlot, 0, 1)
    
    downloadedData = None

    def tickerSearch(self, receivedTicker):
        '''
        self.dataPlot.clear()
        data = self.downloadedData = yf.download(receivedTicker, period="1mo", interval="1d")
        print("Downloaded", receivedTicker)
        dates = data.index.strftime("%Y/%m/%d").tolist()
        dateIndexes = list(range(0, len(dates)))
        closePrices = data["Close"].to_numpy().flatten().tolist()
        datesAxis = pg.AxisItem(orientation="bottom")
        datesAxis.setTicks([[(index, date) for index, date in zip(dateIndexes, dates)]])
        self.dataPlot.plot(x=list(range(0, len(data))), y=closePrices)
        self.dataPlot.setAxisItems({"bottom": datesAxis})
        '''
        pass
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()