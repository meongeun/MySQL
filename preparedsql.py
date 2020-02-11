import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

host_name = "SYSPHARM"
username = "root"
password = "1111"
database_name = "practice"
cnx = mysql.connector.connect(host=host_name, user=username, password=password, database=database_name, use_pure=True)

curprep = cnx.cursor(cursor_class=MySQLCursorPrepared)
#cursor = cnx.cursor(prepared=True)
cur = cnx.cursor()

prepstmt = "INSERT INTO ex1 (name) VALUES (%s)"

    # Preparing the statement is done only once. It can be done before
    # without data, or later with data.
#curprep.execute(prepstmt, ('Geert'),)

#prepstmt = prepstmt.format(cnx.db_scan_table)
#cur.execute(prepstmt, ('Geert'),)

    # Insert 3 records
names = ('Geert', 'Jan', 'Michel')
for name in names:
    curprep.execute(prepstmt, (name,))
    cnx.commit()


#stmt = "SELECT * FROM ex1 WHERE age = %s" # (1)
#curprep.execute(stmt, (5,))                            # (2)
# ... fetch data ...
#curperp.execute(stmt, (10,))  
cnx.close()
 
