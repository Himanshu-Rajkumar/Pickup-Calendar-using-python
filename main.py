import tkinter as tk
from tkcalendar import DateEntry

app=tk.Tk()
app.title("Himanshu kumar")
date_entry=DateEntry(app,date_patter="dd/mm/yyyy",background="black",borderwidth=5)
date_entry.pack(padx=10,pady=10)
button=tk.Button(app,text="Show Selected Date")
button.pack(pady=5)
app.mainloop()
