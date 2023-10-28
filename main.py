from Human import Human
from Market import Market


class Main:
    market: Market = Market()
    human1 = Human("Ivan")
    human2 = Human("Vlad")
    market.acceptToMarket(human1)
    market.acceptToMarket(human2)
    market.update()

