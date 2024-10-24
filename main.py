from json_reader import read_json_file
from csv_reader import read_csv_file
from databse import connect_to_db, create_tables, insert_database, insert_user, get_high_classification
import os

def main():

    # Database connection parameters
    dbname = os.environ.get('POSTGRES_NAME', default='postgres')
    user =  os.environ.get('POSTGRES_USER', default='postgres')
    password = os.environ.get('POSTGRES_PASSWORD', default='postgres')
    # Connect to the database
    conn = connect_to_db(dbname, user, password)

    if conn == None:
        exit(1)

    create_tables(conn)

    # Read and process CSV data
    csv_data = read_csv_file('users.csv')

    if csv_data:
        for row in csv_data:
            is_active = row['user_state'] == 'active'
            insert_user(conn, row['user_id'], is_active, row['user_manager'], row['email'])
            print(f"Email: {row['email']}")
            print("-" * 40)

    # Read and process JSON data
    json_data = read_json_file('clasification.json')

    if json_data:
        for record in json_data:
            insert_database(conn, record['database_name'], record['classification'], record['owner_id'])
            print(f"Database Name: {record['database_name']}")
            print("-" * 40)

    high_classifications = get_high_classification(conn)

    # Output the results
    for row in high_classifications:
        print(row[-1])

    
    #TODO: for each record send and email
        #TODO: Create send email function

    
    
    conn.close()

if __name__ == '__main__':
    main()
