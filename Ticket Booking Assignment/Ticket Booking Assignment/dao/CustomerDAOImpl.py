from util.DB_Connect import db_connection
from entity.Customer import Customer

class CustomerDAOImpl:
    def insert_customer(self, customer):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Customer (customer_name, email, phone_number) VALUES (?, ?, ?)",
                       (customer.customer_name, customer.email, customer.phone_number))
        conn.commit()
        conn.close()

    def get_customer_by_id(self, customer_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer WHERE customer_id = ?", (customer_id,))
        row = cursor.fetchone()
        conn.close()
        return Customer(row.customer_id, row.customer_name, row.email, row.phone_number) if row else None

    def update_customer(self, customer):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Customer SET customer_name = ?, email = ?, phone_number = ? WHERE customer_id = ?",
                       (customer.customer_name, customer.email, customer.phone_number, customer.customer_id))
        conn.commit()
        conn.close()

    def delete_customer(self, customer_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Customer WHERE customer_id = ?", (customer_id,))
        conn.commit()
        conn.close()

    def get_all_customers(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer")
        rows = cursor.fetchall()
        conn.close()
        return [Customer(row.customer_id, row.customer_name, row.email, row.phone_number) for row in rows]
