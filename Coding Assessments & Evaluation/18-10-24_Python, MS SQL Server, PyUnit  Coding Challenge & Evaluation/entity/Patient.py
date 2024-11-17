# entity/Patient.py

class Patient:
    def __init__(self, patientId=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactNumber=None, address=None):
        self.__patientId = patientId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__contactNumber = contactNumber
        self.__address = address


    # Getters
    def getPatientId(self):
        return self.__patientId
    
    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName
    
    def getDateOfBirth(self):
        return self.__dateOfBirth

    def getGender(self):
        return self.__gender

    def getContactNumber(self):
        return self.__contactNumber
    
    def getAddress(self):
        return self.__address

    # Setters
    def setPatientId(self, patientId):
        self.__patientId = patientId

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setDateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def setGender(self, gender):
        self.__gender = gender

    def setContactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def setAddress(self, address):
        self.__address = address


    def __str__(self):
        return f"Patient ID: {self.__patientId}, Name: {self.__firstName} {self.__lastName}, DOB: {self.__dateOfBirth}, Gender: {self.__gender}, Contact: {self.__contactNumber}, Address: {self.__address}"
