from app.main_window import MainWindow
import tkinter as tk

def main() -> None:
    root = tk.Tk()
    root.withdraw()
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
