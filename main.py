import tkinter as tk
from tkinter import font
import win32print

class PrinterApp:
    """
    A simple GUI application to view and set the default Windows printer.
    """
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self._create_widgets()
        self._populate_printer_list()

    def setup_window(self):
        """Configures the main application window."""
        self.root.title("Default Printer Setter")
        self.root.minsize(width=360, height=480)
        self.root.resizable(False, False) 

    def _create_widgets(self):
        """Creates and lays out all the widgets in the application."""
        title_font = font.Font(family="Verdana", size=14, weight="bold")
        listbox_font = font.Font(family="Verdana", size=10)
        button_font = font.Font(family="Verdana", size=10)
        status_font = font.Font(family="Verdana", size=9, slant="italic")

        lbl_printers = tk.Label(self.root, text="Available Printers", font=title_font)
        lbl_printers.pack(padx=20, pady=(20, 10))

        list_frame = tk.Frame(self.root)
        self.lbox_printers = tk.Listbox(list_frame, font=listbox_font, width=40, height=15)
        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.lbox_printers.yview)
        self.lbox_printers.config(yscrollcommand=scrollbar.set)
        
        self.lbox_printers.pack(side="left", fill="y")
        scrollbar.pack(side="right", fill="y")
        list_frame.pack(padx=20, pady=5)

        self.btn_set_printer = tk.Button(
            self.root, 
            text="Set as Default Printer", 
            font=button_font, 
            bg="#DDDDDD", 
            command=self._set_default_printer
        )
        self.btn_set_printer.pack(pady=20, ipadx=10, ipady=5)

        self.status_label = tk.Label(self.root, text="Please select a printer.", font=status_font, fg="gray")
        self.status_label.pack(pady=(10, 0), fill="x")

    def _populate_printer_list(self):
        """Fetches and displays the list of local printers."""
        try:
            printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
            for printer in printers:
                # printer[2] is the printer name
                self.lbox_printers.insert(tk.END, printer[2])
        except Exception as e:
            self.update_status(f"Error fetching printers: {e}", "red")

    def _set_default_printer(self):
        """Sets the selected printer as the default."""
        selected_indices = self.lbox_printers.curselection()
        
        if not selected_indices:
            self.update_status("Please select a printer from the list first!", "orange")
            return
            
        try:
            selected_index = selected_indices[0]
            selected_item = self.lbox_printers.get(selected_index)
            win32print.SetDefaultPrinter(selected_item)
            
            self.update_status(f"Success! '{selected_item}' is now the default.", "green")
            print(f"'{selected_item}' set as the default printer.") 
        except Exception as e:
            self.update_status(f"An error occurred: {e}", "red")
            print(f"An error occurred: {e}")

    def update_status(self, message, color):
        """Updates the status label with a new message and color."""
        self.status_label.config(text=message, fg=color)
    
    def run(self):
        """Starts the Tkinter event loop."""
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PrinterApp(root)
    app.run()