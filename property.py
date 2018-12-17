class Stock(object):

    def __init__(self, stockName):

        # '_' is just a convention and does nothing
        self.__stockName  = stockName   # private now


    @property # when you do Stock.name, it will call this function
    def getname(self):
        return self.__stockName

    @getname.setter # when you do Stock.name = x, it will call this function
    def setname(self, name):
        self.__stockName = name

if __name__ == "__main__":
      myStock = Stock("100")

      #myStock.__stockName  # It is private. You can't access it.

      #Now you can myStock.name
      myStock.setname = float(raw_input("input to your stock: " + str(myStock.getname)+" ? "))
      print myStock.getname
