import psycopg2
import psycopg2.extras

from ClientIn import ClientIn

class ClientOut(ClientIn):
    def __init__(self, firstname, lastname, age, gender, total_balance, id=None):
        super().__init__(firstname, lastname, age, gender)
        self.total_balance = total_balance
        self.id = id


    @classmethod
    def get_user_by_Id(cls, id):
        conn = cls.__connect()
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("""SELECT c.id AS id,
                                c.firstname AS firstname,
                                c.lastname AS lastName,
                                c.age as age,
                                c.gender as gender,
                                SUM(a.balance) AS total_balance
                                FROM clients AS c
                                JOIN accounts AS a
                                ON c.id = a.client_id
                                WHERE c.id = %s
                                GROUP BY c.id, c.firstname, c.lastname;                   
                                """, (id,))
                    client = cur.fetchone()
                    if not client:
                        return None
                    return ClientOut(**client)
                except Exception as e:
                    print(f"the client couldn't be get: {e}")

    def __repr__(self) -> str:
        return super().__repr__() + " balance: " + str(self.total_balance)

