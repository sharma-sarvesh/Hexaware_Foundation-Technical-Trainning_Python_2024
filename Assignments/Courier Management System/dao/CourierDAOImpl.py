# dao/CourierDAOImpl.py

# dao/CourierDAOImpl.py

from dao.CourierDAO import CourierDAO
from util.DBConnection import DBConnection
from entity.Courier import Courier
from myexceptions.TrackingNumberNotFoundException import TrackingNumberNotFoundException

class CourierDAOImpl(CourierDAO):

    def create_courier(self, courier: Courier) -> None:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        query = '''INSERT INTO Courier (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, 
                    Weight, Status, TrackingNumber, DeliveryDate) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        values = (courier.get_CourierID(), courier.get_SenderName(), courier.get_SenderAddress(),
                    courier.get_ReceiverName(), courier.get_ReceiverAddress(), courier.get_Weight(),
                    courier.get_Status(), courier.get_TrackingNumber(), courier.get_DeliveryDate(), 
                    )
        cursor.execute(query, values)
        conn.commit()
        # cursor.close()
        # conn.close()

    def get_courier_by_id(self, courier_id: int) -> Courier:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Courier WHERE CourierID = ?"
        cursor.execute(query, (courier_id,))
        row = cursor.fetchone()
        # cursor.close()
        # conn.close()
        if row:
            return Courier(*row)
        raise TrackingNumberNotFoundException(f"Courier with ID {courier_id} not found.")

    def update_courier(self, courier: Courier) -> None:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()

        # Ensure you use the correct method names from the Courier class
        update_query = '''UPDATE Courier 
                        SET Status = ?, TrackingNumber = ?, DeliveryDate = ?
                        WHERE CourierID = ?'''
        cursor.execute(update_query, (courier.get_Status(), courier.get_TrackingNumber(), courier.get_DeliveryDate(), courier.get_CourierID()))
        
        conn.commit()
        cursor.close()
        conn.close()

    def delete_courier(self, courier_id: int) -> None:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Courier WHERE CourierID = ?"
        cursor.execute(query, (courier_id,))
        conn.commit()
        # cursor.close()
        # conn.close()

    def get_all_couriers(self) -> list:
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Courier"
        cursor.execute(query)
        rows = cursor.fetchall()
        # Create a list of Courier objects
        couriers = [Courier(*row) for row in rows]
        # Close the cursor and connection
        cursor.close()
        conn.close()
        return couriers
