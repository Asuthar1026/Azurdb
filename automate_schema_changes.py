import pymysql

# Create the database connection directly
connection = pymysql.connect(
    host='astha-db.mysql.database.azure.com',  
    user='root_astha',  
    password='Secret55',  
    database='db1'
)

# Path to the SQL file
script_path = 'update_projects_sigma.sql'

# Read the SQL script from the file
with open(script_path, 'r') as file:
    sql_script = file.read()

# Create a cursor object to execute SQL queries
cursor = connection.cursor()  

# Execute each SQL statement individually (split by semicolon)
for statement in sql_script.split(';'):
    if statement.strip():  # Execute only non-empty statements
        cursor.execute(statement)

connection.commit()  # Commit all changes at once
cursor.close()  # Close the cursor
connection.close()  # Close the connection

print("Execution completed successfully")
