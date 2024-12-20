from abc import ABC, abstractmethod

class Resident(ABC):
    def __init__(self, name: str, services_cost: float) -> None:
        self.name = name
        self.services_cost = services_cost

    @abstractmethod
    def calculate_cost(self) -> float:
        pass

    def __str__(self):
        """Отображение информации о жильце."""
        return f"Имя: {self.name}\n" \
               f"Тип жильца: {self.__class__.__name__}\n" \
               f"Стоимость услуг: {self.services_cost} рублей"

class StandardResident(Resident):
    def calculate_cost(self) -> float:
        return self.services_cost  # Стоимость услуг без льгот

class PrivilegedResident(Resident):
    def calculate_cost(self) -> float:
        discount = 0.1 * self.services_cost  # Льгота 10%
        return self.services_cost - discount
