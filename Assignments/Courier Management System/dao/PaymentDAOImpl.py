# dao/PaymentDAOImpl.py

from dao.PaymentDAO import PaymentDAO
from util.DBConnection import DBConnection
from entity.Payment import Payment
import pyodbc 

class PaymentDAOImpl(PaymentDAO):
    def create_payment(self, payment):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = '''INSERT INTO Payment (PaymentID, Amount, PaymentDate, CourierID) 
                        VALUES (?, ?, ?, ?)'''
            values = (payment.get_PaymentID(), payment.get_Amount(), payment.get_PaymentDate(), 
                        payment.get_CourierID())
            cursor.execute(query, values)
            conn.commit()

    def get_payment_by_id(self, payment_id: int):
        try:
            with DBConnection.get_connection() as conn:
                with conn.cursor() as cursor:
                    query = "SELECT PaymentID, CourierID, LocationID, Amount, PaymentDate FROM Payment WHERE PaymentID = ?"
                    cursor.execute(query, (payment_id,))
                    row = cursor.fetchone()

                    if row:
                        return Payment(*row)
                    else:
                        raise PaymentNotFoundException(f"Payment with ID {payment_id} not found.")
        
        except pyodbc.Error as e:
            print(f"An error occurred while fetching the payment: {e}")


    def update_payment(self, payment):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = '''UPDATE Payment 
                        SET Amount = ?, PaymentDate = ?, CourierID = ? 
                        WHERE PaymentID = ?'''
            values = (payment.get_Amount(), payment.get_PaymentDate(), payment.get_CourierID(), 
                        payment.get_PaymentID())
            cursor.execute(query, values)
            conn.commit()

    def delete_payment(self, payment_id):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = "DELETE FROM Payment WHERE PaymentID = ?"
            cursor.execute(query, (payment_id,))
            conn.commit()

    def get_all_payments(self):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM Payment"
            cursor.execute(query)
            return [Payment(*row) for row in cursor.fetchall()]
