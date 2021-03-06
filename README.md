# PoloniexTradeGUI
(unofficial)

 [![Documentation](https://codedocs.xyz/swalecko/PoloniexTradeGUI.svg)](https://codedocs.xyz/swalecko/PoloniexTradeGUI/)
 

**Donations:** 
XMR: 49wH4MLdp62BrG7pUuh7dJ51icq1T2edpNJpHt7R2qoJTpuR7oK81jWXxH5K6Rz1nZHneK24jj7XdZDmc7U2W2dH8aso46n

Trading app for XMR and ETH at the Poloniex exchange using the Poloniex API.

##Current Features:
  - Supported Currencies for trading: XMR and ETH
  - Price informations 
  - Balances, Balances included open orders
  - 24h High, 24h Low and 24h Change 
  - Open Orders 
    - Note: to cancel an open order double click the cell with the order number
  - History 
  - Trading (Simple Buy and Sell)
    - Note: "A" Auto Button for setting current BTC price in the sell section and Total BTC in the sell section  
  - Configuration: Poloniex Public and Secret Key

##Future Features:
  - There's more to come..
  
##Pre-Information:
  - Based on Qt 5.5.1
  - Using Qt Creator for the design
  - Using Pyqt for the python code
  - Written in Python 3
  
##Requirements:
  - Python 3   
    - Additional modules:  
      - json  
      - requests  
  - PyQt5

##How to use:
  - Execute the PoloTrader.pyw file 
  - When you execute the app for the first time, you need to add your PUBLIC and SECRET API Keys in the Configuration tab and save them.  
    A file "key.py" will be created with the following content:     
    first line: "PUBLIC_KEY = '<key>'"   
    second line: "SECRET_KEY = '<key>'"     
    **Important**: You need to restart the app to activate the keys
  - Happy trading :-)  
  Alternative:
  - Use for example pyinstaller to create a package or a "one-file" for execution  
    Installation: pip install pyinstaller  
    Command Example: pyinstaller -w -n PoloTrader -i XMRicon.ico -F PoloTrader.pyw   
    More information for pyinstaller: http://www.pyinstaller.org/


##Screenshot:

![Screenshot](https://raw.github.com/swalecko/PoloTradeGui/master/Dashboard_screenshot.JPG?raw=true "Open Orders Tab")




