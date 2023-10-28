from zope.interface import Interface

from Actor import Actor


class QueueBehaviour(Interface):
    def takeInQueue(self, actor: Actor):
        pass

    def takeOrders(self):
        pass

    def giveOrders(self):
        pass

    def releaseFromQueue(self):
        pass
