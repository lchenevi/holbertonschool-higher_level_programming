#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Extract MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select all states from the states table and sort by id in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows in a list of tuples
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Disconnect from server
    db.close()
