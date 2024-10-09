import pymysql
import os
 
# Database connection
connection = pymysql.connect(
    host=os.getenv('DB_HOST'),         
    user=os.getenv('DB_USER'),          
    password=os.getenv('DB_PASSWORD'),  
    database=os.getenv('DB_NAME')
)
 
cursor = connection.cursor()
 
# Open and execute the SQL script
with open('update_companydb_schema.sql', 'r') as file:
    sql_script = file.read()
    sql_commands = sql_script.split(';')
    for command in sql_commands:
        if command.strip():
            cursor.execute(command)
 
connection.commit()
cursor.close()
connection.close()
 
print("completed")
