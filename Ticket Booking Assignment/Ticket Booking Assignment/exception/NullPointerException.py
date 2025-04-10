class NullPointerException(Exception):
    def __init__(self, message="Null value encountered. Make sure all required fields are filled."):
        super().__init__(message)
