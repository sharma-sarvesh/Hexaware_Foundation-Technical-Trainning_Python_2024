class Appointment:
    def __init__(self, appointmentId=None, patientId=None, doctorId=None, appointmentDate=None, description=None, patientName=None, doctorName=None):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description
        self.patientName = patientName  
        self.doctorName = doctorName      

    # Getters
    def getAppointmentId(self):
        return self.appointmentId

    def getPatientId(self):
        return self.patientId

    def getDoctorId(self):
        return self.doctorId

    def getAppointmentDate(self):
        return self.appointmentDate

    def getDescription(self):
        return self.description

    def getPatientName(self):
        return self.patientName  

    def getDoctorName(self):
        return self.doctorName  

    # Setters
    def setAppointmentId(self, appointmentId):
        self.appointmentId = appointmentId

    def setPatientId(self, patientId):
        self.patientId = patientId

    def setDoctorId(self, doctorId):
        self.doctorId = doctorId

    def setAppointmentDate(self, appointmentDate):
        self.appointmentDate = appointmentDate

    def setDescription(self, description):
        self.description = description

    def setPatientName(self, patientName):
        self.patientName = patientName  

    def setDoctorName(self, doctorName):
        self.doctorName = doctorName  

    def __str__(self):
        return (f"Appointment ID: {self.appointmentId}, Patient ID: {self.patientId},"
                f"Patient Name: {self.patientName}, Doctor ID: {self.doctorId},"
                f"Doctor Name: {self.doctorName}, Appointment Date: {self.appointmentDate},"
                f"Description: {self.description}")
