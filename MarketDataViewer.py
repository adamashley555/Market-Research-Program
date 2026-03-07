import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QWidget, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Market Modeling Tool")

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
        tickerPrompt = QLabel("Enter Ticker: ")
        infoMenuLayout.addWidget(tickerPrompt, 0, 0)
        
        self.searchBox = QLineEdit()
        self.searchBox.returnPressed.connect(lambda: self.tickerSearch(self.searchBox.text()))
        infoMenuLayout.addWidget(self.searchBox, 0, 1)

        searchSpacer = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        infoMenuLayout.addItem(searchSpacer, 1, 0)

        self.EPSLabel = QLabel("Earnings Per Share (EPS): ")
        infoMenuLayout.addWidget(self.EPSLabel, 2, 0)

        #Add Space at Bottom
        rowTotal = infoMenuLayout.rowCount()

        infoMenuLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), rowTotal+1, 0)

        statsButton = QPushButton("View statistics")
        infoMenuLayout.addWidget(statsButton, rowTotal+2, 0)

        # Create Graph
        self.dataPlot = FigureCanvas(Figure())
        mainLayout.setColumnStretch(1, 4)
        mainLayout.addWidget(self.dataPlot, 0, 1)
    
    downloadedData = None

    def tickerSearch(self, receivedTicker):
        receivedTicker = yf.Ticker(receivedTicker)
        plotFigure = self.dataPlot.figure
        self.dataPlot.figure.clf()
        data = self.downloadedData = receivedTicker.history(period="1mo", interval="1d")
        print("Downloaded", receivedTicker)
        #data.columns = data.columns.droplevel(1)

        indexList = list(range(0, len(data)))

        ax = plotFigure.add_subplot()
        ax.set_axisbelow(True)

        up = data[data.Close >= data.Open]
        down = data[data.Close < data.Open]

        width = .5
        width2 = .03

        ax.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color="green")
        ax.bar(up.index, up.High-up.Low, width2, bottom=up.Low, color="green")

        ax.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color="red")
        ax.bar(down.index, down.High-down.Low, width2, bottom=down.Low, color="red")

        ax.tick_params(axis='x', rotation=30)

        ax.grid(True)

        self.dataPlot.draw()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()