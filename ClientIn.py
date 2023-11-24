import psycopg2
import psycopg2.extras


class ClientIn:
    def __init__(self, firstname, lastname, age, gender, id=None):
        assert isinstance(firstname, str), "firstName has to be a string"
        assert isinstance(lastname, str), "lastName has to be a string"
        assert isinstance(age, int), "age has to be an integer"
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.__id = id
        
    @staticmethod
    def __connect():
        conn = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "root",
            database = "bankapp"
        )
        return conn
    
    def add_user(self):         
        conn = self.__connect()
        with conn:
            with conn.cursor(cursor_factory= psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("""INSERT INTO clients (firstname, lastname, age, gender)
                                VALUES (%s, %s, %s, %s)""", (self.firstname, self.lastname, self.age, self.gender))
                except Exception as e:
                    print("Problem accessing database ...")
                    print(e)
        conn.close()
        print("welcome to bankapp.")

    @classmethod
    def get_user_by_Id(cls, id):
        conn = psycopg2.connect(
                host = "localhost",
                port = "5432",
                user = "postgres",
                password = "root",
                database = "bankapp"
            )
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("SELECT * FROM clients WHERE id = %s;", (id,))
                    client = cur.fetchone()
                    if not client:
                        return None
                    return ClientIn(**client)
                except Exception as e:
                    print(f"Server Problem: {e}")

    def __repr__(self) -> str:
        return self.firstname + " " + self.lastname + " " + str(self.age) + " y.o " + self.gender

