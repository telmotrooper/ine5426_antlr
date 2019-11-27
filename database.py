import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('test.db')

# Create table
conn.execute('''
CREATE TABLE IF NOT EXISTS symbols
(id INTEGER, line INTEGER, column INTEGER, token TEXT, lexeme TEXT, scope TEXT)
''')
