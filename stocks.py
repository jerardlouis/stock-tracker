class StockPortfolio:
    '''This class describes a stock portfolio'''

    #Initializes the stock portfolio
    def __init__(self,name):
        self.name = name
        self.stocks = {}

    #Allows the user to purcase more stocks
    def buyMore(self,ticker,shares):

        #Checks to see if stock is in the portfolio
        if ticker in self.stocks:
            #Updates the aforementioned stock balance
            self.stocks[ticker] += shares
        else:
            #Appends the stock to the portfolio with the given stock quantity
            self.stocks.update({ticker:shares})

    #Allows the user to sell their stocks      
    def sellOff(self,ticker,shares):

        #Checks to see if the stock is in the portfolio
        if ticker in self.stocks:
            #Updates the aforementioned stock balance
            self.stocks[ticker] -= shares
        else:
            #Reminds the user that they do not own this stock
            return('You do not own this stock')

'''
To use: 
>>> import stocks
>>> stocks = stocks.StockPortfolio('Your name')
>>> stocks.buyMore('Stock name',250)
>>> stocks.sellOff('Stock name',50)
'''
