
import csv
import tkinter as tk
from tkinter import ttk, simpledialog
import hashlib
import datetime
import multiprocessing

'''def create_blockchain_from_csv_file(filename):
    ch = input('Do you want to enter a new record? (T for yes) ')
    if ch == 'T' or ch == 't':
        apaar_id = input('Enter the Apaar ID of the student: ')
        name = input('Enter the name: ')
        class_ = input('Enter the class: ')
        marks = input('Enter the marks: ')
        achievements = input('Enter the achievements: ')
        competition = input('Enter the name of the competition took part in: ')
        comp_result = input('Enter the result of the competition took part in: ')
        final_remarks = input('Enter the remark: ')
        write_new_data_to_csv_file(filename, apaar_id, name, class_, marks, achievements, competition, comp_result, final_remarks)
'''

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = datetime.datetime.now()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_str = str(self.data) + str(self.timestamp) + str(self.nonce) + str(self.previous_hash)
        return hashlib.sha256(data_str.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_hash = self.get_latest_block().hash
        new_block = Block(data, previous_hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def get_latest_block(self):
        return self.chain[-1]

def for_ui(filename, blockchain):
    def submit_data():
        apaar_id_val = apaar_id.get()
        name_val = name.get()
        class_val = class_.get()
        marks_val = marks.get()
        achievements_val = achievements.get()
        competition_val = competition.get()
        comp_result_val = comp_result.get()
        final_remarks_val = final_remarks.get()

        data = [apaar_id_val, name_val, class_val, marks_val, achievements_val, competition_val, comp_result_val, final_remarks_val]

        # Add the Apaar ID to the Apaar ID block in the blockchain
        blockchain.add_block(apaar_id_val)

        # Add the data to the Data block in the blockchain
        blockchain.add_block(data)

        write_new_data_to_csv_file(filename, apaar_id_val, name_val, class_val, marks_val, achievements_val, competition_val, comp_result_val, final_remarks_val)
        clear_fields()
        display_data()

    def clear_fields():
        apaar_id.set('')
        name.set('')
        class_.set('')
        marks.set('')
        achievements.set('')
        competition.set('')
        comp_result.set('')
        final_remarks.set('')

    def display_data():
        data = read_csv_file(filename)
        for record in tree.get_children():
            tree.delete(record)
        for idx, row in enumerate(data, start=1):
            tree.insert('', 'end', values=(idx, *row))

    def read_data():
        clear_fields()
        display_data()

    def search_data():
        apaar_id_to_search = simpledialog.askstring("Search Record", "Enter Apaar ID to search:")
        if apaar_id_to_search is not None:
            display_search_results(apaar_id_to_search)

    def display_search_results(apaar_id_to_search):
        data = read_csv_file(filename)
        results = [row for row in data if row[0] == apaar_id_to_search]
        for record in tree.get_children():
            tree.delete(record)
        for idx, row in enumerate(results, start=1):
            tree.insert('', 'end', values=(idx, *row))

    def update_record():
        apaar_id_to_update = simpledialog.askstring("Update Record", "Enter Apaar ID to update:")
        if apaar_id_to_update is not None:
            update_data_window(apaar_id_to_update)

    def delete_record():
        apaar_id_to_delete = simpledialog.askstring("Delete Record", "Enter Apaar ID to delete:")
        if apaar_id_to_delete is not None:
            delete_data(apaar_id_to_delete)

    def delete_data(apaar_id_to_delete):
        data = read_csv_file(filename)
        updated_data = [row for row in data if row[0] != apaar_id_to_delete]
        write_updated_data_to_csv_file(filename, updated_data)
        display_data()

    def exit_program():
        root.destroy()

    def update_data_window(apaar_id_to_update):
        update_window = tk.Toplevel(root)
        update_window.title("Update Record")
        update_window.configure(bg="#121212")

        name_label = tk.Label(update_window, text="Name:", font=("TkDefaultFont", 10, "bold"), bg="#333333", fg="white")
        name_label.grid(row=0, column=0, sticky='w')
        name_entry = tk.Entry(update_window, bg="#E0E0E0", fg="#121212")
        name_entry.grid(row=0, column=1)

        class_label = tk.Label(update_window, text="Class:", font=("TkDefaultFont", 10, "bold"), bg="#333333", fg="white")
        class_label.grid(row=1, column=0, sticky='w')
        class_entry = tk.Entry(update_window, bg="#E0E0E0", fg="#121212")
        class_entry.grid(row=1, column=1)

        marks_label = tk.Label(update_window, text="Marks:", font=("TkDefaultFont", 10, "bold"), bg="#333333", fg="white")
        marks_label.grid(row=2, column=0, sticky='w')
        marks_entry = tk.Entry(update_window, bg="#E0E0E0", fg="#121212")
        marks_entry.grid(row=2, column=1)

        achievements_label = tk.Label(update_window, text="Achievements:", font=("TkDefaultFont", 10, "bold"), bg="#333333", fg="white")
        achievements_label.grid(row=3, column=0, sticky='w')
        achievements_entry = tk.Entry(update_window, bg="#E0E0E0", fg="#121212")
        achievements_entry.grid(row=3, column=1)

        competition_label = tk.Label(update_window, text="Competition:", font=("TkDefaultFont", 10, "bold"), bg="#333333", fg="white")
        competition_label.grid(row=4, column=0, sticky='w')
        competition_entry = tk.Entry(update_window, bg="#E0E0E0", fg="#121212")
        competition_entry.grid(row=4, column=1)

        result_label = tk.Label(update_window, text="Result:", font=("TkDefaultFont", 10, "bold"), bg="#333333", fg="white")
        result_label.grid(row=5, column=0, sticky='w')
        result_entry = tk.Entry(update_window, bg="#E0E0E0", fg="#121212")
        result_entry.grid(row=5, column=1)

        remarks_label = tk.Label(update_window, text="Remarks:", font=("TkDefaultFont", 10, "bold"), bg="#333333", fg="white")
        remarks_label.grid(row=6, column=0, sticky='w')
        remarks_entry = tk.Entry(update_window, bg="#E0E0E0", fg="#121212")
        remarks_entry.grid(row=6, column=1)

        submit_button = tk.Button(update_window, text="Submit", command=lambda: update_data(apaar_id_to_update), bg="#E0E0E0", fg="#121212")
        submit_button.grid(row=7, column=0, columnspan=2)

        def update_data(apaar_id_to_update):
            data = read_csv_file(filename)
            updated_data = []

            # Initialize updated_data with the current data
            for row in data:
                updated_data.append(row)

            for row in updated_data:
                if row[0] == apaar_id_to_update:
                    row[1] = name_entry.get()
                    row[2] = class_entry.get()
                    row[3] = marks_entry.get()
                    row[4] = achievements_entry.get()
                    row[5] = competition_entry.get()
                    row[6] = result_entry.get()
                    row[7] = remarks_entry.get()

            write_updated_data_to_csv_file(filename, updated_data)
            display_data()
            update_window.destroy()

    def delete_all_data():
        confirmation = simpledialog.askstring("Confirm Deletion", "Are you sure you want to delete all data? (Type 'YES' to confirm):")
        if confirmation == "YES":
            with open(filename, 'w', newline="") as f:
                f.truncate(0)  # Clear the file
            display_data()
    process_pool = multiprocessing.Pool()

    def submit_data_parallel():
        process_pool.apply_async(submit_data)
    root = tk.Tk()
    root.title("APAAR User Interface")
    root.configure(bg="#121212")

    apaar_id = tk.StringVar()
    name = tk.StringVar()
    class_ = tk.StringVar()
    marks = tk.StringVar()
    achievements = tk.StringVar()
    competition = tk.StringVar()
    comp_result = tk.StringVar()
    final_remarks = tk.StringVar()

    label_title = tk.Label(root, text="Enter information for the new record:", font=("TkDefaultFont", 12, "bold"), fg="white", bg="black")
    label_title.grid(row=0, column=0, columnspan=2, sticky='w')

    tk.Label(root, text="Apaar ID:", font=("TkDefaultFont", 10, "bold"), fg="white", bg="black").grid(row=1, column=0, sticky='w')
    apaar_id_entry = tk.Entry(root, textvariable=apaar_id, bg="#E0E0E0", fg="#121212")
    apaar_id_entry.grid(row=1, column=1)

    tk.Label(root, text="Name:", font=("TkDefaultFont", 10, "bold"), fg="white", bg="black").grid(row=2, column=0, sticky='w')
    name_entry = tk.Entry(root, textvariable=name, bg="#E0E0E0", fg="#121212")
    name_entry.grid(row=2, column=1)

    tk.Label(root, text="Class:", font=("TkDefaultFont", 10, "bold"), fg="white", bg="black").grid(row=3, column=0, sticky='w')
    class_entry = tk.Entry(root, textvariable=class_, bg="#E0E0E0", fg="#121212")
    class_entry.grid(row=3, column=1)

    tk.Label(root, text="Marks:", font=("TkDefaultFont", 10, "bold"), fg="white", bg="black").grid(row=4, column=0, sticky='w')
    marks_entry = tk.Entry(root, textvariable=marks, bg="#E0E0E0", fg="#121212")
    marks_entry.grid(row=4, column=1)

    tk.Label(root, text="Achievements:", font=("TkDefaultFont", 10, "bold"), fg="white", bg="black").grid(row=5, column=0, sticky='w')
    achievements_entry = tk.Entry(root, textvariable=achievements, bg="#E0E0E0", fg="#121212")
    achievements_entry.grid(row=5, column=1)

    tk.Label(root, text="Competition Took Part In:", font=("TkDefaultFont", 10, "bold"), fg="white", bg="black").grid(row=6, column=0, sticky='w')
    competition_entry = tk.Entry(root, textvariable=competition, bg="#E0E0E0", fg="#121212")
    competition_entry.grid(row=6, column=1)

    tk.Label(root, text="Competition Result:", font=("TkDefaultFont", 10, "bold"), fg="white", bg="black").grid(row=7, column=0, sticky='w')
    comp_result_entry = tk.Entry(root, textvariable=comp_result, bg="#E0E0E0", fg="#121212")
    comp_result_entry.grid(row=7, column=1)

    tk.Label(root, text="Final Remarks:", font=("TkDefaultFont", 10, "bold"), fg="white", bg="black").grid(row=8, column=0, sticky='w')
    final_remarks_entry = tk.Entry(root, textvariable=final_remarks, bg="#E0E0E0", fg="#121212")
    final_remarks_entry.grid(row=8, column=1)

    submit_button = tk.Button(root, text="Submit", command=submit_data, bg="#E0E0E0", fg="#121212")
    submit_button.grid(row=9, column=0, columnspan=2)

    read_button = tk.Button(root, text="Read", command=read_data, bg="#E0E0E0", fg="#121212")
    read_button.grid(row=10, column=0, columnspan=2)

    search_button = tk.Button(root, text="Search", command=search_data, bg="#E0E0E0", fg="#121212")
    search_button.grid(row=11, column=0, columnspan=2)

    update_button = tk.Button(root, text="Update Record", command=update_record, bg="#E0E0E0", fg="#121212")
    update_button.grid(row=12, column=0, columnspan=2)

    delete_button = tk.Button(root, text="Delete Record", command=delete_record, bg="#E0E0E0", fg="#121212")
    delete_button.grid(row=13, column=0, columnspan=2)

    exit_button = tk.Button(root, text="Exit", command=exit_program, bg="#E0E0E0", fg="#121212")
    exit_button.grid(row=14, column=0, columnspan=2, sticky='sw')

    # Add a "Delete All Data" button
    delete_button_all = tk.Button(root, text="Delete All Data", command=delete_all_data, bg="#E0E0E0", fg="#121212")
    delete_button_all.grid(row=14, column=1, columnspan=2)
    
    # Create a Treeview to display the data in a table format with a Chinese black backdrop
    style = ttk.Style()
    style.configure("Treeview.Heading", background="#E0E0E0", foreground="#121212")  # For column headers
    style.configure("Treeview", background="#E0E0E0", fieldbackground="#E0E0E0", foreground="black")  # For data columns

    tree = ttk.Treeview(root, columns=("S.no", "Apaar ID", "Name", "Class", "Marks", "Achievements", "Competition", "Result", "Remarks"))

    tree.heading('#1', text="S.no")
    tree.heading('#2', text="Apaar ID")
    tree.heading('#3', text="Name")
    tree.heading('#4', text="Class")
    tree.heading('#5', text="Marks")
    tree.heading('#6', text="Achievements")
    tree.heading('#7', text="Competition")
    tree.heading('#8', text="Result")
    tree.heading('#9', text="Remarks")

    tree.column("#1", width=50, anchor='center')   # S.no
    tree.column("#2", width=100, anchor='center')  # Apaar ID
    tree.column("#3", width=150, anchor='center')  # Name
    tree.column("#4", width=100, anchor='center')  # Class
    tree.column("#5", width=100, anchor='center')  # Marks
    tree.column("#6", width=150, anchor='center')  # Achievements
    tree.column("#7", width=200, anchor='center')  # Competition
    tree.column("#8", width=100, anchor='center')  # Result
    tree.column("#9", width=200, anchor='center')  # Remarks

    tree.grid(row=0, column=2, rowspan=14, columnspan=5, sticky='news')

    display_data()

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.geometry("1000x500")  # Set initial window size

    root.mainloop()

def write_new_data_to_csv_file(filename, apaar_id, name, class_, marks, achievements, competition, comp_result, final_remarks):
    with open(filename, 'a+', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([apaar_id, name, class_, marks, achievements, competition, comp_result, final_remarks])

def write_updated_data_to_csv_file(filename, data):
    with open(filename, 'w', newline="") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

def read_csv_file(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
    return data

def main():
    filen = input('Enter the name of the CSV file: ')
    filename = filen + '.csv'

    with open(filename, 'a+'):
        pass

    blockchain = Blockchain()
    for_ui(filename, blockchain)

if __name__ == '__main__':
    main()

