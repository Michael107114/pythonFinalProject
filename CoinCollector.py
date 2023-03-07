
class CoinCollector:

    # constructor so you cannot instantiate this class
    def __init(self):
        pass

    def parseChange(self, coins):
        value = 0
        faces = {'P' : 1, 'N': 5, 'D': 10, 'Q' : 25, 'H': 50, 'W': 100}
        for letter in coins.upper():
            coin = faces.get(letter, 0)
            value += coin

        return value
