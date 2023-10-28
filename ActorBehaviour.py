
class ActorBehaviour:

    def __init__(self):
        self.pickUpOrder = None
        self.makeOrder = None

    def setMakeOrder(self):
        self.makeOrder = bool(True)

    def setTakeOrder(self: bool):
        self.pickUpOrder = bool(True)

    def isMakeOrder(self):
        return self.makeOrder

    def isTakeOrder(self):
        return self.pickUpOrder
