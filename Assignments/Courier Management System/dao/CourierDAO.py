# dao/CourierDAO.py

from abc import ABC, abstractmethod

class CourierDAO(ABC):
    @abstractmethod
    def create_courier(self, courier):
        pass

    @abstractmethod
    def get_courier_by_id(self, courier_id):
        pass

    @abstractmethod
    def update_courier(self, courier):
        pass

    @abstractmethod
    def delete_courier(self, courier_id):
        pass

    @abstractmethod
    def get_all_couriers(self):
        pass
