# entity/MaintenanceRecord.py

class MaintenanceRecord:
    def __init__(self, maintenance_id=None, maintenance_date=None, description=None, cost=None, asset_id=None):
        self.__maintenance_id = maintenance_id
        self.__maintenance_date = maintenance_date
        self.__description = description
        self.__cost = cost
        self.__asset_id = asset_id

    # Getters and Setters
    def get_maintenance_id(self):
        return self.__maintenance_id

    def set_maintenance_id(self, maintenance_id):
        self.__maintenance_id = maintenance_id

    def get_maintenance_date(self):
        return self.__maintenance_date

    def set_maintenance_date(self, maintenance_date):
        self.__maintenance_date = maintenance_date

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def get_asset_id(self):
        return self.__asset_id

    def set_asset_id(self, asset_id):
        self.__asset_id = asset_id

    def __str__(self):
        return f"MaintenanceRecord [ID={self.__maintenance_id}, Date={self.__maintenance_date}, Description={self.__description}, Cost={self.__cost}]"
