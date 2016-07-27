#! /usr/bin/python

import sqlite3
import sys

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('CREATE TABLE projects (pid INTEGER PRIMARY KEY AUTOINCREMENT, pname TEXT )')
c.execute('INSERT INTO projects (pname) VALUES("test")')
c.execute('CREATE TABLE jobs (pid, jid INTEGER PRIMARY KEY AUTOINCREMENT, jname, date)')

c.execute('CREATE TABLE annots (jid, seqid, genecode, EC, GOs, KEGGs)')
c.execute('INSERT INTO annots(seqid, GOs) VALUES("seq1", "GOtest")')

conn.commit()
conn.close()

#-------------------------------------------------------------------------------
def load_b2go(b2go_f, jid):

    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    with open(b2go_f) as f:
        for line in f:
            seqid = line.split()[0]
            go = line.split()[1]

            c.execute('INSERT INTO annots(seqid, GOs) VALUES(?, ?)', (seqid, go))

    conn.commit()
    conn.close()

#-------------------------------------------------------------------------------
if __name__ == "__main__":

    load_b2go(sys.argv[1], 1)
