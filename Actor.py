from abc import abstractmethod, ABC
from ActorBehaviour import ActorBehaviour


class Actor(ActorBehaviour):

    def __init__(self, name: str):
        super().__init__()
        self._name = name

    def isTakeOrder(self: bool):
        pass

    def isMakeOrder(self: bool):
        pass

    @abstractmethod
    def getName(self):
        return self._name
