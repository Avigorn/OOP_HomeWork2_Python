from Actor import Actor


class Human(Actor):

    def __init__(self, name: str):
        super().__init__(name)

    def getName(self: str):
        return super().getName()

    def setMakeOrder(self):
        super().isMakeOrder()

    def setTakeOrder(self):
        super().isTakeOrder()

    def isMakeOrder(self):
        return super().isMakeOrder

    def isTakeOrder(self):
        return super().isTakeOrder
