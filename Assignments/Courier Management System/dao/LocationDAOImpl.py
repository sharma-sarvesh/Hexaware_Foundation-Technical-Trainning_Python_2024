# dao/LocationDAOImpl.py

from dao.LocationDAO import LocationDAO
from util.DBConnection import DBConnection
from entity.Location import Location

class LocationDAOImpl(LocationDAO):
    def create_location(self, location):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = '''INSERT INTO Location (LocationID, LocationName, Address) 
                        VALUES (?, ?, ?)'''
            values = (location.get_LocationID(), location.get_LocationName(), location.get_Address())
            cursor.execute(query, values)
            conn.commit()

    def get_location_by_id(self, location_id):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM Location WHERE LocationID = ?"
            cursor.execute(query, (location_id,))
            row = cursor.fetchone()
            return Location(*row) if row else None

    def update_location(self, location):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = '''UPDATE Location 
                        SET LocationName = ?, Address = ? 
                        WHERE LocationID = ?'''
            values = (location.get_LocationName(), location.get_Address(), location.get_LocationID())
            cursor.execute(query, values)
            conn.commit()

    def delete_location(self, location_id):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = "DELETE FROM Location WHERE LocationID = ?"
            cursor.execute(query, (location_id,))
            conn.commit()

    def get_all_locations(self):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM Location"
            cursor.execute(query)
            return [Location(*row) for row in cursor.fetchall()]
