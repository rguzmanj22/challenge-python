from json_reader import read_json_file
from csv_reader import read_csv_file
from databse import connect_to_db, create_tables, insert_classification, insert_user, get_high_classification
from sednmail import send_email
import os

def main():

    # Database connection parameters
    dbname = os.environ.get('POSTGRES_NAME', default='postgres')
    user =  os.environ.get('POSTGRES_USER', default='postgres')
    password = os.environ.get('POSTGRES_PASSWORD', default='postgres')

    # Variables E-mail
    apikey = os.environ.get('MAILGUN_APIKEY')
    domain= os.environ.get('MAILGUN_DOMAIN')
    sender_email= os.environ.get('MAILGUN_SENDER_EMAIL')
    
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
            insert_classification(conn, record['database_name'], record['classification'], record['owner_id'])
            print(f"Database Name: {record['database_name']}")
            print("-" * 40)

    high_classifications = get_high_classification(conn)
    conn.close()
    
    if high_classifications:
        subject = "Solicitud Revalida Base de Datos"
        for row in high_classifications:
            to_email=row[-1]
            dbname=row[1]
            body = "Cordial saludo, solicitamos su confirmación de la clasificación de la siguiente base de datos %s con clasificación alta-high" % (dbname)
            send_email(apikey,domain,sender_email,to_email,subject,body)
            print("Email sent successfully!", to_email, dbname)
        

if __name__ == '__main__':
    main()
