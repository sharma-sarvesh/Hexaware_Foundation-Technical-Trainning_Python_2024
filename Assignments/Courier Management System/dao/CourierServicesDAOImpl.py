# dao/CourierServiceDAOImpl.py

from dao.CourierServicesDAO import CourierServiceDAO
from util.DBConnection import DBConnection
from entity.CourierServices import CourierService
import pyodbc

class CourierServicesDAOImpl(CourierServiceDAO):

    def create_courier_service(self, courier_service: CourierService) -> None:
        try:
            with DBConnection.get_connection() as conn:
                with conn.cursor() as cursor:
                    query = '''INSERT INTO CourierServices (ServiceID, ServiceName, Cost) 
                            VALUES (?, ?, ?)'''
                    values = (courier_service.get_ServiceID(), courier_service.get_ServiceName(), courier_service.get_Cost())
                    cursor.execute(query, values)
                    conn.commit()
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")


    def get_courier_service_by_id(self, service_id: int) -> CourierService:
        try:
            with DBConnection.get_connection() as conn:
                with conn.cursor() as cursor:
                    query = "SELECT ServiceID, ServiceName, Cost FROM CourierServices WHERE ServiceID = ?"
                    cursor.execute(query, (service_id,))
                    row = cursor.fetchone()
                    if row:
                        return CourierService(*row)
                    return None
        except Exception as e:
            print(f"An error occurred: {e}")


    def update_courier_service(self, courier_service: CourierService) -> None:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        
        # Update query
        update_query = '''
            UPDATE CourierServices 
            SET ServiceName = ?, Cost = ? 
            WHERE ServiceID = ?
        '''
        
        cursor.execute(update_query, (
            courier_service.get_ServiceName(),
            courier_service.get_Cost(),
            courier_service.get_ServiceID()
        ))
        
        conn.commit()
        cursor.close()
        conn.close()

    def delete_courier_service(self, service_id: str) -> None:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM CourierServices WHERE ServiceID = ?"
        cursor.execute(query, (service_id,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_all_courier_services(self) -> list:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM CourierServices"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [CourierService(*row) for row in rows]
