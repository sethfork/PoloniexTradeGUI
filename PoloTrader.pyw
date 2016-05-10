import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QTextEdit, QWidget, QDialog, QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import QThread
import main_thread
import thread_getusd
import key
import ui_ResourceFile

from main import Ui_MainWindow

class MyGui(QtWidgets.QMainWindow, Ui_MainWindow):    
    def __init__(self, parent=None):
        super(MyGui, self).__init__(parent)
        self.setupUi(self)

        _translate = QtCore.QCoreApplication.translate
        self.lnSellPrice.setText(_translate("MainWindow", str(0.0))) 
        self.lnSellAmount.setText(_translate("MainWindow", str(0.0)))
        self.lnSellTotal.setText(_translate("MainWindow", str(0.0)))
        self.lnBuyPrice.setText(_translate("MainWindow", str(0.0))) 
        self.lnBuyAmount.setText(_translate("MainWindow", str(0.0)))
        self.lnBuyTotal.setText(_translate("MainWindow", str(0.0))) 

        self.lnPublicKey.setPlaceholderText("Insert your Poloniex Public key..")
        self.lnSecretKey.setPlaceholderText("Insert your Poloniex Secret key..")


    def setTaskWindowTitle(self, gui, price):
        self.gui = gui
        _translate = QtCore.QCoreApplication.translate
        self.gui.setWindowTitle(_translate("MainWindow", str(price)))
    def setMenu(self, menu):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/XMRicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        menu.setWindowIcon(icon)
        _translate = QtCore.QCoreApplication.translate
    def setLcdMonero(self,lcdmonero):
        _translate = QtCore.QCoreApplication.translate
        self.lcdMonero.display(_translate("MainWindow", lcdmonero))
    def setLcdBitcoin(self,lcdbitcoin):
        _translate = QtCore.QCoreApplication.translate
        self.lcdBitcoin.display(_translate("MainWindow", lcdbitcoin))
    def setLcdEthereum(self,lcdethereum):
        _translate = QtCore.QCoreApplication.translate
        self.lcdEthereum.display(_translate("MainWindow", lcdethereum)) 
    def setUSDPrice(self, usd):
        _translate = QtCore.QCoreApplication.translate
        self.lnPriceUSD.setText(_translate("MainWindow", str(usd)))    
    def setXMRPrice(self, price):
        _translate = QtCore.QCoreApplication.translate
        self.lnPriceBTC.setText(_translate("MainWindow", str(price)))
    def setETHPrice(self, price):
        _translate = QtCore.QCoreApplication.translate
        self.lnPriceETH.setText(_translate("MainWindow", str(price)))
    def setHigh(self, high):
        _translate = QtCore.QCoreApplication.translate
        self.lnHigh.setText(_translate("MainWindow", str(high)))
    def setLow(self, low):
        _translate = QtCore.QCoreApplication.translate
        self.lnLow.setText(_translate("MainWindow", str(low)))        
    def setChange(self, change):
        _translate = QtCore.QCoreApplication.translate
        self.lnChange.setText(_translate("MainWindow", change))    
    def setLcdMoneroinclIO(self, moneroinclio):
        _translate = QtCore.QCoreApplication.translate
        self.lcdMoneroinclO.display(_translate("MainWindow", moneroinclio))
    def setLcdEthereuminclIO(self, ethereuminclio):
        _translate = QtCore.QCoreApplication.translate
        self.lcdEthereuminclO.display(_translate("MainWindow", ethereuminclio))
    def setSellBTCTotal(self, sellbtctotal):
        _translate = QtCore.QCoreApplication.translate
        self.lnSellTotal.setText(_translate("MainWindow", str(sellbtctotal)))
    def setSellBTCPrice(self, sellbtcprice):
        _translate = QtCore.QCoreApplication.translate
        self.lnSellPrice.setText(_translate("MainWindow", str(sellbtcprice)))   
    def setBuyXMRAmount(self, buyxmramount):
        _translate = QtCore.QCoreApplication.translate
        self.lnBuyAmount.setText(_translate("MainWindow", str(buyxmramount)))
    def setBuyBTCTotal(self, buybtctotal):
        _translate = QtCore.QCoreApplication.translate
        self.lnBuyTotal.setText(_translate("MainWindow", str(buybtctotal)))








def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MyGui()
    form.show()
    form.setMenu(form)
    myThread = main_thread.Thread(form, key.PUBLIC_KEY, key.SECRET_KEY)
    myThread.start()
    myThread.clickBuy()
    myThread.clickSell()
    myThread.clickSaveConfiguration()
    myThread.clickSellGetBTCPrice()
    myThread.clickBuyGetBTCTotal()
    myThread.cancelOrder()
    myThread_getusd = thread_getusd.Thread(form)
    myThread_getusd.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
	main()