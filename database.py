import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('test.db')

# Create table
# conn.execute('''
# CREATE TABLE IF NOT EXISTS symbols
# (id INTEGER, line INTEGER, column INTEGER, token TEXT, lexeme TEXT, scope TEXT)
# ''')

def setScope(lexeme, scope):
  conn.execute(f'''
  UPDATE symbols SET scope = {scope} WHERE id = (SELECT id FROM symbols WHERE lexeme = '{lexeme}' AND scope IS NULL LIMIT 1)
  ''')
  conn.commit()

def checkForScopeError(lexeme, scope):
  c = conn.cursor()
  c.execute(f'''SELECT COUNT(id) FROM symbols WHERE lexeme = '{lexeme}' AND scope = {scope}''')
  if c.fetchone()[0] > 1:
    return True
  return False
