OGC Sec. School Data Base Credentials
user="avnadmin",              
password="AVNS_blUS8t5v_YlvF0J_omz",         
host="pg-353bb115-adeitanemmanuel086-380.h.aivencloud.com",            
port="26014",                  
database="defaultdb",    
sslmode="require"

1. Accessing  Aiven Cloud PostgreSQL via Python
!pip install psycopg2
import psycopg2

try:
    # Replace these with your actual Aiven credentials
    connection = psycopg2.connect(
        user="your_aiven_username",
        password="your_aiven_password",
        host="your_aiven_hostname",  # e.g., pg-12345.aivencloud.com
        port="your_aiven_port",      # e.g., 21061
        database="your_aiven_database_name",
        sslmode="require"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students;")  # Example query
    results = cursor.fetchall()
    for row in results:
        print(row)

except Exception as error:
    print(f"Error occurred: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()



2. Accessing Aiven Cloud PostgreSQL via PGAdmin
PGAdmin needs to connect to your Aiven PostgreSQL instance using the provided credentials.

Add a New Server:
Open PGAdmin and right-click on "Servers" in the Object Browser and select "Create" > "Server".
Enter Connection Details:
Name: Give it a name like "Aiven PostgreSQL".
Host: Use the hostname from Aiven, e.g., pg-12345.aivencloud.com.
Port: The port from Aiven, e.g., 21061.
Maintenance DB: Your Aiven database_name.
Username: The Aiven username.
Password: The Aiven password.
SSL Configuration:
Go to the SSL tab and set SSL Mode to require.
Save the connection, and you should be able to browse the database schema and run queries using PGAdmin.


3. Accessing Aiven Cloud PostgreSQL via Power BI
Steps to Connect Aiven PostgreSQL to Power BI:
Open Power BI Desktop.
Connect to PostgreSQL:
Click on Get Data > PostgreSQL.
If this is the first time you're connecting to PostgreSQL from Power BI, you may need to install the PostgreSQL connector. Power BI will prompt you to install it.
Enter Connection Details:
Server: Your Aiven hostname and port in the format pg-12345.aivencloud.com:21061.
Database: Your Aiven database name.
Credentials:
Power BI will ask for the PostgreSQL username and password. Enter the Aiven credentials.
SSL Configuration:
Power BI will also prompt for SSL configuration. Set SSL mode to require as Aiven requires secure connections.
Select Tables:
Once connected, Power BI will show the available tables. The user can now choose the tables and fields for visualization.