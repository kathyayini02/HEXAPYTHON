class InvalidBookingIDException(Exception):
    def __init__(self, message="Invalid Booking ID. No booking found with the provided ID."):
        super().__init__(message)
