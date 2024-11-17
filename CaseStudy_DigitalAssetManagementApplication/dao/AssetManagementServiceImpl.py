# dao/AssetManagementServiceImpl.py

import pyodbc
from entity.Asset import Asset
from entity.AssetAllocation import AssetAllocation
from entity.MaintenanceRecord import MaintenanceRecord
from entity.Reservation import Reservation
from dao.AssetManagementService import AssetManagementService
from util.DBConnection import DBConnection
from myexceptions.AssetNotFoundException import AssetNotFoundException
from myexceptions.AssetNotMaintainException import AssetNotMaintainException
from datetime import datetime

class AssetManagementServiceImpl(AssetManagementService):

    def __init__(self):
        self.conn = DBConnection.get_connection()


    def add_new_asset(self, asset: Asset) -> bool:
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO Assets (Name, Type, SerialNumber, PurchaseDate, Location, Status, OwnerID)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (asset.get_name(), asset.get_type(), asset.get_serial_number(), asset.get_purchase_date(), asset.get_location(), asset.get_status(), asset.get_owner_id()))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error adding asset: {e}")
            return False


    def update_the_asset(self, asset: Asset) -> bool:
        try:
            cursor = self.conn.cursor()

            # create new SQL query based on the provided asset details
            update_fields = []
            parameters = []

            if asset.get_name() != "":
                update_fields.append("Name=?")
                parameters.append(asset.get_name())

            if asset.get_type() != "":
                update_fields.append("Type=?")
                parameters.append(asset.get_type())

            if asset.get_serial_number() != "":
                update_fields.append("SerialNumber=?")
                parameters.append(asset.get_serial_number())

            if asset.get_purchase_date() != "":
                update_fields.append("PurchaseDate=?")
                parameters.append(asset.get_purchase_date())

            if asset.get_location() != "":
                update_fields.append("Location=?")
                parameters.append(asset.get_location())

            if asset.get_status() != "":
                update_fields.append("Status=?")
                parameters.append(asset.get_status())

            parameters.append(asset.get_asset_id())
            
            if not update_fields:  # No fields to update
                print("No changes to update.")
                return False

            # Build the final SQL query
            query = f"UPDATE Assets SET {', '.join(update_fields)} WHERE AssetID=?"
            
            # Execute the query
            cursor.execute(query, parameters)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating asset: {e}")
            return False


    def get_asset_by_id(self, asset_id: int) -> Asset:
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM Assets WHERE AssetID=?"
            cursor.execute(query, (asset_id,))

            row = cursor.fetchone()
            if row:
                # Create an object Asset from the fetched data
                return Asset(
                    asset_id=row[0],
                    name=row[1],
                    asset_type=row[2],
                    serial_number=row[3],
                    purchase_date=row[4],
                    location=row[5],
                    status=row[6],
                    owner_id=row[7]
                )
            else:
                print(f"Asset with ID {asset_id} not found.")
                return None
        except Exception as e:
            print(f"Error fetching asset: {e}")
            return None


    def deleteing_asset(self, asset_id: int) -> bool:
        try:
            cursor = self.conn.cursor()

            # Check if the asset is currently allocated
            check_query = "SELECT COUNT(*) FROM Asset_Allocations WHERE AssetID = ? AND ReturnDate IS NULL"
            cursor.execute(check_query, (asset_id,))
            is_allocated = cursor.fetchone()[0] > 0  # True if there are any allocations

            if is_allocated:
                print("Asset is currently allocated and cannot be deleted.")
                return False            

            # if not allocated, delete it
            query = "SELECT * FROM Assets WHERE AssetID=?"
            cursor.execute(query, (asset_id,))
            asset = cursor.fetchone()
            if asset is None:
                raise AssetNotFoundException(asset_id)

            query = "DELETE FROM Assets WHERE AssetID=?"
            cursor.execute(query, (asset_id,))
            self.conn.commit()
            return True
        except AssetNotFoundException as e:
            print(f"Exception: {e}")
            return False
        except Exception as e:
            print(f"Error deleting asset: {e}")
            return False


    def allocating_asset(self, asset_allocation: AssetAllocation) -> bool:
        try:
            cursor = self.conn.cursor()
            
            # Get asset ID and employee ID from the AssetAllocation object
            asset_id = asset_allocation.get_asset_id()
            employee_id = asset_allocation.get_employee_id()
            allocation_date = asset_allocation.get_allocation_date()

            # Check if asset exists
            query = "SELECT * FROM Assets WHERE AssetID=?"
            cursor.execute(query, (asset_id,))
            asset = cursor.fetchone()

            if asset is None:
                raise AssetNotFoundException(asset_id)

            # Check if the asset is currently allocated
            check_query = "SELECT COUNT(*) FROM Asset_Allocations WHERE AssetID = ? AND ReturnDate IS NULL"
            cursor.execute(check_query, (asset_id,))
            is_allocated = cursor.fetchone()[0] > 0  # True if there are any allocations

            if is_allocated:
                print("Asset is already allocated.")
                return False  

            # Get last maintenance date
            last_maintenance_query = "SELECT MAX(MaintenanceDate) FROM Maintenance_Records WHERE AssetID=?"
            cursor.execute(last_maintenance_query, (asset_id,))
            last_maintenance_date = cursor.fetchone()[0]

            # Check if the last maintenance was done within 2 years
            if last_maintenance_date:
                current_date = datetime.now().date()  # Convert current datetime to date
                delta_years = (current_date - last_maintenance_date).days / 365
                if delta_years >= 2:
                    raise AssetNotMaintainException(asset_id)

            # Allocate the asset if everything is fine
            query = """
                INSERT INTO Asset_Allocations (AllocationDate, AssetID, EmployeeID)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (allocation_date, asset_id, employee_id))
            self.conn.commit()
            print("Asset allocated successfully.")
            return True

        except AssetNotFoundException as e:
            print(f"Exception: {e}")
            return False
        except AssetNotMaintainException as e:
            print(f"Exception: {e}")
            return False
        except Exception as e:
            print(f"Error allocating asset: {e}")
            return False


    def deallocating_asset(self, asset_id: int, employee_id: int, return_date: str) -> bool:
        try:
            cursor = self.conn.cursor()
            
            # check for valid allocation
            check_query = """
                SELECT COUNT(*)
                FROM Asset_Allocations
                WHERE AssetID=? AND EmployeeID=? AND ReturnDate IS NULL
            """
            cursor.execute(check_query, (asset_id, employee_id))
            allocation_exists = cursor.fetchone()[0] > 0  # Check if any allocation exists
            if not allocation_exists:
                print("No valid allocation found for the provided Asset ID and Employee ID.")
                return False
            
            # deallocate the asset if valid allocation exist
            query = """
                UPDATE Asset_Allocations
                SET ReturnDate=?
                WHERE AssetID=? AND EmployeeID=? AND ReturnDate IS NULL
            """
            cursor.execute(query, (return_date, asset_id, employee_id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deallocating asset: {e}")
            return False


    def performing_maintenance(self, maintenance_record: MaintenanceRecord) -> bool:
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO Maintenance_Records (MaintenanceDate, Description, Cost, AssetID)
                VALUES (?, ?, ?, ?)
            """
            # Use the MaintenanceRecord object's getters to access its properties
            cursor.execute(query, (
                maintenance_record.get_maintenance_date(),
                maintenance_record.get_description(),
                maintenance_record.get_cost(),
                maintenance_record.get_asset_id()
            ))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error performing maintenance: {e}")
            return False


    def reserving_asset(self, reservation: Reservation) -> bool:
        try:
            cursor = self.conn.cursor()

            # Check if the asset exists
            asset_check_query = """
                SELECT COUNT(*)
                FROM Assets
                WHERE AssetID=?
            """
            cursor.execute(asset_check_query, (reservation.get_asset_id(),))
            asset_exists = cursor.fetchone()[0] > 0
            
            if not asset_exists:
                raise ValueError(f"Asset ID {reservation.get_asset_id()} not found.")

            # Check if the employee exists
            employee_check_query = """
                SELECT COUNT(*)
                FROM Employees
                WHERE EmployeeID=?
            """
            cursor.execute(employee_check_query, (reservation.get_employee_id(),))
            employee_exists = cursor.fetchone()[0] > 0
            
            if not employee_exists:
                raise ValueError(f"Employee ID {reservation.get_employee_id()} not found.")

            # Check if the asset is currently allocated
            check_query = """
                SELECT COUNT(*)
                FROM Asset_Allocations
                WHERE AssetID=? AND ReturnDate IS NULL
            """
            cursor.execute(check_query, (reservation.get_asset_id(),))
            is_allocated = cursor.fetchone()[0] > 0  # True if asset is allocated
            
            if is_allocated:
                print("Asset is currently allocated and cannot be reserved.")
                return False

            # Proceed with reserving the asset if it's available
            query = """
                INSERT INTO Reservations (ReservationDate, StartDate, EndDate, Status, AssetID, EmployeeID)
                VALUES (?, ?, ?, 'Pending', ?, ?)
            """
            cursor.execute(query, (
                reservation.get_reservation_date(),
                reservation.get_start_date(),
                reservation.get_end_date(),
                reservation.get_asset_id(),
                reservation.get_employee_id()
            ))
            self.conn.commit()
            return True
        except ValueError as ve:
            print(f"Validation Error: {ve}")
            return False
        except Exception as e:
            print(f"Error reserving asset: {e}")
            return False


    def withdrawing_reservation(self, reservation_id: int) -> bool:
        try:
            cursor = self.conn.cursor()

            # Check if the reservation exists
            check_query = "SELECT COUNT(*) FROM Reservations WHERE ReservationID=?"
            cursor.execute(check_query, (reservation_id,))
            reservation_exists = cursor.fetchone()[0] > 0  # True if reservation exists

            if not reservation_exists:
                print("Error: Reservation ID does not exist.")
                return False

            # Proceed with withdrawal if reservation exists
            delete_query = "DELETE FROM Reservations WHERE ReservationID=?"
            cursor.execute(delete_query, (reservation_id,))
            self.conn.commit()
            print("Reservation withdrawn successfully.")
            return True
        except Exception as e:
            print(f"Error withdrawing reservation: {e}")
            return False

