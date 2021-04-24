
from functools import partial
import sqlite3


#Class for database storage
class DatabaseStorage(): 
    def __init__(self): 
        self.first_name = "" 
        self.last_name = "" 
        self.email = "" 
        self.complaint = "" 
        self.num_upvotes= ""

    #creates the database, adds info to it, saves it
    def submit(self): 
        #connect to the database 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor 
        c.execute("INSERT INTO complaints VALUES (:id, :first, :last, :email, :complaint, :upvotes)", 
            {'id':hash(self.complaint),
             'first':self.first_name, 
             'last':self.last_name,
             'email':self.email,
             'complaint':self.complaint,
             'upvotes':self.num_upvotes
            }    
        )
        conn.commit() 
        conn.close() 

    #access information from the database using dicts
    def query(self):
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor 
        c.execute("SELECT * oid FROM complaints")
        records = c.fetchall()

        query_table = {} 
        for record in records:
            key = record[0]
            value = (record[4], record[5])
            query_table[key] = value 
        
        conn.commit()
        conn.close()
        
        return query_table

    #delete a specific complaint from the database
    def delete(self, deletion): 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor
        c.execute("DELETE from complaints WHERE self.complaint="+deletion)
        conn.commit()
        conn.close 
