import sqlite3

def getdb():
    try:
        conn = sqlite3.conect("phonebook_project/phonebook_database.db")
        cursor = conn.currsor
        return cursor
    except:
        return False

def getBusinesses():
    #connects to db
    db = getdb()
    #specify query
    query = "SELECT business_name, business_category, postcode, telephone FROM business"
    db.execute(query)
    results = db.fetchall()
    
    '''function to return details of all business in the db. the table should contain...'''
    
    return results

def 