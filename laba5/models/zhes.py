from models.database import DatabaseManager
from models.resident import StandardResident, PrivilegedResident

class ZHES:
    def __init__(self):
        """Инициализация ЖЭС."""
        self.residents = {}
        self.db_manager = DatabaseManager()
        self.load_residents_from_db()

    def load_residents_from_db(self):
        """Загрузка жильцов из базы данных."""
        residents_data = self.db_manager.get_all_residents()
        for resident_data in residents_data:
            _, name, services_cost, resident_type = resident_data
            resident_type_obj = StandardResident(name, services_cost) if resident_type == "StandardResident" else PrivilegedResident(name, services_cost)
            self.residents[name] = resident_type_obj

    def add_new_resident(self, name, services_cost, resident_type):
        """Добавить нового жильца."""
        if name in self.residents:
            raise ValueError(f"Жилец с именем '{name}' уже существует.")
        
        if not (0 < services_cost < 5000):
            raise ValueError("Стоимость услуг должна быть положительным числом между 1 и 5000.")

        resident = resident_type(name, services_cost)
        self.residents[name] = resident

        # Сохранение в базу данных
        self.db_manager.add_resident({
            "name": name,
            "services_cost": services_cost,
            "resident_type": resident_type.__name__
        })

    def get_total_services_cost(self):
        """Получить сумму всех услуг."""
        total = 0
        for resident in self.residents.values():
            total += resident.calculate_cost()
        return total
