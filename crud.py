import sqlite3

# Підключення до бази даних SQLite (або створення нової, якщо вона не існує)
conn = sqlite3.connect('CRUDdatabase.db')
cursor = conn.cursor()

# Створення таблиці
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER)''')
conn.commit()

# CRUD операції

# Create (створення запису)
def create_user(name, age):
    cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()
    print(f'User {name} added successfully.')

# Read (читання запису)
def read_users():
    cursor.execute('''SELECT * FROM users''')
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f'ID: {row[0]}, Name: {row[1]}, Age: {row[2]}')
    else:
        print('No users found.')

# Update (оновлення запису)
def update_user(user_id, new_name, new_age):
    cursor.execute('''UPDATE users SET name=?, age=? WHERE id=?''', (new_name, new_age, user_id))
    conn.commit()
    print(f'User with ID {user_id} updated successfully.')

# Delete (видалення запису)
def delete_user(user_id):
    cursor.execute('''DELETE FROM users WHERE id=?''', (user_id,))
    conn.commit()
    print(f'User with ID {user_id} deleted successfully.')

# Приклад використання CRUD операцій
if __name__ == '__main__':
    # Create
    create_user('Alice', 30)
    create_user('Bob', 25)

    # Read
    print('\nCurrent users:')
    read_users()

    # Update
    update_user(1, 'Alice Smith', 31)

    # Read updated users
    print('\nUpdated users:')
    read_users()

    # Delete
    delete_user(2)

    # Read remaining users
    print('\nUsers after deletion:')
    read_users()

# Закриття з'єднання з базою даних SQLite
conn.close()
