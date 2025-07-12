import tkinter as tk
import calendar
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calendar")
        self.root.geometry("400x400")
        
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        self.header = tk.Label(root, text="", font=("Arial", 16), pady=10)
        self.header.pack()

        self.text = tk.Text(root, width=30, height=10, font=("Courier", 12))
        self.text.pack()

        nav_frame = tk.Frame(root)
        nav_frame.pack(pady=10)

        tk.Button(nav_frame, text="<< Prev", command=self.prev_month).grid(row=0, column=0, padx=5)
        tk.Button(nav_frame, text="Today", command=self.go_to_today).grid(row=0, column=1, padx=5)
        tk.Button(nav_frame, text="Next >>", command=self.next_month).grid(row=0, column=2, padx=5)

        self.show_calendar(self.current_year, self.current_month)

    def show_calendar(self, year, month):
        self.header.config(text=f"{calendar.month_name[month]} {year}")
        self.text.delete("1.0", tk.END)
        cal = calendar.month(year, month)
        self.text.insert(tk.END, cal)

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.show_calendar(self.current_year, self.current_month)

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.show_calendar(self.current_year, self.current_month)

    def go_to_today(self):
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.show_calendar(self.current_year, self.current_month)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
