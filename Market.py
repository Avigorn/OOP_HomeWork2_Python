from typing import List
from zope.interface import implementer
from Actor import Actor
from QueueBehaviour import QueueBehaviour
from MarketBehavior import MarketBehaviour


@implementer(QueueBehaviour)
@implementer(MarketBehaviour)
class Market:

    def __init__(self):
        self._queue: List[Actor] = []

    def acceptToMarket(self, actor: Actor):
        print(f'{actor.getName()} пришел в магазин')
        self.takeInQueue(actor)

    def takeInQueue(self, actor: Actor):
        print(f'{actor.getName()} встал в очередь')
        self._queue.append(actor)

    def takeOrders(self):
        actor: Actor
        for actor in self._queue:
            if actor.isMakeOrder():
                actor.setMakeOrder()
                print(f'{actor.getName()} сделал свой заказ')

    def giveOrders(self):
        actor: Actor
        for actor in self._queue:
            if actor.isMakeOrder():
                actor.setTakeOrder()
                print(f'{actor.getName()} получил свой заказ')

    def releaseFromQueue(self):
        releasedActors: List[Actor] = []
        for actor in self._queue:
            if actor.isTakeOrder():
                releasedActors.append(actor)
                print(f'{actor.getName()} вышел из очереди и готов уходить')
        self.releaseFromMarket(releasedActors)

    def releaseFromMarket(self, actors: List[Actor]):
        actor: Actor
        for actor in actors:
            print(f'{actor.getName()} вышел из магазина')
            self._queue.remove(actor)

    def update(self):
        self.takeOrders()
        self.giveOrders()
        self.releaseFromQueue()
