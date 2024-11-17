class Courier:
    def __init__(self, CourierID=None, SenderName=None, SenderAddress=None, ReceiverName=None, ReceiverAddress=None, 
                 Weight=None, Status=None, TrackingNumber=None, DeliveryDate=None):
        self._CourierID = CourierID
        self._SenderName = SenderName
        self._SenderAddress = SenderAddress
        self._ReceiverName = ReceiverName
        self._ReceiverAddress = ReceiverAddress
        self._Weight = Weight
        self._Status = Status
        self._TrackingNumber = TrackingNumber
        self._DeliveryDate = DeliveryDate

    # Getters and Setters
    def get_CourierID(self):
        return self._CourierID

    def set_CourierID(self, CourierID):
        self._CourierID = CourierID

    def get_SenderName(self):
        return self._SenderName

    def set_SenderName(self, SenderName):
        self._SenderName = SenderName

    def get_SenderAddress(self):
        return self._SenderAddress

    def set_SenderAddress(self, SenderAddress):
        self._SenderAddress = SenderAddress

    def get_ReceiverName(self):
        return self._ReceiverName

    def set_ReceiverName(self, ReceiverName):
        self._ReceiverName = ReceiverName

    def get_ReceiverAddress(self):
        return self._ReceiverAddress

    def set_ReceiverAddress(self, ReceiverAddress):
        self._ReceiverAddress = ReceiverAddress

    def get_Weight(self):
        return self._Weight

    def set_Weight(self, Weight):
        self._Weight = Weight

    def get_Status(self):
        return self._Status

    def set_Status(self, Status):
        self._Status = Status

    def get_TrackingNumber(self):
        return self._TrackingNumber

    def set_TrackingNumber(self, TrackingNumber):
        self._TrackingNumber = TrackingNumber

    def get_DeliveryDate(self):
        return self._DeliveryDate

    def set_DeliveryDate(self, DeliveryDate):
        self._DeliveryDate = DeliveryDate

    def __repr__(self):
        return f"Courier(CourierID={self._CourierID}, SenderName={self._SenderName}, ReceiverName={self._ReceiverName}, Status={self._Status})"
