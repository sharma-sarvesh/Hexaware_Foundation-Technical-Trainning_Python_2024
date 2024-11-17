class TrackingNumberNotFoundException(Exception):
    def __init__(self, message="Tracking number not found."):
        self.message = message
        super().__init__(self.message)
