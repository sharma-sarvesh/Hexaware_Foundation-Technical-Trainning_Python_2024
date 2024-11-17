class User:
    def __init__(self, UserID=None, Name=None, Email=None, Password=None, ContactNumber=None, Address=None):
        self._UserID = UserID
        self._Name = Name
        self._Email = Email
        self._Password = Password
        self._ContactNumber = ContactNumber
        self._Address = Address

    # Getters and Setters
    def get_UserID(self):
        return self._UserID

    def set_UserID(self, UserID):
        self._UserID = UserID

    def get_Name(self):
        return self._Name

    def set_Name(self, Name):
        self._Name = Name

    def get_Email(self):
        return self._Email

    def set_Email(self, Email):
        self._Email = Email

    def get_Password(self):
        return self._Password

    def set_Password(self, Password):
        self._Password = Password

    def get_ContactNumber(self):
        return self._ContactNumber

    def set_ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    def get_Address(self):
        return self._Address

    def set_Address(self, Address):
        self._Address = Address

    def __repr__(self):
        return f"User(UserID={self._UserID}, Name={self._Name}, Email={self._Email})"
