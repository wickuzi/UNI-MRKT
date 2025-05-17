from Models.Entities.User import User
from werkzeug.security import generate_password_hash, check_password_hash

class ModelUser:

    @classmethod
    def register(cls, conn, user):
        try:
            cursor = conn.cursor()
            sql_check = "SELECT id FROM user WHERE correo = %s"
            cursor.execute(sql_check, (user.correo,))
            if cursor.fetchone():
                cursor.close()
                return "Correo ya registrado"

            # Cifrar la contraseña antes de guardarla
            hashed_password = generate_password_hash(user.password)
            sql_insert = "INSERT INTO user (username, correo, password) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert, (user.username, user.correo, hashed_password))
            conn.commit()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"

    @classmethod
    def login(cls, conn, user):
        try:
            cursor = conn.cursor()
            sql = "SELECT id, username, correo, password FROM user WHERE correo = %s"
            cursor.execute(sql, (user.correo,))
            row = cursor.fetchone()
            cursor.close()

            if row is not None:
                hash_from_db = row[3]
                password_correcta = check_password_hash(hash_from_db, user.password)
                if password_correcta:
                    return User(row[0], row[1], row[2], None)
            return None
        except Exception as ex:
            raise Exception(f"Error al hacer login: {ex}")
        
    @classmethod
    def get_by_id(cls, conn, id):
        try:
            cursor = conn.cursor()
            sql = "SELECT id, username, correo FROM user WHERE id = %s"
            cursor.execute(sql,(id,))
            row = cursor.fetchone()
            cursor.close()

            if row is not None:
                    return User(row[0], row[1], row[2], None)
            else:
                  return None
        except Exception as ex:
            raise Exception(f"Error al hacer login: {ex}")
