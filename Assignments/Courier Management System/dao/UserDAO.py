# dao/UserDAO.py

from abc import ABC, abstractmethod

class UserDAO(ABC):
    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def update_user(self, user):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass

    @abstractmethod
    def get_all_users(self):
        pass
