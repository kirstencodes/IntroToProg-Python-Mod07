# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with exceptions and the pickle module
# ChangeLog (Who,When,What):
# KElghoroury, 3.1.2021, Created script
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
import pickle
filename = "JournalEntries.txt"

# Functions ---------------------------------------------------------------------- #
def journal_entry():
    new_date = input("Date: ")
    if new_date.lower() == 'exit':
        exit()
    new_entry = input("Write your new journal entry here: ")
    new_journal_entry = [new_date, new_entry]
    return new_journal_entry

def write_data_to_file(file_name, new_journal_entry):
    file = open(file_name, "ab")
    pickle.dump(new_journal_entry, file)
    file.close()

def read_data_from_file(file_name):
    file = open(file_name, "rb")
    existing_journal = []
    while(True):
        try:
            existing_journal.append(pickle.load(file))
        except EOFError:
            break
    file.close()
    return existing_journal

# Main ---------------------------------------------------------------------- #
print("Welcome to your digital journal! Type 'exit' in 'Date:' to exit the program." + "\n")
print("Your existing journal entries are: " + "\n")
existing_journal = read_data_from_file(filename)
print(existing_journal)

while(True):
    new_journal_entry = journal_entry()
    write_data_to_file(filename, new_journal_entry)