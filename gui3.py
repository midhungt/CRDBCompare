import tkinter as tk
import subprocess

class CompareDataGUI:
    def __init__(self, master):
        self.master = master
        master.title("Compare Data GUI")

        self.hostname_label = tk.Label(master, text="Hostname:")
        self.hostname_label.grid(row=0, column=0)

        self.hostname_entry = tk.Entry(master)
        self.hostname_entry.grid(row=0, column=1)

        self.port_label = tk.Label(master, text="Port:")
        self.port_label.grid(row=1, column=0)

        self.port_entry = tk.Entry(master)
        self.port_entry.grid(row=1, column=1)

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.grid(row=2, column=0)

        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=2, column=1)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=3, column=0)

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=3, column=1)

        self.database_label = tk.Label(master, text="Database:")
        self.database_label.grid(row=4, column=0)

        self.database_entry = tk.Entry(master)
        self.database_entry.grid(row=4, column=1)

        self.protocol_label = tk.Label(master, text="Protocol:")
        self.protocol_label.grid(row=5, column=0)

        self.protocol_var = tk.StringVar(master)
        self.protocol_var.set("TCP") # Default value
        self.protocol_options = ["TCP", "UDP"]
        self.protocol_dropdown = tk.OptionMenu(master, self.protocol_var, *self.protocol_options)
        self.protocol_dropdown.grid(row=5, column=1)

        self.policy_label = tk.Label(master, text="Policy:")
        self.policy_label.grid(row=6, column=0)

        self.policy_var = tk.StringVar(master)
        self.policy_var.set("Data Retention") # Default value
        self.policy_options = ["Data Retention", "Access Control"]
        self.policy_dropdown = tk.OptionMenu(master, self.policy_var, *self.policy_options)
        self.policy_dropdown.grid(row=6, column=1)

        self.standard_label = tk.Label(master, text="Standard:")
        self.standard_label.grid(row=7, column=0)

        self.standard_var = tk.StringVar(master)
        self.standard_var.set("GDPR") # Default value
        self.standard_options = ["GDPR", "HIPAA"]
        self.standard_dropdown = tk.OptionMenu(master, self.standard_var, *self.standard_options)
        self.standard_dropdown.grid(row=7, column=1)

        self.messaging_label = tk.Label(master, text="Messaging:")
        self.messaging_label.grid(row=8, column=0)

        self.messaging_var = tk.StringVar(master)
        self.messaging_var.set("Apache Kafka") # Default value
        self.messaging_options = ["Apache Kafka", "RabbitMQ"]
        self.messaging_dropdown = tk.OptionMenu(master, self.messaging_var, *self.messaging_options)
        self.messaging_dropdown.grid(row=8, column=1)

        self.streaming_label = tk.Label(master, text="Streaming:")
        self.streaming_label.grid(row=9, column=0)

        self.streaming_var = tk.StringVar(master)
        self.streaming_var.set("Apache Flink") # Default value
        self.streaming_options = ["Apache Flink", "Apache Storm"]
        self.streaming_dropdown = tk.OptionMenu(master, self.streaming_var, *self.streaming_options)
        self.streaming_dropdown.grid(row=9, column=1)

        self.compare_button = tk.Button(master, text="Compare Data", command=self.compare_data)
        self.compare_button.grid(row=10, column=1)

    def compare_data(self):
        hostname = self.hostname_entry.get()
        port = self.port_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        database = self.database_entry.get()
        protocol = self.protocol_var.get()
        policy = self.policy_var.get()
        standard = self.standard_var.get()
        messaging = self.messaging_var.get()
        streaming = self.streaming_var.get()

        subprocess.call(["python", "crdbcompare.py", hostname, port, username, password, database, protocol, policy, standard, messaging, streaming])

root = tk.Tk()
my_gui = CompareDataGUI(root)
root.mainloop()