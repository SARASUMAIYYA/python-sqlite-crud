CREATE TABLE IF NOT EXISTS Registration (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    DateOfBirth DATE,
    PhoneNumber TEXT
);
