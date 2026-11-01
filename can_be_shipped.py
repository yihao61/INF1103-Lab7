from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    @abstractmethod
    def get_shipping_cost(self) -> float:
        '''Calculate a non-negative shipping charge.'''