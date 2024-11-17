class Payment:
    def __init__(self, PaymentID=None, CourierID=None, LocationID=None, Amount=None, PaymentDate=None):
        self._PaymentID = PaymentID
        self._CourierID = CourierID
        self._LocationID = LocationID
        self._Amount = Amount
        self._PaymentDate = PaymentDate

    # Getters and Setters
    def get_PaymentID(self):
        return self._PaymentID

    def set_PaymentID(self, PaymentID):
        self._PaymentID = PaymentID

    def get_CourierID(self):
        return self._CourierID

    def set_CourierID(self, CourierID):
        self._CourierID = CourierID

    def get_LocationID(self):
        return self._LocationID

    def set_LocationID(self, LocationID):
        self._LocationID = LocationID

    def get_Amount(self):
        return self._Amount

    def set_Amount(self, Amount):
        self._Amount = Amount

    def get_PaymentDate(self):
        return self._PaymentDate

    def set_PaymentDate(self, PaymentDate):
        self._PaymentDate = PaymentDate

    def __repr__(self):
        return f"Payment(PaymentID={self._PaymentID}, CourierID={self._CourierID}, Amount={self._Amount}, PaymentDate={self._PaymentDate})"
