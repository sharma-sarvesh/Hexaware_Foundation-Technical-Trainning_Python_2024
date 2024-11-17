class CourierService:
    def __init__(self, ServiceID=None, ServiceName=None, Cost=None):
        self._ServiceID = ServiceID
        self._ServiceName = ServiceName
        self._Cost = Cost

    # Getters and Setters
    def get_ServiceID(self):
        return self._ServiceID

    def set_ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    def get_ServiceName(self):
        return self._ServiceName

    def set_ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    def get_Cost(self):
        return self._Cost

    def set_Cost(self, Cost):
        self._Cost = Cost

    def __repr__(self):
        return f"CourierService(ServiceID={self._ServiceID}, ServiceName={self._ServiceName}, Cost={self._Cost})"
