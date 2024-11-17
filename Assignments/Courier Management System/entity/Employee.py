class Employee:
    def __init__(self, EmployeeID=None, Name=None, Email=None, ContactNumber=None, Role=None, Salary=None):
        self._EmployeeID = EmployeeID
        self._Name = Name
        self._Email = Email
        self._ContactNumber = ContactNumber
        self._Role = Role
        self._Salary = Salary

    # Getters and Setters
    def get_EmployeeID(self):
        return self._EmployeeID

    def set_EmployeeID(self, EmployeeID):
        self._EmployeeID = EmployeeID

    def get_Name(self):
        return self._Name

    def set_Name(self, Name):
        self._Name = Name

    def get_Email(self):
        return self._Email

    def set_Email(self, Email):
        self._Email = Email

    def get_ContactNumber(self):
        return self._ContactNumber

    def set_ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    def get_Role(self):
        return self._Role

    def set_Role(self, Role):
        self._Role = Role

    def get_Salary(self):
        return self._Salary

    def set_Salary(self, Salary):
        self._Salary = Salary

    def __repr__(self):
        return f"Employee(EmployeeID={self._EmployeeID}, Name={self._Name}, Role={self._Role}, Salary={self._Salary})"
