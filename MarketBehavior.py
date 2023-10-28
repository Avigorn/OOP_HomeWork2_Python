from typing import List
from zope.interface import Interface
from Actor import Actor


class MarketBehaviour(Interface):
    def acceptToMarket(self, actor: Actor):
        pass

    def releaseFromMarket(self, actors: List[Actor]):
        pass

    def update(self):
        pass
