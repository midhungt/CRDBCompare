import tkinter as tk
import subprocess

class App:
    def __init__(self, master):
        self.master = master
        master.title("Database Compare Tool")

        # Create input fields
        tk.Label(master, text="Hostname").grid(row=0)
        tk.Label(master, text="Port").grid(row=1)
        tk.Label(master, text="Username").grid(row=2)
        tk.Label(master, text="Password").grid(row=3)
        tk.Label(master, text="Database").grid(row=4)

        self.hostname_entry = tk.Entry(master)
        self.port_entry = tk.Entry(master)
        self.username_entry = tk.Entry(master)
        self.password_entry = tk.Entry(master, show="*")
        self.database_entry = tk.Entry(master)

        self.hostname_entry.grid(row=0, column=1)
        self.port_entry.grid(row=1, column=1)
        self.username_entry.grid(row=2, column=1)
        self.password_entry.grid(row=3, column=1)
        self.database_entry.grid(row=4, column=1)

        # Create button to run script
        tk.Button(master, text="Compare Databases", command=self.run_script).grid(row=5, column=0, columnspan=2)
        tk.Button(master, text="Clear Results", command=self.clearToTextInput).grid(row=7, column=0, columnspan=2)

        # Create text widget to display output
        self.output_text = tk.Text(master)
        self.output_text.grid(row=6, column=0, columnspan=2)
    def clearToTextInput(self):
        self.output_text.delete("start","end")

    def run_script(self):
        # Get input values
        hostname = self.hostname_entry.get()
        port = self.port_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        database = self.database_entry.get()

        # Validate input values
        if not self.validate_input(hostname, port, username, password, database):
            return

        # Run script and display output
        try:
            output = subprocess.check_output(['python', 'crdbcompare.py', hostname, port, username, password, database])
        except subprocess.CalledProcessError as e:
            self.output_text.insert(tk.END, f"Error: {e.output.decode('utf-8')}")
        else:
            self.output_text.insert(tk.END, output.decode('utf-8'))

    def validate_input(self, hostname, port, username, password, database):
        # Validate that all fields are filled in
        if not hostname or not port or not username or not password or not database:
            self.output_text.insert(tk.END, "Error: All fields are required.\n")
            return False

        # Validate port number
        try:
            port = int(port)
            if port < 1 or port > 65535:
                raise ValueError
        except ValueError:
            self.output_text.insert(tk.END, "Error: Port number must be between 1 and 65535.\n")
            return False

        # Add more input validation as needed

        return True

root = tk.Tk()
app = App(root)
root.mainloop()