import psycopg2
import psycopg2.extras


class ClientIn:
    def __init__(self, firstName, lastName, age, gender):
        assert isinstance(firstName, str), "firstName has to be a string"
        assert isinstance(lastName, str), "lastName has to be a string"
        assert isinstance(age, int), "age has to be an integer"
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender
        
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
                    cur.execute("""INSERT INTO clients (firstName, lastName, age, gender)
                                VALUES (%s, %s, %s, %s)""", (self.firstName, self.lastName, self.age, self.gender))
                except Exception as e:
                    print("Problem accessing database ...")
                    print(e)
        conn.close()
        print("welcome to bankapp.")

    def __repr__(self) -> str:
        return self.firstName + " " + self.lastName + " " + str(self.age) + " y.o " + self.gender
