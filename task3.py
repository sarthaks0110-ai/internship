import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime

reminders = {}

# Show calendar
def show_calendar(year, month):
    cal = calendar.month(year, month)
    calendar_text.delete(1.0, tk.END)
    calendar_text.insert(tk.END, cal)

# Validate date format
def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Add reminder
def add_reminder():
    date = date_entry.get().strip()
    text = reminder_entry.get().strip()

    if not date or not text:
        messagebox.showwarning("Input Error", "Fill all fields")
        return

    if not validate_date(date):
        messagebox.showerror("Invalid Date", "Use YYYY-MM-DD format")
        return

    reminders.setdefault(date, []).append(text)

    messagebox.showinfo("Success", f"Reminder added for {date}")
    print("DEBUG:", reminders)  # helps debug

    date_entry.delete(0, tk.END)
    reminder_entry.delete(0, tk.END)

# View reminders
def view_reminders():
    date = date_entry.get().strip()

    if not validate_date(date):
        messagebox.showerror("Invalid Date", "Use YYYY-MM-DD format")
        return

    if date in reminders:
        reminder_list = "\n• " + "\n• ".join(reminders[date])
        messagebox.showinfo(f"Reminders for {date}", reminder_list)
    else:
        messagebox.showinfo("No Reminders", f"No reminders for {date}")

# Update calendar
def update_calendar():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())
        show_calendar(year, month)
    except ValueError:
        messagebox.showerror("Error", "Enter valid year and month")

# GUI
root = tk.Tk()
root.title("Calendar and Reminder App")
root.geometry("500x500")

calendar_text = tk.Text(root, height=10, width=40)
calendar_text.pack(pady=10)

frame1 = tk.Frame(root)
frame1.pack()

tk.Label(frame1, text="Year:").grid(row=0, column=0)
year_entry = tk.Entry(frame1, width=10)
year_entry.grid(row=0, column=1)
year_entry.insert(0, datetime.now().year)

tk.Label(frame1, text="Month:").grid(row=0, column=2)
month_entry = tk.Entry(frame1, width=10)
month_entry.grid(row=0, column=3)
month_entry.insert(0, datetime.now().month)

tk.Button(frame1, text="Show Calendar", command=update_calendar).grid(row=0, column=4)

frame2 = tk.Frame(root)
frame2.pack(pady=10)

tk.Label(frame2, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
date_entry = tk.Entry(frame2, width=15)
date_entry.grid(row=0, column=1)

tk.Label(frame2, text="Reminder:").grid(row=1, column=0)
reminder_entry = tk.Entry(frame2, width=25)
reminder_entry.grid(row=1, column=1)

tk.Button(root, text="Add Reminder", command=add_reminder).pack(pady=5)
tk.Button(root, text="View Reminders", command=view_reminders).pack(pady=5)

show_calendar(datetime.now().year, datetime.now().month)

root.mainloop()