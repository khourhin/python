import sqlite3

# Initiate the db
conn = sqlite3.connect('demo_data/example.db')
c = conn.cursor()

# Feed the db
c.execute('CREATE TABLE pup (position int, nreads int)')
with open('demo_data/toindex.txt') as f:
    for line in f:
        c.execute('INSERT INTO pup VALUES ({0}, {1})'.format(line.split()[0],
                                                              line.split()[1]))
conn.commit()

# Query the db
c.execute('SELECT * FROM pup WHERE position > 102')
print(c.fetchall())

conn.close()

