# dao/HospitalServiceImpl.py

import pyodbc
from entity.Appointment import Appointment
from dao.IHospitalService import IHospitalService
from util.DBConnection import DBConnection
from myexceptions.PatientNumberNotFoundException import PatientNumberNotFoundException

class HospitalServiceImpl(IHospitalService):

    def __init__(self):
        self.connection = DBConnection.getConnection()

    def getAppointmentById(self, appointmentId):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT a.appointmentId, a.patientId, a.doctorId, a.appointmentDate, a.description,p.firstName AS patientFirstName, p.lastName AS patientLastName,
                    d.firstName AS doctorFirstName, d.lastName AS doctorLastName
            FROM Appointment a
            JOIN Patient p ON a.patientId = p.patientId
            JOIN Doctor d ON a.doctorId = d.doctorId
            WHERE a.appointmentId = ?
            """
            cursor.execute(query, (appointmentId,))
            row = cursor.fetchone()
            
            if row:
                appointment = Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    doctorId=row[2],
                    appointmentDate=row[3],
                    description=row[4],
                    patientName=f"{row[5]} {row[6]}",  # Concatenate first and last name
                    doctorName=f"{row[7]} {row[8]}"    # Concatenate first and last name
                )
                return appointment
            else:
                raise PatientNumberNotFoundException(f"Appointment with ID {appointmentId} not found.")
        except Exception as e:
            print("Error in getAppointmentById:", e)
            return None


    # def getAppointmentsForPatient(self, patientId):
    #     cursor = self.connection.cursor()
    #     cursor.execute("SELECT * FROM Appointment WHERE patientId = ?", patientId)
    #     appointments = []
    #     for row in cursor.fetchall():
    #         appointments.append(Appointment(appointmentId=row[0], patientId=row[1], doctorId=row[2], appointmentDate=row[3], description=row[4]))
    #     return appointments
        
    def getAppointmentsForPatient(self, patientId):
        appointments = []
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT a.appointmentId, a.patientId, p.firstName AS patientFirstName, p.lastName AS patientLastName, 
                    a.doctorId, d.firstName AS doctorFirstName, d.lastName AS doctorLastName, 
                    a.appointmentDate, a.description
            FROM Appointment a
            JOIN Patient p ON a.patientId = p.patientId
            JOIN Doctor d ON a.doctorId = d.doctorId
            WHERE a.patientId = ?
            """
            cursor.execute(query, (patientId,))
            rows = cursor.fetchall()
            for row in rows:
                appointment = Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    patientName=f"{row[2]} {row[3]}",  # Concatenate first and last names
                    doctorId=row[4],
                    doctorName=f"{row[5]} {row[6]}",  # Concatenate first and last names
                    appointmentDate=row[7],
                    description=row[8]
                )
                appointments.append(appointment)
            return appointments
        except PatientNumberNotFoundException as e:
            print(f"Error: {e}")
            return appointments  
        except Exception as e:
            print(f"Error fetching appointments for patient {patientId}: {e}")
            return appointments
        finally:
            cursor.close()  # Close the cursor after use

    # def getAppointmentsForDoctor(self, doctorId):
    #     cursor = self.connection.cursor()
    #     cursor.execute("SELECT * FROM Appointment WHERE doctorId = ?", doctorId)
    #     appointments = []
    #     for row in cursor.fetchall():
    #         appointments.append(Appointment(appointmentId=row[0], patientId=row[1], doctorId=row[2], appointmentDate=row[3], description=row[4]))
    #     return appointments

    def getAppointmentsForDoctor(self, doctorId):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT a.appointmentId, a.patientId, p.firstName AS patientFirstName, p.lastName AS patientLastName, a.doctorId, d.firstName AS doctorFirstName, d.lastName AS doctorLastName, 
                    a.appointmentDate, a.description
            FROM Appointment a
            JOIN Patient p ON a.patientId = p.patientId
            JOIN Doctor d ON a.doctorId = d.doctorId
            WHERE a.doctorId = ?
            """
            cursor.execute(query, (doctorId,))
            rows = cursor.fetchall()

            appointments = []
            for row in rows:
                appointment = Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    patientName=f"{row[2]} {row[3]}",
                    doctorId=row[4],
                    doctorName=f"{row[5]} {row[6]}",
                    appointmentDate=row[7],
                    description=row[8]
                )
                appointments.append(appointment)
            return appointments
        except Exception as e:
            print("Error in getAppointmentsForDoctor:", e)
            return []
        finally:
            cursor.close()  # Close the cursor after use

    def scheduleAppointment(self, appointment: Appointment):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO Appointment (patientId, doctorId, appointmentDate, description)
            VALUES (?, ?, ?, ?)
        """, appointment.getPatientId(), appointment.getDoctorId(), appointment.getAppointmentDate(), appointment.getDescription())
        self.connection.commit()
        return appointment.appointmentId  # Return the generated appointment ID

    def updateAppointment(self, appointment: Appointment):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE Appointment 
            SET patientId = ?, doctorId = ?, appointmentDate = ?, description = ? 
            WHERE appointmentId = ?
        """, appointment.getPatientId(), appointment.getDoctorId(), appointment.getAppointmentDate(), appointment.getDescription(), appointment.getAppointmentId())
        self.connection.commit()
        return True

    def cancelAppointment(self, appointmentId):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Appointment WHERE appointmentId = ?", appointmentId)
        self.connection.commit()
        return True
