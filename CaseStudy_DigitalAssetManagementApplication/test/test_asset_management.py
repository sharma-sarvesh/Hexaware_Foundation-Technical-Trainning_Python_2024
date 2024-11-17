import uuid

import sys
import os
import pytest
import pyodbc
from entity.Asset import Asset
from entity.MaintenanceRecord import MaintenanceRecord
from entity.Reservation import Reservation
from dao.AssetManagementServiceImpl import AssetManagementServiceImpl
from util.DBConnection import DBConnection

# Add project root directory to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'S:GIT/Hexaware_CaseStudy')))


@pytest.fixture(scope='module')
def db_connection():
    """create a connection to db"""
    conn = DBConnection.get_connection()
    assert conn is not None, "Database connection failed"
    yield conn  # Provide the connection to the tests
    DBConnection.close_connection()  # Close the connection after all tests


@pytest.fixture(scope='function')
def asset_service():
    """provide an instance of AssetManagementService for each test."""
    return AssetManagementServiceImpl()


@pytest.fixture(scope='function')
def setup_test_data(db_connection):
    """Insert necessary test data before each test and clean up afterward."""
    cursor = db_connection.cursor()
    # insert test data before running the test
    yield
    # delete any test data inserted for test


# Test 1. to add a new asset and verify it was added successfully
def test_add_asset_success(asset_service, setup_test_data, db_connection):
    asset = Asset()
    asset.set_name("Test Asset")
    asset.set_type("Test Type")
    
    # Use a unique serial number generated with uuid
    unique_serial_number = "SN" + str(uuid.uuid4())[:8]  # Use first 8 characters for simplicity
    asset.set_serial_number(unique_serial_number)
    asset.set_purchase_date("2024-10-21")
    asset.set_location("Test Location")
    asset.set_status("In Use")
    asset.set_owner_id(1)

    result = asset_service.add_new_asset(asset)
    assert result is True  # asset was added successfully

    # asset exist in the db
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Assets WHERE SerialNumber=?", (unique_serial_number,))
    retrieved_asset = cursor.fetchone()

    assert retrieved_asset is not None  # asset was found
    assert retrieved_asset.Name == asset.get_name()  # check if the name matches


# Test 2 to perform maintenance on an asset and verify it was logged correctly
def test_perform_maintenance_success(asset_service, setup_test_data, db_connection):
    asset_id = 1
    maintenance_date = "2024-11-22"
    description = "Regular maintenance check"
    cost = 150.00

    maintenance_record = MaintenanceRecord()
    maintenance_record.set_maintenance_date(maintenance_date)
    maintenance_record.set_description(description)
    maintenance_record.set_cost(cost)
    maintenance_record.set_asset_id(asset_id)

    result = asset_service.performing_maintenance(maintenance_record)
    assert result is True  # maintenance was logged

    # maintenance record exists in the db
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Maintenance_Records WHERE AssetID=? AND MaintenanceDate=?", (asset_id, maintenance_date))
    retrieved_record = cursor.fetchone()

    assert retrieved_record is not None
    assert retrieved_record.Description == description
    assert retrieved_record.Cost == cost


# Test 3 to reserve an asset and verify it was reserved correctly
def test_reserve_asset_success(asset_service, setup_test_data, db_connection):
    asset_id = 8
    employee_id = 1
    reservation_date = "2024-10-21"
    start_date = "2024-10-22"
    end_date = "2024-10-25"

    reservation = Reservation(
        reservation_date=reservation_date,
        start_date=start_date,
        end_date=end_date,
        asset_id=asset_id,
        employee_id=employee_id
    )

    result = asset_service.reserving_asset(reservation)
    assert result is True  # Verify the asset was reserved

    # Verify the reservation exists in the database
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Reservations WHERE AssetID=? AND ReservationDate=?", (asset_id, reservation_date))
    retrieved_reservation = cursor.fetchone()

    assert retrieved_reservation is not None
    assert retrieved_reservation.EmployeeID == employee_id  # Check if the employee ID matches


# Test to reserve an asset with an invalid employee ID
def test_reserve_asset_invalid_employee_id(asset_service, setup_test_data):
    asset_id = 1
    invalid_employee_id = 999  # random employee ID which is not in db
    reservation_date = "2024-10-21"
    start_date = "2024-10-22"
    end_date = "2024-10-25"

    reservation = Reservation(
        reservation_date=reservation_date,
        start_date=start_date,
        end_date=end_date,
        asset_id=asset_id,
        employee_id=invalid_employee_id
    )

    result = asset_service.reserving_asset(reservation)
    assert result is False  # reservation fails with an invalid employee ID


# Test to reserve an asset with an invalid asset ID
def test_reserve_asset_invalid_asset_id(asset_service, setup_test_data):
    invalid_asset_id = 999  # asset ID which isnot in db
    employee_id = 1
    reservation_date = "2024-10-21"
    start_date = "2024-10-22"
    end_date = "2024-10-25"

    reservation = Reservation(
        reservation_date=reservation_date,
        start_date=start_date,
        end_date=end_date,
        asset_id=invalid_asset_id,
        employee_id=employee_id
    )

    result = asset_service.reserving_asset(reservation)
    assert result is False  # reservation fails with an invalid asset ID
