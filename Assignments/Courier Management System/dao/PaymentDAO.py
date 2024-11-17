# dao/PaymentDAO.py
from abc import ABC, abstractmethod

class PaymentDAO(ABC):
    @abstractmethod
    def create_payment(self, payment):
        pass

    @abstractmethod
    def get_payment_by_id(self, payment_id):
        pass

    @abstractmethod
    def update_payment(self, payment):
        pass

    @abstractmethod
    def delete_payment(self, payment_id):
        pass

    @abstractmethod
    def get_all_payments(self):
        pass
