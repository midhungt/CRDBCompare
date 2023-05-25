from tkinter import *
import subprocess

root = Tk()
root.title("CRDB Compare")

# Function to execute the crdbcompare.py script
def compare_data():
    # Get the input values
    hostname = hostname_entry.get()
    port = port_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    database = database_entry.get()

    # Execute the crdbcompare.py script with the input values
    try:
        #subprocess.run(['python', 'crdbcompare.py', '-h', hostname, '-p', port, '-u', username, '-P', password, '-d', database])
        subprocess.run(['python', 'crdbcompare.py', hostname, port, username, password, database])

    except Exception as e:
        output_label.config(text="Error: " + str(e))

# Create the input labels and entries
hostname_label = Label(root, text="Hostname:")
hostname_label.grid(row=0, column=0)
hostname_entry = Entry(root)
hostname_entry.grid(row=0, column=1)

port_label = Label(root, text="Port:")
port_label.grid(row=1, column=0)
port_entry = Entry(root)
port_entry.grid(row=1, column=1)

username_label = Label(root, text="Username:")
username_label.grid(row=2, column=0)
username_entry = Entry(root)
username_entry.grid(row=2, column=1)

password_label = Label(root, text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(root, show="*")
password_entry.grid(row=3, column=1)

database_label = Label(root, text="Database:")
database_label.grid(row=4, column=0)
database_entry = Entry(root)
database_entry.grid(row=4, column=1)

# Create the compare button
compare_button = Button(root, text="Compare", command=compare_data)
compare_button.grid(row=5, column=0)

# Create the output label
output_label = Label(root, text="")
output_label.grid(row=6, column=0, columnspan=2)

root.mainloop()