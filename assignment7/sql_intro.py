import sqlite3

try:
    # Connect to the database
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database magazines.db connected successfully.")

        # Enable foreign key constraint support
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Create publishers table
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS publishers (
                    publisher_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE
                );
            """)
            print("Table 'publishers' created.")
        except sqlite3.Error as e:
            print("Error creating 'publishers':", e)

        # Create magazines table
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS magazines (
                    magazine_id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL UNIQUE,
                    publisher_id INTEGER NOT NULL,
                    FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
                );
            """)
            print("Table 'magazines' created.")
        except sqlite3.Error as e:
            print("Error creating 'magazines':", e)

        # Create subscribers table
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS subscribers (
                    subscriber_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL
                );
            """)
            print("Table 'subscribers' created.")
        except sqlite3.Error as e:
            print("Error creating 'subscribers':", e)

        # Create subscriptions table
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS subscriptions (
                    subscription_id INTEGER PRIMARY KEY,
                    subscriber_id INTEGER NOT NULL,
                    magazine_id INTEGER NOT NULL,
                    expiration_date TEXT NOT NULL,
                    FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
                    FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
                );
            """)
            print("Table 'subscriptions' created.")
        except sqlite3.Error as e:
            print("Error creating 'subscriptions':", e)
# === FUNCTIONS ===

    def add_publisher(cursor, name):
        try:
            cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        except sqlite3.IntegrityError:
            print(f"Publisher '{name}' already exists.")

    def add_magazine(cursor, title, publisher_name):
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        result = cursor.fetchone()
        if result:
            publisher_id = result[0]
            try:
                cursor.execute("INSERT INTO magazines (title, publisher_id) VALUES (?, ?)", (title, publisher_id))
            except sqlite3.IntegrityError:
                print(f"Magazine '{title}' already exists.")
        else:
            print(f"Publisher '{publisher_name}' not found.")

    def add_subscriber(cursor, name, address):
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone():
            print(f"Subscriber '{name}' at '{address}' already exists.")
        else:
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))

    def add_subscription(cursor, subscriber_name, magazine_title, expiration_date):
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,))
        sub = cursor.fetchone()
        cursor.execute("SELECT magazine_id FROM magazines WHERE title = ?", (magazine_title,))
        mag = cursor.fetchone()

        if not sub:
            print(f"Subscriber '{subscriber_name}' not found.")
            return
        if not mag:
            print(f"Magazine '{magazine_title}' not found.")
            return

        subscriber_id = sub[0]
        magazine_id = mag[0]

        cursor.execute("""
            SELECT * FROM subscriptions 
            WHERE subscriber_id = ? AND magazine_id = ?
        """, (subscriber_id, magazine_id))
        if cursor.fetchone():
            print(f"Subscription already exists for '{subscriber_name}' to '{magazine_title}'.")
        else:
            cursor.execute("""
                INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
                VALUES (?, ?, ?)
            """, (subscriber_id, magazine_id, expiration_date))

    # === INSERT SAMPLE DATA ===

    # Publishers
    add_publisher(cursor, "TechMedia")
    add_publisher(cursor, "Global Press")
    add_publisher(cursor, "ScienceWorld")

    # Magazines
    add_magazine(cursor, "Tech Today", "TechMedia")
    add_magazine(cursor, "World News", "Global Press")
    add_magazine(cursor, "Discover Science", "ScienceWorld")

    # Subscribers
    add_subscriber(cursor, "Alice Smith", "123 Maple Street")
    add_subscriber(cursor, "Bob Johnson", "456 Oak Avenue")
    add_subscriber(cursor, "Carol White", "789 Pine Road")

    # Subscriptions
    add_subscription(cursor, "Alice Smith", "Tech Today", "2025-12-31")
    add_subscription(cursor, "Alice Smith", "World News", "2025-10-01")
    add_subscription(cursor, "Bob Johnson", "Discover Science", "2025-09-15")

    # Commit changes
    conn.commit()
    print("Sample data inserted successfully.")

     # === SQL Queries ===
    print("\nAll subscribers:")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    print("\nMagazines sorted by title:")
    cursor.execute("SELECT * FROM magazines ORDER BY title")
    for row in cursor.fetchall():
        print(row)

    print("\nMagazines published by TechMedia:")
    cursor.execute("""
        SELECT m.title
        FROM magazines m
        JOIN publishers p ON m.publisher_id = p.publisher_id
        WHERE p.name = 'TechMedia'
    """)
    for row in cursor.fetchall():
        print(row)
 
except sqlite3.Error as e:
    print("An error occurred while connecting to the database:", e)
