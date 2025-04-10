class Event:
    def __init__(self, event_id=None, event_name="", event_date="", event_time="", venue_id=None,
                 total_seats=0, available_seats=0, ticket_price=0.0, event_type=""):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_id = venue_id
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def display_event_details(self):
        print(f"Event ID: {self.event_id}, Name: {self.event_name}")
        print(f"Date: {self.event_date}, Time: {self.event_time}")
        print(f"Venue ID: {self.venue_id}, Type: {self.event_type}")
        print(f"Total Seats: {self.total_seats}, Available: {self.available_seats}, Price: ₹{self.ticket_price}")
