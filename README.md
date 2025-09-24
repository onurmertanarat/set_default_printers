# Windows Default Printer Setter

A simple desktop application for Windows that allows users to quickly view and set their default printer from a clean graphical user interface (GUI).

<p>
  <img src="https://github.com/onurmertanarat/set_default_printers/blob/master/assets/set-default-printers-screenshot.PNG" alt="Application Screenshot">
</p>

---

## Features

* **Dynamic Printer Discovery:** Automatically scans and lists all locally installed printers on the system.
* **Simple User Interface:** An easy-to-use and intuitive interface built with Python's standard GUI library, Tkinter.
* **Instant In-App Feedback:** A status bar at the bottom of the application provides immediate confirmation of successful operations or clear error messages.
* **Self-Contained:** Works out-of-the-box after installation without the need for complex configuration files.

---

## Technology Stack

* **Python 3**
* **Tkinter:** For the graphical user interface (part of the standard library).
* **pywin32:** For interacting with the Windows API to list and set printers.

---

## Setup and Usage

### Prerequisites

* Windows Operating System
* Python 3.6+
* pip

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/onurmertanarat/set_default_printers.git](https://github.com/onurmertanarat/set_default_printers.git)
    cd set_default_printers
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # Create the environment
    python -m venv venv

    # Activate on Windows
    venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

Simply run the `main.py` script to launch the GUI:

```sh
python main.py
```

---

## Contact

Onur Mert Anarat

[linkedin.com/in/onurmertanarat](https://www.linkedin.com/in/onurmertanarat)
