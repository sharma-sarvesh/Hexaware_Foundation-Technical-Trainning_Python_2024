# dao/UserDAOImpl.py

from dao.UserDAO import UserDAO
from util.DBConnection import DBConnection
from entity.User import User

class UserDAOImpl(UserDAO):
    def create_user(self, user):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = '''INSERT INTO User_table (UserID, Name, Email, Password, ContactNumber, Address) 
                        VALUES (?, ?, ?, ?, ?, ?)'''
            values = (user.get_UserID(), user.get_Name(), user.get_Email(), user.get_Password(),
                        user.get_ContactNumber(), user.get_Address())
            cursor.execute(query, values)
            conn.commit()

    def get_user_by_id(self, user_id):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM User_table WHERE UserID = ?"
            cursor.execute(query, (user_id,))
            row = cursor.fetchone()
            return User(*row) if row else None

    def update_user(self, user):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = '''UPDATE User_table 
                        SET Name = ?, Email = ?, Password = ?, ContactNumber = ?, Address = ? 
                        WHERE UserID = ?'''
            values = (user.get_Name(), user.get_Email(), user.get_Password(), 
                        user.get_ContactNumber(), user.get_Address(), user.get_UserID())
            cursor.execute(query, values)
            conn.commit()

    def delete_user(self, user_id):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = "DELETE FROM User_table WHERE UserID = ?"
            cursor.execute(query, (user_id,))
            conn.commit()

    def get_all_users(self):
        with DBConnection.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM User_table"
            cursor.execute(query)
            return [User(*row) for row in cursor.fetchall()]
