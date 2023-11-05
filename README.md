# APAAR Link: A Blockchain-based Student Record System

APAAR Link is an innovative project that leverages blockchain technology to store and manage student records securely and efficiently. It provides a user-friendly graphical user interface (GUI) using tkinter, 
a Python library for creating GUIs. The records include various information such as APAAR ID, name, class, marks, achievements, competition, and remarks. APAAR ID is a unique 12-digit identification number that tracks 
students’ academic journey and achievements. APAAR is the new Indian standard for student record management, as per the National Education Policy (NEP) 2020. We have implemented Apaar using a simple and elegant 
interface in Python, a popular and versatile programming language. We have also planned to add more features and functionalities to APAAR Link in the future.


# Modules

1. CSV Module: The csv module in Python is used for reading and writing data to CSV files1. It provides functionality to both read from and write data to CSV files. The csv.reader and csv.writer objects read and write sequences. Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes.

2. Tkinter Module: Tkinter is the standard Python interface to the Tk GUI toolkit. It provides a powerful object-oriented interface to the Tk GUI toolkit. It includes support for a variety of widgets (e.g., buttons, labels) and events (e.g., button clicks), and it allows you to create complex GUIs with a lot of functionality.

3. Datetime Module: The datetime module in Python is used for dealing with real dates and times. It provides classes for manipulating dates and times in both simple and complex ways. The datetime module includes functions to parse strings representing dates and times as well as to format dates and times as strings.

4. Hashlib Module: The hashlib module in Python provides a uniform interface to many different secure hash and message digest algorithms5. It includes secure hash algorithms like SHA1, SHA224, SHA256, SHA384, SHA512, and others. It’s used for creating fixed size irreversible hash strings from input data of any size.

5. Multiprocessing Module: The multiprocessing module in Python is a powerful tool that allows you to create multiple processes. It offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. This module also introduces APIs which do not have analogs in the threading module, like the Pool object, which offers a convenient means of parallelizing the execution of a function across multiple input values


# Technicalities

1. **Python Programming**: The code is written in Python, a high-level, interpreted programming language known for its readability and versatility.

2. **Tkinter GUI**: The tkinter library is used to create the graphical user interface (GUI). The ttk module, which stands for Themed Tkinter, is also imported to provide access to the Tk themed widget set.

3. **CSV File Handling**: The csv module is imported, indicating that the program interacts with a CSV file. The functions `write_new_data_to_csv_file`, `read_csv_file`, and `write_updated_data_to_csv_file` are used to write new data, read existing data, and update existing data in the CSV file, respectively.

4. **Data Entry**: The `submit_data` function retrieves data from the GUI’s entry fields, writes this data to a CSV file, clears the fields, and then displays the updated data.

5. **Data Display**: The `display_data` function reads data from the CSV file and displays it in a tree view.

6. **Data Search**: The `search_data` function prompts the user to enter an Apaar ID to search for. The `display_search_results` function then displays any matching results.

7. **Data Update**: The `update_record` function prompts the user to enter an Apaar ID to update. The `update_data_window` function creates a new window for updating records.

8. **Data Deletion**: The `delete_record` function prompts the user to enter an Apaar ID to delete. The `delete_data` function then deletes the corresponding record from the CSV file and updates the display. The `delete_all_data` function deletes all data from the CSV file after confirming with the user.

9. **Program Exit**: The `exit_program` function destroys the root window, effectively closing the program.

10. **Tkinter Variables**: StringVar objects are created for each data attribute. These objects are used to get and set the values of the entry fields in the GUI.

11. **Execution Entry Point**: The `if __name__ == '__main__':` line is the execution entry point of the program. When the script is run directly (not imported), the `main` function is called.

12. **CSV Header**: The program prompts the user to indicate whether the CSV file already has a header. If the user indicates that it does not, the program writes a header to the file.

13. **Blockchain**: The `Block` and `Blockchain` classes are used to create a simple blockchain for storing the Apaar IDs. The `Block` class includes methods for calculating the hash of a block and mining a block. The `Blockchain` class includes methods for creating the genesis block, adding a block to the chain, and getting the latest block.

14. **UI Function Call**: The `for_ui` function is called with `filename` as an argument. This function creates and runs the GUI for the program.


Author: © Nirmal Bhartia School, 2023
