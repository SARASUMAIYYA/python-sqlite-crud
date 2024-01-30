# python-sqlite-crud
Python SQLite CRUD Operations This Python script allows users to perform CRUD (Create, Read, Update, Delete) operations on a SQLite database containing user registration information. The 'Registration' table is used to store records with fields like ID, Name, Email, and Date of Birth.

Options:
Create Record:

Choice: 1
Prompt: Enter Name, Email, and Date of Birth to create a new record.
Behavior:
If the record is successfully created, the script prints "Record created successfully."
If there's an error creating the record, it prints an error message.
Read Records:

Choice: 2
Prompt: No additional input required.
Behavior:
Fetches all records from the 'Registration' table and prints them.
If there's an error reading records, it prints an error message.
Update Record:

Choice: 3
Prompt: Enter Record ID to update, and then provide the new Name, Email, and Date of Birth.
Behavior:
If the record with the specified ID is found and updated, it prints "Record updated successfully."
If the record is not found, it prints "Record not found."
If there's an error updating the record, it prints an error message.
Delete Record:

Choice: 4
Prompt: Enter Record ID to delete.
Behavior:
If the record with the specified ID is found and deleted, it prints "Record deleted successfully."
If the record is not found, it prints "Record not found."
If there's an error deleting the record, it prints an error message.
Exit:

Choice: 5
Prompt: No additional input required.
Behavior:
Exits the program with the message "Exiting program."
Record ID Handling:
When updating or deleting a record, the script prompts the user to enter the Record ID.
If the provided Record ID is not found in the database, the script prints "Record not found."
Error Handling:
If there's an error during any operation (creating, reading, updating, or deleting records), the script prints an error message.
Usage:
Run the script using python registration.py.
Follow the prompts to perform CRUD operations interactively.


Use viusal studio code

Steps:

#Installation

Python

SQL Lite

SQL Lite Viewer( for viewing database)

Clone repository

 Run the following command in the terminal
 
 python registration.py



