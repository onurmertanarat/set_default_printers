from pynput import keyboard
import win32print


def set_microsoft_xps_document_writer():
    try:
        win32print.SetDefaultPrinter("Microsoft XPS Document Writer")
        print(f"Microsoft XPS Document Writer set as the default printer.")
    except Exception as e:
        print(f"An error occurred: {e}")


def set_microsoft_print_to_pdf():
    try:
        win32print.SetDefaultPrinter("Microsoft Print to PDF")
        print(f"Microsoft Print to PDF set as the default printer.")
    except Exception as e:
        print(f"An error occurred: {e}")


def set_fax():
    try:
        win32print.SetDefaultPrinter("Fax")
        print(f"Fax set as the default printer.")
    except Exception as e:
        print(f"An error occurred: {e}")


with keyboard.GlobalHotKeys({
    "<ctrl>+<alt>+1": set_microsoft_xps_document_writer,
    "<ctrl>+<alt>+2": set_microsoft_print_to_pdf,
    "<ctrl>+<alt>+3": set_fax,
}) as h:
    h.join()
