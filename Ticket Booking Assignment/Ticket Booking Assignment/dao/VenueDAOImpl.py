
from util.DB_Connect import db_connection

from entity.Venue import Venue

class VenueDAOImpl:

    def insert_venue(self, venue):
        conn = db_connection()
        if conn is None:
            raise Exception("Database connection failed.")
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Venue (venue_name, address) VALUES (?, ?)", (venue.venue_name, venue.address))
            conn.commit()
        except Exception as e:
            print(f"❌ Error inserting venue: {e}")
        finally:
            conn.close()

    def get_venue_by_id(self, venue_id):
        conn = db_connection()
        if conn is None:
            raise Exception("Database connection failed.")
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Venue WHERE venue_id = ?", (venue_id,))
            row = cursor.fetchone()
            return Venue(row.venue_id, row.venue_name, row.address) if row else None
        except Exception as e:
            print(f"❌ Error fetching venue: {e}")
            return None
        finally:
            conn.close()

    def update_venue(self, venue):
        conn = db_connection()
        if conn is None:
            raise Exception("Database connection failed.")
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE Venue SET venue_name = ?, address = ? WHERE venue_id = ?",
                           (venue.venue_name, venue.address, venue.venue_id))
            conn.commit()
        except Exception as e:
            print(f"❌ Error updating venue: {e}")
        finally:
            conn.close()

    def delete_venue(self, venue_id):
        conn = db_connection()
        if conn is None:
            raise Exception("Database connection failed.")
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Venue WHERE venue_id = ?", (venue_id,))
            conn.commit()
        except Exception as e:
            print(f"❌ Error deleting venue: {e}")
        finally:
            conn.close()

    def get_all_venues(self):
        conn = db_connection()
        if conn is None:
            raise Exception("Database connection failed.")
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Venue")
            rows = cursor.fetchall()
            return [Venue(row.venue_id, row.venue_name, row.address) for row in rows]
        except Exception as e:
            print(f"❌ Error retrieving venues: {e}")
            return []
        finally:
            conn.close()
