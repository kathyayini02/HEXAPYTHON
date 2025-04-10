class Booking:
    def __init__(self, booking_id=None, customer_id=None, event_id=None, num_tickets=0,
                 total_cost=0.0, booking_date=None):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.event_id = event_id
        self.num_tickets = num_tickets
        self.total_cost = total_cost
        self.booking_date = booking_date

    def display_booking_details(self):
        print(f"Booking ID: {self.booking_id}")
        print(f"Customer ID: {self.customer_id}, Event ID: {self.event_id}")
        print(f"Tickets Booked: {self.num_tickets}, Total Cost: ₹{self.total_cost}")
        print(f"Booking Date: {self.booking_date}")
