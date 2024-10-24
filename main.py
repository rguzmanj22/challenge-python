from json_reader import read_json_file
from csv_reader import read_csv_file
from databse import connect_to_db, create_tables, insert_database, insert_user, get_user_by_id
import os

def main():

    # Database connection parameters
    dbname = os.environ.get('POSTGRES_NAME', default='postgres')
    user =  os.environ.get('POSTGRES_USER', default='postgres')
    password = os.environ.get('POSTGRES_PASSWORD', default='postgres')
    # Connect to the database
    print("dbname, user, password", dbname, user, password)
    conn = connect_to_db(dbname, user, password)

    if conn == None:
        exit(1)

    create_tables(conn)

    # Read and process CSV data
    csv_data = read_csv_file('users.csv')

    if csv_data:
        print("CSV Data:")
        for row in csv_data:
            is_active = row['user_state'] == 'active'
            insert_user(conn, row['user_id'], is_active, row['user_manager'], row['email'])
            print(f"Row ID: {row['row_id']}")
            print(f"Email: {row['email']}")
            print("-" * 40)

    # Read and process JSON data
    json_data = read_json_file('databases.json')

    if json_data:
        print("JSON Data:")
        for record in json_data:
            insert_database(conn, record['database_name'], record['classification'], record['owner_id'])
            print(f"ID: {record['id']}")
            print(f"Database Name: {record['database_name']}")
            print("-" * 40)

    #TODO: Update database CSV with low, medium and high values
    #TODO: get all databases with high classification
    #TODO: for each record send and email
        #TODO: Create send email function

    
    if conn:
        # Create tables
        

        # Insert a user
        #

        # Retrieve a user by ID
        #user = get_user_by_id(conn, 'user123')
        #print(f"Retrieved user: {user}")

        # Insert a database entry
        #insert_database(conn, 'Supplier Information', 'Confidential', 1)

        # Close the connection
        conn.close()

if __name__ == '__main__':
    main()
