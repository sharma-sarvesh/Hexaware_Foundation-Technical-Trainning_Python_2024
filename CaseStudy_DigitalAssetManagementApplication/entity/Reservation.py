# entity/Reservation.py

class Reservation:
    def __init__(self, reservation_id=None, reservation_date=None, start_date=None, end_date=None, status=None, asset_id=None, employee_id=None):
        self.__reservation_id = reservation_id
        self.__reservation_date = reservation_date
        self.__start_date = start_date
        self.__end_date = end_date
        self.__status = status
        self.__asset_id = asset_id
        self.__employee_id = employee_id

    # Getters and Setters
    def get_reservation_id(self):
        return self.__reservation_id

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def get_reservation_date(self):
        return self.__reservation_date

    def set_reservation_date(self, reservation_date):
        self.__reservation_date = reservation_date

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_asset_id(self):
        return self.__asset_id

    def set_asset_id(self, asset_id):
        self.__asset_id = asset_id

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def __str__(self):
        return f"Reservation [ID={self.__reservation_id}, ReservationDate={self.__reservation_date}, StartDate={self.__start_date}, EndDate={self.__end_date}, Status={self.__status}]"
