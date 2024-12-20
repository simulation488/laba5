import tkinter as tk
from tkinter import ttk, messagebox

class RateWindow:
    def __init__(self, parent, zhes):
        self.parent = parent
        self.zhes = zhes

        self.window = tk.Toplevel(parent)
        self.window.title("Информация о жильцах")
        self.window.geometry("400x400")

        self.residents_listbox = tk.Listbox(self.window)
        self.residents_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.update_residents_list()

        ttk.Button(self.window, text="Показать информацию о жильце", command=self.show_resident_info).pack(pady=10)
        ttk.Button(self.window, text="Сохранить список", command=self.save_residents_list).pack(pady=10)

    def update_residents_list(self):
        self.residents_listbox.delete(0, tk.END)
        for name in self.zhes.residents:
            self.residents_listbox.insert(tk.END, name)

    def show_resident_info(self):
        try:
            selected_name = self.residents_listbox.get(tk.ACTIVE)
            resident = self.zhes.residents.get(selected_name)
            if resident:
                resident_info = (
                    f"Имя: {resident.name}\n"
                    f"Тип жильца: {resident.__class__.__name__}\n"
                    f"Стоимость услуг: {resident.services_cost}"
                )
                messagebox.showinfo("Информация о жильце", resident_info)
            else:
                messagebox.showerror("Ошибка", "Жилец не найден.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def save_residents_list(self):
        try:
            with open("residents_list.txt", "w") as file:
                for name, resident in self.zhes.residents.items():
                    file.write(f"Имя: {resident.name}, "
                               f"Тип жильца: {resident.__class__.__name__}, "
                               f"Стоимость услуг: {resident.services_cost}\n")

            for name, resident in self.zhes.residents.items():
                self.zhes.db_manager.update_resident({
                    "name": name,
                    "services_cost": resident.services_cost,
                    "resident_type": resident.__class__.__name__
                })

            messagebox.showinfo("Успех", "Список жильцов сохранен.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить данные. Ошибка: {str(e)}")
