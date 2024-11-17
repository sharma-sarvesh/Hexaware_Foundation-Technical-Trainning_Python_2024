# dao/CourierServiceDAO.py
from abc import ABC, abstractmethod

class CourierServiceDAO(ABC):
    @abstractmethod
    def create_courier_service(self, courier_service):
        pass

    @abstractmethod
    def get_courier_service_by_id(self, service_id):
        pass

    @abstractmethod
    def update_courier_service(self, courier_service):
        pass

    @abstractmethod
    def delete_courier_service(self, service_id):
        pass

    @abstractmethod
    def get_all_courier_services(self):
        pass

