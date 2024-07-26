import sqlite3

# Connect to the database
conn = sqlite3.connect('user_agent.sqlite')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE users (
        user_agent TEXT PRIMARY KEY NOT NULL,
        
        browser_family TEXT,
        browser_major TEXT,
        browser_minor TEXT,
        browser_patch TEXT,
        
        os_family TEXT,
        os_major TEXT,
        os_minor TEXT,
        os_patch TEXT,
        os_patch_minor TEXT,
        
        device_family TEXT,
        device_brand TEXT,
        device_model TEXT,
    )
''')

# Insert some data
cursor.execute("INSERT INTO users (name, email) VALUES ('Jane Doe', 'jane@example.com')")

# Commit the changes
conn.commit()

# Retrieve the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()