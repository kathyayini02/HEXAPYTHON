from util.DB_Connect import db_connection
from entity.Event import Event

class EventDAOImpl:
    def insert_event(self, event):
        conn = db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Event (event_name, event_date, event_time, venue_id, 
                   total_seats, available_seats, ticket_price, event_type) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (event.event_name, event.event_date, event.event_time, event.venue_id,
                               event.total_seats, event.available_seats, event.ticket_price, event.event_type))
        conn.commit()
        conn.close()

    def get_event_by_id(self, event_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Event WHERE event_id = ?", (event_id,))
        row = cursor.fetchone()
        conn.close()
        return Event(row.event_id, row.event_name, row.event_date, row.event_time,
                     row.venue_id, row.total_seats, row.available_seats,
                     row.ticket_price, row.event_type) if row else None

    def update_event(self, event):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("""UPDATE Event SET event_name = ?, event_date = ?, event_time = ?, 
                          venue_id = ?, total_seats = ?, available_seats = ?, 
                          ticket_price = ?, event_type = ? WHERE event_id = ?""",
                       (event.event_name, event.event_date, event.event_time, event.venue_id,
                        event.total_seats, event.available_seats, event.ticket_price,
                        event.event_type, event.event_id))
        conn.commit()
        conn.close()

    def delete_event(self, event_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Event WHERE event_id = ?", (event_id,))
        conn.commit()
        conn.close()

    def get_all_events(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Event")
        rows = cursor.fetchall()
        conn.close()
        return [Event(row.event_id, row.event_name, row.event_date, row.event_time,
                      row.venue_id, row.total_seats, row.available_seats,
                      row.ticket_price, row.event_type) for row in rows]
