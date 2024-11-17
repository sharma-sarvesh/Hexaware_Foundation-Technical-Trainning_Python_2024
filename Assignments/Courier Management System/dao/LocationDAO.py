# dao/LocationDAO.py

from abc import ABC, abstractmethod

class LocationDAO(ABC):
    @abstractmethod
    def create_location(self, location):
        pass

    @abstractmethod
    def get_location_by_id(self, location_id):
        pass

    @abstractmethod
    def update_location(self, location):
        pass

    @abstractmethod
    def delete_location(self, location_id):
        pass

    @abstractmethod
    def get_all_locations(self):
        pass
