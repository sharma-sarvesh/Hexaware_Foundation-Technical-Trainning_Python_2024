# dao/EmployeeDAO.py
from abc import ABC, abstractmethod

class EmployeeDAO(ABC):
    @abstractmethod
    def create_employee(self, employee):
        pass

    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass

    @abstractmethod
    def update_employee(self, employee):
        pass

    @abstractmethod
    def delete_employee(self, employee_id):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

