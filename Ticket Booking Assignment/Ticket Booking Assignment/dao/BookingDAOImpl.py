from util.DB_Connect import db_connection
from entity.Booking import Booking

class BookingDAOImpl:
    def insert_booking(self, booking):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Booking (customer_id, event_id, num_tickets, total_cost) VALUES (?, ?, ?, ?)",
                       (booking.customer_id, booking.event_id, booking.num_tickets, booking.total_cost))
        conn.commit()
        conn.close()

    def get_booking_by_id(self, booking_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Booking WHERE booking_id = ?", (booking_id,))
        row = cursor.fetchone()
        conn.close()
        return Booking(row.booking_id, row.customer_id, row.event_id, row.num_tickets, row.total_cost, row.booking_date) if row else None

    def update_booking(self, booking):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Booking SET customer_id = ?, event_id = ?, num_tickets = ?, total_cost = ? WHERE booking_id = ?",
                       (booking.customer_id, booking.event_id, booking.num_tickets, booking.total_cost, booking.booking_id))
        conn.commit()
        conn.close()

    def delete_booking(self, booking_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Booking WHERE booking_id = ?", (booking_id,))
        conn.commit()
        conn.close()

    def get_all_bookings(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Booking")
        rows = cursor.fetchall()
        conn.close()
        return [Booking(row.booking_id, row.customer_id, row.event_id, row.num_tickets, row.total_cost, row.booking_date) for row in rows]
