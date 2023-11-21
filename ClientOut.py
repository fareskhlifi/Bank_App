import psycopg2
import psycopg2.extras

from ClientIn import ClientIn

class ClientOut(ClientIn):
    def __init__(self, firstName, lastName, age, gender, balance, id):
        super().__init__(firstName, lastName, age, gender)
        self.balance = balance
        self.id = id


    @classmethod
    def get_user_by_Id(self, id):
        conn = ClientIn.__connect()
        with conn:
            with conn.cursor(cursor_factory= psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("""SELECT c.id AS id, c.firstname AS firstname,
                                c.lastname AS lastName, SUM(a.balance) AS total_balance
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
                    print(f"There is a problem: {e}")
