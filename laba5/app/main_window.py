import tkinter as tk
from tkinter import ttk, messagebox
from models.zhes import ZHES
from app.client_window import ClientWindow
from app.rate_window import RateWindow

class MainWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Tk()
        self.window.title("Главное окно ЖЭС")
        self.window.geometry("400x400")

        self.zhes = ZHES()

        self._create_buttons()

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def _create_buttons(self):
        button_frame = tk.Frame(self.window)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Button(button_frame, text="Добавить жильца", command=self.open_client_window).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(button_frame, text="Показать информацию о жильцах", command=self.open_rate_window).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(button_frame, text="Вычислить стоимость всех услуг", command=self.show_total_services_cost).pack(fill=tk.X, padx=5, pady=5)

    def open_client_window(self):
        ClientWindow(self.window, self.zhes, self.update_residents_list)

    def open_rate_window(self):
        RateWindow(self.window, self.zhes)

    def show_total_services_cost(self):
        total_services_cost = self.zhes.get_total_services_cost()
        messagebox.showinfo("Стоимость всех услуг", f"Общая стоимость всех услуг: {total_services_cost} рублей")

    def update_residents_list(self):
        pass

    def on_close(self):
        self.window.destroy()
