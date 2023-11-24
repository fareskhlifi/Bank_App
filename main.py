import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    host = "localhost",
    port = "5432",
    user = "postgres",
    password = "root",
    database = "bankapp"
)

with conn:
    with conn.cursor(cursor_factory= psycopg2.extras.DictCursor) as cur:
        cur.execute("""CREATE TABLE clients (id SERIAL PRIMARY KEY,
                    firstname VARCHAR NOT NULL,
                    lastname VARCHAR NOT NULL,
                    age INTEGER NOT NULL,
                    gender VARCHAR);
                    """
                    )
        cur.execute("""CREATE TABLE accounts (id SERIAL PRIMARY KEY,
                    client_id INT NOT NULL,
                    balance FLOAT NOT NULL,
                    FOREIGN KEY (client_id) REFERENCES clients(id));
                    """
                    )  
conn.close()