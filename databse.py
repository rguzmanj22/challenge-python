import pg8000

def connect_to_db(dbname='postgres', user='postgres', password='postgres', host='localhost', port=5432):
    """
    Connect to the PostgreSQL database.
    """
    try:
        conn = pg8000.connect(database=dbname, user=user, password=password, host=host, port=port) 
        print("Connection successful")
        return conn
    except pg8000.ProgrammingError as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_tables(conn):
    """
    Create Users and Databases tables if they do not exist.
    """
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            user_id VARCHAR(50) NOT NULL UNIQUE,
            active BOOLEAN NOT NULL,
            user_manager_id VARCHAR(50),
            email VARCHAR(100) NOT NULL
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Classifications (
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL UNIQUE,
            classification VARCHAR NOT NULL,
            owner_id VARCHAR(50)
        );
    ''')
    
    conn.commit()
    print("Tables created successfully")

    

def insert_user(conn, user_id, active, user_manager_id, email):
    """
    Insert a new user into the Users table.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Users (user_id, active, user_manager_id, email)
            VALUES (%s, %s, %s, %s);
        ''', (user_id, active, user_manager_id, email))
        conn.commit()
        print("User inserted successfully")
    except:
        conn.rollback()
        print("Users already exists")

def insert_classification(conn, name, classification, owner_id):
    """
    Insert a new classification entry into the Classifications table.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Classifications (name, classification, owner_id)
            VALUES (%s, %s, %s);
        ''', (name, classification, owner_id))
        conn.commit()
        print("Classification inserted successfully")
    except:
        conn.rollback()
        print("Classification already exists")

def get_high_classification(conn):

    try: 
        cursor = conn.cursor()

        query = """
        SELECT db.id, db.name, db.classification, u.user_id as owner_id, u2.user_id as manager_id, u2.email as manager_email
        FROM classifications AS db
        INNER JOIN users AS u
        ON db.owner_id = u.user_id
        INNER JOIN users AS u2
        ON u.user_manager_id = u2.user_id
        WHERE db.classification = 'high';
        """

        cursor.execute(query)

        results = cursor.fetchall()
        return results
    except:
        print("error getting high classifications")
        return None

