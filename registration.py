import sqlite3

class RegistrationDB:
    def __init__(self, db_file='registration.db'):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Registration (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT NOT NULL,
                DateOfBirth DATE
            )
        ''')
        self.conn.commit()
        print("Table created successfully.")

    def create_record(self, name, email, dob):
        try:
            self.cursor.execute('''
                INSERT INTO Registration (Name, Email, DateOfBirth)
                VALUES (?, ?, ?)
            ''', (name, email, dob))
            self.conn.commit()
            print("Record created successfully.")
        except Exception as e:
            print(f"Error creating record: {e}")

    def read_records(self):
        try:
            self.cursor.execute('SELECT * FROM Registration')
            records = self.cursor.fetchall()
            return records
        except Exception as e:
            print(f"Error reading records: {e}")
            return None

    def update_record(self, record_id, new_name, new_email, new_dob):
        try:
            self.cursor.execute('''
                UPDATE Registration
                SET Name=?, Email=?, DateOfBirth=?
                WHERE ID=?
            ''', (new_name, new_email, new_dob, record_id))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("Record updated successfully.")
            else:
                print("Record not found.")
        except Exception as e:
            print(f"Error updating record: {e}")

    def delete_record(self, record_id):
        try:
            self.cursor.execute('DELETE FROM Registration WHERE ID=?', (record_id,))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("Record deleted successfully.")
            else:
                print("Record not found.")
        except Exception as e:
            print(f"Error deleting record: {e}")

# Main program
def main():
    db = RegistrationDB()

    while True:
        print("\nOptions:")
        print("1. Create Record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            db.create_record(name, email, dob)

        elif choice == '2':
            records = db.read_records()
            print("Records:", records)

        elif choice == '3':
            record_id = input("Enter Record ID to update: ")
            new_name = input("Enter New Name: ")
            new_email = input("Enter New Email: ")
            new_dob = input("Enter New Date of Birth (YYYY-MM-DD): ")
            db.update_record(record_id, new_name, new_email, new_dob)

        elif choice == '4':
            record_id = input("Enter Record ID to delete: ")
            db.delete_record(record_id)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
