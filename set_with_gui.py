import tkinter as tk
import win32print

frame1 = tk.Tk()
frame1.title("Get Printer List")
frame1.minsize(width=360, height=480)

lbl_printers = tk.Label(frame1, text="Printers")
lbl_printers.config(font=('Verdana', 14, 'bold'))
lbl_printers.pack(padx=20, pady=20)

lbox_printers = tk.Listbox(frame1)
lbox_printers.config(width=35, font=('Verdana', 8, 'normal'))
lbox_printers.pack(padx=10, pady=10)


def get_printer_list():
    for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL):
        lbox_printers.insert(tk.END, printer[2])


get_printer_list()


def on_enter(event):
    btn_set_printer.config(bg='green', fg='white')


def on_leave(event):
    btn_set_printer.config(bg='gray', fg='white')


btn_set_printer = tk.Button(frame1, text="Set Default Printer")
btn_set_printer.config(width=16, height=2)
btn_set_printer.config(font=('Verdana', 10, 'normal'), bg='gray', fg='white')

btn_set_printer.bind("<Enter>", on_enter)
btn_set_printer.bind("<Leave>", on_leave)

btn_set_printer.pack()


def set_default_printer():
    try:
        selected_indices = lbox_printers.curselection()
        selected_index = selected_indices[0]
        selected_item = lbox_printers.get(selected_index)
        win32print.SetDefaultPrinter(selected_item)
        print(f"{selected_item} set as the default printer.")
    except Exception as e:
        print(f"An error occurred: {e}")


btn_set_printer.config(command=set_default_printer)
# printer_name = "Fax"
# set_default_printer(printer_name)

frame1.mainloop()
