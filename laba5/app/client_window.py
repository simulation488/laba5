import tkinter as tk
from tkinter import ttk, messagebox
from models.zhes import ZHES
from models.resident import StandardResident, PrivilegedResident

class ClientWindow:
    def __init__(self, parent: tk.Tk, zhes: ZHES, callback=None) -> None:
        self.window = tk.Toplevel(parent)
        self.window.title("Добавление жильца")
        self.window.geometry("400x400")
        self.zhes = zhes
        self.callback = callback

        self.create_widgets()

    def create_widgets(self) -> None:
        frame = ttk.LabelFrame(self.window, text="Данные жильца")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(frame, text="Имя:").pack(anchor=tk.W, padx=5, pady=2)
        self.name_entry = ttk.Entry(frame)
        self.name_entry.pack(fill=tk.X, padx=5, pady=2)

        ttk.Label(frame, text="Стоимость услуг:").pack(anchor=tk.W, padx=5, pady=2)
        self.services_cost_entry = ttk.Entry(frame)
        self.services_cost_entry.pack(fill=tk.X, padx=5, pady=2)

        ttk.Label(frame, text="Тип жильца:").pack(anchor=tk.W, padx=5, pady=2)
        self.resident_type_var = tk.StringVar()
        self.resident_type_combo = ttk.Combobox(
            frame,
            textvariable=self.resident_type_var,
            values=["Обычный жилец", "Жилец с льготами"]
        )
        self.resident_type_combo.pack(fill=tk.X, padx=5, pady=2)

        button_frame = ttk.Frame(self.window)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(button_frame, text="Добавить", command=self.save_resident).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Отмена", command=self.window.destroy).pack(side=tk.LEFT, padx=5)

    def save_resident(self) -> None:
        try:
            name = self.name_entry.get().strip()
            services_cost = self.services_cost_entry.get().strip()
            resident_type_choice = self.resident_type_combo.get().strip()

            if not name:
                raise ValueError("Имя жильца не может быть пустым.")
            if not services_cost:
                raise ValueError("Стоимость услуг должна быть указана.")
            if not resident_type_choice:
                raise ValueError("Выберите тип жильца.")

            try:
                services_cost = float(services_cost)
                if services_cost <= 0:
                    raise ValueError("Стоимость услуг должна быть положительным числом.")
            except ValueError:
                raise ValueError("Введите корректную стоимость услуг.")

            if resident_type_choice == "Обычный жилец":
                resident_type = StandardResident
            elif resident_type_choice == "Жилец с льготами":
                resident_type = PrivilegedResident
            else:
                raise ValueError("Неверно выбран тип жильца.")

            self.zhes.add_new_resident(name, services_cost, resident_type)

            if self.callback:
                self.callback()

            messagebox.showinfo("Успех", f"Жилец '{name}' успешно добавлен.")
            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка: {str(e)}")
