# entity/Asset.py

class Asset:
    def __init__(self, asset_id=None, name=None, asset_type=None, serial_number=None, purchase_date=None, location=None, status=None, owner_id=None):
        self.__asset_id = asset_id
        self.__name = name
        self.__type = asset_type
        self.__serial_number = serial_number
        self.__purchase_date = purchase_date
        self.__location = location
        self.__status = status
        self.__owner_id = owner_id

    # Getters and Setters
    def get_asset_id(self):
        return self.__asset_id

    def set_asset_id(self, asset_id):
        self.__asset_id = asset_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_type(self):
        return self.__type

    def set_type(self, asset_type):
        self.__type = asset_type

    def get_serial_number(self):
        return self.__serial_number

    def set_serial_number(self, serial_number):
        self.__serial_number = serial_number

    def get_purchase_date(self):
        return self.__purchase_date

    def set_purchase_date(self, purchase_date):
        self.__purchase_date = purchase_date

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_owner_id(self):
        return self.__owner_id

    def set_owner_id(self, owner_id):
        self.__owner_id = owner_id

    def __str__(self):
        return f"Asset [ID={self.__asset_id}, Name={self.__name}, Type={self.__type}, SerialNumber={self.__serial_number}, Status={self.__status}]"
