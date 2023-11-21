import psycopg2
import psycopg2.extras

from ClientOut import ClientOut
from ClientIn import ClientIn

class Account:
    def __init__(self, client_id, balance, id = None):
        assert isinstance(client_id, int), "client_id should be an integer"
        assert isinstance(balance, float), "balance should be a float"
        client = ClientOut.get_user_by_Id(client_id)
        assert client, 'client_id is not present in table "clients"'

        self.client_id = client_id
        self.__balance = balance
        self.id = id

        conn = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "root",
            database = "bankapp"
            )

        with conn:
            with conn.cursor(cursor_factory= psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("""INSERT INTO accounts(client_id, balance) 
                                VALUES (%s, %s)""", (self.client_id, self.balance)
                                )
                except Exception as e:
                    print("Out of service, try again in few minutes...")
                    print(e)

    # getter
    @property
    def balance(self):
        return self.__balance

    #setter
    @balance.setter
    def balance(self, value):
        self.__balance = value

    def __repr__(self) -> str:
        return "the account number " + self.client_id + "has a credit " + self.balance 


account_example = Account(1, 120.0)
print(account_example)
