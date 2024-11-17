# mainmod/MainModule.py

import sys
import os

# Adding the project root directory to the system path
project_root = r'S:\GIT\Hexawarwe_CodingAssessment\CodingChallenge Hospital Management System'
sys.path.append(os.path.abspath(project_root))


from dao.HospitalServiceImpl import HospitalServiceImpl
from entity.Appointment import Appointment
from myexceptions.PatientNumberNotFoundException import PatientNumberNotFoundException


class MainModule:
    def __init__(self):
        self.service = HospitalServiceImpl()

    def display_menu(self):
        print("\n*** Hospital Management System ***")
        print("1. Get Appointment By ID")
        print("2. Get Appointments for Patient")
        print("3. Get Appointments for Doctor")
        print("4. Schedule Appointment")
        print("5. Update Appointment")
        print("6. Cancel Appointment")
        print("0. Exit")
        choice = input("Enter your choice: ")
        return choice

    def run(self):
        while True:
            choice = self.display_menu()
            if choice == '1':
                appointment_id = int(input("Enter Appointment ID: "))
                try:
                    appointment = self.service.getAppointmentById(appointment_id)
                    print(f"Appointment Found: {appointment}")
                except PatientNumberNotFoundException as e:
                    print(e)
            # elif choice == '2':
            #     patient_id = int(input("Enter Patient ID: "))
            #     appointments = self.service.getAppointmentsForPatient(patient_id)
            #     print("Appointments for Patient ID", patient_id)
            #     for appt in appointments:
            #         print(appt)
            elif choice == '2':
                try:
                    patient_id = int(input("Enter Patient ID: "))
                    appointments = self.service.getAppointmentsForPatient(patient_id)
                    
                    if appointments:
                        print(f"Appointments for Patient ID {patient_id}:")
                        for appt in appointments:
                            print(appt)  # Assuming Appointment class has a __str__ method
                    else:
                        print(f"No appointments found for Patient ID {patient_id}")
                
                except PatientNumberNotFoundException as e:
                    print(f"Error: {e}")
                
                except ValueError:
                    print("Invalid input! Patient ID must be an integer.")
                
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            elif choice == '3':
                doctor_id = int(input("Enter Doctor ID: "))
                appointments = self.service.getAppointmentsForDoctor(doctor_id)
                print("Appointments for Doctor ID", doctor_id)
                for appt in appointments:
                    print(appt)
            elif choice == '4':
                appointment = Appointment(
                    patientId=int(input("Enter Patient ID: ")),
                    doctorId=int(input("Enter Doctor ID: ")),
                    appointmentDate=input("Enter Appointment Date (YYYY-MM-DD): "),
                    description=input("Enter Description: ")
                )
                appointment.appointmentId = self.service.scheduleAppointment(appointment)
                print("Appointment Scheduled:", appointment)
            elif choice == '5':
                appointment_id = int(input("Enter Appointment ID to update: "))
                appointment = self.service.getAppointmentById(appointment_id)
                appointment.patientId = int(input("Enter new Patient ID: "))
                appointment.doctorId = int(input("Enter new Doctor ID: "))
                appointment.appointmentDate = input("Enter new Appointment Date (YYYY-MM-DD): ")
                appointment.description = input("Enter new Description: ")
                self.service.updateAppointment(appointment)
                print("Appointment Updated:", appointment)
            elif choice == '6':
                appointment_id = int(input("Enter Appointment ID to cancel: "))
                self.service.cancelAppointment(appointment_id)
                print(f"Appointment with ID {appointment_id} has been canceled.")
            elif choice == '0':
                print("Exiting the Hospital Management System...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main = MainModule()
    main.run()
