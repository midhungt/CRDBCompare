import psycopg2
import sys

import re

def validate_inputs(hostname, port, username, database):
    """Validate the user's input values."""
    # Check if any fields are empty
    if not all([hostname, port, username, database]):
        raise ValueError("All fields are required.")

    # Check if the port number is valid
    if not re.match(r"^\d{1,5}$", port):
        raise ValueError("Invalid port number.")

    # Check if the username and password are valid
    if not re.match(r"^[a-zA-Z0-9_-]{1,30}$", username):
        raise ValueError("Invalid username.")
        
    # Check if the database name is valid
    if not re.match(r"^[a-zA-Z0-9_-]{1,30}$", database):
        raise ValueError("Invalid database name.")
    
validate_inputs(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[5])
# establish connection to the first database
conn1 = psycopg2.connect(
    host=sys.argv[1],
    port=sys.argv[2],
    user=sys.argv[3],
    password=sys.argv[4],
    database=sys.argv[5]
)

# establish connection to the second database
conn2 = psycopg2.connect(
    host="localhost",
    port="26257",
    database="test2",
    user="root",
    password="password2"
)

# create a cursor object for each connection
cur1 = conn1.cursor()
cur2 = conn2.cursor()

# retrieve schema information from the first database
cur1.execute("SELECT table_name, column_name, data_type FROM information_schema.columns where table_schema='public';")
schema1 = cur1.fetchall()

# retrieve schema information from the second database
cur2.execute("SELECT table_name, column_name, data_type FROM information_schema.columns where table_schema='public';")
schema2 = cur2.fetchall()

# print the schema information for each database
print("Schema information for database 1:")
print(schema1)
print("Schema information for database 2:")
print(schema2)

#def compare_indexes_constraints(db1_conn, db2_conn):
#    db1_cur = db1_conn.cursor()
#    db2_cur = db2_conn.cursor()
#
#    # Retrieve table names from both databases
#    db1_cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'test_schema1'")
#    db2_cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'test_schema2'")
#    db1_tables = [row[0] for row in db1_cur.fetchall()]
#    db2_tables = [row[0] for row in db2_cur.fetchall()]
#
#    # Compare indexes and constraints for each table
#    for table_name in set(db1_tables + db2_tables):
#        db1_cur.execute("SELECT indexdef FROM pg_indexes WHERE tablename = %s", (table_name,))
#        db2_cur.execute("SELECT indexdef FROM pg_indexes WHERE tablename = %s", (table_name,))
#        db1_indexes = set([row[0] for row in db1_cur.fetchall()])
#        db2_indexes = set([row[0] for row in db2_cur.fetchall()])
#        if db1_indexes != db2_indexes:
#            print(f"Index differences for table {table_name}:")
#            print(f"In {db1_conn.dsn}: {db1_indexes - db2_indexes}")
#            print(f"In {db2_conn.dsn}: {db2_indexes - db1_indexes}")
#
#        db1_cur.execute("SELECT conname, condeferrable, contype, convalidated FROM pg_constraint WHERE conrelid = %s::regclass", (table_name,))
#        db2_cur.execute("SELECT conname, condeferrable, contype, convalidated FROM pg_constraint WHERE conrelid = %s::regclass", (table_name,))
#        db1_constraints = set([row for row in db1_cur.fetchall()])
#        db2_constraints = set([row for row in db2_cur.fetchall()])
#        if db1_constraints != db2_constraints:
#            print(f"Constraint differences for table {table_name}:")
#            print(f"In {db1_conn.dsn}: {db1_constraints - db2_constraints}")
#            print(f"In {db2_conn.dsn}: {db2_constraints - db1_constraints}")
#
#    db1_cur.close()
#    db2_cur.close()
#
#    #compare_indexes_constraints(conn1, conn2)
def compare_indexes(conn1, conn2):

    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()
    
    cursor1.execute("SELECT table_name, index_name,column_name,null FROM information_schema.statistics WHERE table_schema='public' ORDER BY table_name, index_name,column_name")
    cursor2.execute("SELECT table_name, index_name,column_name,null FROM information_schema.statistics WHERE table_schema='public' ORDER BY table_name, index_name,column_name")
    
    rows1 = cursor1.fetchall()
    rows2 = cursor2.fetchall()
    
    index_diff = []
    
    for i in range(len(rows1)):
        if rows1[i] != rows2[i]:
            index_diff.append(f"Table: {rows1[i][0]}, Index: {rows1[i][1]}")
            index_diff.append(f"Database 1: {rows1[i][2]}, {rows1[i][3]}")
            index_diff.append(f"Database 2: {rows2[i][2]}, {rows2[i][3]}")
            
    if index_diff:
        print("The following index differences were found:")
        for diff in index_diff:
            print(diff)
    else:
        print("No index differences found.")
        
    conn1.close()
    conn2.close()

compare_indexes(conn1,conn2)