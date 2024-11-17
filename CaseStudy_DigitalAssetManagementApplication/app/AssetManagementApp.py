# app\AssetManagementApp.py

import sys
import os
# Adding the project root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'S:\GIT\Hexaware_CaseStudy')))


from dao.AssetManagementServiceImpl import AssetManagementServiceImpl
from entity.Asset import Asset
from entity.AssetAllocation import AssetAllocation
from entity.MaintenanceRecord import MaintenanceRecord
from entity.Employee import Employee
from entity.Reservation import Reservation
from myexceptions.AssetNotFoundException import AssetNotFoundException
from myexceptions.AssetNotMaintainException import AssetNotMaintainException
from util.DBConnection import DBConnection

class AssetManagementApp:
    def __init__(self):
        self.service = AssetManagementServiceImpl()

    def display_menu(self):
        print("\n *** Asset Management System *** ")
        print("1. Add Asset")
        print("2. Update Asset")
        print("3. Delete Asset")
        print("4. Allocate Asset")
        print("5. Deallocate Asset")
        print("6. Perform Maintenance")
        print("7. Reserve Asset")
        print("8. Withdraw Reservation")
        print("9. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option (1-9): ")

            try:
                if choice == '1':
                    self.add_asset()
                elif choice == '2':
                    self.update_asset()
                elif choice == '3':
                    self.delete_asset()
                elif choice == '4':
                    self.allocate_asset()
                elif choice == '5':
                    self.deallocate_asset()
                elif choice == '6':
                    self.perform_maintenance()
                elif choice == '7':
                    self.reserve_asset()
                elif choice == '8':
                    self.withdraw_reservation()
                elif choice == '9':
                    print("Exiting the application.")
                    break
                else:
                    print("Invalid option, please try again.")
            except (AssetNotFoundException, AssetNotMaintainException) as e:
                print(e)
            except Exception as e:
                print(f"An error occurred: {e}")

    def add_asset(self):
        name = input("Enter Asset Name: ")
        asset_type = input("Enter Asset Type: ")
        serial_number = input("Enter Serial Number: ")
        purchase_date = input("Enter Purchase Date (YYYY-MM-DD): ")
        location = input("Enter Asset Location: ")
        status = input("Enter Asset Status: ")
        
        asset = Asset(name=name, asset_type=asset_type, serial_number=serial_number,
                    purchase_date=purchase_date, location=location, status=status)
        if self.service.add_new_asset(asset):
            print("Asset added successfully.")
        else:
            print("Failed to add asset.")


    def update_asset(self):
        asset_id = int(input("Enter asset ID to update asset's details: "))

        existing_asset = self.service.get_asset_by_id(asset_id)

        if not existing_asset:
            print("Asset not found!")
            return
        name = input("Enter new asset name (leave blank for no change): ")
        asset_type = input("Enter new asset type (leave blank for no change): ")
        serial_number = input("Enter new serial number (leave blank for no change): ")
        purchase_date = input("Enter new purchase date (YYYY-MM-DD, leave blank for no change): ")
        location = input("Enter new asset location (leave blank for no change): ")
        status = input("Enter new asset status (leave blank for no change): ")
        # Use existing values if input is blank
        updated_asset = {
            'name': name if name else existing_asset.get_name(),
            'type': asset_type if asset_type else existing_asset.get_type(),
            'serial_number': serial_number if serial_number else existing_asset.get_serial_number(),
            'purchase_date': purchase_date if purchase_date else existing_asset.get_purchase_date(),
            'location': location if location else existing_asset.get_location(),
            'status': status if status else existing_asset.get_status(),
            'owner_id': existing_asset.get_owner_id()  # Not changing the owner
        }

        asset_to_update = Asset(
            asset_id=asset_id,
            name=updated_asset['name'],
            asset_type=updated_asset['type'],
            serial_number=updated_asset['serial_number'],
            purchase_date=updated_asset['purchase_date'],
            location=updated_asset['location'],
            status=updated_asset['status'],
            owner_id=updated_asset['owner_id']
        )

        success = self.service.update_the_asset(asset_to_update)
        
        if success:
            print("Asset updated successfully.")
        else:
            print("Failed to update the asset.")


    def delete_asset(self):
        asset_id = int(input("Enter asset ID to delete: "))
        if self.service.deleteing_asset(asset_id):
            print("Asset deleted successfully.")
        else:
            print("Failed to delete asset.")


    def allocate_asset(self):
        asset_id = int(input("Enter asset ID to allocate: "))
        employee_id = int(input("Enter employee ID to allocate to: "))
        allocation_date = input("Enter allocation date (YYYY-MM-DD): ")

        # Create an AssetAllocation instance with the input values
        asset_allocation = AssetAllocation(
            asset_id=asset_id,
            employee_id=employee_id,
            allocation_date=allocation_date
        )

        if self.service.allocating_asset(asset_allocation):
            print("Asset allocated successfully.")
        else:
            print("Failed to allocate asset.")


    def deallocate_asset(self):
        asset_id = int(input("Enter asset ID to deallocate: "))
        employee_id = int(input("Enter employee ID to deallocate from: "))
        return_date = input("Enter return date (YYYY-MM-DD): ")
        
        success = self.service.deallocating_asset(asset_id, employee_id, return_date)
        
        if success:
            print("Asset deallocated successfully.")
        else:
            print("Failed to deallocate asset.")


    def perform_maintenance(self):
        asset_id = int(input("Enter asset ID for maintenance: "))
        maintenance_date = input("Enter maintenance date (YYYY-MM-DD): ")
        description = input("Enter maintenance description: ")
        cost = float(input("Enter maintenance cost: "))

        # Create a MaintenanceRecord instance with the input values
        maintenance_record = MaintenanceRecord(
            asset_id=asset_id,
            maintenance_date=maintenance_date,
            description=description,
            cost=cost
        )

        if self.service.performing_maintenance(maintenance_record):
            print("Maintenance recorded successfully.")
        else:
            print("Failed to record maintenance.")


    def reserve_asset(self):
        asset_id = int(input("Enter asset ID to reserve: "))
        employee_id = int(input("Enter employee ID making the reservation: "))
        reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
        start_date = input("Enter start date for the reservation (YYYY-MM-DD): ")
        end_date = input("Enter end date for the reservation (YYYY-MM-DD): ")

        # Create a Reservation object
        reservation = Reservation(
            reservation_date=reservation_date,
            start_date=start_date,
            end_date=end_date,
            asset_id=asset_id,
            employee_id=employee_id
        )

        # Call the reserveAsset method from the service implementation
        success = self.service.reserving_asset(reservation)

        if success:
            print("Asset reserved successfully.")
        else:
            print("Failed to reserve asset.")


    def withdraw_reservation(self):
        reservation_id = int(input("Enter reservation ID to withdraw: "))
        success =  self.service.withdrawing_reservation(reservation_id)

        if not success:
            print("Failed to withdraw reservation.")

if __name__ == "__main__":
    DBConnection.get_connection()  # Establish DB connection before running the app
    app = AssetManagementApp()
    app.run()
