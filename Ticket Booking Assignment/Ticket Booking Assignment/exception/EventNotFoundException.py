class EventNotFoundException(Exception):
    def __init__(self, message="Event not found. Please enter a valid event name."):
        super().__init__(message)
