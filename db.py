import sqlite3

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_address(self, user_id):
        """Достаем адрес"""
        result = self.cursor.execute("SELECT `address` FROM `users` WHERE `user_id` = ?", (user_id,))
        
        return result.fetchone()[0]


    def add_record(self, user_id, address):
        """Создаем запись о доходах/расходах"""
        self.cursor.execute("INSERT INTO `users` (`user_id`,`address`) VALUES (?, ?)",(user_id, address,))
    
        return self.conn.commit()

    def delete_record(self, user_id):
        """Удаление запись о доходах/расходах"""
        self.cursor.execute("DELETE FROM `users` WHERE `user_id`=?",(user_id, ))
    
        return self.conn.commit()
   

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()