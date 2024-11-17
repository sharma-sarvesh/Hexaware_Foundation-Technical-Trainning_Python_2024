class Location:
    def __init__(self, LocationID=None, LocationName=None, Address=None):
        self._LocationID = LocationID
        self._LocationName = LocationName
        self._Address = Address

    # Getters and Setters
    def get_LocationID(self):
        return self._LocationID

    def set_LocationID(self, LocationID):
        self._LocationID = LocationID

    def get_LocationName(self):
        return self._LocationName

    def set_LocationName(self, LocationName):
        self._LocationName = LocationName

    def get_Address(self):
        return self._Address

    def set_Address(self, Address):
        self._Address = Address

    def __repr__(self):
        return f"Location(LocationID={self._LocationID}, LocationName={self._LocationName}, Address={self._Address})"
